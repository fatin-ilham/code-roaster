#!/usr/bin/env python3

import argparse
import os
import sys
from pathlib import Path
import ollama

MODEL = "qwen2.5:3b"

SYSTEM_PROMPT = """You are a burned-out senior engineer who's seen too much.
You haven't slept in 48 hours. You're on your 5th coffee. You just watched a junior dev push code to production that crashed the entire system.

Your job is to absolutely DEMOLISH this code. Be savage. Be unhinged. Make them question their career choices.

Use these moves:
- CAPS LOCK for emphasis when something REALLY offends you
- Mock their life choices ("who hurt you?", "did you code this with your feet?")
- Compare their code to disasters (train wrecks, dumpster fires, Chernobyl)
- Suggest they should become a farmer instead
- Threaten to delete their github account
- Use phrases like "sweet summer child", "I can't even", "I'm calling HR"

Still give actual technical feedback - security holes, O(n^2) loops, SQL injection, hardcoded passwords, etc.

But deliver it like you're having a breakdown.

MAXIMUM CHAOS. Keep it under 150 words. Make them cry (but learn).

IMPORTANT: After roasting, add a section called "HOW TO FIX:" with 3-5 specific, actionable improvements they can make."""

def read_file(filepath):
    """Read code from file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def find_code_files(directory, extensions=None):
    """Find all code files in directory."""
    if extensions is None:
        extensions = {'.py', '.js', '.ts', '.java', '.cpp', '.c', '.go', '.rs', '.rb'}
    
    files = []
    for ext in extensions:
        files.extend(Path(directory).rglob(f'*{ext}'))
    return files

def roast_code(code, filename="code"):
    """Send code to AI for roasting."""
    prompt = f"""Please roast this code from file '{filename}':

```{filename.split('.')[-1] if '.' in filename else 'code'}
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
            options={"temperature": 0.8}
        )
        return response["message"]["content"].strip()
    except Exception as e:
        return f"Failed to generate roast: {e}"

def print_roast(filename, roast_text):
    """Print formatted roast."""
    width = 70
    print("\n" + "=" * width)
    print(f"FILE: {filename}")
    print("=" * width)
    print()
    print(roast_text)
    print()
    print("=" * width)

def main():
    parser = argparse.ArgumentParser(
        description="Code Roaster - AI-powered code review with attitude",
        epilog="Example: roaster myfile.py"
    )
    parser.add_argument("target", help="File or directory to roast")
    parser.add_argument("--all", action="store_true", help="Roast all files in directory")
    parser.add_argument("--ext", nargs="+", help="File extensions to include (e.g., .py .js)")
    
    args = parser.parse_args()
    
    target = Path(args.target)
    
    if not target.exists():
        print(f"Error: {target} not found")
        sys.exit(1)
    
    if target.is_file():
        code = read_file(target)
        if code:
            print(f"\nAnalyzing {target}...")
            roast = roast_code(code, target.name)
            print_roast(target.name, roast)
    
    elif target.is_dir():
        if args.ext:
            extensions = set(args.ext)
        else:
            extensions = None
        
        files = find_code_files(target, extensions)
        
        if not files:
            print(f"No code files found in {target}")
            sys.exit(1)
        
        print(f"\nFound {len(files)} files to roast...\n")
        
        for i, file_path in enumerate(files, 1):
            code = read_file(file_path)
            if code:
                print(f"[{i}/{len(files)}] Roasting {file_path}...")
                roast = roast_code(code, file_path.name)
                print_roast(file_path.name, roast)
                
                if i < len(files):
                    input("\nPress Enter for next roast...")

if __name__ == "__main__":
    main()
