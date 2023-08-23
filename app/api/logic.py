from app.db.models import PowerPlantResponse


def get_plant_cost(pp, fuels, activate_co2):
    co2_cost = 0
    energy_cost = 0
    if pp.type == "windturbine":
        return 0
    elif pp.type == "turbojet":
        energy_cost = fuels.kerosine
    elif pp.type == "gasfired":
        energy_cost = fuels.gas
    if activate_co2:
        co2_cost = fuels.CO2
    return energy_cost / pp.efficiency + co2_cost * 0.3


class UnitCommitmentOptimizer:

    def __init__(self, activate_co2: bool = False):
        self.activate_co2 = activate_co2

    def optimize(self, load, powerplants, fuels):
        response = []
        current_load = load
        ordered_plants = self.get_ordered_plants_by_merit(fuels, powerplants)

        for pp in ordered_plants:

            if current_load == 0:
                response.append(PowerPlantResponse(name=pp.name, p=0))
                continue

            energy_max = pp.pmax * fuels.wind / 100 if pp.type == "windturbine" else pp.pmax
            if current_load < energy_max:
                response.append(PowerPlantResponse(name=pp.name, p=round(max(current_load, pp.pmin), 2)))
                current_load -= max(current_load, pp.pmin)
            else:
                response.append(PowerPlantResponse(name=pp.name, p=round(energy_max, 2)))
                current_load -= energy_max

        return response

    def get_ordered_plants_by_merit(self, fuels, powerplants, activate_co2: bool = False):

        return sorted(powerplants,
                      key=lambda x: get_plant_cost(x,
                                                   fuels=fuels,
                                                   activate_co2=self.activate_co2))

