"""
RRB Exam Question Generator — Core Framework
Generates bilingual (EN+HI) questions with VERIFIED answers.
Every math question is computed, not hallucinated.
"""
import json, os, math, random, re
from typing import List, Dict, Any, Callable

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.path.join(BASE_DIR, "public", "data", "questions")

def load_json(path: str) -> List[Dict]:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_json(path: str, data: List[Dict]):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def make_id(prefix: str, num: int) -> str:
    return f"{prefix}-{num:04d}"

def q(difficulty="medium", source_year=2025):
    """Factory for a question dict"""
    return {
        "difficulty": difficulty,
        "sourceYear": source_year,
        "en": {"question": "", "options": [], "explanation": ""},
        "hi": {"question": "", "options": [], "explanation": ""}
    }

# ─── MATH HELPERS ───
def rand_int(a, b):
    return random.randint(a, b)

def rand_choice(arr):
    return random.choice(arr)

def round2(x):
    return round(x, 2)

def round3(x):
    return round(x, 3)

def fmt_num(n):
    """Format number nicely"""
    if n == int(n):
        return str(int(n))
    return f"{n:.2f}"

def hi_num(n):
    """Convert number to Hindi text (for option display, keep numbers as-is in Hindi math)"""
    return str(n)

# Hindi math terms
HI_MATH = {
    "sum": "योग",
    "product": "गुणनफल",
    "difference": "अंतर",
    "quotient": "भागफल",
    "remainder": "शेषफल",
    "square": "वर्ग",
    "cube": "घन",
    "root": "मूल",
    "percent": "प्रतिशत",
    "profit": "लाभ",
    "loss": "हानि",
    "simple_interest": "साधारण ब्याज",
    "compound_interest": "चक्रवृद्धि ब्याज",
    "speed": "गति",
    "distance": "दूरी",
    "time": "समय",
    "area": "क्षेत्रफल",
    "volume": "आयतन",
    "radius": "त्रिज्या",
    "diameter": "व्यास",
    "height": "ऊंचाई",
    "base": "आधार",
    "average": "औसत",
    "ratio": "अनुपात",
}

print("Core generator framework loaded.")
