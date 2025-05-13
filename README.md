## C# Chatbot Assistant

This project is an embedding-based chatbot system designed to answer questions related to C#/.NET technologies. If a similar question is not found in the dataset, it queries the Google Gemini API to generate a short and technical response, then saves the new question-answer pair to the dataset and updates the embedding index.

---

## Features

```
- Embedding-based similarity search using FAISS
- Technical answer generation with Gemini 2.0 Flash
- JSON-based data storage (questions and answers)
- Automatic dataset updating
- Keyword filtering to detect technical questions
- Docker support
```

---

## Project Structure

```
chatbot_assistant/
├── data/
│   ├── data.json
│   └── extended_data.json
├── src/
│   └── app.py
├── README.md
├── requirements.txt
├── venv/
```

---

## Installation (Manual)

### 1. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Variables

Create a `.env` file and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

### 3. Run the App

```bash
python app.py
```

---

## Running with Docker

### 1. Create a Dockerfile

Place the following `Dockerfile` in the root directory:

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
```

### 2. `requirements.txt`

```txt
faiss-cpu
sentence-transformers
python-dotenv
google-generativeai
numpy
```

### 3. Build and Run the Container

```bash
docker build -t csharp-chatbot .
docker run --env GEMINI_API_KEY=your_api_key_here -it csharp-chatbot
```

> Note: You cannot directly pass the `.env` file to Docker. You must pass the API key using the `--env` parameter.

