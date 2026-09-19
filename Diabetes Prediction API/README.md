# Diabetes Prediction API

A simple machine learning API for predicting diabetes using SVM and FastAPI.

## How to Run

Open Command Prompt in the project folder.

1. Install the requirements

```bash
pip install -r requirements.txt
```

2. Start the FastAPI server

```bash
uvicorn ml_api:app
```

Keep this terminal running.

3. Run the API implementation

Open a **new Command Prompt** without closing the previous terminal and run:

```bash
python api_implementation.py
```

The prediction result will be displayed in the terminal.


## Workflow

User Input
    ↓
FastAPI
    ↓
StandardScaler
    ↓
SVM Model
    ↓
Prediction
    ↓
Diabetic / Not Diabetic
