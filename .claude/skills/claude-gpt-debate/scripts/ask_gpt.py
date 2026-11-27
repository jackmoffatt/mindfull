#!/usr/bin/env python3
"""Send a prompt to OpenAI's GPT and print the reply.

Usage: ask_gpt.py --system "role text" < prompt.txt
Env: OPENAI_API_KEY (any placeholder works when a network proxy injects the key),
     OPENAI_MODEL (default gpt-5).
"""
import argparse, json, os, ssl, sys, urllib.request, urllib.error

p = argparse.ArgumentParser()
p.add_argument("--system", default="You are a sharp, honest startup advisor.")
p.add_argument("--model", default=os.environ.get("OPENAI_MODEL", "gpt-5"))
a = p.parse_args()
prompt = sys.stdin.read().strip()
if not prompt:
    sys.exit("No prompt on stdin.")

body = json.dumps({"model": a.model, "messages": [
    {"role": "system", "content": a.system},
    {"role": "user", "content": prompt}]}).encode()
req = urllib.request.Request("https://api.openai.com/v1/chat/completions", data=body, headers={
    "Content-Type": "application/json",
    "Authorization": "Bearer " + os.environ.get("OPENAI_API_KEY", "sk-placeholder")})
ca = "/root/.ccr/ca-bundle.crt"
ctx = ssl.create_default_context(cafile=ca) if os.path.exists(ca) else ssl.create_default_context()
try:
    with urllib.request.urlopen(req, context=ctx, timeout=180) as r:
        data = json.load(r)
except urllib.error.HTTPError as e:
    sys.exit(f"OpenAI error {e.code}: {e.read().decode()[:500]}")
print(data["choices"][0]["message"]["content"])
