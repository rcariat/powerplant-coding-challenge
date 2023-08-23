from app.api.logic import UnitCommitmentOptimizer


def create_response(payload):
    # Instantiate an optimizer object
    uco = UnitCommitmentOptimizer(activate_co2=False)

    # Get results from optimizer
    result = uco.optimize(payload.load, payload.powerplants, payload.fuels)

    return result
