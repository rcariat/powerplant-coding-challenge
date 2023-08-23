from fastapi import FastAPI

from app.db.models import Payload
from app.api import api

import logging

logging.basicConfig(filename='app.log',
                    filemode='w',
                    level=logging.ERROR,
                    format='%(name)s - %(levelname)s - %(message)s')

app = FastAPI()


@app.get("/")
def root():
    return {"message": "I am G-Root. Try another route."}

@app.post("/productionplan")
def create_response(payload: Payload):

    return api.create_response(payload)
