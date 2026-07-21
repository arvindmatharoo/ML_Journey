from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle 
import uvicorn

model = pickle.load(open("persoanlity_model.pkl","rb"))
scaler = pickle.load(open('scaler.pkl','rb'))
pca = pickle.load(open('pca.pkl','rb'))


app = FastAPI()

class InputData(BaseModel):
    Time_spent_Alone: int
    Stage_fear: int  # Encoded (Yes=1, No=0)
    Social_event_attendance: int
    Going_outside: int
    Drained_after_socializing: int  # Encoded
    Friends_circle_size: int
    Post_frequency: int

@app.post('/predict')
def predict(data : InputData):
    features = np.array([[data.Time_spent_Alone, data.Stage_fear,
                          data.Social_event_attendance, data.Going_outside,
                          data.Drained_after_socializing,
                          data.Friends_circle_size, data.Post_frequency]])
    
    scaled = scaler.transform(features)
    reduced = pca.transform(scaled)
    prediction = model.predict(reduced)

    return {'Personality': 'Introvert' if prediction[0] == 1 else "Extrovert"}
