import streamlit as st
import requests
import json

# Azure Translator API details
AZURE_KEY = "Your_Azure_Key"  # Replace with your Azure Translator key
AZURE_ENDPOINT = "https://api.cognitive.microsofttranslator.com/"
AZURE_REGION = "eastus"  # Example: "eastus"

# Function to translate text
def translate_text(text, target_lang):
    url = f"{AZURE_ENDPOINT}/translate?api-version=3.0&to={target_lang}"
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Ocp-Apim-Subscription-Region": AZURE_REGION,
        "Content-Type": "application/json",
    }
    body = [{"text": text}]
    
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        translation = response.json()
        return translation[0]["translations"][0]["text"]
    else:
        return "Error: Unable to translate text. Check API credentials."

# Streamlit UI
st.title("Azure Translator with Streamlit")

# User input
text_to_translate = st.text_input("Enter text to translate:")
target_language = st.selectbox("Select target language:", ["fr", "es", "de", "zh", "hi", "ta", "te", "ar", "ru", "ja"])

if st.button("Translate"):
    translated_text = translate_text(text_to_translate, target_language)
    st.success(f"Translated Text: {translated_text}")
