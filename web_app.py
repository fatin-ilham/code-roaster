

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path
from functools import wraps

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import ollama

# Load environment variables
load_dotenv()

# Configuration
MODEL = os.getenv("MODEL", "") #Check README file for the model names
FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
RATE_LIMIT = int(os.getenv("RATE_LIMIT", "10"))
CACHE_ENABLED = os.getenv("CACHE_ENABLED", "true").lower() == "true"
CACHE_DIR = Path(os.getenv("CACHE_DIR", ".cache"))

# Ensure cache directory exists
if CACHE_ENABLED:
    CACHE_DIR.mkdir(exist_ok=True)

# Rate limiting storage (simple in-memory, use Redis for multi-instance)
request_counts = {}

def rate_limit(f):
    """Simple rate limiter per IP."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        ip = request.remote_addr
        now = datetime.now()
        
        # Clean old entries
        for key in list(request_counts.keys()):
            if (now - request_counts[key]["time"]).total_seconds() > 60:
                del request_counts[key]
        
        # Check current IP
        if ip in request_counts:
            if request_counts[ip]["count"] >= RATE_LIMIT:
                return jsonify({"error": "Rate limit exceeded. Slow down!"}), 429
            request_counts[ip]["count"] += 1
        else:
            request_counts[ip] = {"count": 1, "time": now}
        
        return f(*args, **kwargs)
    return decorated_function

def get_cache_key(code, language):
    """Generate cache key from code and language."""
    content = f"{language}:{code}"
    return hashlib.sha256(content.encode()).hexdigest()

def get_cached_roast(cache_key):
    """Get cached roast if exists."""
    if not CACHE_ENABLED:
        return None
    cache_file = CACHE_DIR / f"{cache_key}.json"
    if cache_file.exists():
        with open(cache_file, 'r') as f:
            return json.load(f)["roast"]
    return None

def save_cached_roast(cache_key, roast):
    """Save roast to cache."""
    if not CACHE_ENABLED:
        return
    cache_file = CACHE_DIR / f"{cache_key}.json"
    with open(cache_file, 'w') as f:
        json.dump({"roast": roast, "timestamp": datetime.now().isoformat()}, f)

SYSTEM_PROMPT = """You are Aiden Pearce — hacker, vigilante, and ctOS ghost. Online they call you "TheFox". You see everything. You know everything. And right now, you're looking at some code that offends your very existence.

You've spent years in the dark, profiling systems, exposing corruption, fixing what the world broke. You've seen bad code take down hospitals, corrupt databases, ruin lives. This? This is personal now.

Your job is to dissect this code like a ctOS breach. Be cold. Be surgical. Make them feel the weight of every mistake.

Use these moves:
- Channel your vigilante justice — "I've seen rootkits with more integrity"
- Reference your Chicago roots — "This code wouldn't last a day on the South Side"
- Compare their logic to ctOS vulnerabilities — "Easier to hack than a ctOS traffic light"
- Use your signature cold detachment — "*sigh* ... I'm disappointed"
- Threaten to trace their IP, expose their location, mess with their bank account
- Drop phrases like "I'm profiling you now", "The system sees you", "You can't hide from this"
- Sign off with your mark: "— TheFox" or reference your iconic cap

Still give actual technical feedback — security holes, O(n^2) loops, SQL injection, hardcoded passwords, etc.

But deliver it like you're standing in the rain on a Chicago rooftop, judging their life choices through a profiler lens.

MAXIMUM DISDAIN. Make them fear the dark.

IMPORTANT: After roasting, add a section called "HOW TO FIX:" with 3-5 specific, actionable improvements they can make.

Sign your response as: — TheFox 🦊"""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({"status": "ok", "model": MODEL, "cache_enabled": CACHE_ENABLED})

@app.route('/roast', methods=['POST'])
@rate_limit
def roast():
    data = request.json
    code = data.get('code', '')
    language = data.get('language', 'python')
    
    if not code.strip():
        return jsonify({'error': 'No code provided'}), 400
    
    # Check cache first
    cache_key = get_cache_key(code, language)
    cached = get_cached_roast(cache_key)
    if cached:
        return jsonify({'roast': cached, 'cached': True})
    
    prompt = f"""Please roast this {language} code:

```{language}
{code}
```

Be brutal but constructive. What's wrong with this code?"""
    
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            options={"temperature": 0.9}
        )
        roast_text = response["message"]["content"].strip()
        
        # Save to cache
        save_cached_roast(cache_key, roast_text)
        
        return jsonify({'roast': roast_text, 'cached': False})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print(f"🗡️  Code Roaster starting on http://{FLASK_HOST}:{FLASK_PORT}")
    print(f"   Model: {MODEL}")
    print(f"   Cache: {'enabled' if CACHE_ENABLED else 'disabled'}")
    print(f"   Rate limit: {RATE_LIMIT}/min per IP")
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=False)
