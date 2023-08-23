from fastapi import FastAPI, HTTPException

from app.db.models import Payload
from app.api import api

app = FastAPI()


@app.get("/")
def root():
    return {"message": "I am G-Root. Try another route."}

@app.post("/productionplan")
def create_response(payload: Payload):

    return api.create_response(payload)
