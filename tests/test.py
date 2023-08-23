from starlette.testclient import TestClient
from app.main import app
import json

client = TestClient(app)


def test_create_answer():
    body = {
      "load": 910,
      "fuels":
      {
        "gas(euro/MWh)": 13.4,
        "kerosine(euro/MWh)": 50.8,
        "co2(euro/ton)": 20,
        "wind(%)": 60
      },
      "powerplants": [
        {
          "name": "gasfiredbig1",
          "type": "gasfired",
          "efficiency": 0.53,
          "pmin": 100,
          "pmax": 460
        },
        {
          "name": "gasfiredbig2",
          "type": "gasfired",
          "efficiency": 0.53,
          "pmin": 100,
          "pmax": 460
        },
        {
          "name": "gasfiredsomewhatsmaller",
          "type": "gasfired",
          "efficiency": 0.37,
          "pmin": 40,
          "pmax": 210
        },
        {
          "name": "tj1",
          "type": "turbojet",
          "efficiency": 0.3,
          "pmin": 0,
          "pmax": 16
        },
        {
          "name": "windpark1",
          "type": "windturbine",
          "efficiency": 1,
          "pmin": 0,
          "pmax": 150
        },
        {
          "name": "windpark2",
          "type": "windturbine",
          "efficiency": 1,
          "pmin": 0,
          "pmax": 36
        }
      ]
    }

    response = client.post('/productionplan', json=body)
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "windpark1",
            "p": 90.0
        },
        {
            "name": "windpark2",
            "p": 21.6
        },
        {
            "name": "gasfiredbig1",
            "p": 460.0
        },
        {
            "name": "gasfiredbig2",
            "p": 338.4
        },
        {
            "name": "gasfiredsomewhatsmaller",
            "p": 0.0
        },
        {
            "name": "tj1",
            "p": 0.0
        }
    ]

