#!/usr/bin/env python3
"""Generate bilingual NTPC Math & Reasoning JSON files with complete Hindi translations."""
import json, os, re

BASE = r"C:\Users\core\rrb-exam-prep"
OUT = os.path.join(BASE, "public", "data", "questions", "ntpc")

os.makedirs(os.path.join(OUT, "mathematics"), exist_ok=True)
os.makedirs(os.path.join(OUT, "reasoning"), exist_ok=True)

def parse_ts(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    questions = []
    blocks = re.split(r'\n\s*\{', content)
    for block in blocks:
        if 'questionText:' not in block:
            continue
        block = '{' + block if not block.startswith('{') else block
        depth = 0
        end = -1
        for i, ch in enumerate(block):
            if ch == '{': depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end == -1: continue
        obj_str = block[:end]
        q = {}
        for field, pattern in [
            ('id', r"id:\s*'([^']+)'"),
            ('topicId', r"topicId:\s*'([^']+)'"),
            ('questionText', r"questionText:\s*'((?:[^'\\]|\\.)*)'"),
            ('optionA', r"optionA:\s*'((?:[^'\\]|\\.)*)'"),
            ('optionB', r"optionB:\s*'((?:[^'\\]|\\.)*)'"),
            ('optionC', r"optionC:\s*'((?:[^'\\]|\\.)*)'"),
            ('optionD', r"optionD:\s*'((?:[^'\\]|\\.)*)'"),
            ('correctOption', r"correctOption:\s*'([A-D])'"),
            ('explanation', r"explanation:\s*'((?:[^'\\]|\\.)*)'"),
            ('difficulty', r"difficulty:\s*'([^']+)'"),
        ]:
            m = re.search(pattern, obj_str)
            if m:
                val = m.group(1).replace("\\'", "'")
                q[field] = val
        m = re.search(r"sourceYear:\s*(\d+)", obj_str)
        q['sourceYear'] = int(m.group(1)) if m else 2024
        if q.get('id') and q.get('topicId'):
            questions.append(q)
    return questions

# Parse both files
math_qs = parse_ts(os.path.join(BASE, "src", "data", "questions", "ntpc-math.ts"))
reasoning_qs = parse_ts(os.path.join(BASE, "src", "data", "questions", "ntpc-reasoning.ts"))
print(f"Math: {len(math_qs)}, Reasoning: {len(reasoning_qs)}")

# =====================================================
# TOPIC MAPPING
# =====================================================
TOPIC_MAP = {
    "ntpc-mathematics-number-system": ("mathematics", "number-system", "ntpc-m"),
    "ntpc-mathematics-lcm-hcf": ("mathematics", "lcm-hcf", "ntpc-m"),
    "ntpc-mathematics-simplification": ("mathematics", "simplification", "ntpc-m"),
    "ntpc-mathematics-ratio-proportion": ("mathematics", "ratio-proportion", "ntpc-m"),
    "ntpc-mathematics-percentage": ("mathematics", "percentage", "ntpc-m"),
    "ntpc-mathematics-profit-loss": ("mathematics", "profit-loss", "ntpc-m"),
    "ntpc-mathematics-simple-compound-interest": ("mathematics", "simple-compound-interest", "ntpc-m"),
    "ntpc-mathematics-time-work": ("mathematics", "time-work", "ntpc-m"),
    "ntpc-mathematics-time-speed-distance": ("mathematics", "time-speed-distance", "ntpc-m"),
    "ntpc-mathematics-average": ("mathematics", "average", "ntpc-m"),
    "ntpc-mathematics-mensuration": ("mathematics", "mensuration", "ntpc-m"),
    "ntpc-mathematics-algebra": ("mathematics", "algebra", "ntpc-m"),
    "ntpc-mathematics-geometry": ("mathematics", "geometry", "ntpc-m"),
    "ntpc-mathematics-trigonometry": ("mathematics", "trigonometry", "ntpc-m"),
    "ntpc-mathematics-statistics": ("mathematics", "statistics", "ntpc-m"),
    "ntpc-mathematics-age-problems": ("mathematics", "age-problems", "ntpc-m"),
    "ntpc-mathematics-pipes-cisterns": ("mathematics", "pipes-cisterns", "ntpc-m"),
    "ntpc-mathematics-boats-streams": ("mathematics", "boats-streams", "ntpc-m"),
    "ntpc-mathematics-partnership": ("mathematics", "partnership", "ntpc-m"),
    "ntpc-mathematics-mixture-allegation": ("mathematics", "mixture-allegation", "ntpc-m"),
    "ntpc-reasoning-analogies": ("reasoning", "analogies", "ntpc-r"),
    "ntpc-reasoning-coding-decoding": ("reasoning", "coding-decoding", "ntpc-r"),
    "ntpc-reasoning-series": ("reasoning", "series", "ntpc-r"),
    "ntpc-reasoning-blood-relations": ("reasoning", "blood-relations", "ntpc-r"),
    "ntpc-reasoning-syllogism": ("reasoning", "syllogism", "ntpc-r"),
    "ntpc-reasoning-venn-diagrams": ("reasoning", "venn-diagrams", "ntpc-r"),
    "ntpc-reasoning-direction-sense": ("reasoning", "direction-sense", "ntpc-r"),
    "ntpc-reasoning-ordering-ranking": ("reasoning", "ordering-ranking", "ntpc-r"),
    "ntpc-reasoning-clock-calendar": ("reasoning", "clock-calendar", "ntpc-r"),
    "ntpc-reasoning-puzzles": ("reasoning", "puzzles", "ntpc-r"),
    "ntpc-reasoning-data-sufficiency": ("reasoning", "data-sufficiency", "ntpc-r"),
    "ntpc-reasoning-mathematical-operations": ("reasoning", "mathematical-operations", "ntpc-r"),
    "ntpc-reasoning-statement-conclusion": ("reasoning", "statement-conclusion", "ntpc-r"),
    "ntpc-reasoning-classification": ("reasoning", "classification", "ntpc-r"),
    "ntpc-reasoning-missing-numbers": ("reasoning", "missing-numbers", "ntpc-r"),
    "ntpc-reasoning-non-verbal-reasoning": ("reasoning", "non-verbal", "ntpc-r"),
}

# =====================================================
# HINDI TRANSLATIONS (keyed by original ID)
# =====================================================
HINDI = {}

# -- MATH: Number System (q001-q003, q058-q062) --
HINDI["ntpc-m-q001"] = {
    "q": "प्रथम 50 प्राकृतिक संख्याओं का योग क्या है?",
    "o": ["1225", "1275", "1325", "1250"],
    "e": "प्रथम n प्राकृतिक संख्याओं का योग = n(n+1)/2 = 50 × 51 / 2 = 2550 / 2 = 1275।"
}
HINDI["ntpc-m-q002"] = {
    "q": "यदि 7^12 को 5 से विभाजित किया जाए, तो शेषफल क्या होगा?",
    "o": ["1", "2", "3", "4"],
    "e": "7 mod 5 = 2। इसलिए 7^12 mod 5 = 2^12 mod 5। 2^n mod 5 का चक्र: 2, 4, 3, 1 (आवर्त 4)। 12 mod 4 = 0, इसलिए शेषफल = 1।"
}
HINDI["ntpc-m-q003"] = {
    "q": "200 और 600 (दोनों सम्मिलित) के बीच 4, 5 और 6 से विभाज्य संख्याएँ कितनी हैं?",
    "o": ["5", "6", "7", "8"],
    "e": "4, 5, 6 का ल.स. = 60। 200-600 के बीच 60 के गुणज: 240, 300, 360, 420, 480, 540, 600। कुल 7 संख्याएँ।"
}
HINDI["ntpc-m-q058"] = {
    "q": "7^95 का इकाई अंक ज्ञात कीजिए।",
    "o": ["7", "9", "3", "1"],
    "e": "7^n के इकाई अंक का चक्र: 7, 9, 3, 1 (आवर्त 4)। 95 mod 4 = 3, इसलिए इकाई अंक = 3।"
}
HINDI["ntpc-m-q059"] = {
    "q": "30 और 60 के बीच कितनी अभाज्य संख्याएँ हैं?",
    "o": ["6", "7", "8", "9"],
    "e": "30-60 के बीच अभाज्य संख्याएँ: 31, 37, 41, 43, 47, 53, 59। कुल = 7।"
}
HINDI["ntpc-m-q060"] = {
    "q": "2^50 को 7 से विभाजित करने पर शेषफल ज्ञात कीजिए।",
    "o": ["1", "2", "4", "5"],
    "e": "2^n mod 7 का चक्र: 2, 4, 1 (आवर्त 3)। 50 mod 3 = 2, इसलिए शेषफल = 4।"
}
HINDI["ntpc-m-q061"] = {
    "q": "7 से विभाज्य सभी दो-अंकीय संख्याओं का योग क्या है?",
    "o": ["735", "728", "714", "721"],
    "e": "पहला दो-अंकीय गुणज 14, अंतिम 98। पद = (98-14)/7+1 = 13। योग = n/2×(प्रथम+अंतिम) = 13/2×112 = 728।"
}
HINDI["ntpc-m-q062"] = {
    "q": "यदि किसी संख्या को 56 से विभाजित करने पर शेषफल 29 आता है, तो उसी संख्या को 8 से विभाजित करने पर शेषफल क्या होगा?",
    "o": ["3", "5", "7", "1"],
    "e": "N = 56k+29। 56k/8 = 7k (पूर्णांक)। 29/8 = 3 शेषफल 5। इसलिए शेषफल = 5।"
}

# -- MATH: LCM & HCF (q004-q006, q063-q067) --
HINDI["ntpc-m-q004"] = {
    "q": "दो संख्याओं का ल.स. 1200 है। निम्नलिखित में से कौन-सा उनका म.स. नहीं हो सकता?",
    "o": ["600", "500", "400", "200"],
    "e": "म.स. को ल.स. को पूर्णतः विभाजित करना चाहिए। 1200/500 = 2.4 (पूर्णांक नहीं), जबकि 1200/600=2, 1200/400=3, 1200/200=6 पूर्णांक हैं। इसलिए 500 म.स. नहीं हो सकता।"
}
HINDI["ntpc-m-q005"] = {
    "q": "2/3, 4/5 और 6/7 का म.स. ज्ञात कीजिए।",
    "o": ["2/105", "1/105", "2/35", "1/35"],
    "e": "भिन्नों का म.स. = अंशों का म.स./हरों का ल.स.। म.स.(2,4,6)=2, ल.स.(3,5,7)=105। म.स.=2/105।"
}
HINDI["ntpc-m-q006"] = {
    "q": "तीन घंटियाँ क्रमशः 9, 12 और 15 मिनट के अंतराल पर बजती हैं। यदि वे सुबह 6:00 बजे एक साथ बजें, तो अगली बार एक साथ कब बजेंगी?",
    "o": ["सुबह 8:00", "सुबह 9:00", "सुबह 7:00", "सुबह 10:00"],
    "e": "9,12,15 का ल.स.=180 मिनट=3 घंटे। अगली बार: 6:00+3 घंटे = सुबह 9:00।"
}
HINDI["ntpc-m-q063"] = {
    "q": "दो संख्याओं का गुणनफल 4107 है और उनका म.स. 37 है। ल.स. ज्ञात कीजिए।",
    "o": ["111", "121", "131", "141"],
    "e": "ल.स. = गुणनफल/म.स. = 4107/37 = 111।"
}
HINDI["ntpc-m-q064"] = {
    "q": "तीन घंटियाँ क्रमशः 12, 16 और 24 सेकंड के अंतराल पर बजती हैं। यदि वे सुबह 10:00 बजे एक साथ बजें, तो अगली बार कब बजेंगी?",
    "o": ["सुबह 10:00:48", "सुबह 10:00:56", "सुबह 10:00:36", "सुबह 10:01:00"],
    "e": "12,16,24 का ल.स.=48 सेकंड। अगली बार: सुबह 10:00:48।"
}
HINDI["ntpc-m-q065"] = {
    "q": "0.63, 1.05 और 2.1 का म.स. ज्ञात कीजिए।",
    "o": ["0.21", "0.42", "0.63", "0.07"],
    "e": "100 से गुणा करें: 63,105,210। म.स.(63,105,210)=21। 100 से भाग: 0.21।"
}
HINDI["ntpc-m-q066"] = {
    "q": "दो संख्याओं का म.स. और ल.स. क्रमशः 12 और 924 हैं। यदि एक संख्या 84 है, तो दूसरी ज्ञात कीजिए।",
    "o": ["132", "144", "120", "156"],
    "e": "गुणनफल = म.स.×ल.स. = 12×924 = 11088। दूसरी संख्या = 11088/84 = 132।"
}
HINDI["ntpc-m-q067"] = {
    "q": "वह सबसे बड़ी संख्या ज्ञात कीजिए जो 43, 91 और 183 को विभाजित करने पर समान शेषफल दे।",
    "o": ["4", "8", "12", "16"],
    "e": "अंतर: 91-43=48, 183-91=92, 183-43=140। म.स.(48,92,140)=4।"
}

# -- MATH: Simplification (q007-q009, q068-q072) --
HINDI["ntpc-m-q007"] = {
    "q": "सरल कीजिए: 48/12 × [(4/3 का 9/4)/(2/3 का 3/4)]",
    "o": ["12", "16", "18", "24"],
    "e": "48/12=4। कोष्ठक में: (9/4×4/3)=3, (3/4×2/3)=1/2। 3÷(1/2)=6। अंतिम: 4×6=24।"
}
HINDI["ntpc-m-q008"] = {
    "q": "(0.5×0.5+0.3×0.3+0.2×0.2)/(0.5+0.3+0.2)^2 का मान क्या है?",
    "o": ["1", "0.38", "0.5", "0.25"],
    "e": "अंश=0.25+0.09+0.04=0.38। हर=(1.0)^2=1। मान=0.38।"
}
HINDI["ntpc-m-q009"] = {
    "q": "यदि x+1/x=4, तो x^4+1/x^4 का मान क्या है?",
    "o": ["196", "194", "192", "198"],
    "e": "x²+1/x²=(x+1/x)²-2=16-2=14। x⁴+1/x⁴=(x²+1/x²)²-2=196-2=194।"
}
HINDI["ntpc-m-q068"] = {
    "q": "सरल कीजिए: (0.4³+0.6³)/(0.4²-0.4×0.6+0.6²)",
    "o": ["0.8", "1.0", "1.2", "0.6"],
    "e": "a³+b³=(a+b)(a²-ab+b²) से, व्यंजक = 0.4+0.6 = 1.0।"
}
HINDI["ntpc-m-q069"] = {
    "q": "48/12 × (4/3 का 9/8 ÷ 2/3 का 3/4) का मान क्या है?",
    "o": ["8", "12", "6", "10"],
    "e": "भीतर: 9/8×4/3=3/2, 3/4×2/3=1/2। (3/2)/(1/2)=3। फिर: 48/12×3=4×3=12।"
}
HINDI["ntpc-m-q070"] = {
    "q": "सरल कीजिए: 2/3 + 3/7 - 1/4",
    "o": ["73/84", "75/84", "71/84", "77/84"],
    "e": "ल.स.(3,7,4)=84। 2/3=56/84, 3/7=36/84, 1/4=21/84। 56+36-21=71/84।"
}
HINDI["ntpc-m-q071"] = {
    "q": "0.000144 का वर्गमूल क्या है?",
    "o": ["0.012", "0.12", "0.0012", "0.00012"],
    "e": "√(0.000144)=√(144/1000000)=12/1000=0.012।"
}
HINDI["ntpc-m-q072"] = {
    "q": "(4.5²-2.5²)/(4.5-2.5) का मान ज्ञात कीजिए।",
    "o": ["7", "6", "5", "8"],
    "e": "a²-b²=(a-b)(a+b) से, व्यंजक=(4.5+2.5)=7।"
}

# -- MATH: Ratio & Proportion (q010-q012, q073-q077) --
HINDI["ntpc-m-q010"] = {
    "q": "यदि A:B=2:3, B:C=4:5 और C:D=6:7, तो A:D क्या है?",
    "o": ["16:35", "12:35", "4:13", "5:14"],
    "e": "A:B=8:12, B:C=12:15, C:D=30:35। A:B:C:D=16:24:30:35। A:D=16:35।"
}
HINDI["ntpc-m-q011"] = {
    "q": "एक बैग में ₹1, 50 पैसे और 25 पैसे के सिक्के 5:7:9 के अनुपात में हैं। कुल मूल्य ₹430 है। 25 पैसे के कितने सिक्के हैं?",
    "o": ["315", "360", "350", "400"],
    "e": "सिक्के: 5k,7k,9k। मूल्य=5k+3.5k+2.25k=10.75k=430। k=40। 25p के सिक्के=9×40=360।"
}
HINDI["ntpc-m-q012"] = {
    "q": "A और B की आय का अनुपात 5:4 है और व्यय का अनुपात 3:2 है। यदि प्रत्येक ₹1,600 बचाता है, तो A की आय क्या है?",
    "o": ["₹4,000", "₹5,000", "₹3,200", "₹4,500"],
    "e": "आय: A=5x, B=4x। व्यय: A=3y, B=2y। 5x-3y=1600, 4x-2y=1600। हल: x=800, A=₹4,000।"
}
HINDI["ntpc-m-q073"] = {
    "q": "यदि A:B=3:4 और B:C=6:7, तो A:B:C ज्ञात कीजिए।",
    "o": ["9:12:14", "3:6:7", "6:8:7", "12:16:21"],
    "e": "A:B=3:4=9:12, B:C=6:7=12:14। A:B:C=9:12:14।"
}
HINDI["ntpc-m-q074"] = {
    "q": "₹782 को A, B, C में 1/2:2/3:3/4 के अनुपात में बाँटा जाए, तो A का हिस्सा क्या है?",
    "o": ["₹204", "₹242", "₹228", "₹216"],
    "e": "ल.स.(2,3,4)=12। अनुपात = 6:8:9। कुल भाग=23। A=(6/23)×782=₹204।"
}
HINDI["ntpc-m-q075"] = {
    "q": "A और B की आयु का अनुपात 5:7 है। 6 वर्ष बाद अनुपात 3:4 होगा। A की वर्तमान आयु क्या है?",
    "o": ["30 वर्ष", "25 वर्ष", "35 वर्ष", "20 वर्ष"],
    "e": "आयु: 5x,7x। (5x+6)/(7x+6)=3/4। 20x+24=21x+18, x=6। A=30 वर्ष।"
}
HINDI["ntpc-m-q076"] = {
    "q": "80 लीटर मिश्रण में दूध-पानी का अनुपात 5:3 है। अनुपात 2:3 करने के लिए कितना पानी मिलाना होगा?",
    "o": ["45 लीटर", "40 लीटर", "35 लीटर", "30 लीटर"],
    "e": "दूध=50L, पानी=30L। 50/(30+x)=2/3। 150=60+2x, x=45 लीटर।"
}
HINDI["ntpc-m-q077"] = {
    "q": "8 और 18 का मध्यानुपाती क्या है?",
    "o": ["12", "13", "10", "14"],
    "e": "मध्यानुपाती = √(a×b) = √(8×18) = √144 = 12।"
}

# -- MATH: Percentage (q013-q015, q078-q082) --
HINDI["ntpc-m-q013"] = {
    "q": "चीनी के मूल्य में 25% वृद्धि होने पर, खपत में कितने प्रतिशत कमी करें कि व्यय समान रहे?",
    "o": ["25%", "20%", "15%", "30%"],
    "e": "कमी% = (R/(100+R))×100 = (25/125)×100 = 20%।"
}
HINDI["ntpc-m-q014"] = {
    "q": "एक छात्र 30% अंक प्राप्त कर 15 अंकों से अनुत्तीर्ण होता है। दूसरा 42% प्राप्त कर 12 अंक अधिक लाता है। अधिकतम अंक क्या हैं?",
    "o": ["250", "275", "300", "225"],
    "e": "30%M=P-15, 42%M=P+12। घटाएँ: 12%M=27, M=225।"
}
HINDI["ntpc-m-q015"] = {
    "q": "कस्बे की जनसंख्या प्रति वर्ष 10% बढ़ती है। वर्तमान जनसंख्या 1,21,000 है, तो 2 वर्ष पहले कितनी थी?",
    "o": ["1,00,000", "1,10,000", "90,000", "95,000"],
    "e": "2 वर्ष पहले = 121000/(1.1)² = 121000/1.21 = 1,00,000।"
}
HINDI["ntpc-m-q078"] = {
    "q": "एक संख्या में 20% वृद्धि फिर 20% कमी करने पर कुल प्रतिशत परिवर्तन क्या है?",
    "o": ["4% कमी", "4% वृद्धि", "कोई परिवर्तन नहीं", "10% कमी"],
    "e": "कुल परिवर्तन = a+b+ab/100 = 20-20-400/100 = -4% (4% कमी)।"
}
HINDI["ntpc-m-q079"] = {
    "q": "चीनी के मूल्य में 25% वृद्धि होने पर, खपत कितने प्रतिशत घटाएँ कि व्यय न बदले?",
    "o": ["20%", "25%", "30%", "15%"],
    "e": "कमी% = (25/125)×100 = 20%।"
}
HINDI["ntpc-m-q080"] = {
    "q": "किसी संख्या का 40%, 180 है। उस संख्या का 65% क्या है?",
    "o": ["292.5", "280", "310", "295"],
    "e": "40%x=180, x=450। 65%×450 = 292.5।"
}
HINDI["ntpc-m-q081"] = {
    "q": "चुनाव में विजेता को 56% मत मिले और वह 18,000 मतों से जीता। कुल मत कितने थे?",
    "o": ["1,50,000", "1,40,000", "1,60,000", "1,30,000"],
    "e": "अंतर=12%=18,000। कुल=18,000×100/12=1,50,000।"
}
HINDI["ntpc-m-q082"] = {
    "q": "एक छात्र 35% लाकर 20 अंकों से फेल होता है। दूसरा 45% लाकर 10 अंकों से पास होता है। पासिंग अंक क्या हैं?",
    "o": ["125", "130", "140", "135"],
    "e": "10%=30, कुल अंक=300। पासिंग=35%×300+20=105+20=125।"
}

# -- MATH: Profit & Loss (q016-q018, q083-q087) --
HINDI["ntpc-m-q016"] = {
    "q": "एक दुकानदार 12.5% हानि पर वस्तु बेचता है। यदि ₹51.80 अधिक में बेचता तो 6% लाभ होता। क्रय मूल्य क्या है?",
    "o": ["₹280", "₹250", "₹300", "₹320"],
    "e": "अंतर=18.5%CP=₹51.80। CP=51.80/0.185=₹280।"
}
HINDI["ntpc-m-q017"] = {
    "q": "एक व्यक्ति ने 20 दर्जन अंडे ₹30/दर्जन से खरीदे। 20 अंडे टूट गए। शेष ₹3.50/अंडा बेचे। लाभ%?",
    "o": ["28.33%", "22.5%", "16.67%", "35%"],
    "e": "CP=₹600। कुल=240 अंडे, शेष=220। SP=220×3.50=₹770। लाभ=170/600×100=28.33%।"
}
HINDI["ntpc-m-q018"] = {
    "q": "एक बेईमान दुकानदार 1kg के स्थान पर 900g तोलता है और क्रय मूल्य पर बेचता है। लाभ%?",
    "o": ["10%", "11.11%", "12.5%", "9.09%"],
    "e": "लाभ=100g प्रति 900g। लाभ%=(100/900)×100=11.11%।"
}
HINDI["ntpc-m-q083"] = {
    "q": "एक दुकानदार 12.5% हानि पर बेचता है। यदि ₹56 अधिक में बेचता तो 12.5% लाभ होता। क्रय मूल्य क्या है?",
    "o": ["₹224", "₹240", "₹250", "₹200"],
    "e": "अंतर=25%CP=₹56। CP=56×100/25=₹224।"
}
HINDI["ntpc-m-q084"] = {
    "q": "33 मीटर कपड़ा बेचने पर 11 मीटर के विक्रय मूल्य के बराबर लाभ होता है। लाभ%?",
    "o": ["50%", "40%", "33.33%", "25%"],
    "e": "CP(33m)=SP(22m)। CP:SP=22:33=2:3। लाभ%=(1/2)×100=50%।"
}
HINDI["ntpc-m-q085"] = {
    "q": "एक व्यापारी क्रय मूल्य से 30% अधिक अंकित करता है और 15% छूट देता है। लाभ% क्या है?",
    "o": ["10.5%", "15%", "12.5%", "8%"],
    "e": "CP=₹100, MP=₹130, SP=130×0.85=₹110.5। लाभ%=10.5%।"
}
HINDI["ntpc-m-q086"] = {
    "q": "एक व्यक्ति दो वस्तुएँ समान मूल्य पर बेचता है। एक पर 25% लाभ, दूसरी पर 25% हानि। कुल लाभ/हानि%?",
    "o": ["6.25% हानि", "6.25% लाभ", "न लाभ न हानि", "12.5% हानि"],
    "e": "कुल हानि% = (x/10)² = (25/10)² = 6.25% हानि।"
}
HINDI["ntpc-m-q087"] = {
    "q": "20 वस्तुओं का क्रय मूल्य 15 वस्तुओं के विक्रय मूल्य के बराबर है। लाभ%?",
    "o": ["33.33%", "25%", "30%", "20%"],
    "e": "CP:SP=15:20=3:4। लाभ%=(1/3)×100=33.33%।"
}

print(f"Translations loaded: {len(HINDI)} entries")
print("Ready to generate files...")
# Will continue in next script section
