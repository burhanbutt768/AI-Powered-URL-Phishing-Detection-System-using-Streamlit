🛡️ AI-Powered URL Threat Detection System

An AI-powered cybersecurity project that analyzes URLs and classifies them into multiple threat categories using Machine Learning.

The system leverages a Random Forest Classifier trained on a malicious URL dataset and provides an interactive dashboard for URL analysis, model evaluation, and feature inspection.


📌 Overview

Cybercriminals frequently use malicious URLs to conduct phishing attacks, distribute malware, and compromise user accounts.

This project aims to detect potentially harmful URLs by extracting structural features from URLs and applying Machine Learning techniques to classify them into different categories.

URL Categories

* Benign
* Defacement
* Malware
* Phishing


🚀 Features

🔍 URL Threat Detection

* Real-time URL analysis
* Multi-class URL classification
* Confidence score generation
* Instant prediction through dashboard

📊 Dataset Analytics

* Dataset overview
* Class distribution visualization
* Dataset preview table

📈 Model Performance Evaluation

* Classification Report
* Confusion Matrix
* Performance metrics visualization

⚙️ Feature Analysis

* URL feature extraction
* Feature importance ranking
* Model interpretability

📝 Prediction History

* Track analyzed URLs
* Export prediction history as CSV


🧠 Machine Learning Pipeline

1. Data Collection

The project uses a labeled malicious URL dataset containing URLs categorized as:

* Benign
* Defacement
* Malware
* Phishing

2. Data Preprocessing

Performed the following preprocessing steps:

* Missing value removal
* Duplicate record removal
* Label encoding

3. Feature Engineering

The following features are extracted from each URL:

| Feature        | Description                   |
| -------------- | ----------------------------- |
| URL Length     | Total length of URL           |
| Dots           | Number of "." characters      |
| Hyphens        | Number of "-" characters      |
| @ Symbol       | Presence of "@"               |
| Digits         | Count of numerical characters |
| HTTPS          | HTTPS usage                   |
| Login Keyword  | Presence of "login"           |
| Secure Keyword | Presence of "secure"          |
| Bank Keyword   | Presence of "bank"            |
| Double Slash   | Count of "//"                 |

4. Model Training

Algorithm Used:

RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

The dataset is split into:

* 70% Training Data
* 30% Testing Data

using stratified sampling.


🖥️ Dashboard Features

The Streamlit dashboard includes:

URL Detection

* URL input
* Threat prediction
* Confidence score
* Extracted feature table

Dataset Analytics

* Dataset size
* Unique URLs
* Class distribution charts

Model Performance

* Classification Report
* Confusion Matrix

Feature Analysis

* Feature importance chart
* Most influential features

Prediction History

* Track previous predictions
* Download results as CSV

🛠️ Technologies Used

Programming Language: Python

Libraries

* Pandas
* Scikit-Learn
* Streamlit
* Matplotlib
* Joblib


📂 Project Structure


AI-URL-Threat-Detector/
│
├── data/
│   └── phishing_dataset.csv
│
├── models/
│   ├── phishing_model.pkl
│   ├── label_encoder.pkl
│   ├── features.pkl
│   ├── report.pkl
│   └── cm.pkl
│
├── src/
│   ├── train.py
│   └── dashboard.py
│
└── README.md


⚡ Installation

Clone the repository: git clone https://github.com/burhanbutt768/AI-URL-Phishing-Detection-System-using-Streamlit.git

cd AI-URL-Phishing-Detection-System-using-Streamlit


🏋️ Training the Model

Run: bash/terminal -> python src/train.py

This will:

* Train the Random Forest model
* Generate classification report
* Generate confusion matrix
* Save trained models



📊 Running the Dashboard


bash/terminal: streamlit run src/dashboard.py

Open: http://localhost:8501



📈 Future Improvements

* Browser Extension
* Batch URL Scanning
* Threat Intelligence Integration
* URL Reputation APIs
* Deep Learning Models
* Explainable AI (XAI)
* Real-Time Monitoring


🎯 Learning Outcomes

Through this project I gained practical experience in:

* Data Cleaning
* Feature Engineering
* Machine Learning Pipelines
* Model Evaluation
* Cybersecurity Analytics
* Dashboard Development
* Streamlit Deployment


👨‍💻 Author

Burhan Abid

BS Computer Science

Aspiring AI & Cybersecurity Engineer


⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub and sharing your feedback.
