# 🔥 Code Roaster

> *"I've seen rootkits with more integrity."* — TheFox

AI-powered code review with attitude. Get your code roasted by Aiden Pearce (TheFox) using OpenRouter API.

![Screenshot](https://via.placeholder.com/800x400/0a0a0f/00d4ff?text=CTOS+Code+Profiler)

## 🎮 Features

- **Watch Dogs CTOS Aesthetic** — Dark terminal UI with cyan accents
- **Aiden Pearce Persona** — Cold, surgical code analysis from TheFox himself
- **OpenRouter API** — Access to top LLMs via OpenRouter (no local model needed)
- **Fast Models** — Use qwen/qwen-2.5-72b-instruct or other powerful models
- **Caching** — Don't wait for the same roast twice
- **Rate Limiting** — Prevent abuse

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- OpenRouter API key (get one at https://openrouter.ai/keys)

### Installation

```bash
git clone https://github.com/yourusername/code-roaster.git
cd code-roaster
pip install -r requirements.txt
```

### Configuration

```bash
# Copy example config
cp .env.example .env

# Edit .env to set your OpenRouter API key and model
OPENROUTER_API_KEY=your_openrouter_key_here
MODEL=qwen/qwen-2.5-72b-instruct  # or any other model from OpenRouter
```

### Run

```bash
python web_app.py
```

Open http://localhost:5000

## 🐳 Docker

```bash
docker build -t code-roaster .
docker run -p 5000:5000 -e OPENROUTER_API_KEY=your_key_here -e MODEL=qwen/qwen-2.5-72b-instruct code-roaster
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
| ![UI](screenshots/ui.png) | ![Roast](screenshots/roast.png) |

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

**Important:** Get your OpenRouter API key from https://openrouter.ai/keys and keep it secure. Never commit it to public repositories.
