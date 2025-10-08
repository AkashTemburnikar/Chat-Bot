# 🎓 Student Assistant Chatbot

A lightweight, local-first **Student Assistant Chatbot** built with **Python**, **Gradio** and **Hugging Face Transformers**.  
It answers common questions about registration, advising, tutoring, financial aid, and general campus info using a hybrid approach:
1) **FAQ lookup** for fast, precise answers
2) **LLM generation** for general/unknown questions

> Demo UI (Gradio) runs locally by default and can be exposed securely for class demos.

---

## ✨ Features
- 🧠 FAQ-guided responses with similarity search (tunable threshold)
- 🤖 LLM (Transformers pipeline) fallback when FAQ isn’t sufficient
- 🖥️ Clean, responsive **Gradio** chat interface (Regenerate / Undo / Clear)
- 🔒 Optional **basic auth** when serving over a public IP
- 🧩 Easy to extend with campus‑specific policies and data

---

## 📦 Tech Stack
- Python 3.10+ (3.12 OK)
- [Gradio](https://gradio.app/) for the web UI
- [Transformers](https://huggingface.co/docs/transformers) for text generation
- [PyTorch](https://pytorch.org/) CPU wheels (works without GPU)
- NumPy < 2 for compatibility with some PyTorch builds

---

## 🔗 Repository
**Student Assistant Chatbot (subfolder in group repo):**  
`Group-Project-HCI/student-assistant-chatbot`

Parent repo (for reference):  
https://github.com/AkashTemburnikar/Group-Project-HCI/tree/main/student-assistant-chatbot

---

## 🧹 Clean Setup (Recommended)
Open your Terminal and run:
```bash
cd yourpath/student-assistant-chatbot
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
```

### 📦 Install dependencies
```bash
pip install -r requirements.txt
```
> If you see a **NumPy 2** warning later, it’s fine — we’ll fix it next.

### 🧠 Fix compatibility (NumPy < 2 for PyTorch)
```bash
pip install "numpy<2" --force-reinstall
```

### ⚙ Optional (recommended for macOS)
Enable CPU fallback for MPS (Metal backend):
```bash
export PYTORCH_ENABLE_MPS_FALLBACK=1
```

### 🚀 Run the chatbot
```bash
python app.py
```
After a few seconds you should see:
```
Running on local URL:  http://127.0.0.1:7860
```

### 🌐 Open it in your browser
Go to → `http://127.0.0.1:7860`  
You’ll see the **Student Assistant Chatbot** UI.

### 🧪 Test messages
Try typing:
- How do I drop a class?
- How can I change my major?
- When is the registration deadline?
- Where can I find tutoring?

### 🧰 (Optional) To stop the server
Press: `Ctrl + C`

---

## 💻 Quick-Start Commands (Ubuntu / WSL)
```bash
sudo apt update && sudo apt install -y git python3-venv python3-pip build-essential
git clone https://github.com/AkashTemburnikar/Group-Project-HCI.git
cd Group-Project-HCI/student-assistant-chatbot
python3 -m venv .venv && source .venv/bin/activate
python -m pip install -U pip setuptools wheel
pip install -r requirements.txt || true
pip install "numpy<2" --force-reinstall
# If torch install fails due to version pinning, install CPU wheels:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
python app.py
```

### macOS (Apple Silicon & Intel)
```bash
# If needed:
xcode-select --install
brew install git python  # or use your system Python 3.x

git clone https://github.com/AkashTemburnikar/Group-Project-HCI.git
cd Group-Project-HCI/student-assistant-chatbot
python3 -m venv .venv && source .venv/bin/activate
python -m pip install -U pip setuptools wheel
pip install -r requirements.txt || true
pip install "numpy<2" --force-reinstall
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
export PYTORCH_ENABLE_MPS_FALLBACK=1   # optional
python app.py
```

---

## 🌍 Public Access (Optional – for Demos)
If you want to reach the app from another device / public IP:

1. **Bind to all interfaces** in `app.py` (or via env vars):
   ```python
   chat.launch(
       server_name="0.0.0.0",
       server_port=7860,
       share=False,
       max_threads=4,
       auth=("student","ChangeMe!42"),   # or use env vars below
   )
   ```
   Or use environment variables:
   ```bash
   export CHATBOT_USER="student"
   export CHATBOT_PASS="ChangeMe!42"
   # (app.py reads CHATBOT_USER/PASS and sets auth automatically if present)
   ```

2. **Open firewall / security group** for TCP **7860** (or your chosen port).  
3. Visit: `http://<your-public-ip>:7860` and log in with your credentials.

> **Security tip:** Restrict access to trusted IPs or keep auth enabled for internet-facing demos.

---

## 🧪 Functional Test Plan (5–10 min)
- Exact FAQ: “How do I drop a class?” → fast, specific
- Near-match FAQ: “I want to withdraw from a course—what’s the process?”
- LLM-only: “What’s the best way to prepare for finals?”
- Policy nuance: “When is the deadline if I’m an international transfer student with scholarship?”
- Buttons: **Regenerate**, **Undo**, **Clear**
- Terminal: watch for errors and latency

---

## 🧯 Troubleshooting
- `ModuleNotFoundError` → ensure venv is active: `source .venv/bin/activate`
- Torch version pin fails → install CPU wheels from PyTorch index
- NumPy incompatibility → `pip install "numpy<2" --force-reinstall`
- Port already in use → `GRADIO_SERVER_PORT=7861 python app.py`
- No public access → bind `0.0.0.0` and open firewall / cloud security group

---

## 🧱 Project Structure
```
student-assistant-chatbot/
├─ app.py                 # Gradio UI + request handling
├─ prompts.py             # System style / prompt templates
├─ faq_loader.py          # Loads FAQ data & similarity search
├─ data/                  # FAQ JSON files
├─ requirements.txt
└─ README.md              # (this file)
```

---

## 🗺️ System Flow
> (Optional) Include a diagram like the one below in `/docs` and reference it here.
```
User Browser → Gradio UI → Request Router
             ↘ FAQ Search (threshold) → Compose Answer → UI
             ↘ LLM (Transformers/Torch) → Compose Answer → UI
```

---

## 🔧 Configuration
- **FAQ threshold** (similarity): tweak in `app.py` where `score >= 0.78`
- **Auth**: set `CHATBOT_USER` / `CHATBOT_PASS` or edit `chat.launch(auth=...)`
- **Port/host**: `CHATBOT_PORT`, `CHATBOT_HOST` env vars (if you added that snippet)

---

## 🙌 Contributing
1. Fork the repo and create a feature branch
2. Make changes with clear commit messages
3. Open a PR with a concise description and screenshots if applicable

---

## 📄 License
MIT (or your class/project’s preferred license).

---

## 👥 Credits
- Project team (HCI Group)
- Open-source libraries: Gradio, Transformers, PyTorch

_Last updated: 2025-10-08 02:51 UTC_
