import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("dataset/phishing.csv")

# Keep only the features that our feature extractor generates
features = [
    "URLLength",
    "DomainLength",
    "IsDomainIP",
    "TLDLength",
    "NoOfSubDomain",
    "NoOfLettersInURL",
    "NoOfDegitsInURL",
    "NoOfEqualsInURL",
    "NoOfQMarkInURL",
    "IsHTTPS",
    "LineOfCode",
    "HasTitle",
    "NoOfImage",
    "NoOfCSS",
    "NoOfJS",
    "HasPasswordField",
    "HasSubmitButton"
]

X = df[features]
y = df["label"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("=" * 50)
print(f"Accuracy : {accuracy * 100:.2f}%")
print("=" * 50)

# Save Model
joblib.dump(model, "models/phishing_model.pkl")

print("✅ Model Saved Successfully")