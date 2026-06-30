#!/usr/bin/env python3
"""Generate all Group D GA and Group D Science bilingual JSON files.
Place in C:/Users/core/rrb-exam-prep and run: python gen_remaining.py
"""
import json, os, re

HERE = r"C:\Users\core\rrb-exam-prep"

def parse_ts(path):
    with open(path, encoding='utf-8') as f:
        c = f.read()
    qs = []
    for blk in re.split(r'\n\s*\{', c):
        if 'questionText:' not in blk: continue
        blk = '{' + blk
        d = 0; e = -1
        for i, ch in enumerate(blk):
            if ch == '{': d += 1
            elif ch == '}': d -= 1
            if d == 0: e = i+1; break
        if e == -1: continue
        s = blk[:e]
        q = {}
        for f in ['id','examId','subjectId','topicId','questionText','optionA','optionB','optionC','optionD','correctOption','explanation','difficulty']:
            m = re.search(rf"{f}:\s*'((?:[^'\\]|\\.)*)'", s)
            if m: q[f] = m.group(1).replace("\\'", "'")
        m = re.search(r"sourceYear:\s*(\d+)", s)
        if m: q['sourceYear'] = int(m.group(1))
        if q.get('id') and q.get('topicId'): qs.append(q)
    return qs

gdga = parse_ts(os.path.join(HERE, r"src\data\questions\groupd-ga.ts"))
gdsc = parse_ts(os.path.join(HERE, r"src\data\questions\groupd-science.ts"))

# Large Hindi translation dictionary
T = {
    # Group D GA - Indian Polity
    "Who is the head of the state in India?": "भारत में राज्य का प्रमुख कौन होता है?",
    "The President of India is the head of the state. The Prime Minister is the head of the government.": "भारत का राष्ट्रपति राज्य का प्रमुख है। प्रधानमंत्री सरकार का प्रमुख है।",
    "How many members are there in the Lok Sabha?": "लोकसभा में कितने सदस्य होते हैं?",
    "The Lok Sabha has a maximum strength of 545 members.": "लोकसभा की अधिकतम सदस्य संख्या 545 है।",
    "Which article of the Indian Constitution deals with the Right to Equality?": "भारतीय संविधान का कौन सा अनुच्छेद समानता के अधिकार से संबंधित है?",
    "Article 14 of the Indian Constitution guarantees the Right to Equality.": "भारतीय संविधान का अनुच्छेद 14 समानता के अधिकार की गारंटी देता है।",
    "On which date was the Constitution of India adopted?": "भारत का संविधान किस तारीख को अपनाया गया था?",
    "The Constitution was adopted on November 26, 1949 and came into effect on January 26, 1950.": "संविधान 26 नवंबर 1949 को अपनाया गया और 26 जनवरी 1950 को लागू हुआ।",
    "How many Schedules are there in the Indian Constitution?": "भारतीय संविधान में कितनी अनुसूचियां हैं?",
    "The Indian Constitution originally had 8 Schedules and now has 12 Schedules.": "भारतीय संविधान में मूलतः 8 और अब 12 अनुसूचियां हैं।",
    "Which article deals with the Right to Education?": "शिक्षा के अधिकार से कौन सा अनुच्छेद संबंधित है?",
    "Article 21A provides free and compulsory education to children aged 6 to 14 years.": "अनुच्छेद 21A 6 से 14 वर्ष के बच्चों को मुफ्त और अनिवार्य शिक्षा प्रदान करता है।",
    "What is the term of a Rajya Sabha member?": "राज्यसभा सदस्य का कार्यकाल कितना होता है?",
    "A Rajya Sabha member serves for 6 years.": "राज्यसभा सदस्य 6 वर्ष का कार्यकाल पूरा करता है।",
    "Who appoints the Governor of a state in India?": "भारत में राज्य का राज्यपाल कौन नियुक्त करता है?",
    "The Governor is appointed by the President of India.": "राज्यपाल की नियुक्ति भारत के राष्ट्रपति द्वारा की जाती है।",
    "The Constitution borrowed the Parliamentary system from which country?": "संविधान ने संसदीय प्रणाली किस देश से ली?",
    "India adopted the Parliamentary system from Britain.": "भारत ने ब्रिटेन से संसदीय प्रणाली अपनाई।",
    "Fundamental Duties were added by which Amendment?": "मौलिक कर्तव्य किस संशोधन द्वारा जोड़े गए?",
    "The 42nd Amendment Act of 1976 added Fundamental Duties based on Swaran Singh Committee recommendations.": "42वें संशोधन अधिनियम 1976 ने स्वर्ण सिंह समिति की सिफारिशों पर मौलिक कर्तव्य जोड़े।",
    "Who is known as the Father of Local Self Government in India?": "भारत में स्थानीय स्वशासन के जनक कौन माने जाते हैं?",
    "Lord Ripon is known as the Father of Local Self Government in India.": "लॉर्ड रिपन को भारत में स्थानीय स्वशासन का जनक माना जाता है।",
    
    # Group D GA - Economics
    "What is the currency of India?": "भारत की मुद्रा क्या है?",
    "The Indian Rupee (INR) is the official currency of India, regulated by RBI.": "भारतीय रुपया (INR) भारत की आधिकारिक मुद्रा है, जो RBI द्वारा नियंत्रित है।",
    "Who is the current Governor of the Reserve Bank of India (as of 2025)?": "भारतीय रिज़र्व बैंक के वर्तमान गवर्नर (2025 तक) कौन हैं?",
    "Sanjay Malhotra assumed charge as the 26th Governor of RBI in December 2024.": "संजय मल्होत्रा ने दिसंबर 2024 में RBI के 26वें गवर्नर का कार्यभार संभाला।",
    "GST stands for:": "GST का पूरा नाम क्या है?",
    "GST stands for Goods and Services Tax, implemented from July 1, 2017.": "GST का अर्थ वस्तु एवं सेवा कर है, जो 1 जुलाई 2017 से लागू हुआ।",
    "Where is the headquarters of the RBI?": "RBI का मुख्यालय कहां है?",
    "The RBI headquarters is in Mumbai, Maharashtra.": "RBI का मुख्यालय मुंबई, महाराष्ट्र में है।",
    "What is the currency symbol of the Indian Rupee?": "भारतीय रुपये का मुद्रा चिह्न क्या है?",
    "The Indian Rupee symbol was adopted on July 15, 2010, designed by Udaya Kumar.": "भारतीय रुपया चिह्न 15 जुलाई 2010 को अपनाया गया, उदय कुमार द्वारा डिज़ाइन किया गया।",
    "Income Tax in India is levied under which list?": "भारत में आयकर किस सूची के तहत लगाया जाता है?",
    "Income tax falls under the Union List (List I) of the Seventh Schedule.": "आयकर सातवीं अनुसूची की संघ सूची (सूची I) के अंतर्गत आता है।",
    "Which institution was replaced by NITI Aayog in 2015?": "2015 में NITI आयोग ने किस संस्था का स्थान लिया?",
    "NITI Aayog replaced the Planning Commission on January 1, 2015.": "NITI आयोग ने 1 जनवरी 2015 को योजना आयोग का स्थान लिया।",
    "Who presents the Union Budget in Parliament?": "संसद में केंद्रीय बजट कौन प्रस्तुत करता है?",
    "The Union Budget is presented by the Finance Minister in the Lok Sabha.": "केंद्रीय बजट वित्त मंत्री द्वारा लोकसभा में प्रस्तुत किया जाता है।",
    "What is the full form of UPI?": "UPI का पूरा नाम क्या है?",
    "UPI stands for Unified Payments Interface, developed by NPCI and launched in 2016.": "UPI का अर्थ यूनिफाइड पेमेंट्स इंटरफेस है, NPCI द्वारा विकसित और 2016 में लॉन्च किया गया।",
    "Which is the highest denomination coin currently minted in India?": "भारत में वर्तमान में ढाला जाने वाला सबसे बड़ा सिक्का कौन सा है?",
    "The highest denomination coin currently minted is Rs 20.": "वर्तमान में ढाला जाने वाला सबसे बड़ा सिक्का 20 रुपये का है।",
    "What does GDP stand for?": "GDP का पूरा नाम क्या है?",
    "GDP stands for Gross Domestic Product, the total monetary value of goods/services produced within a country.": "GDP का अर्थ सकल घरेलू उत्पाद है, जो किसी देश में उत्पादित वस्तुओं/सेवाओं का कुल मौद्रिक मूल्य है।",
}

# For unmapped texts, keep English
def hi(text):
    return T.get(text, text)

def make_file(qs, tid, prefix, out_dir):
    tqs = sorted([q for q in qs if q['topicId'] == tid], key=lambda x: x['id'])
    if not tqs: return 0
    os.makedirs(out_dir, exist_ok=True)
    out = []
    for i, q in enumerate(tqs, 1):
        eid = f"{prefix}-{i:04d}"
        opts = [q['optionA'], q['optionB'], q['optionC'], q['optionD']]
        out.append({
            "id": eid, "correctOption": q['correctOption'],
            "difficulty": q['difficulty'], "sourceYear": q['sourceYear'],
            "en": {"question": q['questionText'], "options": opts, "explanation": q['explanation']},
            "hi": {"question": hi(q['questionText']), "options": [hi(o) for o in opts], "explanation": hi(q['explanation'])}
        })
    fn = tid.split('-group-d-gk-',1)[-1] if 'group-d-gk-' in tid else tid
    fp = os.path.join(out_dir, f"{fn}.json")
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return len(out)

# Group D GA topics
ga_dir = os.path.join(HERE, r"public\data\questions\group-d\general-awareness")
ga_topics = [
    ('group-d-gk-indian-polity', 'groupd-ga', ga_dir),
    ('group-d-gk-economics', 'groupd-ga', ga_dir),
    ('group-d-gk-current-affairs', 'groupd-ga', ga_dir),
    ('group-d-gk-sports', 'groupd-ga', ga_dir),
    ('group-d-gk-art-culture', 'groupd-ga', ga_dir),
    ('group-d-gk-government-schemes', 'groupd-ga', ga_dir),
    ('group-d-gk-important-days', 'groupd-ga', ga_dir),
    ('group-d-gk-general-knowledge', 'groupd-ga', ga_dir),
]

# Group D Science topics
sc_dir = os.path.join(HERE, r"public\data\questions\group-d\general-science")
sci_topics = [
    ('group-d-science-physics-motion', 'groupd-s', sc_dir),
    ('group-d-science-physics-force-laws', 'groupd-s', sc_dir),
    ('group-d-science-physics-work-energy-power', 'groupd-s', sc_dir),
    ('group-d-science-physics-gravitation', 'groupd-s', sc_dir),
    ('group-d-science-physics-sound', 'groupd-s', sc_dir),
    ('group-d-science-physics-light', 'groupd-s', sc_dir),
    ('group-d-science-physics-electricity', 'groupd-s', sc_dir),
    ('group-d-science-physics-magnetism', 'groupd-s', sc_dir),
    ('group-d-science-physics-heat-thermodynamics', 'groupd-s', sc_dir),
    ('group-d-science-chemistry-matter', 'groupd-s', sc_dir),
    ('group-d-science-chemistry-atoms-molecules', 'groupd-s', sc_dir),
    ('group-d-science-chemistry-acids-bases-salts', 'groupd-s', sc_dir),
    ('group-d-science-chemistry-metals-nonmetals', 'groupd-s', sc_dir),
    ('group-d-science-chemistry-carbon-compounds', 'groupd-s', sc_dir),
    ('group-d-science-chemistry-periodic-table', 'groupd-s', sc_dir),
    ('group-d-science-chemistry-chemical-reactions', 'groupd-s', sc_dir),
    ('group-d-science-biology-cell-structure', 'groupd-s', sc_dir),
    ('group-d-science-biology-tissues', 'groupd-s', sc_dir),
    ('group-d-science-biology-nutrition', 'groupd-s', sc_dir),
    ('group-d-science-biology-respiration', 'groupd-s', sc_dir),
    ('group-d-science-biology-transportation', 'groupd-s', sc_dir),
    ('group-d-science-biology-excretion', 'groupd-s', sc_dir),
    ('group-d-science-biology-reproduction', 'groupd-s', sc_dir),
    ('group-d-science-biology-genetics', 'groupd-s', sc_dir),
    ('group-d-science-biology-diseases', 'groupd-s', sc_dir),
    ('group-d-science-biology-ecology', 'groupd-s', sc_dir),
]

tf = 0; tq = 0
for tid, pfx, od in ga_topics:
    n = make_file(gdga, tid, pfx, od)
    if n:
        print(f"GroupD GA | {tid}: {n} q")
        tf += 1; tq += n

for tid, pfx, od in sci_topics:
    n = make_file(gdsc, tid, pfx, od)
    if n:
        print(f"GroupD Sci | {tid}: {n} q")
        tf += 1; tq += n

print(f"\nGenerated {tf} files, {tq} questions total")
print("Done! Run this script to create all remaining files.")
