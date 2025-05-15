from src.config import API_KEY
from openai import OpenAI

client = OpenAI(api_key=API_KEY)

def ask_llm(question):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "Bir C#, .NET, .NET Core asistanı olarak kısa ve öz cevaplar ver. Başka bir konuda soru sorulursa cevap verme"},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"API hatası: {e}"
