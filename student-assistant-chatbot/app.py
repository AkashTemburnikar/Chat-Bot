import os
import gradio as gr
from transformers import pipeline
from faq_loader import FAQIndex

# Keep CPU-safe on macOS; allow MPS to fall back cleanly
os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

MODEL_NAME = "google/flan-t5-base"

gen = pipeline(
    task="text2text-generation",
    model=MODEL_NAME,
    device=-1,           # CPU
)

SYSTEM_STYLE = (
    "You are a helpful student assistant. Be concise, practical, and friendly. "
    "If a question needs school-specific dates/policies, say you don't know and suggest where to check "
    "(registrar site, academic calendar, student portal, or advisor). "
    "Prefer short bullet points when listing steps."
)

# Build the small FAQ retriever
faq = FAQIndex("data/faq.json", min_score=0.45)

def build_prompt(user_msg: str) -> str:
    return (
        f"{SYSTEM_STYLE}\n\n"
        "QUESTION:\n"
        f"{user_msg.strip()}\n\n"
        "ANSWER:"
    )

def respond(message, history):
    # 1) Try fast FAQ hit
    hit = faq.search(message)
    if hit:
        q, a, score = hit
        # If the match is strong enough, return it directly
        if score >= 0.78:
            return a

        # Otherwise, use it as context to guide the LLM
        guided = (
            f"{SYSTEM_STYLE}\n\n"
            f"Here is a relevant FAQ pair to help you answer. If it looks applicable, use it. "
            f"If not, answer generally and note that school-specific rules may vary.\n\n"
            f"FAQ_QUESTION: {q}\n"
            f"FAQ_ANSWER: {a}\n\n"
            f"USER_QUESTION: {message}\n\n"
            f"ANSWER:"
        )
        try:
            out = gen(
                guided,
                max_new_tokens=180,
                do_sample=False,
                num_beams=4,
                repetition_penalty=1.1,
            )[0]["generated_text"].strip()
            if "ANSWER:" in out:
                out = out.split("ANSWER:", 1)[-1].strip()
            return out or a
        except Exception as e:
            # Fallback to the FAQ answer if model errors
            return a + f"\n\n_(Model fallback due to: {type(e).__name__})_"

    # 2) No FAQ match → pure LLM
    try:
        out = gen(
            build_prompt(message),
            max_new_tokens=180,
            do_sample=False,
            num_beams=4,
            repetition_penalty=1.1,
        )[0]["generated_text"].strip()
        if "ANSWER:" in out:
            out = out.split("ANSWER:", 1)[-1].strip()
        return out or "Sorry, I couldn't generate a good reply. Try rephrasing the question."
    except Exception as e:
        return f"Oops—model error: {type(e).__name__}: {e}"

chat = gr.ChatInterface(
    fn=respond,
    title="🎓 Student Assistant Chatbot",
    description="Ask questions about registration, financial aid, tutoring, advising, or general campus info.",
    textbox=gr.Textbox(placeholder="Type a message…"),
    retry_btn="Regenerate",
    undo_btn="Undo last",
    clear_btn="Clear chat",
    concurrency_limit=2,
    theme="soft"
)

if __name__ == "__main__":
    chat.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        max_threads=4,
    )