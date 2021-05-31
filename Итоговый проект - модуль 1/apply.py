from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn
from sklearn.linear_model import Ridge
import joblib

class BatchModel(BaseModel):
  "Параметры запроса"
  id : str
  x : List[List[float]]

app = FastAPI()

@app.post("/")
def train_model(modinfo : BatchModel):
  "Обработка запроса"
  model = joblib.load('models/' + modinfo.id)
  result = model.predict(modinfo.x) 
  return { 'y': list(result) }

if __name__ == '__main__':
  uvicorn.run('apply:app', port = 8082)