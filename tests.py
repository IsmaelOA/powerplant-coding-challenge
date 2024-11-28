import requests
import json

# Define the URL of the local service
url = "http://127.0.0.1:8888/productionplan"

# Define the payloads
payloads = [
    {
        "load": 480,
        "fuels": {
            "gas(euro/MWh)": 13.4,
            "kerosine(euro/MWh)": 50.8,
            "co2(euro/ton)": 20,
            "wind(%)": 60
        },
        "powerplants": [
            {"name": "gasfiredbig1", "type": "gasfired", "efficiency": 0.53, "pmin": 100, "pmax": 460},
            {"name": "gasfiredbig2", "type": "gasfired", "efficiency": 0.53, "pmin": 100, "pmax": 460},
            {"name": "windpark1", "type": "windturbine", "efficiency": 1, "pmin": 0, "pmax": 150},
            {"name": "windpark2", "type": "windturbine", "efficiency": 1, "pmin": 0, "pmax": 36}
        ]
    },
    {
        "load": 300,
        "fuels": {
            "gas(euro/MWh)": 15.5,
            "kerosine(euro/MWh)": 52.0,
            "co2(euro/ton)": 22,
            "wind(%)": 80
        },
        "powerplants": [
            {"name": "gasfiredbig1", "type": "gasfired", "efficiency": 0.50, "pmin": 50, "pmax": 300},
            {"name": "turbojet1", "type": "turbojet", "efficiency": 0.30, "pmin": 0, "pmax": 50},
            {"name": "windpark1", "type": "windturbine", "efficiency": 1, "pmin": 0, "pmax": 200}
        ]
    },
    {
        "load": 100,
        "fuels": {
            "gas(euro/MWh)": 10.0,
            "kerosine(euro/MWh)": 45.0,
            "co2(euro/ton)": 18,
            "wind(%)": 100
        },
        "powerplants": [
            {"name": "gasfiredbig1", "type": "gasfired", "efficiency": 0.60, "pmin": 20, "pmax": 100},
            {"name": "windpark1", "type": "windturbine", "efficiency": 1, "pmin": 0, "pmax": 50},
            {"name": "windpark2", "type": "windturbine", "efficiency": 1, "pmin": 0, "pmax": 50}
        ]
    }
]

# Send each payload and print the response
for i, payload in enumerate(payloads, start=1):
    expected_load = payload["load"]
    print(f"Sending payload {i}, expected load {expected_load}")
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        response_data = response.json()
        total_power = sum(plant["p"] for plant in response_data)
        print(f"Response {i}:\n{json.dumps(response_data, indent=2)}")
        print(f"Total power generated: {total_power}")
        if total_power == expected_load:
            print(f"The total power matches the expected load ({expected_load}).\n")
        else:
            print(f"The total power ({total_power}) does NOT match the expected load ({expected_load}).\n")
    else:
        print(f"Payload {i} failed with status code {response.status_code} and error: {response.text}\n")
