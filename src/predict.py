import pandas as pd
import joblib

model = joblib.load("models/phishing_model.pkl")

def predict(features):

    df = pd.DataFrame([features])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0]

    print("Prediction:", prediction)
    print("Probability:", probability)

    confidence = round(max(probability) * 100, 2)

    if prediction == 1:
        result = "Legitimate Website ✅"
    else:
        result = "Phishing Website ⚠️"

    return result, confidence