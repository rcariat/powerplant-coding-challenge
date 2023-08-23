from pydantic import BaseModel
from typing import List

class Powerplants(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: int
    pmax: int

class Fuels(BaseModel):
    gas: float
    kerosine: float
    co2: int
    wind: int

class Payload(BaseModel):
    load: int
    fuels: Fuels
    powerplants: List[Powerplants]

class Answer(BaseModel):
    name: str
    p: float

class Response(BaseModel):
    answers: List[Answer]