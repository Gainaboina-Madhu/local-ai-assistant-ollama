# local-ai-assistant-ollama
A Flask-based Local AI Assistant powered by LangChain, Ollama, and the Gemma 3 (1B) LLM, featuring a modern responsive UI for private, offline AI interactions.


# 🤖 Local AI Assistant using Ollama & Gemma 3

A lightweight AI Assistant built with **Flask**, **LangChain**, and **Ollama**, powered by the **Gemma 3 (1B)** pretrained Large Language Model (LLM).

This application allows users to interact with a locally hosted AI model through a clean and responsive web interface. Since the model runs entirely on your machine using Ollama, **no cloud API or OpenAI API key is required**, ensuring privacy, fast response times, and offline capability.

---

## 📖 Project Description

This project demonstrates how to integrate a **local Large Language Model (LLM)** into a Flask web application using **LangChain** and **Ollama**.

The user enters a question in the web interface, which is processed through a LangChain prompt pipeline and sent to the locally running **Gemma 3 (1B)** model. The AI-generated response is then displayed back to the user in real time.

This project is suitable for learning:

- Local LLM deployment
- LangChain prompt pipelines
- Flask web development
- AI application development
- Ollama integration

---

# 📸 Application Preview

![Application UI](screenshots/homepage.png)

---

# ✨ Features

- 🤖 Local AI inference using Ollama
- 💬 Interactive question-answer interface
- 🧠 Powered by Gemma 3 (1B)
- ⚡ Fast local responses
- 🔒 No external API calls
- 🌐 Simple Flask web application
- 🎨 Clean and modern responsive UI
- 🛠 Easy to extend for future AI projects

---

# 🚀 Tech Stack

- Python
- Flask
- LangChain
- Ollama
- Gemma 3 (1B)
- HTML5
- CSS3

---

# 📂 Project Structure

```text
local-ai-assistant-ollama/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│      └── index.html
│

```

---

# ⚙️ How It Works

1. User enters a question in the web interface.
2. Flask receives the request.
3. LangChain formats the prompt.
4. Ollama sends the prompt to the Gemma 3 model.
5. The model generates a response locally.
6. Flask displays the response back to the user.

---

# 🛠 Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/local-ai-assistant-ollama.git

cd local-ai-assistant-ollama
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download and install Ollama from:

https://ollama.com/download

---

## 5. Download Gemma 3 Model

```bash
ollama pull gemma3:1b
```

---

## 6. Start Ollama

```bash
ollama serve
```

---

## 7. Run Flask Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 💡 Example

### User Question

```
Explain Artificial Intelligence.
```

### AI Response

```
Artificial Intelligence (AI) is a branch of computer science that enables machines to simulate human intelligence by learning from data, recognizing patterns, solving problems, and making decisions.
```

---

# 📦 Requirements

- Python 3.10+
- Flask
- LangChain
- LangChain-Ollama
- Ollama
- Gemma 3 (1B)

---

# 🔒 Privacy

Unlike cloud-based AI services, this application performs inference **entirely on your local machine**.

Benefits include:

- No API keys required
- Offline usage
- Faster local inference
- Better data privacy
- No user prompts sent to external servers

---

# 📈 Future Improvements

- 💬 Chat history
- 🌙 Light/Dark mode toggle
- 📋 Copy response button
- 🎤 Voice input
- 📄 Export conversation as PDF
- 📚 Retrieval-Augmented Generation (RAG)
- 📂 Upload PDF and ask questions
- 🌐 Multi-model support (Llama, Mistral, Gemma)

---

# 🎯 Learning Outcomes

This project helped demonstrate practical knowledge of:

- Building AI-powered web applications
- Integrating LangChain with local LLMs
- Running Large Language Models using Ollama
- Prompt engineering fundamentals
- Flask backend development
- Frontend design with HTML & CSS

---

# 👨‍💻 Author

**Your Name**

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# ⭐ If you found this project useful

If you like this project, consider giving it a ⭐ on GitHub!

---

# 📄 License

This project is licensed under the MIT License.
