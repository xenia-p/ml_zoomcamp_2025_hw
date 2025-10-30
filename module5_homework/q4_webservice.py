import pickle
import uvicorn
from fastapi import FastAPI

from typing import Dict, Any, Literal

with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(customer):
    result = pipeline.predict_proba(customer)[0,1]
    return float(result)


app = FastAPI(title='predict_app')

@app.post('/predict')
def predict(customer: Dict[str, Any]):
    pred_proba = predict_single(customer)
    return pred_proba

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=9696)
