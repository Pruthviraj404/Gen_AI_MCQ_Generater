# Gen_AI_MCQ_Generater

A **Streamlit-based Generative AI application** that automatically generates Multiple Choice Questions (MCQs) from a PDF using **Groq LLMs**.

This project is useful for:

* Students preparing exam questions
* Teachers creating practice tests
* Anyone converting study material into MCQs quickly

---

## 🚀 Features

* 📄 Upload PDF files
* 🧠 Automatically extracts text from PDF
* ✍️ Generates **5 MCQs** based on the content
* 🎯 Select difficulty level (Easy / Medium / Hard)
* 📦 Uses **Groq LLM (LLaMA 3.3 70B)**
* 🔐 Secure API key handling using `.env`
* 🖥️ Simple and clean Streamlit UI

---

## 🗂️ Project Structure

```
GenAI_MCQ_Generator/
│
├── app.py               # Streamlit app entry point
├── generate.py          # MCQ generation logic (Groq API)
├── text_extrater.py     # PDF text extraction utilities
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (API key)
├── .gitignore           # Ignored files (venv, secrets, cache)
└── README.md            # Project documentation
```

---

## 🧑‍💻 Tech Stack

* **Python 3.10+**
* **Streamlit** – frontend UI
* **Groq SDK** – LLM inference
* **PyPDF / PDFMiner** – PDF text extraction
* **JSON** – structured MCQ output

---

## 🔑 Environment Setup (IMPORTANT)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Pruthviraj404/Gen_AI_MCQ_Generater.git
cd GenAI_MCQ_Generator
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Groq API Key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

⚠️ **Never push your API key to GitHub**

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser.

---

---

## 🧪 How It Works

1. Upload a PDF
2. Text is extracted automatically
3. Groq LLM generates MCQs in strict JSON format
4. MCQs are displayed in the UI
5. Answers can be hidden or shown as required

---
