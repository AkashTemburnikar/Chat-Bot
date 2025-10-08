Here’s the complete README.md file content for your version (the one using flan-t5-base and faq_loader.py).
You can copy-paste this directly into your project as README.md:

⸻

🎓 Student Assistant Chatbot

A lightweight, local Gradio chatbot that helps students answer academic and campus-related questions using a hybrid approach — combining a FAQ-based retriever with a language model (google/flan-t5-base).

⸻

🧠 Overview

This chatbot:
	•	Retrieves answers from a local FAQ database (data/faq.json) using TF-IDF similarity.
	•	Uses FLAN-T5 (a lightweight instruction-tuned model) to generate responses when:
	•	No FAQ entry matches closely, or
	•	The match is weak and needs more context.
	•	Provides concise, friendly, and practical answers while reminding users to check official sources for school-specific details.

⸻

📁 Project Structure

student-assistant-chatbot/
├── app.py              # Main app – combines FAQ + model + Gradio chat UI
├── faq_loader.py       # TF-IDF based FAQ retriever
├── data/
│   └── faq.json        # Your editable FAQ file
└── requirements.txt    # Dependencies (with macOS-safe versions)


⸻

⚙️ Features

✅ Hybrid answering system — combines local FAQ retrieval and text generation
✅ Offline-friendly — all computation runs locally (no cloud API calls)
✅ Model fallback — gracefully falls back to model-only mode if no FAQ matches
✅ Practical responses — short, friendly, and focused
✅ Easy customization — edit or extend data/faq.json anytime

⸻

🚀 Quick Start

1️⃣ Setup Virtual Environment

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

Step 1 — FAQ Search

faq_loader.py uses TF-IDF vectorization to find the most similar question in faq.json.
	•	If score ≥ 0.78 → returns FAQ answer directly
	•	If 0.45 ≤ score < 0.78 → uses the FAQ Q/A as context for the model
	•	If score < 0.45 → ignores FAQ and uses LLM response

Step 2 — Model Response

If needed, flan-t5-base generates an answer guided by a system prompt:

“You are a helpful student assistant. Be concise, practical, and friendly…”

Step 3 — Output

The chatbot shows the final response in Gradio’s web chat interface.

⸻

🗃️ FAQ Customization

You can add, edit, or remove FAQ entries inside data/faq.json:

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

	•	Use plain text.
	•	Avoid embedding links to school systems unless necessary.
	•	Keep it general so the chatbot’s model can adapt.

⸻

💡 Example Questions (Not in FAQ)

Ask open-ended, non-policy questions like:
	•	“What are some good ways to manage stress before exams?”
	•	“How can I write a polite email to a professor?”
	•	“Any tips for effective group study?”
	•	“How can I stay organized with multiple classes?”
	•	“What’s the best way to prepare for midterms?”

These prompts work better for model-based responses.

⸻

🧩 Requirements

requirements.txt

gradio==4.44.1
gradio-client==1.3.0
transformers==4.44.2
torch==2.1.2
scikit-learn==1.4.2
numpy<2

Make sure you’re using Python 3.9 or later, ideally 3.9.6 for macOS compatibility.

⸻

🧰 Troubleshooting

Issue	Fix
❌ `TypeError: unsupported operand type(s) for	`
⚠️ NumPy crash	pip install "numpy<2" --force-reinstall
⚠️ ModuleNotFoundError: No module named 'sklearn'	Install via pip install scikit-learn==1.4.2
⚠️ Invalid HTTP request received	Harmless; ignore if the app runs fine
⚠️ Slow model load	First-time download; cached afterward under ~/.cache/huggingface


⸻

🧠 Technical Summary

Component	Purpose
TF-IDF Retriever	Matches similar FAQ questions using cosine similarity
Flan-T5 Model	Generates general or guided answers
Gradio ChatInterface	Provides the user-friendly web chat UI
Hybrid Logic	Chooses between FAQ and model depending on similarity score


⸻

🧑‍💻 Author Notes
	•	Built for educational demo purposes (HCI group project).
	•	Fully local and self-contained (no external API dependencies).
	•	Modular — easily replace flan-t5-base with another text2text-generation model.

⸻

📜 License

Open for educational or personal use. Add your institution or author credits if required for submission.