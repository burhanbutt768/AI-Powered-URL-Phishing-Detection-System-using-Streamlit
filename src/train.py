import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix
)

# --------------------
# LOAD DATASET
# --------------------

df = pd.read_csv("../data/phishing_dataset.csv")

print("\nDataset Size:", len(df))

print("\nDataset Head:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())


# --------------------
# CLEAN DATA
# --------------------

df = df.dropna()
df = df.drop_duplicates()

print("\nAfter Cleaning:")
print(df.shape)


# --------------------
# LABEL ENCODING
# --------------------

le = LabelEncoder()
df["type"] = le.fit_transform(df["type"])

print("\nClasses:")
print(le.classes_)


# --------------------
# FEATURE NAMES
# --------------------

feature_names = [
    "url_length",
    "dots",
    "hyphens",
    "at_symbol",
    "digits",
    "https",
    "login",
    "secure",
    "bank",
    "double_slash"
]


# --------------------
# FEATURE EXTRACTION
# --------------------

def extract_features(url):

    return [
        len(url),
        url.count("."),
        url.count("-"),
        url.count("@"),
        sum(c.isdigit() for c in url),
        1 if "https" in url else 0,
        1 if "login" in url.lower() else 0,
        1 if "secure" in url.lower() else 0,
        1 if "bank" in url.lower() else 0,
        url.count("//")
    ]


# --------------------
# BUILD FEATURES
# --------------------

X = []

for url in df["url"]:

    X.append(extract_features(url))

X = pd.DataFrame(
    X,
    columns=feature_names
)

# Type (0 = benign, 1 = defacement, 2 = malware, 3 = phishing)
y = df["type"]


# --------------------
# SPLIT DATA
# --------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)


# --------------------
# CREATE MODEL
# --------------------

model = RandomForestClassifier(n_estimators=100, random_state=42)


# --------------------
# TRAIN MODEL
# --------------------

model.fit(X_train, y_train)

print("\nTraining Complete")


# --------------------
# FEATURE IMPORTANCE
# --------------------

print("\nFeature Importance:")

importances = model.feature_importances_

for name, score in zip(feature_names, importances):
    print(f"{name}: {score:.4f}")


# --------------------
# PREDICTION
# --------------------

y_pred = model.predict(X_test)


# --------------------
# CONFUSION MATRIX
# --------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")

print(cm)


# --------------------
# CLASSIFICATION REPORT
# --------------------

print("\nClassification Report:")

report = classification_report(y_test, y_pred)
print(report)


# --------------------
# SAVE MODEL
# --------------------

joblib.dump(
    model,
    "../models/phishing_model.pkl"
)

joblib.dump(
    le,
    "../models/label_encoder.pkl"
)

joblib.dump(
    feature_names,
    "../models/features.pkl"
)

joblib.dump(report, "../models/report.pkl")
joblib.dump(cm, "../models/cm.pkl")

print("\nModel Saved")



# --------------------
# TEST URL
# --------------------

test_url = ("secure-paypal-login.com")

print("\nTesting URL:")

print(test_url)


test_features = (extract_features(test_url))
test_df = pd.DataFrame([test_features], columns=feature_names)

prediction = model.predict(test_df)
result = (le.inverse_transform(prediction)[0])

print("\nPrediction:", result)


# --------------------
# CONFIDENCE SCORE
# --------------------

probability = model.predict_proba(test_df)
confidence = (max(probability[0]) * 100)

print(f"Confidence: " f"{confidence:.2f}%")