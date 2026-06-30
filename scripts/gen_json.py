#!/usr/bin/env python3
"""Generate all bilingual NTPC JSON question files from TS source data."""
import json, os, re

BASE = r"C:\Users\core\rrb-exam-prep"
OUT = os.path.join(BASE, "public", "data", "questions", "ntpc")

os.makedirs(os.path.join(OUT, "mathematics"), exist_ok=True)
os.makedirs(os.path.join(OUT, "reasoning"), exist_ok=True)

# Read the TS source files
def read_ts_questions(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Extract all question objects using regex
    questions = []
    # Find all { ... } blocks after the array opening
    pattern = r'\{[^{}]*?(?:\{[^{}]*?\}[^{}]*?)*?\}'
    # More robust: split by '  {' and parse each
    blocks = re.findall(r'\{\s*\n\s*id:.*?\n\s*\}', content, re.DOTALL)
    
    # Simpler approach: find each block starting with id:
    raw = content[content.find('['):content.rfind('];')+1]
    # Remove comments
    raw = re.sub(r'//.*?\n', '\n', raw)
    
    # Extract questions more carefully
    q_blocks = re.findall(r'\{[^}]*?(?:\{[^}]*?\}[^}]*?)*?\}', raw)
    
    result = []
    for block in q_blocks:
        q = {}
        # Extract fields
        m = re.search(r"id:\s*'([^']+)'", block)
        if not m: continue
        q['id'] = m.group(1)
        m = re.search(r"topicId:\s*'([^']+)'", block)
        if m: q['topicId'] = m.group(1)
        m = re.search(r"questionText:\s*'((?:[^'\\]|\\.)*)'", block)
        if m: q['questionText'] = m.group(1).replace("\\'", "'")
        m = re.search(r"optionA:\s*'((?:[^'\\]|\\.)*)'", block)
        if m: q['optionA'] = m.group(1)
        m = re.search(r"optionB:\s*'((?:[^'\\]|\\.)*)'", block)
        if m: q['optionB'] = m.group(1)
        m = re.search(r"optionC:\s*'((?:[^'\\]|\\.)*)'", block)
        if m: q['optionC'] = m.group(1)
        m = re.search(r"optionD:\s*'((?:[^'\\]|\\.)*)'", block)
        if m: q['optionD'] = m.group(1)
        m = re.search(r"correctOption:\s*'([^']+)'", block)
        if m: q['correctOption'] = m.group(1)
        m = re.search(r"explanation:\s*'((?:[^'\\]|\\.)*)'", block)
        if m: q['explanation'] = m.group(1).replace("\\'", "'")
        m = re.search(r"difficulty:\s*'([^']+)'", block)
        if m: q['difficulty'] = m.group(1)
        m = re.search(r"sourceYear:\s*(\d+)", block)
        if m: q['sourceYear'] = int(m.group(1))
        else: q['sourceYear'] = 2024
        result.append(q)
    return result

print("Reading math questions...")
math_qs = read_ts_questions(os.path.join(BASE, "src", "data", "questions", "ntpc-math.ts"))
print(f"Found {len(math_qs)} math questions")

print("Reading reasoning questions...")
reasoning_qs = read_ts_questions(os.path.join(BASE, "src", "data", "questions", "ntpc-reasoning.ts"))
print(f"Found {len(reasoning_qs)} reasoning questions")
