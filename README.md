# local-ai-assistant-ollama
A Flask-based Local AI Assistant powered by LangChain, Ollama, and the Gemma 3 (1B) LLM, featuring a modern responsive UI for private, offline AI interactions.

# 🤖 Local AI Assistant using Ollama & Gemma 3

A lightweight AI Assistant built with **Flask**, **LangChain**, and **Ollama**, powered by the **Gemma 3 (1B)** pretrained Large Language Model (LLM).

This project demonstrates how to integrate a locally hosted LLM into a Flask web application with a clean, modern interface. The application performs **100% local inference**, ensuring privacy, fast response times, and no dependency on external AI APIs.

---

## 📸 Application Preview

<p align="center">
  <img src="screenshots/homepage.png" alt="Local AI Assistant UI" width="900">
</p>

---

## 📖 Overview

The Local AI Assistant enables users to interact with a locally running **Gemma 3 (1B)** model through a responsive web interface.

Using **LangChain** for prompt orchestration and **Ollama** for local model serving, the application processes user questions and generates AI-powered responses directly on your machine without requiring an internet connection or an API key.

This project is ideal for developers learning:

- Large Language Models (LLMs)
- LangChain
- Ollama
- Flask
- AI-powered Web Applications
- Prompt Engineering

---

## ✨ Features

- 🤖 Local AI inference using Ollama
- 🧠 Powered by Google's Gemma 3 (1B) model
- 💬 Interactive Question & Answer interface
- ⚡ Fast local response generation
- 🔒 Completely private (no cloud APIs)
- 🌐 Responsive Flask web application
- 🎨 Modern dark-themed UI
- 📦 Lightweight and easy to run
- 🛠 Beginner-friendly project structure

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Flask | Backend Web Framework |
| LangChain | Prompt Management |
| Ollama | Local LLM Runtime |
| Gemma 3 (1B) | Pretrained Language Model |
| HTML5 | Frontend |
| CSS3 | Styling |

---

## ⚙️ How It Works

1. User enters a question.
2. Flask receives the request.
3. LangChain formats the prompt.
4. Ollama sends it to the Gemma 3 model.
5. Gemma generates the response locally.
6. Flask renders the answer back to the browser.

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/local-ai-assistant-ollama.git
cd local-ai-assistant-ollama
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download Ollama

https://ollama.com/download

### Download Gemma 3 Model

```bash
ollama pull gemma3:1b
```

### Start Ollama

```bash
ollama serve
```

### Run the Application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```text
local-ai-assistant-ollama/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│     └── index.html
│
├── screenshots/
│     └── homepage.png
│
└── static/
```

---

## 🔒 Privacy

Since the model runs locally using Ollama:

- No OpenAI API Key required
- No external API calls
- Offline capable
- Better data privacy
- Faster inference for local workloads

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Flask Web Development
- LangChain Prompt Pipelines
- Ollama Integration
- Local Large Language Models
- Prompt Engineering
- Responsive Frontend Design

---

## 🚀 Future Improvements

- 💬 Chat History
- 📋 Copy Response Button
- 🎤 Voice Input
- 📄 Export Chat as PDF
- 📂 PDF Question Answering (RAG)
- 🌐 Multiple Model Selection
- 🌙 Light/Dark Theme Toggle

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

## 📄 License

This project is licensed under the MIT License.

# ⭐ If you found this project useful

If you like this project, consider giving it a ⭐ on GitHub!

---

# 📄 License

This project is licensed under the MIT License.
