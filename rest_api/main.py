import pendulum
import logging
import uvicorn
import numpy as np
import pandas as pd

from pydantic import BaseModel
from fastapi import FastAPI
from typing import List, Union, Any
from model import predict, confidence
from sklearn.preprocessing import Normalizer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__) 

app = FastAPI(debug=True)
transformers = None

class InputFeature(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class InputList(BaseModel):
    items: List[Union[InputFeature,List]]

class Output(BaseModel):
    predictions: list
    confidences: list
    executed_at: str

@app.on_event("startup")
def load_data():
    global transformers
    iris_dataset = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
    X = iris_dataset.iloc[:, 0:4].values
    transformers = Normalizer().fit(X)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predict", response_model=Output, status_code=200)
def get_prediction(payload: InputList):
    items = payload.items
    input_normalized = normalization(items,type(items[0])) 
    prediction_list = predict(input_normalized)
    confidence_list = confidence(prediction_list)
    prediction_class = [int(np.argmax(item)) for item in prediction_list]

    if not prediction_class:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"predictions": prediction_class, "confidences":confidence_list, "executed_at": str(pendulum.now('Asia/Jakarta'))}
    return response_object

def normalization(X_list, type_data=InputFeature):
    global transformers
    if type_data is InputFeature:
        X_list = np.asarray([list(item.dict().values()) for item in X_list])
    X_list = transformers.transform(X_list)
    return X_list.tolist()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")