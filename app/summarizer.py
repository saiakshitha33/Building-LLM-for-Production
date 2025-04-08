from app.llm_utils import call_gpt

def summarize_text(text: str) -> str:
    prompt = f"""
    Summarize the following document in simple English. Highlight key takeaways:

    {text[:3500]}  # GPT-4 context safety
    """
    return call_gpt(prompt)