from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):

    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int

# loading the saved model
standard_scaler = pickle.load(open('standard_scaler.sav', 'rb'))
diabetes_model = pickle.load(open('trained_model.sav', 'rb'))

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)


    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']   
    bp = input_dictionary['BloodPressure']
    st = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']

    input_list = [preg, glu, bp, st, insulin, bmi, dpf, age]

    input_list = standard_scaler.transform([input_list])
    prediction = diabetes_model.predict(input_list)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'