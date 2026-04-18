# 🔥 Code Roaster

> *"I've seen rootkits with more integrity."* — TheFox

AI-powered code review with attitude. Get your code roasted by Aiden Pearce (TheFox) using local AI.

![Screenshot](https://github.com/user-attachments/assets/3ca8ab84-bad0-4888-9d99-d83e129945c1)

## 🎮 Features

- **Watch Dogs CTOS Aesthetic** — Dark terminal UI with cyan accents
- **Aiden Pearce Persona** — Cold, surgical code analysis from TheFox himself
- **Local AI** — Runs on your machine with Ollama (no API keys needed)
- **Fast Models** — Optimized for 8-16GB RAM systems
- **Caching** — Don't wait for the same roast twice
- **Rate Limiting** — Prevent abuse

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- [Ollama](https://ollama.com) installed
- 8GB+ RAM recommended

### Installation

```bash
git clone https://github.com/yourusername/code-roaster.git
cd code-roaster
pip install -r requirements.txt

# Pull a fast model (choose one)
ollama pull phi4-mini        # Recommended - fast & snarky
ollama pull llama3.2:1b      # Ultra fast
ollama pull qwen2.5:3b       # Higher quality, slower
```

### Configuration

```bash
# Copy example config
cp .env.example .env

# Edit .env to set your model
MODEL=phi4-mini
```

### Run

```bash
python web_app.py
```

Open http://localhost:5000

## 🐳 Docker

```bash
docker build -t code-roaster .
docker run -p 5000:5000 -e MODEL=phi4-mini code-roaster
```

## 🖥️ CLI Mode

Roast from terminal:

```bash
# Single file
python roaster.py myfile.py

# Directory
python roaster.py ./my-project --all

# Specific extensions
python roaster.py ./project --ext .py .js .ts
```


## 📸 Screenshots

| CTOS Interface | Aiden Roasting |
|---------------|----------------|
| ![UI](https://github.com/user-attachments/assets/aacb6bda-7a9d-4dc1-97c2-08228d5a954f) | ![Roast](https://github.com/user-attachments/assets/c438b8fd-5c72-4f06-ae41-8f127bdd0acb) |
## 🦊 TheFox's Roast Style

- *"I'm profiling you now..."*
- *"Easier to hack than a ctOS traffic light"*
- *"This code wouldn't last a day on the South Side"*
- *"I've backdoored servers with better architecture"*

## 🔧 Supported Languages

- Python
- JavaScript / TypeScript
- Java
- C / C++
- Go
- Rust
- Ruby

## 📝 License

MIT — Do what you want, just don't make Aiden angry.

---

**Note:** This is a fan project. Watch Dogs and Aiden Pearce are trademarks of Ubisoft.
