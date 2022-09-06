import os
import logging
import tensorflow as tf
import numpy as np

from pydantic import BaseModel
from tensorflow import keras

logger = logging.getLogger(__name__)  

def predict(x_input):
    model_file = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'model/model_ann.h5'))
    logger.info(model_file)

    model = keras.models.load_model(model_file)
    predict = model.predict(x_input)

    tf.keras.backend.clear_session()
    del model

    return predict.tolist()

def confidence(preds):
    return [max(item) for item in preds]

