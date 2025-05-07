# Acunmedya Akademi Chatbot

A lightweight chatbot project developed to help students at Acunmedya Akademi quickly get answers to frequently asked questions using semantic similarity.

---

## What's New

This is an improved version of the initial rule-based chatbot that only relied on simple keyword matching and NLTK preprocessing.  
The initial version **did not use any embedding** or similarity calculation.

Key enhancements in this version:

- ✅ Integrated **MiniLM-L12** model from `sentence-transformers` for semantic understanding.
- ✅ Embedded all questions using a pre-trained language model for better semantic representation.
- ✅ Applied **cosine similarity** to match user questions with dataset questions.
- ✅ Higher flexibility in recognizing reworded or paraphrased student questions.

---

## 🐳 Running with Docker (Recommended)

To ensure a consistent environment across different machines, you can run this chatbot using Docker.

### Step-by-step Instructions

1. **Clone the repository or download the source files manually.**

2. **Make sure [Docker](https://www.docker.com/products/docker-desktop/) is installed on your system.**

3. **Open a terminal in the project root folder (where `app.py` or `chatbot.py` and `requirements.txt` exist).**

4. **Build the Docker image:**

   ```bash
   docker build -t chatbot_assistant .
   ```

5. **Run the Docker container interactively:**

   ```bash
   docker run -it chatbot_assistant
   ```

Or instead of building and running that Docker image, you can;

1. **Download the required libraries**, by using:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the chatbot.py while you are in the project folder** by using;

   ```bash
   python3 chatbot.py
   ```

---

## Example `requirements.txt`

Your `requirements.txt` should include:

```
sentence-transformers
torch
```

If you use additional libraries like `nltk` for preprocessing, make sure they are also listed.

---

## Future Plans

This chatbot is the foundation for a broader goal.

Planned enhancements:

- Integration with **OpenAI API** for more advanced and intelligent responses.
- Development of a **web or mobile interface** to make the chatbot more accessible.
- Dataset expansion to cover more diverse and complex academic questions.
- Deployment within **Acunmedya Akademi** as a real-time student support tool.

This project is expected to evolve into a powerful assistant tailored for educational environments.

---
