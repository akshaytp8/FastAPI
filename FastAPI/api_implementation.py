import requests

url = 'http://127.0.0.1:8000/diabetes_prediction'

input_data_for_model = {
    'Pregnancies': 2,
    'Glucose': 120,
    'BloodPressure': 70,
    'SkinThickness': 20,
    'Insulin': 79,
    'BMI': 25.0,
    'DiabetesPedigreeFunction': 0.5,
    'Age': 30
}

response = requests.post(url, json=input_data_for_model)

print(response.text)