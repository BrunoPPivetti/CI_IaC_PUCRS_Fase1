from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello':'World'}

@app.get('/status')
def read_status():
    return {'status':'OK'}

@app.get('/pucrs')
def read_projeto():
    return {'fase 1':'devops'}