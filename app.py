import streamlit as st
import joblib

st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)

@st.cache_resource
def load_model():
    return joblib.load("email_spam_nb_model.pkl")

model = load_model()

st.title("📧 Email Spam Detection")
st.write("Classify an email as Spam or Not Spam using Naive Bayes.")

subject = st.text_input("Email Subject")
message = st.text_area("Email Body", height=180)

if st.button("Check Email"):
    email_text = (subject.strip() + " " + message.strip()).strip()

    if not email_text:
        st.warning("Please enter an email subject or body.")
    else:
        prediction = model.predict([email_text])[0]

        if prediction == "spam":
            st.error("⚠️ Prediction: SPAM")
        else:
            st.success("✅ Prediction: NOT SPAM (HAM)")

st.caption(
    "Academic demonstration only. Predictions are not a guarantee "
    "that an email is safe or malicious."
)
