import json
import os

technical_keywords = [
"c#", ".net", "asp.net", "mvc", "razor", "entity framework", "asp",
    "viewbag", "viewdata", "controller", "model", "startup.cs", "configure", "linq",
    "taghelper", "dependency injection", "middleware", "async", "await", "partialview",
    "partial view",
]

def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def is_technical_question(question):
    question = question.lower()
    return any(keyword in question for keyword in technical_keywords)

def truncate(text, max_len=500):
    return text[:max_len] + "..." if len(text) > max_len else text
