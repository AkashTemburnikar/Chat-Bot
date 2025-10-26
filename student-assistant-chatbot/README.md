# 🎓 Student Assistant Chatbot

A lightweight **local Gradio chatbot** that helps students answer academic and campus-related questions using a **hybrid approach** — combining a FAQ-based retriever with a lightweight language model (`google/flan-t5-base`).

---

## 🧠 Overview

This chatbot:

- Retrieves answers from a local FAQ database (`data/faq.json`) using **TF-IDF similarity**.  
- Uses **FLAN-T5**, an instruction-tuned model, to generate responses when:
  - No FAQ entry matches closely, **or**
  - The match is weak and needs more context.  
- Provides concise, friendly, and practical answers while reminding users to check official sources for school-specific details.

---

## 📁 Project Structure

student-assistant-chatbot/
├── app.py              # Main app – combines FAQ + model + Gradio chat UI
├── faq_loader.py       # TF-IDF based FAQ retriever
├── data/
│   └── faq.json        # Editable FAQ file
└── requirements.txt    # Dependencies (macOS-safe versions)

---

## ⚙️ Features

✅ Hybrid answering system — combines local FAQ retrieval + model generation  
✅ Offline-friendly — all computation runs locally (no cloud API calls)  
✅ Smart fallback — gracefully switches to model-only mode when needed  
✅ Concise, practical answers — focused and user-friendly  
✅ Easy customization — edit `data/faq.json` anytime  

---

## 🚀 Quick Start

### 1️⃣ Setup Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate

2️⃣ Install Dependencies

pip install -r requirements.txt

If you’re on macOS and see NumPy or MPS warnings:

pip install "numpy<2" --force-reinstall
export PYTORCH_ENABLE_MPS_FALLBACK=1

3️⃣ Run the App

python app.py

Then open your browser and go to:
👉 http://127.0.0.1:7860

⸻

💬 How It Works

🧩 Step 1 — FAQ Search

faq_loader.py uses TF-IDF vectorization to find the most similar question in faq.json.

Similarity Score	Action
≥ 0.78	Return FAQ answer directly
0.45 – 0.78	Use FAQ Q/A as context for model
< 0.45	Ignore FAQ and use LLM response

🤖 Step 2 — Model Response

If needed, flan-t5-base generates an answer guided by this system prompt:

“You are a helpful student assistant. Be concise, practical, and friendly…”

💬 Step 3 — Output

The chatbot shows the final response in Gradio’s ChatInterface.

⸻

🗃️ FAQ Customization

Edit data/faq.json to add or update entries:

[
  {
    "question": "How do I drop a class?",
    "answer": "Log into your student portal, open your schedule page, select the course, and choose Drop/Withdraw. Check deadlines on the academic calendar."
  },
  {
    "question": "How do I request transcripts?",
    "answer": "Go to the Registrar section in your portal and choose Official or Unofficial transcripts."
  }
]

📝 Tips:
	•	Use plain text.
	•	Avoid unnecessary external links.
	•	Keep it general so the model can adapt.

⸻

💡 Example Questions (Not in FAQ)

Ask open-ended or general questions such as:
	•	“What are some good ways to manage stress before exams?”
	•	“How can I write a polite email to a professor?”
	•	“Any tips for effective group study?”
	•	“How can I stay organized with multiple classes?”
	•	“What’s the best way to prepare for midterms?”

These trigger model-based responses.

⸻

🧩 Requirements

requirements.txt:

gradio==4.44.1
gradio-client==1.3.0
transformers==4.44.2
torch==2.1.2
scikit-learn==1.4.2
numpy<2

🐍 Use Python 3.9+ (3.9.6 recommended for macOS compatibility)


⸻

🧠 Technical Summary

Component	Purpose
TF-IDF Retriever	Matches similar FAQ questions using cosine similarity
Flan-T5 Model	Generates guided answers
Gradio ChatInterface	Provides web-based chat UI
Hybrid Logic	Chooses between FAQ and model depending on similarity


⸻

👨‍💻 Author Notes
	•	Built for educational demo purposes (HCI group project).
	•	Fully local — no external API dependencies.
	•	Modular — you can easily swap flan-t5-base with any text2text model.

⸻

📜 License

Open for educational or personal use.
Add your institution or author credits if required for submission.

⸻
