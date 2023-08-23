from pydantic import BaseModel, Field
from typing import List

class Powerplants(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: int
    pmax: int

class Fuels(BaseModel):
    gas: float = Field(alias="gas(euro/MWh)")
    kerosine: float = Field(alias="kerosine(euro/MWh)")
    co2: int = Field(alias="co2(euro/ton)")
    wind: int = Field(alias="wind(%)")

class Payload(BaseModel):
    load: int
    fuels: Fuels
    powerplants: List[Powerplants]

class Answer(BaseModel):
    name: str
    p: float

class Response(BaseModel):
    answers: List[Answer]