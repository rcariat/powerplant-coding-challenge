from app.api.logic import UnitCommitmentOptimizer


def create_response(payload):
    uco = UnitCommitmentOptimizer(activate_co2=False)

    result = uco.optimize(payload.load, payload.powerplants, payload.fuels)

    return result
