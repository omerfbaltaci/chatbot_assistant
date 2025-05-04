````markdown
# Acunmedya Akademi Chatbot

A lightweight chatbot project developed to help students at Acunmedya Akademi quickly get answers to frequently asked questions using semantic similarity.

---

## 🚀 What's New

This is an improved version of the initial rule-based chatbot that only relied on simple keyword matching and NLTK preprocessing.  
The initial version **did not use any embedding** or similarity calculation.

Key enhancements in this version:

- ✅ Integrated **MiniLM-L12** model from `sentence-transformers` for semantic understanding.
- ✅ Embedded all questions using pre-trained language model for better representation.
- ✅ Applied **cosine similarity** to match user questions with dataset questions.
- ✅ Much higher flexibility in recognizing varied question forms (paraphrases, rewordings, etc).

---

## ⚙️ Installation & Usage

!! At this version, there is a problem which causing embedding scores to be too low. Trying to fix. !!

To get started with the project:

1. Clone the repository or download the files manually.
2. Make sure Python 3.7+ is installed.
3. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
    ````

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the chatbot using:

   ```bash
   python chatbot.py
   ```

---

## 📦 Example `requirements.txt`

Your `requirements.txt` should include:

```
sentence-transformers
torch
```

Add any other packages you used (e.g., `nltk` if you still use some preprocessing features).

---

## 🔮 Future Plans

This project is the foundation for a broader goal.

Planned enhancements:

* Integration with **OpenAI API** for richer and more intelligent responses.
* Developing a **web or mobile interface** for better accessibility.
* Expanding the dataset to cover more diverse and detailed academic questions.
* Deployment within the **Acunmedya Akademi** as an internal student support tool.

This chatbot is expected to evolve into a full-featured assistant tailored for educational environments.

---