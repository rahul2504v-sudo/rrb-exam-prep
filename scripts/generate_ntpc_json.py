#!/usr/bin/env python3
"""Generate bilingual JSON question files for NTPC Math and Reasoning from TS source files."""
import json, os, re

BASE = r"C:\Users\core\rrb-exam-prep"
OUT_DIR = os.path.join(BASE, "public", "data", "questions", "ntpc")

# Create output directories
os.makedirs(os.path.join(OUT_DIR, "mathematics"), exist_ok=True)
os.makedirs(os.path.join(OUT_DIR, "reasoning"), exist_ok=True)

# Topic mapping: topicId -> (category, filename)
TOPIC_MAP = {
    # Mathematics (20 topics - includes mixture-allegation)
    "ntpc-mathematics-number-system": ("mathematics", "number-system"),
    "ntpc-mathematics-lcm-hcf": ("mathematics", "lcm-hcf"),
    "ntpc-mathematics-simplification": ("mathematics", "simplification"),
    "ntpc-mathematics-ratio-proportion": ("mathematics", "ratio-proportion"),
    "ntpc-mathematics-percentage": ("mathematics", "percentage"),
    "ntpc-mathematics-profit-loss": ("mathematics", "profit-loss"),
    "ntpc-mathematics-simple-compound-interest": ("mathematics", "simple-compound-interest"),
    "ntpc-mathematics-time-work": ("mathematics", "time-work"),
    "ntpc-mathematics-time-speed-distance": ("mathematics", "time-speed-distance"),
    "ntpc-mathematics-average": ("mathematics", "average"),
    "ntpc-mathematics-mensuration": ("mathematics", "mensuration"),
    "ntpc-mathematics-algebra": ("mathematics", "algebra"),
    "ntpc-mathematics-geometry": ("mathematics", "geometry"),
    "ntpc-mathematics-trigonometry": ("mathematics", "trigonometry"),
    "ntpc-mathematics-statistics": ("mathematics", "statistics"),
    "ntpc-mathematics-age-problems": ("mathematics", "age-problems"),
    "ntpc-mathematics-pipes-cisterns": ("mathematics", "pipes-cisterns"),
    "ntpc-mathematics-boats-streams": ("mathematics", "boats-streams"),
    "ntpc-mathematics-partnership": ("mathematics", "partnership"),
    "ntpc-mathematics-mixture-allegation": ("mathematics", "mixture-allegation"),
    # Reasoning (16 topics)
    "ntpc-reasoning-analogies": ("reasoning", "analogies"),
    "ntpc-reasoning-coding-decoding": ("reasoning", "coding-decoding"),
    "ntpc-reasoning-series": ("reasoning", "series"),
    "ntpc-reasoning-blood-relations": ("reasoning", "blood-relations"),
    "ntpc-reasoning-syllogism": ("reasoning", "syllogism"),
    "ntpc-reasoning-venn-diagrams": ("reasoning", "venn-diagrams"),
    "ntpc-reasoning-direction-sense": ("reasoning", "direction-sense"),
    "ntpc-reasoning-ordering-ranking": ("reasoning", "ordering-ranking"),
    "ntpc-reasoning-clock-calendar": ("reasoning", "clock-calendar"),
    "ntpc-reasoning-puzzles": ("reasoning", "puzzles"),
    "ntpc-reasoning-data-sufficiency": ("reasoning", "data-sufficiency"),
    "ntpc-reasoning-mathematical-operations": ("reasoning", "mathematical-operations"),
    "ntpc-reasoning-statement-conclusion": ("reasoning", "statement-conclusion"),
    "ntpc-reasoning-classification": ("reasoning", "classification"),
    "ntpc-reasoning-missing-numbers": ("reasoning", "missing-numbers"),
    "ntpc-reasoning-non-verbal-reasoning": ("reasoning", "non-verbal"),
}

###############################################################################
# HINDI TRANSLATION DICTIONARIES
###############################################################################

# Math translations
MATH_HINDI = {
    # NUMBER SYSTEM (q001-q003, q058-q062) = 8 questions
    "ntpc-m-q001": {
        "question": "प्रथम 50 प्राकृतिक संख्याओं का योग क्या है?",
        "options": ["1225", "1275", "1325", "1250"],
        "explanation": "प्रथम n प्राकृतिक संख्याओं का योग = n(n+1)/2 = 50 × 51 / 2 = 2550 / 2 = 1275।"
    },
    "ntpc-m-q002": {
        "question": "यदि 7^12 को 5 से विभाजित किया जाए, तो शेषफल क्या होगा?",
        "options": ["1", "2", "3", "4"],
        "explanation": "7 mod 5 = 2। इसलिए 7^12 mod 5 = 2^12 mod 5। 2^n mod 5 का चक्र: 2, 4, 3, 1 (हर 4 पर दोहराता है)। 12 mod 4 = 0, इसलिए शेषफल चक्र का चौथा मान = 1।"
    },
    "ntpc-m-q003": {
        "question": "200 और 600 (दोनों सम्मिलित) के बीच कितनी संख्याएँ 4, 5 और 6 से विभाज्य हैं?",
        "options": ["5", "6", "7", "8"],
        "explanation": "4, 5, 6 का ल.स. = 60। 200 और 600 के बीच 60 के गुणज: 240, 300, 360, 420, 480, 540, 600। कुल 7 संख्याएँ।"
    },
    "ntpc-m-q058": {
        "question": "7^95 का इकाई अंक ज्ञात कीजिए।",
        "options": ["7", "9", "3", "1"],
        "explanation": "7^n के इकाई अंक का चक्र: 7, 9, 3, 1 (अवधि 4)। 95 mod 4 = 3, इसलिए इकाई अंक चक्र का तीसरा = 3।"
    },
    "ntpc-m-q059": {
        "question": "30 और 60 के बीच कितनी अभाज्य संख्याएँ हैं?",
        "options": ["6", "7", "8", "9"],
        "explanation": "30 और 60 के बीच अभाज्य संख्याएँ: 31, 37, 41, 43, 47, 53, 59। कुल = 7।"
    },
    "ntpc-m-q060": {
        "question": "2^50 को 7 से विभाजित करने पर शेषफल ज्ञात कीजिए।",
        "options": ["1", "2", "4", "5"],
        "explanation": "2^n mod 7 का चक्र: 2, 4, 1 (अवधि 3)। 50 mod 3 = 2, इसलिए शेषफल = 4।"
    },
    "ntpc-m-q061": {
        "question": "7 से विभाज्य सभी दो-अंकीय संख्याओं का योग क्या है?",
        "options": ["735", "728", "714", "721"],
        "explanation": "7 का पहला दो-अंकीय गुणज 14 है, अंतिम 98 है। पदों की संख्या = (98-14)/7 + 1 = 13। योग = n/2 × (प्रथम + अंतिम) = 13/2 × 112 = 13 × 56 = 728।"
    },
    "ntpc-m-q062": {
        "question": "यदि किसी संख्या को 56 से विभाजित करने पर शेषफल 29 आता है, तो उसी संख्या को 8 से विभाजित करने पर शेषफल क्या होगा?",
        "options": ["3", "5", "7", "1"],
        "explanation": "मान लीजिए N = 56k + 29। 8 से विभाजित करने पर: 56k/8 = 7k (पूर्णांक)। 29/8 = 3 शेषफल 5। इसलिए शेषफल 5 है।"
    },

    # LCM & HCF (q004-q006, q063-q067) = 8 questions
    "ntpc-m-q004": {
        "question": "दो संख्याओं का ल.स. 1200 है। निम्नलिखित में से कौन-सा उनका म.स. नहीं हो सकता?",
        "options": ["600", "500", "400", "200"],
        "explanation": "म.स. को ल.स. को पूर्णतः विभाजित करना चाहिए। 1200/500 = 2.4 (पूर्णांक नहीं), जबकि 1200/600=2, 1200/400=3, 1200/200=6 सभी पूर्णांक हैं। इसलिए 500 म.स. नहीं हो सकता।"
    },
    "ntpc-m-q005": {
        "question": "2/3, 4/5 और 6/7 का म.स. ज्ञात कीजिए।",
        "options": ["2/105", "1/105", "2/35", "1/35"],
        "explanation": "भिन्नों का म.स. = अंशों का म.स. / हरों का ल.स.। म.स.(2,4,6) = 2। ल.स.(3,5,7) = 105। इसलिए म.स. = 2/105।"
    },
    "ntpc-m-q006": {
        "question": "तीन घंटियाँ क्रमशः 9, 12 और 15 मिनट के अंतराल पर बजती हैं। यदि वे सभी सुबह 6:00 बजे एक साथ बजती हैं, तो वे अगली बार एक साथ कब बजेंगी?",
        "options": ["सुबह 8:00", "सुबह 9:00", "सुबह 7:00", "सुबह 10:00"],
        "explanation": "9, 12, 15 का ल.स. = 180 मिनट = 3 घंटे। वे पुनः सुबह 6:00 + 3 घंटे = सुबह 9:00 बजे एक साथ बजेंगी।"
    },
    "ntpc-m-q063": {
        "question": "दो संख्याओं का गुणनफल 4107 है और उनका म.स. 37 है। ल.स. ज्ञात कीजिए।",
        "options": ["111", "121", "131", "141"],
        "explanation": "ल.स. = गुणनफल / म.स. = 4107 / 37 = 111।"
    },
    "ntpc-m-q064": {
        "question": "तीन घंटियाँ क्रमशः 12, 16 और 24 सेकंड के अंतराल पर बजती हैं। यदि वे सभी सुबह 10:00 बजे एक साथ बजती हैं, तो वे अगली बार एक साथ कब बजेंगी?",
        "options": ["सुबह 10:00:48", "सुबह 10:00:56", "सुबह 10:00:36", "सुबह 10:01:00"],
        "explanation": "12, 16, 24 का ल.स. = 48। वे हर 48 सेकंड पर एक साथ बजती हैं। अगली बार: सुबह 10:00:48।"
    },
    "ntpc-m-q065": {
        "question": "0.63, 1.05 और 2.1 का म.स. ज्ञात कीजिए।",
        "options": ["0.21", "0.42", "0.63", "0.07"],
        "explanation": "100 से गुणा करें: 63, 105, 210। म.स.(63, 105, 210) = 21। 100 से भाग दें: 0.21।"
    },
    "ntpc-m-q066": {
        "question": "दो संख्याओं का म.स. और ल.स. क्रमशः 12 और 924 हैं। यदि एक संख्या 84 है, तो दूसरी संख्या ज्ञात कीजिए।",
        "options": ["132", "144", "120", "156"],
        "explanation": "गुणनफल = म.स. × ल.स. = 12 × 924 = 11088। दूसरी संख्या = 11088 / 84 = 132।"
    },
    "ntpc-m-q067": {
        "question": "वह सबसे बड़ी संख्या ज्ञात कीजिए जो 43, 91 और 183 को विभाजित करने पर प्रत्येक स्थिति में समान शेषफल दे।",
        "options": ["4", "8", "12", "16"],
        "explanation": "अंतर: 91-43=48, 183-91=92, 183-43=140। 48, 92, 140 का म.स. = 4।"
    },

    # SIMPLIFICATION (q007-q009, q068-q072) = 8 questions
    "ntpc-m-q007": {
        "question": "सरल कीजिए: 48 / 12 × [(9/4 का 4/3) / (3/4 का 2/3)]",
        "options": ["12", "16", "18", "24"],
        "explanation": "48/12 = 4। कोष्ठक के अंदर: (9/4 × 4/3) = 3। (3/4 × 2/3) = 1/2। तो 3 / (1/2) = 3 × 2 = 6। अंतिम: 4 × 6 = 24।"
    },
    "ntpc-m-q008": {
        "question": "(0.5 × 0.5 + 0.3 × 0.3 + 0.2 × 0.2) / (0.5 + 0.3 + 0.2)^2 का मान क्या है?",
        "options": ["1", "0.38", "0.5", "0.25"],
        "explanation": "अंश = 0.25 + 0.09 + 0.04 = 0.38। हर = (1.0)^2 = 1। इसलिए मान = 0.38।"
    },
    "ntpc-m-q009": {
        "question": "यदि x + 1/x = 4, तो x^4 + 1/x^4 का मान क्या है?",
        "options": ["196", "194", "192", "198"],
        "explanation": "x^2 + 1/x^2 = (x + 1/x)^2 - 2 = 16 - 2 = 14। x^4 + 1/x^4 = (x^2 + 1/x^2)^2 - 2 = 14^2 - 2 = 196 - 2 = 194।"
    },
    "ntpc-m-q068": {
        "question": "सरल कीजिए: 0.4 × 0.4 × 0.4 + 0.6 × 0.6 × 0.6 / (0.4 × 0.4 - 0.4 × 0.6 + 0.6 × 0.6)",
        "options": ["0.8", "1.0", "1.2", "0.6"],
        "explanation": "a^3 + b^3 = (a+b)(a^2-ab+b^2) का प्रयोग करें, जहाँ a=0.4, b=0.6। व्यंजक = (0.4+0.6) × (a^2-ab+b^2) / (a^2-ab+b^2) = 0.4+0.6 = 1.0।"
    },
    "ntpc-m-q069": {
        "question": "48 / 12 × (4/3 का 9/8 / 2/3 का 3/4) का मान क्या है?",
        "options": ["8", "12", "6", "10"],
        "explanation": "पहले आंतरिक हल करें: 4/3 का 9/8 = 9/8 × 4/3 = 3/2। 2/3 का 3/4 = 3/4 × 2/3 = 1/2। (3/2)/(1/2) = 3। फिर: 48/12 × 3 = 4 × 3 = 12।"
    },
    "ntpc-m-q070": {
        "question": "सरल कीजिए: 2/3 + 3/7 - 1/4।",
        "options": ["73/84", "75/84", "71/84", "77/84"],
        "explanation": "3, 7, 4 का ल.स. = 84। 2/3 = 56/84, 3/7 = 36/84, 1/4 = 21/84। परिणाम = 56 + 36 - 21 = 71/84।"
    },
    "ntpc-m-q071": {
        "question": "0.000144 का वर्गमूल क्या है?",
        "options": ["0.012", "0.12", "0.0012", "0.00012"],
        "explanation": "sqrt(0.000144) = sqrt(144/1000000) = 12/1000 = 0.012।"
    },
    "ntpc-m-q072": {
        "question": "मान ज्ञात कीजिए: (4.5)^2 - (2.5)^2 / (4.5 - 2.5)",
        "options": ["7", "6", "5", "8"],
        "explanation": "a^2 - b^2 = (a-b)(a+b) का प्रयोग करें। व्यंजक = (4.5-2.5)(4.5+2.5)/(4.5-2.5) = 4.5+2.5 = 7।"
    },
}

print("Script structure ready. Will generate JSON files.")
print("This is a placeholder - the full generation script is too large for one write_file call.")
print("I need to build the JSON files incrementally.")
