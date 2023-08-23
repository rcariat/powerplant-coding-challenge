from app.db.models import PowerPlantResponse
import numpy as np

def get_plant_cost(pp, fuels, activate_co2):
    """
    Function to evaluate a power plant cost
    :param pp: power plant object including its efficiency attribute
    :param fuels: contain cost in euro/MWh for gas, kerosine and CO2
    :param activate_co2: boolean to take into consideration co2 in the cost computation
    :return: power plant's eur cost per MWh produced
    """
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
    """
    Class to implement different unit commitment optimization methods
    """
    def __init__(self, activate_co2: bool = False):
        self.activate_co2 = activate_co2

    def optimize(self, load, powerplants, fuels, method = 'merit_order'):
        """
        Forward inputs to selected methods
        :param load: The load is the amount of energy (MWh) that need to be generated during one hour
        :param powerplants: contain all powerplant objects
        :param fuels: contain cost in euro/MWh for gas, kerosine and CO2 + % wind
        :param method: method to optimize with
        :return: list of PowerPlantResponse with name and p produced
        """
        if method == 'merit_order':
            return self.merit_order(load, powerplants, fuels)
        if method == 'gradient_descent':
            #TODO
            return []

    def get_ordered_plants_by_merit(self, fuels, powerplants):
        """
        Sort powerplants by eur cost / MWh
        :param fuels: contain cost in euro/MWh for gas, kerosine and CO2 + % wind
        :param powerplants: unsorted list of all powerplant objects
        :param activate_co2: boolean to take into consideration co2 in the cost computation
        :return: list of powerplants sorted by eur cost / MWh
        """
        return sorted(powerplants,
                      key=lambda x: get_plant_cost(x,
                                                   fuels=fuels,
                                                   activate_co2=self.activate_co2))

    def merit_order(self, load, powerplants, fuels):
        """
        Simplest method
        :param load: The load is the amount of energy (MWh) that need to be generated during one hour
        :param powerplants: contain all powerplant objects
        :param fuels: contain cost in euro/MWh for gas, kerosine and CO2 + % wind
        :return: list of PowerPlantResponse with name and p produced
        """
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


    def gradient_descent(self, load, powerplants, fuels):

        coeffs = np.array()
        X = np.array()

