# Azure Translator with Streamlit 🌐🚀

This project demonstrates how to build a simple translation app using **Azure Translator** and **Streamlit**.  
It takes user input text, detects the source language, and translates it into the selected target language.

---

## 🚀 Prerequisites

Before you begin, make sure you have:

- A **Microsoft Azure account**.
- An **Azure Translator key** from [Azure Cognitive Services](https://portal.azure.com/).
- Python installed (`>=3.7`).
- Basic packages installed: `streamlit`, `requests`.

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/jms-luck/Azure-Translator.git
cd Azure-Translator
```

### 2. Install required packages

```bash
pip install streamlit requests
```

### 3. 🔑 Setting up Azure Translator Key

- Go to the Azure Portal.
- Search for "Cognitive Services" and create a Translator resource.
- After creation, go to the Keys and Endpoint section.
- Note down:

  - Key (Subscription Key)
  - Endpoint URL
  - Region (example: eastus, southeastasia)

Example:

```makefile
Key:       YOUR_AZURE_TRANSLATOR_KEY
Endpoint:  https://api.cognitive.microsofttranslator.com/
Region:    YOUR_REGION
```

---

## 📄 How to Run the App

In your terminal, run:

```bash
streamlit run app.py
```

It will open a local server like:

```
Local URL: http://localhost:8501
```

---

## 🌟 Example

**Input:**

```
Text: Bonjour tout le monde
Target Language Code: en
```

**Output:**

```
Translation: Hello everyone
```

---

## 📚 Notes

- Language Codes are based on ISO codes: Supported Languages List.
- Make sure your Azure key and endpoint are valid.
- **Never expose your Azure Key publicly.** Use environment variables or `secrets.toml` for production deployment.

---

## 📜 License

This project is licensed under the MIT License.
