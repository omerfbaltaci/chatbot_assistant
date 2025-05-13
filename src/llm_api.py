import google.generativeai as genai
from src.config import API_KEY

genai.configure(api_key=API_KEY)

def ask_llm(question):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"API hatası: {e}"
