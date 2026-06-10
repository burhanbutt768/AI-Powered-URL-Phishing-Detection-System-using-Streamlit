import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# ------------------
# PAGE CONFIG
# ------------------

st.set_page_config(
    page_title="AI Cybersecurity Dashboard",
    layout="wide"
)

# ------------------
# LOAD FILES
# ------------------

model = joblib.load(
    "../models/phishing_model.pkl"
)

encoder = joblib.load(
    "../models/label_encoder.pkl"
)

feature_names = joblib.load(
    "../models/features.pkl"
)

report = joblib.load(
    "../models/report.pkl"
)

cm = joblib.load(
    "../models/cm.pkl"
)

dataset = pd.read_csv(
    "../data/phishing_dataset.csv"
)

# ------------------
# HISTORY
# ------------------

if "history" not in st.session_state:
    st.session_state.history = []

# ------------------
# FEATURE EXTRACTION
# ------------------

def extract_features(url):

    return [

        len(url),

        url.count("."),

        url.count("-"),

        url.count("@"),

        sum(
            c.isdigit()
            for c in url
        ),

        1 if "https" in url else 0,

        1 if "login" in url.lower() else 0,

        1 if "secure" in url.lower() else 0,

        1 if "bank" in url.lower() else 0,

        url.count("//")
    ]

# ------------------
# SIDEBAR
# ------------------

with st.sidebar:

    st.title("🛡️ Dashboard")

    st.info("""
AI URL Threat Detection

Model:
Random Forest

Classes:
Benign
Defacement
Malware
Phishing
""")

    st.metric(
        "Dataset Size",
        len(dataset)
    )

# ------------------
# TITLE
# ------------------

st.title(
    "🛡️ AI Cybersecurity Dashboard"
)

# ------------------
# TABS
# ------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([

    "🔍 Detection",

    "📊 Dataset",

    "📈 Performance",

    "⚙️ Features",

    "📝 History"
])

# ==================================================
# TAB 1
# ==================================================

with tab1:

    st.header(
        "URL Detection"
    )

    url = st.text_input(
        "Enter URL"
    )

    if st.button(
        "Analyze"
    ):

        values = extract_features(
            url
        )

        df = pd.DataFrame(

            [values],

            columns=feature_names
        )

        pred = model.predict(
            df
        )

        result = (
            encoder
            .inverse_transform(
                pred
            )[0]
        )

        prob = model.predict_proba(
            df
        )

        confidence = (
            max(prob[0]) * 100
        )

        st.success(
            f"Prediction: {result}"
        )

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        st.progress(
            confidence / 100
        )

        st.subheader(
            "Extracted Features"
        )

        st.dataframe(df)

        st.session_state.history.append({

            "URL": url,

            "Prediction": result,

            "Confidence":
                round(confidence, 2)
        })

# ==================================================
# TAB 2
# ==================================================

with tab2:

    st.header(
        "Dataset Analytics"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total URLs",
            len(dataset)
        )

    with col2:

        st.metric(
            "Unique URLs",
            dataset["url"].nunique()
        )

    st.subheader(
        "Class Distribution"
    )

    counts = (
        dataset["type"]
        .value_counts()
    )

    fig, ax = plt.subplots()

    ax.pie(
        counts,
        labels=counts.index,
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

    st.subheader(
        "Distribution Chart"
    )

    fig2, ax2 = plt.subplots()

    counts.plot(
        kind="bar",
        ax=ax2
    )

    st.pyplot(fig2)

    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(
        dataset.head(20)
    )

# ==================================================
# TAB 3
# ==================================================

with tab3:

    st.header(
        "Model Performance"
    )

    st.subheader(
        "Classification Report"
    )

    st.text(report)

    st.subheader(
        "Confusion Matrix"
    )

    st.dataframe(
        pd.DataFrame(cm)
    )

# ==================================================
# TAB 4
# ==================================================

with tab4:

    st.header(
        "Feature Importance"
    )

    importance = (
        model.feature_importances_
    )

    imp_df = pd.DataFrame({

        "Feature":
            feature_names,

        "Importance":
            importance
    })

    st.dataframe(
        imp_df
    )

    fig3, ax3 = plt.subplots()

    ax3.barh(

        feature_names,

        importance
    )

    st.pyplot(fig3)

# ==================================================
# TAB 5
# ==================================================

with tab5:

    st.header(
        "Prediction History"
    )

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df
    )

    if not history_df.empty:

        csv = history_df.to_csv(
            index=False
        )

        st.download_button(

            "Download CSV",

            csv,

            file_name="prediction_history.csv",

            mime="text/csv"
        )