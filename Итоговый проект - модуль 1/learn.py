"""Пример работы сервиса обучения модели.

Показывает только организацию взаимодействия с клиентом и, через файловую системы, сервисом применения модели.
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn
from uuid import uuid1
from sklearn.linear_model import Ridge
import joblib

class TrainSamples(BaseModel):
  "Параметры запроса"
  x : List[List[float]]
  y : List[float]

app = FastAPI()

@app.post("/")
def train_model(samples : TrainSamples):
  "Обработка запроса"
  name = str(uuid1())
  model = Ridge()
  model.fit(samples.x, samples.y)
  joblib.dump(model, 'models/' + name)
  return { 'id': name }


if __name__ == '__main__':
  uvicorn.run('train:app', port = 8081)