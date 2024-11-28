from flask import Blueprint, request, jsonify
from powerplants.units import GasFiredPlant, TurboJetPlant, WindTurbinePlant

production_plan_bp = Blueprint('production_plan', __name__)

def parse_powerplants(data):
    """
    Converts the list of power plants into instances of specific classes.
    """
    plant_classes = {
        "gasfired": GasFiredPlant,
        "turbojet": TurboJetPlant,
        "windturbine": WindTurbinePlant,
    }

    powerplants = []
    for plant in data:
        plant_class = plant_classes.get(plant["type"])
        if plant_class:
            powerplants.append(
                plant_class(
                    name=plant["name"],
                    pmin=plant["pmin"],
                    pmax=plant["pmax"],
                    efficiency=plant["efficiency"],
                )
            )
    return powerplants

def calculate_production_plan(load, fuels, powerplants):
    """
    Calculate the production plan, filling the requested load with plants sorted by unit cost.
    Redistribute MWh if needed to meet Pmin requirements.
    """
    # Sort plants by unit cost (ascending)
    powerplants.sort(key=lambda plant: plant.unit_cost(fuels))

    plan = []
    remaining_load = load

    for i, plant in enumerate(powerplants):
        if remaining_load <= 0:
            break

        # Calculate production for the current plant
        production = min(plant.pmax, remaining_load)

        # Ensure Pmin is met
        if production < plant.pmin:
            production = 0  # If we can't meet Pmin, we assign nothing

        # Add production to the plan
        plan.append({"name": plant.name, "p": production})
        remaining_load -= production

        # If next plant can't meet Pmin, redistribute
        if i < len(powerplants) - 1 and remaining_load > 0:
            next_plant = powerplants[i + 1]
            if remaining_load < next_plant.pmin:
                deficit = next_plant.pmin - remaining_load
                for prev in reversed(plan):
                    if prev["p"] > plant.pmin:
                        adjustment = min(prev["p"] - plant.pmin, deficit)
                        prev["p"] -= adjustment
                        remaining_load += adjustment
                        deficit -= adjustment

                        if deficit <= 0:
                            break

                # Check if redistribution was successful
                if remaining_load < next_plant.pmin:
                    return {"error": "Redistribution failed to meet Pmin requirements"}, 400

    # Ensure the total load is met
    if remaining_load > 0:
        return {"error": "The load cannot be met with the available plants"}, 400

    return plan, 200

@production_plan_bp.route('/productionplan', methods=['POST'])
def production_plan():
    """
    Endpoint to calculate the production plan.
    """
    try:
        data = request.get_json()

        load = data['load']
        fuels = data['fuels']
        powerplants = parse_powerplants(data['powerplants'])

        plan, status = calculate_production_plan(load, fuels, powerplants)
        return jsonify(plan), status

    except KeyError as e:
        return jsonify({"error": f"Missing required key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
