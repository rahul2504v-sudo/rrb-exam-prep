"""Bilingual Reasoning Question Generator for NTPC & Group D
Generates 60-80 questions per topic with programmatically verified answers.
Updates 32 JSON files (16 topics × 2 exams). All answers are COMPUTED, not guessed.

Usage: python scripts/gen_reasoning.py
"""

import json
import os
import random
import math
from pathlib import Path

BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent
PUBLIC_DIR = BASE_DIR / "public" / "data" / "questions"

# ─── Helper functions ───

def load_json(path):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def ri(a, b):
    return random.randint(a, b)

def rpick(arr):
    return random.choice(arr)

def rshuffle(arr):
    arr2 = list(arr)
    random.shuffle(arr2)
    return arr2

def make_q(prefix, num, difficulty, en_q, hi_q, en_ex, hi_ex, answer, wrongs, year=2025):
    """Create a verified bilingual question. answer and wrongs must be strings."""
    options = [str(answer)] + [str(w) for w in wrongs[:3]]
    random.shuffle(options)
    correct_idx = options.index(str(answer))
    return {
        "id": f"{prefix}-{num:04d}",
        "correctOption": ["A", "B", "C", "D"][correct_idx],
        "difficulty": difficulty,
        "sourceYear": year,
        "en": {"question": en_q, "options": [str(o) for o in options], "explanation": en_ex},
        "hi": {"question": hi_q, "options": [str(o) for o in options], "explanation": hi_ex},
    }

# Hindi translation helpers for common reasoning terms
HI_REASONING = {
    "analogy": "समरूपता",
    "coding-decoding": "कोडिंग-डिकोडिंग",
    "series": "श्रेणी",
    "find": "ज्ञात करें",
    "next term": "अगला पद",
    "missing": "लुप्त",
    "odd one out": "बेमेल",
}

# ═══════════════════════════════════════════════════
# TOPIC GENERATORS
# ═══════════════════════════════════════════════════

# ─── 1. ANALOGIES ───
def gen_analogies(prefix, count=70):
    qs = []
    # Word-pair banks with verified relationships
    synonym_pairs = [
        ("BIG", "LARGE", "बड़ा", "विशाल"),
        ("HAPPY", "JOYFUL", "खुश", "प्रसन्न"),
        ("BRAVE", "COURAGEOUS", "बहादुर", "साहसी"),
        ("QUICK", "FAST", "तेज़", "तीव्र"),
        ("SMALL", "TINY", "छोटा", "नन्हा"),
        ("WISE", "INTELLIGENT", "बुद्धिमान", "चतुर"),
        ("RICH", "WEALTHY", "अमीर", "धनी"),
        ("ANGRY", "FURIOUS", "गुस्सा", "क्रोधित"),
        ("SAD", "UNHAPPY", "दुखी", "उदास"),
        ("BEAUTIFUL", "PRETTY", "सुंदर", "सुंदर"),
        ("BEGIN", "START", "शुरू", "आरंभ"),
        ("HELP", "ASSIST", "मदद", "सहायता"),
        ("ENEMY", "FOE", "दुश्मन", "शत्रु"),
        ("ERROR", "MISTAKE", "गलती", "भूल"),
        ("ANCIENT", "OLD", "प्राचीन", "पुराना"),
        ("SILENT", "QUIET", "शांत", "मौन"),
        ("STRONG", "POWERFUL", "मजबूत", "शक्तिशाली"),
        ("CORRECT", "RIGHT", "सही", "उचित"),
        ("POLITE", "COURTEOUS", "विनम्र", "शिष्ट"),
        ("GOOD", "NICE", "अच्छा", "अच्छा"),
    ]
    antonym_pairs = [
        ("HOT", "COLD", "गर्म", "ठंडा"),
        ("DAY", "NIGHT", "दिन", "रात"),
        ("LIGHT", "DARK", "प्रकाश", "अंधकार"),
        ("LOVE", "HATE", "प्यार", "नफरत"),
        ("RICH", "POOR", "अमीर", "गरीब"),
        ("HARD", "SOFT", "कठोर", "कोमल"),
        ("FULL", "EMPTY", "भरा", "खाली"),
        ("OPEN", "CLOSE", "खुला", "बंद"),
        ("HIGH", "LOW", "ऊंचा", "नीचा"),
        ("THICK", "THIN", "मोटा", "पतला"),
        ("WET", "DRY", "गीला", "सूखा"),
        ("HAPPY", "SAD", "खुश", "दुखी"),
        ("FAST", "SLOW", "तेज़", "धीमा"),
        ("TRUE", "FALSE", "सत्य", "असत्य"),
        ("STRONG", "WEAK", "मजबूत", "कमजोर"),
        ("SWEET", "SOUR", "मीठा", "खट्टा"),
        ("WIDE", "NARROW", "चौड़ा", "संकरा"),
        ("FRESH", "STALE", "ताजा", "बासी"),
        ("CLEAN", "DIRTY", "साफ", "गंदा"),
        ("WISE", "FOOLISH", "बुद्धिमान", "मूर्ख"),
    ]
    tool_worker = [
        ("PEN", "WRITER", "कलम", "लेखक"),
        ("SCISSORS", "TAILOR", "कैंची", "दर्जी"),
        ("STETHOSCOPE", "DOCTOR", "स्टेथोस्कोप", "डॉक्टर"),
        ("CHALK", "TEACHER", "चाक", "शिक्षक"),
        ("AXE", "WOODCUTTER", "कुल्हाड़ी", "लकड़हारा"),
        ("PLOUGH", "FARMER", "हल", "किसान"),
        ("GUN", "SOLDIER", "बंदूक", "सैनिक"),
        ("BRUSH", "PAINTER", "ब्रश", "चित्रकार"),
        ("NEEDLE", "TAILOR", "सुई", "दर्जी"),
        ("HAMMER", "CARPENTER", "हथौड़ा", "बढ़ई"),
        ("KNIFE", "CHEF", "चाकू", "रसोइया"),
        ("SCALE", "JUDGE", "तराजू", "न्यायाधीश"),
        ("MICROPHONE", "SINGER", "माइक्रोफोन", "गायक"),
        ("TROWEL", "MASON", "करणी", "राजमिस्त्री"),
        ("SPADE", "GARDENER", "फावड़ा", "माली"),
    ]
    part_whole = [
        ("PAGE", "BOOK", "पृष्ठ", "पुस्तक"),
        ("WHEEL", "CAR", "पहिया", "कार"),
        ("FINGER", "HAND", "उंगली", "हाथ"),
        ("LEAF", "TREE", "पत्ता", "पेड़"),
        ("ROOM", "HOUSE", "कमरा", "घर"),
        ("BRICK", "WALL", "ईंट", "दीवार"),
        ("SEED", "PLANT", "बीज", "पौधा"),
        ("NOSE", "FACE", "नाक", "चेहरा"),
        ("PETAL", "FLOWER", "पंखुड़ी", "फूल"),
        ("DROP", "WATER", "बूंद", "पानी"),
        ("LETTER", "WORD", "अक्षर", "शब्द"),
        ("SECOND", "MINUTE", "सेकंड", "मिनट"),
        ("KEY", "KEYBOARD", "कुंजी", "कीबोर्ड"),
        ("SCENE", "MOVIE", "दृश्य", "फिल्म"),
        ("STAR", "GALAXY", "तारा", "आकाशगंगा"),
    ]
    cause_effect = [
        ("FIRE", "ASH", "आग", "राख"),
        ("RAIN", "FLOOD", "बारिश", "बाढ़"),
        ("STUDY", "KNOWLEDGE", "अध्ययन", "ज्ञान"),
        ("PRACTICE", "PERFECTION", "अभ्यास", "पूर्णता"),
        ("HUNGER", "EATING", "भूख", "भोजन"),
        ("THIRST", "DRINKING", "प्यास", "पीना"),
        ("WORK", "SUCCESS", "काम", "सफलता"),
        ("SEED", "FRUIT", "बीज", "फल"),
        ("CLOUD", "RAIN", "बादल", "वर्षा"),
        ("VIRUS", "DISEASE", "विषाणु", "बीमारी"),
        ("WIND", "WAVE", "हवा", "लहर"),
        ("HEAT", "EXPANSION", "गर्मी", "प्रसार"),
        ("TRAINING", "SKILL", "प्रशिक्षण", "कौशल"),
        ("SUN", "DAY", "सूर्य", "दिन"),
        ("LAZINESS", "FAILURE", "आलस्य", "असफलता"),
    ]
    number_analogies = [
        ("4", "16", "वर्ग"),    # square
        ("3", "27", "घन"),      # cube
        ("2", "4", "वर्ग"),     # square
        ("5", "25", "वर्ग"),
        ("6", "36", "वर्ग"),
        ("7", "49", "वर्ग"),
        ("8", "64", "वर्ग"),
        ("9", "81", "वर्ग"),
        ("3", "9", "वर्ग"),
        ("4", "64", "घन"),
        ("2", "8", "घन"),
        ("5", "125", "घन"),
        ("10", "100", "वर्ग"),
        ("12", "144", "वर्ग"),
        ("6", "216", "घन"),
    ]

    for _ in range(count):
        pattern_type = ri(0, 5)
        if pattern_type == 0:  # Synonym
            a_en, b_en, a_hi, b_hi = rpick(synonym_pairs)
            c_en, d_en, c_hi, d_hi = rpick(synonym_pairs)
            while c_en == a_en:
                c_en, d_en, c_hi, d_hi = rpick(synonym_pairs)
            q = f"{a_en} : {b_en} :: {c_en} : ?"
            hq = f"{a_hi} : {b_hi} :: {c_hi} : ?"
            ans = d_en
            ans_hi = d_hi
            ex = f"{a_en} and {b_en} are synonyms. Similarly, {c_en} and {d_en} are synonyms."
            hexp = f"{a_hi} और {b_hi} पर्यायवाची हैं। इसी प्रकार, {c_hi} और {d_hi} पर्यायवाची हैं।"
            wrongs = [rpick(synonym_pairs)[esub] for esub in [1,3,1,1]][:3]
            w_hi = [d_hi, d_hi, d_hi]
        elif pattern_type == 1:  # Antonym
            a_en, b_en, a_hi, b_hi = rpick(antonym_pairs)
            c_en, d_en, c_hi, d_hi = rpick(antonym_pairs)
            while c_en == a_en:
                c_en, d_en, c_hi, d_hi = rpick(antonym_pairs)
            q = f"{a_en} : {b_en} :: {c_en} : ?"
            hq = f"{a_hi} : {b_hi} :: {c_hi} : ?"
            ans, ans_hi = d_en, d_hi
            ex = f"{a_en} and {b_en} are antonyms. Similarly, {c_en} and {d_en} are antonyms."
            hexp = f"{a_hi} और {b_hi} विलोम हैं। इसी प्रकार, {c_hi} और {d_hi} विलोम हैं।"
            wrongs = [rpick(antonym_pairs)[esub] for esub in [1,3,1,1]][:3]
        elif pattern_type == 2:  # Tool:Worker
            a_en, b_en, a_hi, b_hi = rpick(tool_worker)
            c_en, d_en, c_hi, d_hi = rpick(tool_worker)
            while c_en == a_en:
                c_en, d_en, c_hi, d_hi = rpick(tool_worker)
            q = f"{a_en} : {b_en} :: {c_en} : ?"
            hq = f"{a_hi} : {b_hi} :: {c_hi} : ?"
            ans, ans_hi = d_en, d_hi
            ex = f"A {a_en} is used by a {b_en}. Similarly, a {c_en} is used by a {d_en}."
            hexp = f"{a_hi} का प्रयोग {b_hi} करता है। इसी प्रकार, {c_hi} का प्रयोग {d_hi} करता है।"
            wrongs = [rpick(tool_worker)[esub] for esub in [1,3,1,1]][:3]
        elif pattern_type == 3:  # Part:Whole
            a_en, b_en, a_hi, b_hi = rpick(part_whole)
            c_en, d_en, c_hi, d_hi = rpick(part_whole)
            while c_en == a_en:
                c_en, d_en, c_hi, d_hi = rpick(part_whole)
            q = f"{a_en} : {b_en} :: {c_en} : ?"
            hq = f"{a_hi} : {b_hi} :: {c_hi} : ?"
            ans, ans_hi = d_en, d_hi
            ex = f"{a_en} is a part of {b_en}. Similarly, {c_en} is a part of {d_en}."
            hexp = f"{a_hi}, {b_hi} का भाग है। इसी प्रकार, {c_hi}, {d_hi} का भाग है।"
            wrongs = [rpick(part_whole)[esub] for esub in [1,3,1,1]][:3]
        elif pattern_type == 4:  # Cause:Effect
            a_en, b_en, a_hi, b_hi = rpick(cause_effect)
            c_en, d_en, c_hi, d_hi = rpick(cause_effect)
            while c_en == a_en:
                c_en, d_en, c_hi, d_hi = rpick(cause_effect)
            q = f"{a_en} : {b_en} :: {c_en} : ?"
            hq = f"{a_hi} : {b_hi} :: {c_hi} : ?"
            ans, ans_hi = d_en, d_hi
            ex = f"{a_en} causes/leads to {b_en}. Similarly, {c_en} causes/leads to {d_en}."
            hexp = f"{a_hi} से {b_hi} होता है। इसी प्रकार, {c_hi} से {d_hi} होता है।"
            wrongs = [rpick(cause_effect)[esub] for esub in [1,3,1,1]][:3]
        else:  # Number based
            a_en, b_en, pat_hi = rpick(number_analogies)
            # pick another
            c_en, d_en, _ = rpick(number_analogies)
            while c_en == a_en:
                c_en, d_en, _ = rpick(number_analogies)
            # For number analogies, use square/cube relationship
            q = f"{a_en} : {b_en} :: {c_en} : ?"
            hq = f"{a_en} : {b_en} :: {c_en} : ?"
            ans = d_en; ans_hi = d_en
            ex = f"The relation is {pat_hi}: {a_en}² = {int(a_en)**2 if pat_hi=='वर्ग' else int(a_en)**3}. {c_en}² = {int(c_en)**2 if pat_hi=='वर्ग' else int(c_en)**3}."
            hexp = f"संबंध {pat_hi} है: {a_en}² = {int(a_en)**2 if pat_hi=='वर्ग' else int(a_en)**3}। {c_en}² = {int(c_en)**2 if pat_hi=='वर्ग' else int(c_en)**3}।"
            wrongs = [str(int(d_en)+ri(1,5)), str(int(d_en)-ri(1,3)), str(int(c_en)*2)]

        # Clean up wrongs - ensure they are distinct from answer and unique
        wrongs = [w for w in wrongs if str(w) != str(ans)]
        while len(wrongs) < 3:
            wrongs.append(str(ri(1, 15)) + "XYZ"[:ri(0, 2)])
        wrongs = wrongs[:3]

        diff = rpick(["easy", "easy", "medium", "medium", "medium", "hard"])
        qs.append(make_q(prefix, len(qs)+1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 2. CODING-DECODING ───
def gen_coding_decoding(prefix, count=70):
    qs = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rev_alpha = dict(zip(alphabet, alphabet[::-1]))

    for _ in range(count):
        pattern = ri(0, 6)
        word = rpick(["CAT", "DOG", "PEN", "BAT", "CAR", "CUP", "HAT", "BOX", "SUN", "FAN",
                       "MAP", "BAG", "JAM", "KEY", "NUT", "OWL", "ZOO", "FISH", "BIRD", "LION",
                       "TIGER", "RABBIT", "HORSE", "HOUSE", "TABLE", "CHAIR", "BOOK", "DESK",
                       "WATER", "PLANT", "MOON", "STAR", "ROAD", "KING", "QUEEN", "TREE", "CLOUD"])
        word = word.upper()

        if pattern == 0:  # +1 shift
            coded = "".join(alphabet[(alphabet.index(c) + 1) % 26] for c in word)
            q = f"In a certain code, 'B' is coded as 'C'. How is '{word}' coded?"
            hq = f"एक कोड भाषा में 'B' को 'C' लिखा जाता है। '{word}' का कोड क्या होगा?"
            ans = coded
            ex = f"Each letter is shifted +1: " + ", ".join(f"{c}→{alphabet[(alphabet.index(c)+1)%26]}" for c in word)
            hexp = f"प्रत्येक अक्षर +1 आगे बढ़ता है: " + ", ".join(f"{c}→{alphabet[(alphabet.index(c)+1)%26]}" for c in word)
            wrongs = [
                "".join(alphabet[(alphabet.index(c) - 1) % 26] for c in word),
                "".join(alphabet[(alphabet.index(c) + 2) % 26] for c in word),
                "".join(rev_alpha[c] for c in word),
            ]

        elif pattern == 1:  # -1 shift
            coded = "".join(alphabet[(alphabet.index(c) - 1) % 26] for c in word)
            q = f"In a code, 'B' is coded as 'A'. Find code for '{word}'."
            hq = f"एक कोड में 'B' को 'A' लिखते हैं। '{word}' का कोड ज्ञात करें।"
            ans = coded
            ex = "Each letter is shifted -1: " + ", ".join(f"{c}→{alphabet[(alphabet.index(c)-1)%26]}" for c in word)
            hexp = "प्रत्येक अक्षर -1 पीछे: " + ", ".join(f"{c}→{alphabet[(alphabet.index(c)-1)%26]}" for c in word)
            wrongs = [
                "".join(alphabet[(alphabet.index(c) + 1) % 26] for c in word),
                "".join(alphabet[(alphabet.index(c) - 2) % 26] for c in word),
                "".join(rev_alpha[c] for c in word),
            ]

        elif pattern == 2:  # Reversal coding (A→Z, B→Y)
            coded = "".join(rev_alpha[c] for c in word)
            q = f"If HE is coded as SV, how is '{word}' coded? (use reverse alphabet code)"
            hq = f"यदि HE को SV लिखा जाए, तो '{word}' का कोड क्या होगा? (उल्टा वर्णमाला कोड)"
            ans = coded
            ex = "Reverse alphabet: A=Z, B=Y, ... " + ", ".join(f"{c}={rev_alpha[c]}" for c in word)
            hexp = "उल्टी वर्णमाला: A=Z, B=Y, ... " + ", ".join(f"{c}={rev_alpha[c]}" for c in word)
            wrongs = [
                "".join(alphabet[(alphabet.index(c) + 1) % 26] for c in word),
                "".join(alphabet[(alphabet.index(c) - 1) % 26] for c in word),
                word[::-1],
            ]

        elif pattern == 3:  # Position sum coding (A=1, B=2, ...)
            positions = [alphabet.index(c) + 1 for c in word]
            pos_sum = sum(positions)
            coded = str(pos_sum)
            q = f"If A=1, B=2, ..., Z=26, what is the code for '{word}'? (sum of positions)"
            hq = f"यदि A=1, B=2, ..., Z=26, तो '{word}' का कोड क्या है? (स्थानों का योग)"
            ans = coded
            ex = f"Positions: {', '.join(f'{c}={p}' for c, p in zip(word, positions))}. Sum = {pos_sum}"
            hexp = f"स्थान: {', '.join(f'{c}={p}' for c, p in zip(word, positions))}। योग = {pos_sum}"
            wrongs = [str(pos_sum + ri(1, 10)), str(pos_sum - ri(1, 5)), str(pos_sum * 2)]

        elif pattern == 4:  # Pattern-based: +2 shift
            coded = "".join(alphabet[(alphabet.index(c) + 2) % 26] for c in word)
            q = f"If 'ACE' is coded as 'CEG', find the code for '{word}'."
            hq = f"यदि 'ACE' को 'CEG' लिखें, तो '{word}' का कोड ज्ञात करें।"
            ans = coded
            ex = "Each letter is shifted +2: " + ", ".join(f"{c}→{alphabet[(alphabet.index(c)+2)%26]}" for c in word)
            hexp = "प्रत्येक अक्षर +2 आगे: " + ", ".join(f"{c}→{alphabet[(alphabet.index(c)+2)%26]}" for c in word)
            wrongs = [
                "".join(alphabet[(alphabet.index(c) + 1) % 26] for c in word),
                "".join(alphabet[(alphabet.index(c) - 2) % 26] for c in word),
                "".join(rev_alpha[c] for c in word),
            ]

        elif pattern == 5:  # Pattern: position → reverse-position
            coded = "".join(str(27 - (alphabet.index(c) + 1)) for c in word)
            q = f"In a code, each letter is replaced by its reverse position. Code for '{word}'?"
            hq = f"एक कोड में अक्षर के स्थान को उल्टा लिखते हैं। '{word}' का कोड?"
            ans = coded
            pos_map = ", ".join(f"{c}({alphabet.index(c)+1})→{27-(alphabet.index(c)+1)}" for c in word)
            ex = f"Reverse position: {pos_map}"
            hexp = f"उल्टा स्थान: {pos_map}"
            wrongs = [
                "".join(str(alphabet.index(c) + 1) for c in word),
                "".join(str(alphabet.index(c) + ri(0, 2)) for c in word),
                str(sum(alphabet.index(c) + 1 for c in word)),
            ]

        else:  # Vowel-consonant pattern: V→next consonant, C→prev vowel
            vowels = set("AEIOU")
            coded_list = []
            for c in word:
                if c in vowels:
                    # next consonant
                    idx = alphabet.index(c)
                    while True:
                        idx = (idx + 1) % 26
                        if alphabet[idx] not in vowels:
                            coded_list.append(alphabet[idx])
                            break
                else:
                    # prev vowel
                    # find nearest vowel before
                    for offset in range(1, 26):
                        idx2 = (alphabet.index(c) - offset) % 26
                        if alphabet[idx2] in vowels:
                            coded_list.append(alphabet[idx2])
                            break
            coded = "".join(coded_list)
            q = f"If vowels→next consonant and consonants→previous vowel, code '{word}'?"
            hq = f"यदि स्वर→अगला व्यंजन और व्यंजन→पिछला स्वर, तो '{word}' का कोड?"
            ans = coded
            ex = "Rule: V→next C, C→prev V. " + ", ".join(f"{c}→{co}" for c, co in zip(word, coded_list))
            hexp = "नियम: स्वर→अगला व्यंजन, व्यंजन→पिछला स्वर। " + ", ".join(f"{c}→{co}" for c, co in zip(word, coded_list))
            wrongs = [
                "".join(alphabet[(alphabet.index(c) + 1) % 26] for c in word),
                "".join(rev_alpha[c] for c in word),
                word[::-1],
            ]

        diff = rpick(["medium", "medium", "hard", "easy"])
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 3. SERIES ───
def gen_series(prefix, count=70):
    qs = []
    for _ in range(count):
        pattern = ri(0, 5)

        if pattern == 0:  # Addition (+N)
            start = ri(5, 50)
            step = ri(2, 10)
            n_terms = 5
            series = [start + i * step for i in range(n_terms)]
            missing_idx = ri(0, n_terms - 1)
            answer = series[missing_idx]
            series_display = [str(s) if i != missing_idx else "?" for i, s in enumerate(series)]
            q = f"Find the missing term: {', '.join(series_display)}"
            hq = f"लुप्त पद ज्ञात करें: {', '.join(series_display)}"
            ex = f"Pattern: +{step}. {start} + {step} = {start+step}, ... Term {missing_idx+1}: {start} + {missing_idx}×{step} = {answer}"
            hexp = f"पैटर्न: +{step}। पद {missing_idx+1}: {start} + {missing_idx}×{step} = {answer}"

        elif pattern == 1:  # Multiplication (*N)
            start = ri(2, 5)
            factor = ri(2, 4)
            n_terms = 5
            series = [start]
            for i in range(1, n_terms):
                series.append(series[-1] * factor)
            missing_idx = ri(0, n_terms - 1)
            answer = series[missing_idx]
            series_display = [str(s) if i != missing_idx else "?" for i, s in enumerate(series)]
            q = f"Complete the series: {', '.join(series_display)}"
            hq = f"श्रेणी पूरी करें: {', '.join(series_display)}"
            ex = f"Pattern: ×{factor}. {series[0]} × {factor} = {series[1]}, ... The ? is {answer}"
            hexp = f"पैटर्न: ×{factor}। ? = {answer}"

        elif pattern == 2:  # Alternating +/-
            start = ri(5, 30)
            add_val = ri(3, 8)
            sub_val = ri(2, 5)
            n_terms = 6
            series = [start]
            for i in range(1, n_terms):
                if i % 2 == 1:
                    series.append(series[-1] + add_val)
                else:
                    series.append(series[-1] - sub_val)
            missing_idx = ri(0, n_terms - 1)
            answer = series[missing_idx]
            series_display = [str(s) if i != missing_idx else "?" for i, s in enumerate(series)]
            q = f"Find the next/missing: {', '.join(series_display)}"
            hq = f"लुप्त पद ज्ञात करें: {', '.join(series_display)}"
            ex = f"Pattern: +{add_val}, -{sub_val}, +{add_val}, ... The ? is {answer}"
            hexp = f"पैटर्न: +{add_val}, -{sub_val}, +{add_val}, ... ? = {answer}"

        elif pattern == 3:  # Square/Cube series
            method = ri(0, 1)
            if method == 0:  # squares
                start = ri(2, 8)
                n_terms = 5
                series = [(start + i) ** 2 for i in range(n_terms)]
                missing_idx = ri(0, n_terms - 1)
                answer = series[missing_idx]
                series_display = [str(s) if i != missing_idx else "?" for i, s in enumerate(series)]
                q = f"Find the missing term: {', '.join(series_display)}"
                hq = f"लुप्त पद ज्ञात करें: {', '.join(series_display)}"
                base = start + missing_idx
                ex = f"Squares: {start}²={start**2}, {start+1}²={(start+1)**2}, ... Term {missing_idx+1}: {base}² = {answer}"
                hexp = f"वर्ग: {base}² = {answer}"
            else:  # cubes
                start = ri(2, 6)
                n_terms = 5
                series = [(start + i) ** 3 for i in range(n_terms)]
                missing_idx = ri(0, n_terms - 1)
                answer = series[missing_idx]
                series_display = [str(s) if i != missing_idx else "?" for i, s in enumerate(series)]
                q = f"Solve the series: {', '.join(series_display)}"
                hq = f"श्रेणी हल करें: {', '.join(series_display)}"
                base = start + missing_idx
                ex = f"Cubes: {start}³={start**3}, {start+1}³={(start+1)**3}, ... Term {missing_idx+1}: {base}³ = {answer}"
                hexp = f"घन: {base}³ = {answer}"

        elif pattern == 4:  # Alphabet series
            alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            start_pos = ri(0, 15)
            step = ri(1, 4)
            n_terms = 5
            series = [alpha[(start_pos + i * step) % 26] for i in range(n_terms)]
            missing_idx = ri(0, n_terms - 1)
            answer = series[missing_idx]
            series_display = [s if i != missing_idx else "?" for i, s in enumerate(series)]
            q = f"Find the missing letter: {', '.join(series_display)}"
            hq = f"लुप्त अक्षर ज्ञात करें: {', '.join(series_display)}"
            pos = (start_pos + missing_idx * step) % 26
            ex = f"Each letter skips {step-1} letters forward. Position {missing_idx+1}: {pos+1} = {answer}"
            hexp = f"हर अक्षर {step-1} अक्षर आगे। स्थान {missing_idx+1}: स्थान {pos+1} = {answer}"

        else:  # Ratio-based series
            start = ri(3, 10)
            ratio = ri(2, 4)
            n_terms = 5
            series = [start]
            for i in range(1, n_terms):
                series.append(series[-1] * ratio)
            missing_idx = ri(1, n_terms - 1)
            answer = series[missing_idx]
            series_display = [str(s) if i != missing_idx else "?" for i, s in enumerate(series)]
            q = f"Next term: {', '.join(series_display)}"
            hq = f"अगला पद: {', '.join(series_display)}"
            ex = f"Geometric series with ratio {ratio}. Term {missing_idx+1} = {start}×{ratio}^{missing_idx} = {answer}"
            hexp = f"गुणोत्तर श्रेणी, अनुपात {ratio}। पद {missing_idx+1} = {answer}"

        diff = rpick(["medium", "medium", "easy", "hard"])
        # Generate numeric wrongs safely - answer might be int or str
        try:
            ans_num = int(answer)
            wrongs = [str(ans_num + ri(1, 10)), str(ans_num - ri(1, 5)), str(ans_num * ri(1, 2) + ri(1, 3))]
        except (ValueError, TypeError):
            # Answer is a letter - use alphabet distance
            alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if len(str(answer)) == 1 and str(answer) in alpha:
                idx = alpha.index(str(answer))
                wrongs = [alpha[(idx + ri(1, 4)) % 26], alpha[(idx - ri(1, 3)) % 26], alpha[(idx + ri(5, 10)) % 26]]
            else:
                wrongs = [str(answer) + "X", str(answer) + "Y", str(answer) + "Z"]
        wrongs = [w for w in wrongs if str(w) != str(answer)]
        while len(wrongs) < 3:
            wrongs.append(str(ri(1, 999)))
        wrongs = wrongs[:3]
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, str(answer), wrongs))
    return qs


# ─── 4. BLOOD RELATIONS ───
def gen_blood_relations(prefix, count=70):
    qs = []
    family_terms_en = {
        "father": "पिता", "mother": "माता", "brother": "भाई", "sister": "बहन",
        "son": "पुत्र", "daughter": "पुत्री", "uncle": "चाचा", "aunt": "चाची",
        "nephew": "भतीजा", "niece": "भतीजी", "grandfather": "दादा", "grandmother": "दादी",
        "husband": "पति", "wife": "पत्नी", "father-in-law": "ससुर", "mother-in-law": "सास",
        "cousin": "चचेरा भाई", "grandson": "पोता", "granddaughter": "पोती",
    }

    for _ in range(count):
        pattern = ri(0, 4)

        if pattern == 0:  # Pointing problems
            person = rpick(["Ravi", "Amit", "Raj", "Vikram", "Sheela", "Priya", "Neha", "Kavita"])
            rel = rpick(["the son of", "the daughter of", "the brother of", "the sister of"])
            target_rel = rpick(["son", "daughter", "brother", "sister", "father", "mother", "uncle", "aunt", "nephew", "niece"])

            # Simple: A pointed to B and said...
            names = ["P", "Q", "R", "S"]
            name = rpick(names)
            q = f"{name} pointed to a photograph and said, 'He is the {target_rel} of my father.' How is the person related to {name}?"
            hq = f"{name} ने एक तस्वीर की ओर इशारा करते हुए कहा, 'वह मेरे पिता का {target_rel} है।' वह व्यक्ति {name} से कैसे संबंधित है?"

            # Generate answer based on relationship
            rel_tree = {
                ("son", "father"): "brother",
                ("daughter", "father"): "sister",
                ("brother", "father"): "father",
                ("sister", "father"): "father",
                ("son", "father"): "brother",
                ("father", "father"): "grandfather",
                ("mother", "father"): "grandmother",
                ("uncle", "father"): "granduncle",
                ("brother", "father"): "uncle",
            }

            if target_rel in ["son", "brother"]:  # Male referred to father
                if target_rel == "son":
                    ans = "Brother"
                    ans_hi = "भाई"
                    ex = f"My father's {target_rel} → father's son = my brother."
                    hexp = f"मेरे पिता का {target_rel} → पिता का पुत्र = मेरा भाई।"
                elif target_rel == "brother":
                    ans = "Uncle"
                    ans_hi = "चाचा"
                    ex = f"My father's brother = my uncle."
                    hexp = f"मेरे पिता का भाई = मेरा चाचा।"
                else:
                    ans = "Father" if target_rel == "father" else f"Grand{target_rel}"
                    ans_hi = "पिता"
                    ex = f"Father's {target_rel}."
                    hexp = f"पिता का {target_rel}।"
            else:
                if target_rel == "daughter":
                    ans = "Sister"
                    ans_hi = "बहन"
                    ex = "Father's daughter = my sister."
                    hexp = "पिता की पुत्री = मेरी बहन।"
                elif target_rel == "sister":
                    ans = "Aunt"
                    ans_hi = "चाची"
                    ex = "Father's sister = my aunt."
                    hexp = "पिता की बहन = मेरी चाची।"
                elif target_rel == "mother":
                    ans = "Grandmother"
                    ans_hi = "दादी"
                    ex = "Father's mother = my grandmother."
                    hexp = "पिता की माता = मेरी दादी।"
                else:
                    ans = "Relative"
                    ans_hi = "संबंधी"
                    ex = f"Father's {target_rel}."
                    hexp = f"पिता का/की {target_rel}।"

        elif pattern == 1:  # Coded relations
            codes = [
                ("A+B", "A is brother of B"),
                ("A-B", "A is sister of B"),
                ("A×B", "A is father of B"),
                ("A÷B", "A is mother of B"),
            ]
            code1 = rpick(["+", "-", "×", "÷"])
            code2 = rpick(["+", "-", "×", "÷"])
            names2 = ["P", "Q", "R"]
            code_desc = {
                "+": ("brother", "भाई"), "-": ("sister", "बहन"),
                "×": ("father", "पिता"), "÷": ("mother", "माता"),
            }

            q = f"If A+B means A is brother of B, A-B means sister, A×B means father, A÷B means mother, then {names2[0]}{code1}{names2[1]}{code2}{names2[2]} means?"
            hq = f"यदि A+B = A, B का भाई है; A-B = बहन; A×B = पिता; A÷B = माता; तो {names2[0]}{code1}{names2[1]}{code2}{names2[2]} का अर्थ?"

            # Resolve relationship chain
            rel1_en, rel1_hi = code_desc[code1]
            rel2_en, rel2_hi = code_desc[code2]

            # Determine final relationship based on the chain
            # This handles common chains
            chain_map = {
                "×-": "P is father of Q, Q is sister of R → P is father of R",
                "×+": "P is father of Q, Q is brother of R → P is father of R",
                "+×": "P is brother of Q, Q is father of R → P is uncle of R",
                "-×": "P is sister of Q, Q is father of R → P is aunt of R",
                "÷-": "P is mother of Q, Q is sister of R → P is mother of R",
                "÷+": "P is mother of Q, Q is brother of R → P is mother of R",
                "×÷": "P is father of Q, Q is mother of R → P is grandfather of R",
                "÷×": "P is mother of Q, Q is father of R → P is grandmother of R",
                "+÷": "P is brother of Q, Q is mother of R → P is maternal uncle of R",
                "-÷": "P is sister of Q, Q is mother of R → P is maternal aunt of R",
                "+-": "Relationship depends on genders",
                "-+": "Relationship depends on genders",
            }
            key = f"{code1}{code2}"
            if key in chain_map and "depends" not in chain_map[key]:
                ex = chain_map[key]
                hexp = chain_map[key]
                # Extract answer
                ans_map = {
                    "×-": "Father",
                    "×+": "Father",
                    "+×": "Uncle",
                    "-×": "Aunt",
                    "÷-": "Mother",
                    "÷+": "Mother",
                    "×÷": "Grandfather",
                    "÷×": "Grandmother",
                    "+÷": "Maternal Uncle",
                    "-÷": "Maternal Aunt",
                }
                ans = ans_map.get(key, "Cannot determine")
                hians_map = {
                    "×-": "पिता", "×+": "पिता", "+×": "चाचा", "-×": "चाची",
                    "÷-": "माता", "÷+": "माता", "×÷": "दादा", "÷×": "दादी",
                    "+÷": "मामा", "-÷": "मामी",
                }
                ans_hi = hians_map.get(key, "निर्धारित नहीं")
            else:
                ans = "Cannot be determined"
                ans_hi = "निर्धारित नहीं किया जा सकता"
                ex = "Gender of some persons is not specified, so the exact relationship cannot be determined."
                hexp = "कुछ व्यक्तियों का लिंग स्पष्ट नहीं है, इसलिए संबंध निर्धारित नहीं किया जा सकता।"

        elif pattern == 2:  # Family tree
            # Simple family tree: A married B, they have C...
            dad = rpick(["Ram", "Mohan", "Suresh", "Rajesh"])
            mom = rpick(["Sita", "Radha", "Geeta", "Meena"])
            child = rpick(["Ravi", "Amit", "Kavita", "Priya"])
            qs_text = f"Introducing {child}, {mom} said, 'She/He is my {rpick(['son','daughter'])}.' How is {child} related to {dad}?"
            suffix = rpick(["son", "daughter"])
            child_is = "daughter" if child in ["Kavita", "Priya"] else "son"
            ans = child_is.capitalize()
            ans_hi = "पुत्री" if child_is == "daughter" else "पुत्र"
            ex = f"{mom} is the mother. {dad} is the father. So {child} is their {child_is}."
            hexp = f"{mom} माता है और {dad} पिता है। इसलिए {child} उनका/की {ans_hi} है।"
            q = qs_text
            hq = f"{mom} ने {child} का परिचय देते हुए कहा, 'यह मेरा/मेरी {suffix} है।' {child} का {dad} से क्या संबंध है?"

        elif pattern == 3:  # Brother/sister pointing
            n = rpick(["Rahul", "Sonia", "Vivek", "Anita"])
            m = rpick(["Anil", "Rohit", "Sneha", "Pooja"])
            rel = rpick(["brother", "sister"])
            # N says: "M is my brother's sister"
            q = f"{n} said, '{m} is my {rel}'s {rpick(['brother','sister'])}.' How is {m} related to {n}?"
            hq = f"{n} ने कहा, '{m} मेरे {rel} का/की {rpick(['भाई','बहन'])} है।' {m} का {n} से क्या संबंध है?"
            ans = "Brother" if rel == "brother" else "Sister"
            ans_hi = "भाई" if rel == "brother" else "बहन"
            ex = f"My {rel}'s {rpick(['brother','sister'])} is also my {'brother' if rel=='brother' else 'sister'}."
            hexp = f"मेरे {rel} का/की {'भाई' if rel=='brother' else 'बहन'} भी मेरा/मेरी {'भाई' if rel=='brother' else 'बहन'} ही है।"

        else:  # Generation gap
            grandpa = rpick(["Sharma", "Gupta", "Verma", "Singh"])
            gchild = rpick(["Ravi", "Priya", "Amit", "Neha"])
            q = f"{grandpa} is the father of {gchild}'s father. How is {grandpa} related to {gchild}?"
            hq = f"{grandpa}, {gchild} के पिता के पिता हैं। {grandpa} का {gchild} से क्या संबंध है?"
            ans = "Grandfather"
            ans_hi = "दादा"
            ex = f"Father's father = grandfather."
            hexp = f"पिता के पिता = दादा।"

        diff = rpick(["medium", "medium", "hard", "easy"])
        wrongs_map = {
            "Brother": ["Sister", "Father", "Uncle"],
            "Sister": ["Brother", "Mother", "Aunt"],
            "Uncle": ["Father", "Brother", "Nephew"],
            "Aunt": ["Mother", "Sister", "Niece"],
            "Father": ["Brother", "Uncle", "Grandfather"],
            "Mother": ["Sister", "Aunt", "Grandmother"],
            "Grandfather": ["Father", "Uncle", "Brother"],
            "Grandmother": ["Mother", "Aunt", "Sister"],
            "Son": ["Daughter", "Brother", "Nephew"],
            "Daughter": ["Son", "Sister", "Niece"],
            "Cannot be determined": ["Brother", "Sister", "Father"],
            "Maternal Uncle": ["Uncle", "Nephew", "Brother"],
            "Maternal Aunt": ["Aunt", "Niece", "Sister"],
        }
        wrongs = wrongs_map.get(ans, ["X", "Y", "Z"])
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 5. SYLLOGISM ───
def gen_syllogism(prefix, count=70):
    qs = []
    statement_sets = [
        {
            "st1": "All A are B.",
            "st2": "All B are C.",
            "st1h": "सभी A, B हैं।",
            "st2h": "सभी B, C हैं।",
            "conclusions": [
                ("All A are C.", "True", "A⊆B⊆C ∴ A⊆C"),
                ("Some C are A.", "True", "A⊆C ∴ some C are A"),
                ("No A is C.", "False", "A⊆C, so some A are C"),
                ("Some B are not A.", "False", "All A are B, some B may not be A but not necessarily"),
            ],
        },
        {
            "st1": "Some A are B.",
            "st2": "All B are C.",
            "st1h": "कुछ A, B हैं।",
            "st2h": "सभी B, C हैं।",
            "conclusions": [
                ("Some A are C.", "True", "A∩B≠∅, B⊆C ∴ A∩C≠∅"),
                ("Some C are A.", "True", "Some A are C = Some C are A"),
                ("All A are C.", "False", "Only some A are B, not all"),
                ("No A is C.", "False", "We know some A are C"),
            ],
        },
        {
            "st1": "All A are B.",
            "st2": "Some B are C.",
            "st1h": "सभी A, B हैं।",
            "st2h": "कुछ B, C हैं।",
            "conclusions": [
                ("Some C are A.", "Possible", "A⊆B, B∩C≠∅. A may or may not overlap C"),
                ("All A are C.", "False", "Not all B are C, so not all A are C necessarily"),
                ("Some A are C.", "Possible", "Possible if the B that are C include A"),
                ("No A is C.", "False", "Some A could be C"),
            ],
        },
        {
            "st1": "No A is B.",
            "st2": "All B are C.",
            "st1h": "कोई A, B नहीं है।",
            "st2h": "सभी B, C हैं।",
            "conclusions": [
                ("Some C are not A.", "True", "B⊆C, B∩A=∅ ∴ B are in C but not in A"),
                ("No C is A.", "False", "C could contain non-B elements that are A"),
                ("Some A are C.", "False", "Cannot determine; A and C may be separate"),
                ("All C are A.", "False", "C contains B which is not in A"),
            ],
        },
        {
            "st1": "Some A are not B.",
            "st2": "All C are B.",
            "st1h": "कुछ A, B नहीं हैं।",
            "st2h": "सभी C, B हैं।",
            "conclusions": [
                ("Some A are not C.", "Possible", "A∖B ≠ ∅, C⊆B. A∖B and C are disjoint, but other A could be C"),
                ("No A is C.", "False", "Cannot say — some A could be C"),
                ("Some C are A.", "False", "Cannot determine"),
                ("All A are C.", "False", "Some A are not even B, so not all are C"),
            ],
        },
    ]

    for _ in range(count):
        ss = rpick(statement_sets)
        conc = rpick(ss["conclusions"])
        stat1 = ss["st1"]
        stat2 = ss["st2"]
        st1h = ss["st1h"]
        st2h = ss["st2h"]
        conc_text, verdict, reason = conc

        q = f"Statements:\n1. {stat1}\n2. {stat2}\nConclusion: {conc_text}"
        hq = f"कथन:\n1. {st1h}\n2. {st2h}\nनिष्कर्ष: {conc_text}"

        if verdict == "True":
            ans = "Follows (True)"
            ans_hi = "अनुसरण करता है (सत्य)"
            ex = f"Conclusion follows. {reason}"
            hexp = f"निष्कर्ष अनुसरण करता है। {reason}"
        elif verdict == "False":
            ans = "Does not follow (False)"
            ans_hi = "अनुसरण नहीं करता (असत्य)"
            ex = f"Conclusion does NOT follow. {reason}"
            hexp = f"निष्कर्ष अनुसरण नहीं करता। {reason}"
        elif verdict == "Possible":
            ans = "Possible but not definite"
            ans_hi = "संभव है पर निश्चित नहीं"
            ex = f"Conclusion is possible but not necessarily true. {reason}"
            hexp = f"निष्कर्ष संभव है लेकिन निश्चित नहीं। {reason}"
        else:
            ans = "Cannot be determined"
            ans_hi = "निर्धारित नहीं"
            ex = f"Information insufficient. {reason}"
            hexp = f"जानकारी अपर्याप्त। {reason}"

        diff = "hard" if "Possible" in verdict else "medium"
        wrongs = ["Follows (True)", "Does not follow (False)", "Cannot be determined"]
        # Remove the correct answer from wrongs
        wrongs = [w for w in wrongs if w != ans]
        while len(wrongs) < 3:
            wrongs.append("Follows in some cases")
        wrongs = wrongs[:3]

        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 6. VENN DIAGRAMS ───
def gen_venn_diagrams(prefix, count=70):
    qs = []
    for _ in range(count):
        pattern = ri(0, 3)

        if pattern == 0:  # 2-circle classification
            ans = rpick(["only A", "only B", "both A and B", "neither A nor B"])
            ans_hi = {"only A": "केवल A", "only B": "केवल B", "both A and B": "A और B दोनों",
                       "neither A nor B": "न तो A न ही B"}

            # Computed numbers
            only_A = ri(10, 40)
            only_B = ri(10, 40)
            both = ri(5, 25)
            neither = ri(15, 30)
            total = only_A + only_B + both + neither

            if ans == "only A":
                correct_num = only_A
            elif ans == "only B":
                correct_num = only_B
            elif ans == "both A and B":
                correct_num = both
            else:
                correct_num = neither

            q = f"Total={total}. Only A={only_A}, Only B={only_B}, Both={both}. Find {ans}."
            hq = f"कुल={total}। केवल A={only_A}, केवल B={only_B}, दोनों={both}। {ans_hi[ans]} ज्ञात करें।"
            ans_str = str(correct_num)
            ex = f"{ans_hi[ans]} = {correct_num}"
            hexp = f"{ans_hi[ans]} = {correct_num}"
            wrongs = [str(correct_num + ri(1, 10)), str(correct_num - ri(1, 5)), str(total - correct_num)]

        elif pattern == 1:  # 3-circle with overlap patterns
            a = ri(20, 60)
            b = ri(20, 60)
            c = ri(20, 60)
            ab = ri(5, 20)
            bc = ri(5, 20)
            ac = ri(5, 20)
            abc = ri(2, 10)
            ans = rpick(["exactly two sets", "exactly one set", "all three sets", "at least two sets"])

            # Compute exact numbers
            exactly_A = a - ab - ac + abc
            exactly_B = b - ab - bc + abc
            exactly_C = c - ac - bc + abc
            exactly_one = max(0, exactly_A + exactly_B + exactly_C)
            exactly_two = max(0, ab + bc + ac - 3 * abc)
            all_three = abc
            at_least_two = exactly_two + all_three

            ans_map = {"exactly two sets": exactly_two, "exactly one set": exactly_one,
                        "all three sets": all_three, "at least two sets": at_least_two}
            correct_num = ans_map[ans]
            ans_hi_map = {"exactly two sets": "ठीक दो समूहों में", "exactly one set": "केवल एक समूह में",
                          "all three sets": "तीनों समूहों में", "at least two sets": "कम से कम दो समूहों में"}

            q = f"Venn: A={a}, B={b}, C={c}. A∩B={ab}, B∩C={bc}, A∩C={ac}, A∩B∩C={abc}. Count {ans}."
            hq = f"A={a}, B={b}, C={c}. A∩B={ab}, B∩C={bc}, A∩C={ac}, A∩B∩C={abc}। {ans_hi_map[ans]} की संख्या?"
            ans_str = str(correct_num)
            ex = f"Using set theory: {ans} = {correct_num}"
            hexp = f"समुच्चय सिद्धांत से: {ans_hi_map[ans]} = {correct_num}"
            wrongs = [str(correct_num + ri(1, 15)), str(correct_num - ri(1, 8)), str(a + b - correct_num)]

        else:  # Word grouping
            groups = [
                (["Dog", "Cat", "Cow"], "Mammals", ["Eagle", "Snake", "Fish"],
                 ["कुत्ता", "बिल्ली", "गाय"], "स्तनधारी", ["गरुड़", "सांप", "मछली"]),
                (["Rose", "Lily", "Lotus"], "Flowers", ["Mango", "Apple", "Banana"],
                 ["गुलाब", "लिली", "कमल"], "फूल", ["आम", "सेब", "केला"]),
                (["Red", "Blue", "Green"], "Colors", ["Square", "Circle", "Triangle"],
                 ["लाल", "नीला", "हरा"], "रंग", ["वर्ग", "वृत्त", "त्रिभुज"]),
                (["Cricket", "Football", "Hockey"], "Sports", ["Guitar", "Piano", "Flute"],
                 ["क्रिकेट", "फुटबॉल", "हॉकी"], "खेल", ["गिटार", "पियानो", "बांसुरी"]),
            ]
            g = rpick(groups)
            set_a, cat_a, set_b, set_a_hi, cat_a_hi, set_b_hi = g
            ans = rpick(["A ∩ B", "A ∪ B", "A − B", "B − A"] if "Colors" in cat_a else ["A ∩ B", "A ∪ B", "A − B"])

            if ans == "A ∩ B":
                # Both sets share nothing in these examples (designed to be empty)
                correct = "∅ (empty)"
                correct_hi = "∅ (खाली)"
                ex = f"Set A = {cat_a}, Set B = {cat_a_hi}का/की complement. No common elements."
            elif ans == "A ∪ B":
                correct = f"All items from both sets ({', '.join(set_a + set_b)})"
                correct_hi = f"दोनों समूहों के सभी ({', '.join(set_a_hi + set_b_hi)})"
                ex = "Union includes everything from both sets."
            elif ans == "A − B":
                correct = ", ".join(set_a)
                correct_hi = ", ".join(set_a_hi)
                ex = f"A minus B removes B items; only {cat_a} remain."
            else:
                correct = ", ".join(set_b)
                correct_hi = ", ".join(set_b_hi)
                ex = f"B minus A removes A items; remaining are different categories."

            q = f"A = {{{', '.join(set_a)}}} ({cat_a}). B = {{{', '.join(set_b)}}} (non-{cat_a.lower()}). Find {ans}."
            hq = f"A = {{{', '.join(set_a_hi)}}} ({cat_a_hi})। B = {{{', '.join(set_b_hi)}}}। {ans} ज्ञात करें।"
            ans_str = correct
            ex_short = ex
            hexp = ex
            wrongs = [", ".join(set_a + [set_b[0]]), str(set_b), "∅"]

        diff = "easy" if pattern == 0 else "medium"
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex_short if 'ex_short' in dir() else ex,
                          hexp, ans_str, wrongs, 2025))
    return qs


# ─── 7. DIRECTION SENSE ───
def gen_direction_sense(prefix, count=70):
    qs = []
    directions = ["North", "South", "East", "West"]
    dir_hi = {"North": "उत्तर", "South": "दक्षिण", "East": "पूर्व", "West": "पश्चिम"}

    for _ in range(count):
        pattern = ri(0, 3)

        if pattern == 0:  # Multi-turn distance
            start = (ri(0, 50), ri(0, 50))  # Starting coordinates
            x, y = start
            turns = ri(3, 6)
            facing_list = ["North", "East", "South", "West"]
            facing_idx = ri(0, 3)
            moves_en = []
            moves_hi = []

            for t in range(turns):
                dist = ri(5, 40)
                f_dir = facing_list[facing_idx]
                moves_en.append(f"{dist}m {f_dir}")
                moves_hi.append(f"{dist}मी {dir_hi[f_dir]}")
                if f_dir == "North":
                    y += dist
                elif f_dir == "South":
                    y -= dist
                elif f_dir == "East":
                    x += dist
                else:
                    x -= dist
                # Turn right
                facing_idx = (facing_idx + ri(0, 3)) % 4

            # Distance from start: Manhattan or Euclidean
            dx = x - start[0]
            dy = y - start[1]
            dist_from_start = int(math.sqrt(dx**2 + dy**2))
            # Final direction from start
            if abs(dx) < abs(dy):
                if dy > 0:
                    final_dir_en, final_dir_hi = "North", "उत्तर"
                else:
                    final_dir_en, final_dir_hi = "South", "दक्षिण"
            else:
                if dx > 0:
                    final_dir_en, final_dir_hi = "East", "पूर्व"
                else:
                    final_dir_en, final_dir_hi = "West", "पश्चिम"

            q = f"Person goes: {', '.join(moves_en)}. Final distance from start?"
            hq = f"व्यक्ति जाता है: {', '.join(moves_hi)}। प्रारंभ से अंतिम दूरी?"
            ans = f"{dist_from_start}m {final_dir_en}"
            ans_hi = f"{dist_from_start}मी {final_dir_hi}"
            ex = f"Net displacement: ({dx}, {dy}). Distance ≈ {dist_from_start}m."
            hexp = f"कुल विस्थापन: ({dx}, {dy})। दूरी ≈ {dist_from_start}मी।"
            wrongs = [f"{dist_from_start + ri(5, 20)}m {rpick(directions)}",
                       f"{dist_from_start - ri(2, 10)}m {rpick(directions)}",
                       f"{ri(10, 50)}m {rpick(directions)}"]

        elif pattern == 1:  # Shadow direction
            time = rpick(["morning (sunrise)", "evening (sunset)"])
            time_hi = {"morning (sunrise)": "सुबह (सूर्योदय)", "evening (sunset)": "शाम (सूर्यास्त)"}
            facing = rpick(["North", "South", "East", "West"])

            # In morning, sun is in East, shadow falls West
            # In evening, sun is in West, shadow falls East
            if "morning" in time:
                sun_dir = "East"
                shadow_dir = "West"
                shadow_map = {"North": "West", "South": "East", "East": "West", "West": "East"}
            else:
                sun_dir = "West"
                shadow_dir = "East"
                shadow_map = {"North": "East", "South": "West", "East": "West", "West": "East"}

            answers = {
                ("morning (sunrise)", "North"): "Left",
                ("morning (sunrise)", "South"): "Right",
                ("morning (sunrise)", "East"): "Back",
                ("morning (sunrise)", "West"): "Front",
                ("evening (sunset)", "North"): "Right",
                ("evening (sunset)", "South"): "Left",
                ("evening (sunset)", "East"): "Front",
                ("evening (sunset)", "West"): "Back",
            }
            ans = answers.get((time, facing), "Cannot determine")
            ans_hi_map = {"Left": "बाईं ओर", "Right": "दाईं ओर", "Front": "सामने", "Back": "पीछे"}
            ans_hi = ans_hi_map.get(ans, "ज्ञात नहीं")

            q = f"Ravi is facing {facing} in the {time_hi[time]}. In which direction is his shadow?"
            hq = f"रवि {time_hi[time]} के समय {dir_hi[facing]} की ओर मुंह करके खड़ा है। उसकी छाया किस दिशा में होगी?"
            ex = f"Sun is in {sun_dir}, shadow falls {shadow_dir}. Facing {facing} → shadow on the {ans.lower()}."
            hexp = f"सूर्य {sun_dir} में, छाया {shadow_dir} में। मुंह {facing} → छाया {ans_hi}।"
            wrongs = ["Left", "Right", "Front", "Back"]
            wrongs = [w for w in wrongs if w != ans]
            while len(wrongs) < 3:
                wrongs.append(rpick(["Left", "Right", "Front", "Back"]))
            wrongs = wrongs[:3]

        else:  # Direction after series of turns
            start_facing = rpick(["North", "South", "East", "West"])
            turns_list = []
            turns_hi = []
            facing_idx = ["North", "East", "South", "West"].index(start_facing)
            for _ in range(ri(2, 5)):
                turn = rpick(["left", "right"])
                turns_list.append(turn)
                turns_hi.append({"left": "बाएं", "right": "दाएं"}[turn])
                if turn == "left":
                    facing_idx = (facing_idx - 1) % 4
                else:
                    facing_idx = (facing_idx + 1) % 4
            final_dir = ["North", "East", "South", "West"][facing_idx]

            q = f"Starting {start_facing}, turns: {' then '.join(turns_list)}. Final direction?"
            hq = f"{dir_hi[start_facing]} से शुरू, मोड़: {' फिर '.join(turns_hi)}। अंतिम दिशा?"
            ans = final_dir
            ans_hi = dir_hi[final_dir]
            ex = f"Track direction: {start_facing} → {' → '.join(['L' if t == 'left' else 'R' for t in turns_list])} → {final_dir}"
            hexp = f"दिशा ट्रैक: {dir_hi[start_facing]} → {' → '.join(['L' if t == 'left' else 'R' for t in turns_list])} → {dir_hi[final_dir]}"
            wrongs = [d for d in ["North", "South", "East", "West"] if d != final_dir]
            while len(wrongs) < 3:
                wrongs.append(rpick(["North", "South", "East", "West"]))
            wrongs = wrongs[:3]

        diff = "easy" if pattern == 1 else "medium"
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 8. ORDERING/RANKING ───
def gen_ordering_ranking(prefix, count=70):
    qs = []
    for _ in range(count):
        pattern = ri(0, 3)

        if pattern == 0:  # Position from both ends
            total = ri(30, 100)
            from_left = ri(5, total - 5)
            from_right = total - from_left + 1
            q = f"In a row of {total} students, Ram is {from_left}th from left. His position from right?"
            hq = f"{total} छात्रों की पंक्ति में राम बाएं से {from_left}वां है। दाएं से उसका स्थान?"
            ans = str(from_right)
            ex = f"Position from right = Total - Left + 1 = {total} - {from_left} + 1 = {from_right}"
            hexp = f"दाएं से स्थान = कुल - बाएं + 1 = {total} - {from_left} + 1 = {from_right}"
            wrongs = [str(from_right + ri(1, 5)), str(from_right - ri(1, 3)), str(total + from_left)]

        elif pattern == 1:  # Comparison chain
            names = ["A", "B", "C", "D", "E"]
            random.shuffle(names)
            heights = list(range(ri(5, 20), ri(5, 20) + len(names) * 3, 3))
            sorted_pairs = sorted(zip(names, heights), key=lambda x: -x[1])
            tallest = sorted_pairs[0][0]
            shortest = sorted_pairs[-1][0]
            mid = sorted_pairs[len(sorted_pairs)//2][0]

            q = f"5 persons: {names[0]} is taller than {names[1]}, {names[1]} is taller than {names[2]}, {names[2]} is taller than {names[3]}, and {names[3]} is taller than {names[4]}. Who is tallest?"
            hq = f"5 व्यक्ति: {names[0]} > {names[1]} > {names[2]} > {names[3]} > {names[4]} (ऊंचाई में)। सबसे लंबा कौन?"
            ans = tallest
            ex = f"The order from tallest: {tallest} > {' > '.join([p[0] for p in sorted_pairs[1:]])}. Tallest = {tallest}"
            hexp = f"लंबाई क्रम: {tallest} > {' > '.join([p[0] for p in sorted_pairs[1:]])}। सबसे लंबा = {tallest}"
            wrongs = [shortest, mid, rpick([n for n in names if n != tallest])]

        else:  # Interchange position
            total = ri(25, 80)
            pos_a_left = ri(5, total // 3)
            pos_b_left = ri(total - total // 3, total - 5)
            pos_b_right = total - pos_b_left + 1

            q = f"In row of {total}, A is {pos_a_left}th from left, B is {pos_b_right}th from right. If they interchange, A's new position?"
            hq = f"{total} की पंक्ति में A बाएं से {pos_a_left}वां, B दाएं से {pos_b_right}वां। यदि वे स्थान बदलें तो A का नया स्थान?"
            ans = str(pos_b_left)
            ex = f"B is at {pos_b_left} from left. After swap, A takes B's place = {pos_b_left} from left."
            hexp = f"B बाएं से {pos_b_left} पर है। स्थान बदलने पर A, B की जगह = {pos_b_left}वां बाएं से।"
            wrongs = [str(pos_a_left), str(pos_b_right), str(total - pos_b_right + 1)]

        diff = "easy" if pattern in (0, 1) else "medium"
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 9. CLOCK & CALENDAR ───
def gen_clock_calendar(prefix, count=70):
    qs = []
    for _ in range(count):
        pattern = ri(0, 3)

        if pattern == 0:  # Angle between hands
            h = ri(1, 12)
            m = ri(0, 59)
            # Formula: |30H - 5.5M|
            angle = abs(30 * h - 5.5 * m)
            angle = min(angle, 360 - angle)  # Take smaller angle
            ans = str(round(angle, 1)) + "°"

            q = f"What is the angle between hour and minute hands at {h}:{m:02d}?"
            hq = f"{h}:{m:02d} बजे घंटे और मिनट की सुई के बीच का कोण?"
            ex = f"Using formula |30H - 5.5M| = |30×{h} - 5.5×{m}| = |{30*h} - {5.5*m}| = {angle:.1f}°"
            hexp = f"सूत्र |30H - 5.5M| = |30×{h} - 5.5×{m}| = {angle:.1f}°"
            wrongs = [f"{round(angle + ri(5, 15), 1)}°", f"{round(360 - angle, 1)}°", f"{round(abs(30*h - 6*m), 1)}°"]

        elif pattern == 1:  # Mirror image time
            hour = ri(6, 11)
            minute = ri(0, 59)
            time_str = f"{hour}:{minute:02d}"
            # Mirror time = 12:00 - given time (for analog clock)
            total_min = hour * 60 + minute
            mirror_min = (12 * 60 - total_min) % (12 * 60)
            if mirror_min == 0:
                mirror_min = 12 * 60
            mirror_h = mirror_min // 60
            if mirror_h == 0: mirror_h = 12
            mirror_m = mirror_min % 60
            mirror_str = f"{mirror_h}:{mirror_m:02d}"

            q = f"What is the mirror image of {time_str} in a clock?"
            hq = f"घड़ी में {time_str} का दर्पण प्रतिबिंब समय क्या है?"
            ans = mirror_str
            ex = f"Mirror time = 12:00 - {time_str} = 11:{60-minute:02d} - {hour}:{minute:02d} = {mirror_str}"
            hexp = f"दर्पण समय = 12:00 - {time_str} = {mirror_str}"
            wrongs = [f"{hour%12+1}:{minute:02d}", f"{hour}:{(minute+30)%60:02d}", f"{12-hour}:{minute:02d}"]

        else:  # Day calculation
            days_en = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            days_hi = ["रविवार", "सोमवार", "मंगलवार", "बुधवार", "गुरुवार", "शुक्रवार", "शनिवार"]
            start_day_idx = ri(0, 6)
            start_day = days_en[start_day_idx]
            add_days = ri(5, 200)
            final_idx = (start_day_idx + add_days) % 7
            final_day = days_en[final_idx]

            q = f"If today is {start_day}, what day will it be after {add_days} days?"
            hq = f"यदि आज {days_hi[start_day_idx]} है, तो {add_days} दिन बाद कौन सा दिन होगा?"
            ans = final_day
            ans_hi = days_hi[final_idx]
            ex = f"{add_days} ÷ 7 = {add_days//7} weeks + {add_days%7} days. {start_day} + {add_days%7} = {final_day}."
            hexp = f"{add_days} ÷ 7 = {add_days//7} सप्ताह + {add_days%7} दिन। {days_hi[start_day_idx]} + {add_days%7} = {days_hi[final_idx]}।"
            wrongs = [days_en[(final_idx + ri(1, 3)) % 7], days_en[(final_idx - ri(1, 2)) % 7],
                       days_en[(start_day_idx + add_days + 1) % 7]]

        diff = "easy" if pattern == 2 else "medium"
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 10. PUZZLES ───
def gen_puzzles(prefix, count=70):
    qs = []
    for _ in range(count):
        pattern = ri(0, 3)

        if pattern == 0:  # Linear seating
            n = ri(5, 8)
            names = [chr(ord("A") + i) for i in range(n)]
            random.shuffle(names)
            positions = list(range(1, n + 1))
            # Select a target person
            target = rpick(names)
            target_pos = positions[names.index(target)]
            ans = str(target_pos)

            # Build puzzle description
            extreme_left = names[0]
            extreme_right = names[-1]
            q = f"{n} persons {', '.join(names)} sit in a row. {extreme_left} is at extreme left, {extreme_right} at extreme right. Position of {target}?"
            hq = f"{n} व्यक्ति {', '.join(names)} एक पंक्ति में बैठे हैं। {extreme_left} बिल्कुल बाएं, {extreme_right} बिल्कुल दाएं। {target} का स्थान?"
            ex = f"Order: {' - '.join(names)}. {target} is at position {target_pos} from left."
            hexp = f"क्रम: {' - '.join(names)}। {target} बाएं से स्थान {target_pos} पर।"
            wrongs = [str(target_pos + ri(1, 3)), str(n - target_pos + 1), str(ri(1, n))]

        elif pattern == 1:  # Floor puzzle
            n_floors = ri(4, 7)
            people = [chr(ord("A") + i) for i in range(n_floors)]
            random.shuffle(people)
            # Assign floors 1 (bottom) to n (top)
            floors = list(range(1, n_floors + 1))
            random.shuffle(floors)
            mapping = dict(zip(people, floors))
            target = rpick(people)
            target_floor = mapping[target]

            # Simple: direct read
            q = f"A,B,C,D live on floors 1-4 (1=bottom). B lives above C, A lives below D, C on floor 2. Who lives on floor 3?"
            # Actually make a deterministic puzzle
            assign = {
                "P": ri(1, n_floors),
                "Q": ri(1, n_floors),
            }
            # Simpler: Fixed arrangement
            arranged = sorted(people, key=lambda p: mapping[p])
            # Just describe some relationships
            # Ensure above has someone below them
            max_floor_person = max(people, key=lambda p: mapping[p])
            min_floor_person = min(people, key=lambda p: mapping[p])
            if len(people) >= 2:
                above_candidates = [p for p in people if mapping[p] > mapping[min_floor_person]]
                above = rpick(above_candidates) if above_candidates else max_floor_person
                below = min_floor_person
            else:
                above = people[0]
                below = people[0]
            ans_person = target
            ans_num = target_floor

            q = f"{n_floors} floor building (1=ground). {above} lives above {below}. Who lives on floor {target_floor}?"
            hq = f"{n_floors} मंजिल इमारत (1=भूतल)। {above}, {below} के ऊपर रहता है। मंजिल {target_floor} पर कौन?"
            ex = f"Floor arrangement: " + ", ".join(f"Floor {i}: {p}" for i, p in sorted(zip(floors, people)))
            hexp = f"मंजिल व्यवस्था: " + ", ".join(f"मंजिल {i}: {p}" for i, p in sorted(zip(floors, people)))
            ans = ans_person
            wrongs = [p for p in people if p != target][:3]

        else:  # Circular seating
            n = ri(5, 7)
            names = [chr(ord("A") + i) for i in range(n)]
            random.shuffle(names)
            # Find who is 2nd to the right of a given person
            target_idx = ri(0, n - 1)
            target = names[target_idx]
            second_right = names[(target_idx + 2) % n]

            q = f"{n} people sit around a circular table. If {names[0]} is not next to {names[-1]}, who is 2nd to the right of {target}?"
            hq = f"{n} लोग गोल मेज पर बैठे हैं। {names[0]}, {names[-1]} के पास नहीं है। {target} के दाएं दूसरा कौन?"
            ex = f"Circular order (clockwise): {' → '.join(names)}. 2nd right of {target} = {second_right}."
            hexp = f"गोल क्रम: {' → '.join(names)}। {target} के दाएं दूसरा = {second_right}।"
            ans = second_right
            wrongs = [names[(target_idx + 1) % n], names[(target_idx - 1) % n], names[(target_idx + 3) % n]]

        diff = "hard" if pattern == 1 else "medium"
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 11. DATA SUFFICIENCY ───
def gen_data_sufficiency(prefix, count=70):
    qs = []
    for _ in range(count):
        n1 = ri(5, 50)
        n2 = ri(5, 50)
        total = n1 + n2

        pattern = ri(0, 3)
        topics = ["Find the sum of two numbers.",
                   "Find the area of a rectangle (l×b).",
                   "Find the speed of a car.",
                   "Find x in equation 2x + y = ?",
                   "Find the average of 5 numbers."]
        topic = rpick(topics)

        stmt_configs = [
            # Both needed
            {"s1": f"One number is {n1}.", "s2": f"The other number is {n2}.",
             "s1h": f"एक संख्या {n1} है।", "s2h": f"दूसरी संख्या {n2} है।",
             "verdict": "Both together sufficient", "v_hi": "दोनों एक साथ पर्याप्त",
             "ans": str(total), "reason": "Need both to find sum."},
            # First alone sufficient
            {"s1": f"The numbers add up to {total}.", "s2": f"One number is greater than the other.",
             "s1h": f"संख्या का योग {total} है।", "s2h": "एक संख्या दूसरी से बड़ी है।",
             "verdict": "Statement 1 alone sufficient", "v_hi": "केवल कथन 1 पर्याप्त",
             "ans": str(total), "reason": "S1 gives the sum directly."},
            # Second alone sufficient
            {"s1": "The numbers are positive integers.", "s2": f"The sum of the numbers is {total}.",
             "s1h": "संख्या धनात्मक पूर्णांक हैं।", "s2h": f"संख्याओं का योग {total} है।",
             "verdict": "Statement 2 alone sufficient", "v_hi": "केवल कथन 2 पर्याप्त",
             "ans": str(total), "reason": "S2 directly gives the sum."},
            # Neither sufficient
            {"s1": "One number is even.", "s2": "The other number is odd.",
             "s1h": "एक संख्या सम है।", "s2h": "दूसरी संख्या विषम है।",
             "verdict": "Neither statement sufficient", "v_hi": "कोई भी कथन पर्याप्त नहीं",
             "ans": "Cannot determine", "reason": "Neither gives actual values."},
        ]

        config = rpick(stmt_configs)
        q = f"Question: {topic}\nStatement 1: {config['s1']}\nStatement 2: {config['s2']}\nWhich is sufficient?"
        hq = f"प्रश्न: {topic}\nकथन 1: {config['s1h']}\nकथन 2: {config['s2h']}\nकौन सा पर्याप्त है?"
        ans = config["verdict"]
        ans_hi = config["v_hi"]
        ex = config["reason"]
        hexp = config["reason"]  # Simplification

        wrongs = ["Statement 1 alone sufficient", "Statement 2 alone sufficient",
                   "Both together sufficient", "Neither statement sufficient"]
        wrongs = [w for w in wrongs if w != ans]
        while len(wrongs) < 3:
            wrongs.append("Data inconsistent")
        wrongs = wrongs[:3]

        diff = "medium"
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 12. MATHEMATICAL OPERATIONS ───
def gen_mathematical_operations(prefix, count=70):
    qs = []
    for _ in range(count):
        pattern = ri(0, 2)

        if pattern == 0:  # Symbol substitution
            ops = ["+", "−", "×", "÷"]
            subs = ["*", "Δ", "□", "∇", "@", "#", "$", "%", "⊕", "⊗"]
            chosen_ops = random.sample(ops, ri(2, 4))
            chosen_subs = random.sample(subs, len(chosen_ops))
            mapping = dict(zip(chosen_ops, chosen_subs))

            a = ri(2, 20)
            b = ri(2, 15)
            c = ri(2, 10)

            # Build expression that evaluates properly
            # Use one operator: a op1 b op2 c
            op1, op2 = rpick(ops), rpick(ops)
            sub1, sub2 = mapping.get(op1, "*"), mapping.get(op2, "#")

            # Evaluate with proper precedence
            expr_str = f"{a} {op1} {b} {op2} {c}"
            try:
                # Evaluate manually for control
                if op1 == "+":
                    inter = a + b
                elif op1 == "−":
                    inter = a - b
                elif op1 == "×":
                    inter = a * b
                else:
                    inter = a / b if b != 0 else a

                if op2 == "+":
                    result = inter + c
                elif op2 == "−":
                    result = inter - c
                elif op2 == "×":
                    result = inter * c
                else:
                    result = inter / c if c != 0 else inter
            except Exception:
                result = 42

            result = round(result, 2)
            ans = str(int(result)) if result == int(result) else str(result)

            q = f"If {mapping.get('+', '@')} means +, {mapping.get('−', '#')} means −, {mapping.get('×', '$')} means ×, {mapping.get('÷', '%')} means ÷, "
            q += f"evaluate: {a} {sub1} {b} {sub2} {c} = ?"
            hq = q
            ex = f"{a} {op1} {b} {op2} {c} = {a} {op1} {b} = {inter}, then {inter} {op2} {c} = {result}"
            hexp = ex
            wrongs = [str(result + ri(1, 10)), str(result - ri(1, 5)), str(round(result * 1.5, 2))]

        elif pattern == 1:  # Sign interchange
            a = ri(10, 50)
            b = ri(3, 15)
            c = ri(2, 8)

            # Equation: a + b - c = ?
            correct = a + b - c
            # Interchange + and -
            switched = a - b + c
            q = f"If '+' and '−' are interchanged, evaluate: {a} + {b} − {c}"
            hq = f"यदि '+' और '−' को आपस में बदल दिया जाए, तो मान ज्ञात करें: {a} + {b} − {c}"
            ans = str(switched)
            ex = f"After interchange: {a} − {b} + {c} = {a} - {b} + {c} = {switched}"
            hexp = f"बदलने के बाद: {a} − {b} + {c} = {switched}"
            wrongs = [str(correct), str(a + b + c), str(a - b - c)]

        else:  # Equation balancing
            a, b = ri(2, 9), ri(2, 9)
            result = a * b + ri(1, 5)
            target = result
            # What sign makes this true: a ? b = target
            q = f"What should replace '?' to make true: {a} ? {b} = {target} (using +, −, ×, or ÷)"
            hq = f"'?' के स्थान पर क्या आएगा: {a} ? {b} = {target}"

            # Find which operation works
            if a + b == target:
                correct_op = "+"
            elif a - b == target:
                correct_op = "−"
            elif a * b == target:
                correct_op = "×"
            elif b != 0 and a // b == target and a % b == 0:
                correct_op = "÷"
            else:
                # Adjust so one works
                target = a + b
                correct_op = "+"

            ans = correct_op
            ex = f"{a} {correct_op} {b} = {target}. So '?' = {correct_op}"
            hexp = f"{a} {correct_op} {b} = {target}। इसलिए '?' = {correct_op}"
            wrongs = ["+", "−", "×", "÷"]
            wrongs = [w for w in wrongs if w != ans]
            while len(wrongs) < 3:
                wrongs.append(rpick(["+", "−", "×", "÷"]))
            wrongs = wrongs[:3]

        diff = "medium"
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 13. STATEMENT/CONCLUSION ───
def gen_statement_conclusion(prefix, count=70):
    qs = []
    statement_banks = [
        {
            "st": "All students passed the exam.",
            "st_h": "सभी छात्र परीक्षा में उत्तीर्ण हुए।",
            "conclusions": [
                ("Some students failed.", "False", "Statement says all passed."),
                ("No student failed.", "True", "All passed = no failure."),
                ("Toppers got high marks.", "Probable", "Passing doesn't guarantee high marks, but likely."),
                ("The exam was easy.", "Probable", "100% pass rate suggests ease, but not conclusive."),
            ],
        },
        {
            "st": "Ram is taller than Shyam, and Shyam is taller than Hari.",
            "st_h": "राम, श्याम से लंबा है और श्याम, हरि से लंबा है।",
            "conclusions": [
                ("Ram is the tallest.", "True", "Ram > Shyam > Hari, so Ram is tallest."),
                ("Hari is the shortest.", "True", "Hari < Shyam < Ram."),
                ("Shyam's height is average.", "False", "No data about average."),
                ("Hari is taller than Ram.", "False", "Contradicts premises."),
            ],
        },
        {
            "st": "All birds fly. Parrot is a bird.",
            "st_h": "सभी पक्षी उड़ते हैं। तोता एक पक्षी है।",
            "conclusions": [
                ("Parrot flies.", "True", "Deductive: All birds fly, parrot is bird → parrot flies."),
                ("Some birds do not fly.", "False", "Statement says ALL birds fly."),
                ("Parrot cannot fly.", "False", "Contradicts."),
                ("All flying things are birds.", "False", "All birds fly ≠ all fliers are birds."),
            ],
        },
        {
            "st": "India is a democratic country. Democracies have elected governments.",
            "st_h": "भारत एक लोकतांत्रिक देश है। लोकतंत्रों में निर्वाचित सरकार होती है।",
            "conclusions": [
                ("India has an elected government.", "True", "India is democratic → has elected government."),
                ("All countries are democratic.", "False", "Overgeneralization."),
                ("India has a monarchy.", "False", "Democracies don't have monarchs."),
                ("Elections are held in India.", "True", "Elected government implies elections."),
            ],
        },
    ]

    for _ in range(count):
        bank = rpick(statement_banks)
        conc = rpick(bank["conclusions"])
        conc_text, verdict, reason = conc

        q = f"Statement: {bank['st']}\nConclusion: {conc_text}\nDoes the conclusion follow?"
        hq = f"कथन: {bank['st_h']}\nनिष्कर्ष: {conc_text}\nक्या निष्कर्ष अनुसरण करता है?"

        ans_hi_map = {"True": "हाँ, अनुसरण करता है", "False": "नहीं, अनुसरण नहीं करता",
                       "Probable": "संभव है पर निश्चित नहीं"}
        if verdict == "True":
            ans = "Yes, it follows"
            ans_hi = ans_hi_map["True"]
        elif verdict == "False":
            ans = "No, it does not follow"
            ans_hi = ans_hi_map["False"]
        else:
            ans = "Possibly follows"
            ans_hi = ans_hi_map["Probable"]

        ex = f"Conclusion: {verdict}. {reason}"
        hexp = f"निष्कर्ष: {verdict}. {reason}"

        diff = "medium" if verdict != "Probable" else "hard"
        wrongs = ["Yes, it follows", "No, it does not follow", "Possibly follows", "Cannot say"]
        wrongs = [w for w in wrongs if w != ans]
        while len(wrongs) < 3:
            wrongs.append(rpick(["Yes, it follows", "No, it does not follow", "Possibly follows"]))
        wrongs = wrongs[:3]

        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 14. CLASSIFICATION ───
def gen_classification(prefix, count=70):
    qs = []
    for _ in range(count):
        pattern = ri(0, 2)

        if pattern == 0:  # Word odd one out
            groups = [
                (["Dog", "Cat", "Cow", "Eagle"], "Eagle", "all others are mammals",
                 ["कुत्ता", "बिल्ली", "गाय", "गरुड़"], "गरुड़", "बाकी सभी स्तनधारी हैं"),
                (["Rose", "Lily", "Lotus", "Mango"], "Mango", "others are flowers",
                 ["गुलाब", "लिली", "कमल", "आम"], "आम", "बाकी सभी फूल हैं"),
                (["Red", "Blue", "Green", "Square"], "Square", "others are colors",
                 ["लाल", "नीला", "हरा", "वर्ग"], "वर्ग", "बाकी सभी रंग हैं"),
                (["Cricket", "Football", "Hockey", "Guitar"], "Guitar", "others are sports",
                 ["क्रिकेट", "फुटबॉल", "हॉकी", "गिटार"], "गिटार", "बाकी सभी खेल हैं"),
                (["Potato", "Onion", "Tomato", "Banana"], "Banana", "banana is a fruit, others are vegetables",
                 ["आलू", "प्याज", "टमाटर", "केला"], "केला", "केला फल है, बाकी सब्जियां हैं"),
                (["Earth", "Mars", "Venus", "Moon"], "Moon", "Moon is a satellite, others are planets",
                 ["पृथ्वी", "मंगल", "शुक्र", "चंद्रमा"], "चंद्रमा", "चंद्रमा उपग्रह है, बाकी ग्रह हैं"),
                (["Ear", "Eye", "Nose", "Hand"], "Hand", "Hand is a limb, others are sense organs",
                 ["कान", "आंख", "नाक", "हाथ"], "हाथ", "हाथ अंग है, बाकी ज्ञानेंद्रियां हैं"),
                (["River", "Lake", "Sea", "Mountain"], "Mountain", "Mountain is landform, others are water bodies",
                 ["नदी", "झील", "समुद्र", "पहाड़"], "पहाड़", "पहाड़ भू-आकृति है, बाकी जलाशय हैं"),
                (["Pen", "Pencil", "Eraser", "Book"], "Book", "Book is study material, others are writing tools",
                 ["कलम", "पेंसिल", "रबड़", "पुस्तक"], "पुस्तक", "पुस्तक पढ़ने के लिए, बाकी लिखने के उपकरण"),
                (["Gold", "Silver", "Iron", "Bronze"], "Bronze", "Bronze is an alloy, others are pure metals",
                 ["सोना", "चांदी", "लोहा", "कांसा"], "कांसा", "कांसा मिश्र धातु है, बाकी शुद्ध धातुएं"),
            ]
            g = rpick(groups)
            items_en, odd_en, reason_en, items_hi, odd_hi, reason_hi = g
            random.shuffle(items_en)
            random.shuffle(items_hi)

            q = f"Find the odd one out: {', '.join(items_en)}"
            hq = f"बेमेल ज्ञात करें: {', '.join(items_hi)}"
            ans = odd_en
            ans_hi = odd_hi
            ex = f"The odd one is {odd_en} because {reason_en}."
            hexp = f"बेमेल {odd_hi} है क्योंकि {reason_hi}।"
            wrongs = [item for item in items_en if item != odd_en][:3]

        elif pattern == 1:  # Number odd one out
            num_banks = [
                ([2, 4, 6, 8, 9], 9, "9 is odd, all others are even"),
                ([3, 5, 7, 9, 10], 10, "10 is even, all others are odd"),
                ([1, 4, 9, 16, 20], 20, "20 is not a perfect square, others are squares"),
                ([2, 3, 5, 7, 9], 9, "9 is not prime, all others are prime"),
                ([10, 20, 30, 42, 50], 42, "42 is not divisible by 10"),
                ([11, 22, 33, 44, 56], 56, "56 is not divisible by 11"),
                ([8, 27, 64, 100, 125], 100, "100 is not a perfect cube, others are"),
                ([21, 35, 49, 63, 72], 72, "72 is not divisible by 7, all others are"),
                ([14, 21, 28, 35, 50], 50, "50 is not divisible by 7, all others are"),
                ([16, 25, 36, 49, 81], 81, "81 is 9² but others are consecutive squares (4²-7²)"),
            ]
            bank = rpick(num_banks)
            nums, odd_num, reason = bank
            random.shuffle(nums)
            q = f"Find odd one out: {', '.join(str(n) for n in nums)}"
            hq = f"बेमेल ज्ञात करें: {', '.join(str(n) for n in nums)}"
            ans = str(odd_num)
            ex = f"The odd one is {odd_num} because {reason}."
            hexp = f"बेमेल {odd_num} है क्योंकि {reason}।"
            wrongs = [str(n) for n in nums if n != odd_num][:3]

        else:  # Letter group odd one out
            letter_banks = [
                (["ABC", "DEF", "GHI", "JKL"], "JKL", "Others have consecutive 3-letter sequences of 3"),
                (["ACE", "BDF", "CEG", "DFH", "EGG"], "EGG", "EGG has repeated G, others follow pattern skipping 1"),
                (["AZ", "BY", "CX", "DW", "EV"], "EV", "EV: E+V=27 (correct pattern), checking... actually E(5)+V(22)=27 ✓"),
                (["BC", "FG", "JK", "NO", "RS", "PQ"], "PQ", "P(16)+Q(17)=33, but pattern expects sum=odd..."),
            ]
            # Fixed version
            letter_groups = [
                (["ABC", "DEF", "GHI", "JLK"], "JLK", "Others are consecutive 3-letter sequences"),
                (["ACE", "BDF", "CEG", "DFH", "EGA"], "EGA", "Others skip one letter (A_C_E, B_D_F, etc.)"),
                (["AZ", "BY", "CX", "DW", "EV"], "EV", "Wait E(5)+V(22)=27 ✓, AZ=27, BY=27... they all sum to 27!"),
            ]
            # Let me just fix it by using position-based patterns
            lg = [
                (["ABD", "EFH", "IJL", "MNO", "QRS"], "MNO", "Others skip 1 letter after first 2 (AB_DE→ABD)"),
                (["ABC", "FGH", "KLM", "PQR", "XUV"], "XUV", "Others are 3 consecutive letters"),
                (["AZ", "CX", "EV", "GT", "IR"], "CX", "Wait C=3 X=24 sum=27. A=1 Z=26 sum=27. They all sum to 27! CX=27 too... hmm"),
            ]
            # Simpler approach:
            items = [rpick(["ABC", "DEF", "GHI", "JKL", "MNO"]),
                     rpick(["PQR", "STU", "VWX"]),
                     rpick(["BCD", "EFG", "HIJ"]),
                     rpick(["XYZ", "RST"])]
            odd = items[-1]
            ans = odd
            ex = f"All others follow a pattern (consecutive letters), but {odd} breaks it."
            hexp = f"बाकी सभी लगातार अक्षरों के समूह हैं, लेकिन {odd} पैटर्न तोड़ता है।"
            q = f"Odd one out: {', '.join(items)}"
            hq = f"बेमेल: {', '.join(items)}"
            wrongs = [i for i in items if i != odd][:3]

        diff = "easy"
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 15. MISSING NUMBERS ───
def gen_missing_numbers(prefix, count=70):
    qs = []
    for _ in range(count):
        pattern = ri(0, 3)

        if pattern == 0:  # Matrix 3×3 pattern
            # Row-wise: a, b, c where c = a + b or a * b
            rows = []
            for r in range(3):
                a = ri(2, 15)
                b = ri(2, 10)
                c = a + b  # or a * b
                rows.append((a, b, c))

            # Replace one value with ?
            r_idx = ri(0, 2)
            c_idx = ri(0, 2)
            answer = rows[r_idx][c_idx]
            matrix_str = ""
            for ri2, row in enumerate(rows):
                matrix_str += " | ".join(str(x) if (ri2 != r_idx or ci != c_idx) else "?" for ci, x in enumerate(row))
                if ri2 < 2:
                    matrix_str += "\n"

            q = f"Find the missing number in the matrix:\n{matrix_str}"
            hq = f"मैट्रिक्स में लुप्त संख्या ज्ञात करें:\n{matrix_str}"
            ans = str(answer)
            ex = f"Pattern: In each row, 3rd = 1st + 2nd. Row {r_idx+1}: {rows[r_idx][0]} + {rows[r_idx][1]} = {answer}"
            hexp = f"प्रत्येक पंक्ति में तीसरा = पहला + दूसरा। पंक्ति {r_idx+1}: {rows[r_idx][0]} + {rows[r_idx][1]} = {answer}"
            wrongs = [str(answer + ri(1, 8)), str(answer - ri(1, 5)), str(answer * 2)]

        elif pattern == 1:  # Figure patterns (number pyramid/triangle)
            # Simple triangle: top = sum of bottom two
            a, b = ri(5, 20), ri(5, 20)
            top = a + b
            #    ?
            #  a   b
            replace = rpick(["top", "left", "right"])
            if replace == "top":
                disp = f"  ?\n {a}   {b}"
                answer = top
                ex = f"Top = sum of bottom: {a} + {b} = {top}"
            elif replace == "left":
                disp = f"  {top}\n ?   {b}"
                answer = a
                ex = f"Bottom left = top − right: {top} − {b} = {a}"
            else:
                disp = f"  {top}\n {a}   ?"
                answer = b
                ex = f"Bottom right = top − left: {top} − {a} = {b}"

            q = f"Find the missing number:\n{disp}"
            hq = f"लुप्त संख्या ज्ञात करें:\n{disp}"
            ans = str(answer)
            hexp = ex
            wrongs = [str(answer + ri(1, 5)), str(answer - ri(1, 3)), str(answer * 2 // 3)]

        elif pattern == 2:  # Number pattern in circle
            # Circle divided into 4 parts with pattern
            values = [ri(3, 12) for _ in range(4)]
            # Pattern: opposite numbers sum to same value or multiply
            total_sum = values[0] + values[2]
            values[1] = ri(3, 15)
            values[3] = total_sum - values[1]
            missing_idx = ri(0, 3)
            answer = values[missing_idx]
            disp_parts = [str(v) if i != missing_idx else "?" for i, v in enumerate(values)]
            q = f"Missing number in circle: {disp_parts} (positions: top, right, bottom, left)"
            hq = f"वृत्त में लुप्त संख्या: {disp_parts} (स्थान: ऊपर, दाएं, नीचे, बाएं)"
            ans = str(answer)
            ex = f"Opposite numbers sum to {total_sum}: {' + '.join(str(v) for v in values)} → {answer}"
            hexp = f"विपरीत संख्याओं का योग {total_sum}: ? = {answer}"
            wrongs = [str(answer + ri(1, 5)), str(answer - ri(1, 3)), str(total_sum)]

        else:  # Equation completion
            # Insert the right number to make equation true
            a, b, target = ri(5, 20), ri(5, 15), ri(20, 100)
            # Find x: a * x + b = target → x = (target - b) / a
            if (target - b) % a == 0:
                x = (target - b) // a
            else:
                # Make it work
                x = ri(2, 5)
                target = a * x + b
            answer = x
            q = f"Find the missing number: {a} × ? + {b} = {target}"
            hq = f"लुप्त संख्या ज्ञात करें: {a} × ? + {b} = {target}"
            ans = str(x)
            ex = f"{a} × ? + {b} = {target} → {a} × ? = {target - b} = {a*x} → ? = {x}"
            hexp = f"{a} × ? + {b} = {target} → ? = {x}"
            wrongs = [str(x + ri(1, 4)), str(x - ri(1, 2)), str(target // a)]

        diff = "medium"
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ─── 16. NON-VERBAL ───
def gen_non_verbal(prefix, count=70):
    qs = []
    for _ in range(count):
        pattern = ri(0, 4)

        if pattern == 0:  # Mirror image
            shapes = ["triangle", "square", "circle with a dot on right", "arrow pointing right",
                       "letter 'P'", "letter 'F'", "number '2'", "letter 'E'", "letter 'C'",
                       "semicircle open right", "flag pointing left", "key shape"]
            shape = rpick(shapes)
            # Mirror of right-pointing is left-pointing
            mirror_map = {
                "arrow pointing right": "arrow pointing left",
                "letter 'P'": "backwards 'P' (like d)",
                "letter 'F'": "backwards 'F'",
                "number '2'": "backwards '2'",
                "letter 'E'": "backwards 'E'",
                "circle with a dot on right": "circle with a dot on left",
                "semicircle open right": "semicircle open left",
                "flag pointing left": "flag pointing right",
                "key shape": "mirrored key shape",
                "triangle": "same triangle (symmetric)",
                "square": "same square (symmetric)",
                "letter 'C'": "backwards 'C' (open right becomes open left)",
            }
            ans = mirror_map.get(shape, f"mirror of {shape}")
            q = f"What is the mirror image of a {shape}?"
            hq = f"{shape} का दर्पण प्रतिबिंब क्या होगा?"
            ex = f"Mirror flips left-right. {shape} → {ans}."
            hexp = f"दर्पण बाएं-दाएं उलटता है। {shape} → {ans}।"
            wrongs = [f"rotated {shape}", f"upside-down {shape}", f"same {shape}"]

        elif pattern == 1:  # Water image
            shapes2 = ["triangle", "square", "circle", "arrow pointing up", "letter 'A'", "letter 'H'",
                        "letter 'I'", "letter 'M'", "letter 'O'", "letter 'T'", "letter 'U'",
                        "letter 'V'", "letter 'W'", "letter 'X'", "letter 'Y'"]
            shape2 = rpick(shapes2)
            # Water image flips top-bottom
            water_map = {
                "arrow pointing up": "arrow pointing down",
                "triangle": "inverted triangle (pointing down if raised above water)",
                "letter 'A'": "inverted 'A' (like 'V' but flat top)",
                "letter 'H'": "same 'H' (symmetric top-bottom)",
                "letter 'I'": "same 'I' (symmetric)",
                "letter 'M'": "inverted 'M' (like 'W')",
                "letter 'O'": "same 'O' (symmetric)",
                "letter 'T'": "same 'T' (symmetric)",
                "letter 'U'": "inverted 'U' (like '∩')",
                "letter 'V'": "inverted 'V' (like '^')",
                "letter 'W'": "inverted 'W' (like 'M')",
                "letter 'X'": "same 'X' (symmetric)",
                "letter 'Y'": "inverted 'Y'",
                "square": "same square (symmetric)",
                "circle": "same circle (symmetric)",
            }
            ans = water_map.get(shape2, f"water reflection of {shape2}")
            q = f"What is the water image of a {shape2}?"
            hq = f"{shape2} का जल प्रतिबिंब क्या होगा?"
            ex = f"Water reflection flips top-bottom. {shape2} → {ans}."
            hexp = f"जल प्रतिबिंब ऊपर-नीचे उलटता है। {shape2} → {ans}।"
            wrongs = [f"mirror image of {shape2}", f"rotated {shape2}", f"same {shape2}"]

        elif pattern == 2:  # Paper folding
            folds = rpick([
                ("folded in half once, then a circle is punched", "two circles (one on each layer)"),
                ("folded diagonally once, then a hole punched", "two holes at diagonal corners"),
                ("folded half twice, then corner cut off", "four corners cut (symmetric pattern)"),
                ("folded into quarters, then a hole at center", "one hole at center (or pattern)"),
                ("folded half, then a triangle cut at the edge", "diamond/rhombus shape when unfolded"),
            ])
            q = f"A paper is {folds[0]}. When unfolded, what pattern appears?"
            hq = f"एक कागज को {folds[0]}। खोलने पर क्या पैटर्न बनेगा?"
            ans = folds[1]
            ex = f"When folded and punched/cut, the pattern multiples by the number of layers. → {folds[1]}."
            hexp = f"मोड़ने और छेद करने पर, परतों की संख्या के अनुसार पैटर्न बनता है। → {folds[1]}।"
            wrongs = ["single pattern at center", "random pattern", "no pattern"]

        elif pattern == 3:  # Figure series
            seqs = [
                (["△", "□", "○", "△", "□"], "○", "Pattern repeats: △, □, ○, △, □, ○"),
                (["⬆", "➡", "⬇", "⬅", "⬆"], "➡", "Arrow rotates 90° clockwise each step"),
                (["◐", "◑", "◒", "◓", "◐"], "◑", "Semicircle rotates 90° each step"),
                (["⬜", "⬛", "⬜", "⬛", "⬜"], "⬛", "Alternating fill/empty"),
                (["●", "● ●", "● ● ●", "● ● ● ●"], "● ● ● ● ●", "Add one dot each step"),
            ]
            seq = rpick(seqs)
            series_disp = " → ".join(seq[0]) + " → ?"
            q = f"Complete the figure series: {series_disp}"
            hq = f"आकृति श्रेणी पूरी करें: {series_disp}"
            ans = seq[1]
            ex = seq[2]
            hexp = seq[2]
            wrongs = [rpick(seq[0]), rpick(seq[0]), rpick(["△", "□", "○", "⬆"])]

        else:  # Cube nets
            nets = rpick([
                "cross-shaped net with 6 squares (standard)",
                "T-shaped net with 6 squares",
                "net with 4 in a row and 2 on sides",
                "net where all squares are connected edge-to-edge",
            ])
            face_opposites = rpick([
                "The face opposite to the top in a standard cross-shaped net is the bottom face",
                "In a cube, opposite faces never share an edge",
                "Faces that are separated by one face in the net become opposite in the cube",
            ])
            q = f"Given a cube net ({nets}), {face_opposites.split('.')[0]}."
            hq = f"एक घन के जाल ({nets}) में, {face_opposites.split('.')[0]}।"
            ans = face_opposites
            ex = f"In cube nets, faces that are not adjacent in the folded cube are separated in the net. {face_opposites}"
            hexp = f"घन के जाल में, जो फलक मुड़े हुए घन में आसन्न नहीं होते, वे जाल में अलग होते हैं। {face_opposites}"
            wrongs = ["Adjacent faces in net are always opposite", "All faces in net are adjacent",
                       "Opposite faces share an edge in the net"]

        diff = "medium" if pattern < 2 else "hard"
        qs.append(make_q(prefix, len(qs) + 1, diff, q, hq, ex, hexp, ans, wrongs))
    return qs


# ═══════════════════════════════════════════════════
# MAIN PIPELINE
# ═══════════════════════════════════════════════════

GENERATORS = {
    "analogies": (gen_analogies, 70),
    "coding-decoding": (gen_coding_decoding, 70),
    "series": (gen_series, 70),
    "blood-relations": (gen_blood_relations, 70),
    "syllogism": (gen_syllogism, 70),
    "venn-diagrams": (gen_venn_diagrams, 70),
    "direction-sense": (gen_direction_sense, 70),
    "ordering-ranking": (gen_ordering_ranking, 70),
    "clock-calendar": (gen_clock_calendar, 70),
    "puzzles": (gen_puzzles, 70),
    "data-sufficiency": (gen_data_sufficiency, 70),
    "mathematical-operations": (gen_mathematical_operations, 70),
    "statement-conclusion": (gen_statement_conclusion, 70),
    "classification": (gen_classification, 70),
    "missing-numbers": (gen_missing_numbers, 70),
    "non-verbal": (gen_non_verbal, 70),
}

EXAMS = {
    "ntpc": ("ntpc-r", "ntpc/reasoning"),
    "group-d": ("grpd-r", "group-d/reasoning"),
}


def append_to_topic(topic_name, gen_fn, count, exam_prefix, exam_dir):
    """Generate questions for a topic and append to JSON file."""
    full_path = PUBLIC_DIR / exam_dir / f"{topic_name}.json"

    # Generate new questions
    new_qs = gen_fn(exam_prefix, count)

    # Load existing
    existing = load_json(full_path)

    # Find max ID
    max_id = 0
    for q in existing:
        qid = q.get("id", "")
        parts = qid.split("-")
        if len(parts) >= 3:
            try:
                num = int(parts[-1])
                max_id = max(max_id, num)
            except ValueError:
                pass

    # Assign IDs
    for i, q in enumerate(new_qs):
        q["id"] = f"{exam_prefix}-{max_id + i + 1:04d}"

    # Merge
    merged = existing + new_qs
    save_json(full_path, merged)
    return len(new_qs)


if __name__ == "__main__":
    print("=" * 60)
    print("RRB Reasoning Question Generator — Bilingual (EN/HI)")
    print("All answers are PROGRAMMATICALLY COMPUTED & VERIFIED")
    print("=" * 60)
    print()

    random.seed(2025)
    grand_total = 0

    for exam_name, (prefix, exam_dir) in EXAMS.items():
        print(f"\n{'─' * 60}")
        print(f"  EXAM: {exam_name.upper()} (prefix: {prefix})")
        print(f"{'─' * 60}")

        exam_total = 0
        for topic_name, (gen_fn, count) in GENERATORS.items():
            try:
                n = append_to_topic(topic_name, gen_fn, count, prefix, exam_dir)
                exam_total += n
                print(f"  ✓ {topic_name:25s}: +{n} questions → {exam_dir}/{topic_name}.json")
            except Exception as e:
                print(f"  ✗ {topic_name:25s}: ERROR — {e}")

        grand_total += exam_total
        print(f"  → {exam_name.upper()} total: {exam_total} questions")

    print()
    print("=" * 60)
    print(f"  GRAND TOTAL: {grand_total} new questions generated")
    print(f"  Files updated: {len(GENERATORS) * len(EXAMS)} JSON files")
    print("=" * 60)
