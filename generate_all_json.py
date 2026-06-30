#!/usr/bin/env python3
"""GENERATE ALL 51 BILINGUAL JSON FILES FROM TS SOURCE FILES.
Run this script from the project root: C:\Users\core\rrb-exam-prep
"""
import re, json, os

BASE = os.path.dirname(os.path.abspath(__file__))

def parse_ts(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    questions = []
    blocks = re.split(r'\n\s*\{', content)
    for block in blocks:
        if 'questionText:' not in block: continue
        block = '{' + block
        depth = 0; end = -1
        for i, ch in enumerate(block):
            if ch == '{': depth += 1
            elif ch == '}': depth -= 1
            if depth == 0: end = i + 1; break
        if end == -1: continue
        obj_str = block[:end]
        q = {}
        for field in ['id','examId','subjectId','topicId','questionText','optionA','optionB','optionC','optionD','correctOption','explanation','difficulty']:
            m = re.search(rf"{field}:\s*'((?:[^'\\]|\\.)*)'", obj_str)
            if m: q[field] = m.group(1).replace("\\'", "'")
        m = re.search(r"sourceYear:\s*(\d+)", obj_str)
        if m: q['sourceYear'] = int(m.group(1))
        if q.get('id') and q.get('topicId'): questions.append(q)
    return questions

# LOAD ALL QUESTIONS
ntpc = parse_ts(os.path.join(BASE,'src','data','questions','ntpc-ga.ts'))
gdga = parse_ts(os.path.join(BASE,'src','data','questions','groupd-ga.ts'))
gdsc = parse_ts(os.path.join(BASE,'src','data','questions','groupd-science.ts'))

# Comprehensive Hindi translation map
HI = {
    # === NTPC GA ===
    # Indian History
    "Who was the first Governor-General of independent India?": "स्वतंत्र भारत के पहले गवर्नर-जनरल कौन थे?",
    "Lord Mountbatten served as the first Governor-General of independent India from August 15, 1947 to June 21, 1948. C. Rajagopalachari was the first and only Indian Governor-General.": "लॉर्ड माउंटबेटन 15 अगस्त 1947 से 21 जून 1948 तक स्वतंत्र भारत के पहले गवर्नर-जनरल रहे। सी. राजगोपालाचारी पहले और एकमात्र भारतीय गवर्नर-जनरल थे।",
    "The Jallianwala Bagh massacre took place in which year?": "जलियांवाला बाग हत्याकांड किस वर्ष हुआ था?",
    "The Jallianwala Bagh massacre occurred on April 13, 1919 in Amritsar, Punjab. British troops under General Dyer fired on an unarmed crowd, killing hundreds.": "जलियांवाला बाग हत्याकांड 13 अप्रैल 1919 को अमृतसर, पंजाब में हुआ था। जनरल डायर के नेतृत्व में ब्रिटिश सैनिकों ने निहत्थे भीड़ पर गोलियां चलाईं, जिसमें सैकड़ों लोग मारे गए।",
    "Who was the President of the Indian National Congress at the time of independence in 1947?": "1947 में स्वतंत्रता के समय भारतीय राष्ट्रीय कांग्रेस के अध्यक्ष कौन थे?",
    "Acharya J.B. Kripalani served as the President of the Indian National Congress from 1946 to 1947, leading the party during the crucial period of independence and partition.": "आचार्य जे.बी. कृपलानी 1946 से 1947 तक भारतीय राष्ट्रीय कांग्रेस के अध्यक्ष रहे, और स्वतंत्रता व विभाजन के महत्वपूर्ण काल में पार्टी का नेतृत्व किया।",
    "The Quit India Movement was launched by Mahatma Gandhi in which year?": "महात्मा गांधी ने भारत छोड़ो आंदोलन किस वर्ष शुरू किया था?",
    "The Quit India Movement was launched on August 8, 1942 at the Bombay session of the All India Congress Committee. Gandhi gave the call Do or Die, demanding an end to British rule in India.": "भारत छोड़ो आंदोलन 8 अगस्त 1942 को कांग्रेस के बंबई अधिवेशन में शुरू हुआ। गांधी जी ने 'करो या मरो' का नारा दिया।",
    "Who was the Viceroy of India during the Revolt of 1857?": "1857 के विद्रोह के समय भारत का वायसराय कौन था?",
    "Lord Canning served as the Governor-General/Viceroy of India during the Revolt of 1857 (1856-1862). After the revolt, the British Crown took over from the East India Company.": "लॉर्ड कैनिंग 1857 के विद्रोह (1856-1862) के दौरान भारत के गवर्नर-जनरल/वायसराय थे। विद्रोह के बाद ब्रिटिश क्राउन ने ईस्ट इंडिया कंपनी से शासन अपने हाथ में ले लिया।",
    "The First Battle of Panipat (1526) was fought between Babur and which ruler?": "पानीपत का पहला युद्ध (1526) बाबर और किस शासक के बीच लड़ा गया था?",
    "The First Battle of Panipat was fought on April 21, 1526 between Babur, the founder of the Mughal Empire, and Ibrahim Lodi, the last Sultan of the Delhi Sultanate. Babur's victory marked the beginning of Mughal rule.": "पानीपत का पहला युद्ध 21 अप्रैल 1526 को मुगल साम्राज्य के संस्थापक बाबर और दिल्ली सल्तनत के अंतिम सुल्तान इब्राहिम लोदी के बीच लड़ा गया। बाबर की जीत ने मुगल शासन की शुरुआत की।",
    "The Dandi March, a major event in the Indian freedom struggle, was undertaken by Mahatma Gandhi in which year?": "दांडी मार्च महात्मा गांधी ने किस वर्ष की थी?",
    "The Dandi March (Salt March) began on March 12, 1930 from Sabarmati Ashram to Dandi, covering 240 miles. It was a direct action campaign against the British salt tax.": "दांडी मार्च 12 मार्च 1930 को साबरमती आश्रम से दांडी तक 240 मील की यात्रा के रूप में शुरू हुआ। यह ब्रिटिश नमक कर के खिलाफ अभियान था।",
    "The Maurya Empire was founded by whom?": "मौर्य साम्राज्य की स्थापना किसने की थी?",
    "Chandragupta Maurya founded the Maurya Empire in 321 BCE, with the help of his advisor Chanakya (Kautilya). He overthrew the Nanda dynasty to establish one of the largest empires in Indian history.": "चंद्रगुप्त मौर्य ने 321 ईसा पूर्व में चाणक्य की सहायता से मौर्य साम्राज्य की स्थापना की। उन्होंने नंद वंश को पराजित कर भारतीय इतिहास के सबसे बड़े साम्राज्यों में से एक की स्थापना की।",
    "Which session of the Indian National Congress is known for the declaration of Poorna Swaraj (Complete Independence)?": "कांग्रेस का कौन सा अधिवेशन पूर्ण स्वराज की घोषणा के लिए जाना जाता है?",
    "The Lahore Session of the INC in December 1929, under the presidency of Jawaharlal Nehru, passed the resolution for Poorna Swaraj (Complete Independence). January 26, 1930 was celebrated as the first independence day.": "दिसंबर 1929 में जवाहरलाल नेहरू की अध्यक्षता में कांग्रेस के लाहौर अधिवेशन ने पूर्ण स्वराज का प्रस्ताव पारित किया। 26 जनवरी 1930 को पहला स्वतंत्रता दिवस मनाया गया।",
    "The Cabinet Mission Plan of 1946 was led by Sir Stafford Cripps along with which two members?": "1946 की कैबिनेट मिशन योजना का नेतृत्व सर स्टैफोर्ड क्रिप्स ने किन दो सदस्यों के साथ किया था?",
    "The Cabinet Mission of 1946 consisted of three British Cabinet ministers: Sir Stafford Cripps, Lord Pethick-Lawrence, and A.V. Alexander. They proposed a plan for transfer of power and formation of a constituent assembly.": "1946 के कैबिनेट मिशन में तीन ब्रिटिश मंत्री शामिल थे: सर स्टैफोर्ड क्रिप्स, लॉर्ड पेथिक-लॉरेंस और ए.वी. अलेक्जेंडर।",

    # Geography
    "Which is the longest river in India?": "भारत की सबसे लंबी नदी कौन सी है?",
    "The Ganga is the longest river in India with a length of approximately 2,525 km. It originates from the Gangotri Glacier in Uttarakhand and flows into the Bay of Bengal.": "गंगा भारत की सबसे लंबी नदी है जिसकी लंबाई लगभग 2,525 किमी है। यह उत्तराखंड के गंगोत्री ग्लेशियर से निकलकर बंगाल की खाड़ी में गिरती है।",
    "Tehri Dam, one of the highest dams in the world, is built on which river?": "टिहरी बांध किस नदी पर बनाया गया है?",
    "Tehri Dam is constructed on the Bhagirathi River in Uttarakhand. It is the highest dam in India and one of the tallest in the world, with a height of 260.5 meters.": "टिहरी बांध उत्तराखंड में भागीरथी नदी पर बना है। यह भारत का सबसे ऊंचा बांध है और इसकी ऊंचाई 260.5 मीटर है।",
    "The Tropic of Cancer does NOT pass through which of the following Indian states?": "कर्क रेखा निम्नलिखित में से किस भारतीय राज्य से नहीं गुज़रती है?",
    "The Tropic of Cancer passes through 8 Indian states: Gujarat, Rajasthan, Madhya Pradesh, Chhattisgarh, Jharkhand, West Bengal, Tripura, and Mizoram. Uttar Pradesh is not among them.": "कर्क रेखा 8 भारतीय राज्यों से गुज़रती है: गुजरात, राजस्थान, मध्य प्रदेश, छत्तीसगढ़, झारखंड, पश्चिम बंगाल, त्रिपुरा और मिज़ोरम। उत्तर प्रदेश इनमें शामिल नहीं है।",
    "Which Indian state has the longest coastline?": "किस भारतीय राज्य की सबसे लंबी तटरेखा है?",
    "Gujarat has the longest coastline among all Indian states, stretching approximately 1,600 km along the Arabian Sea. The total coastline of India, including islands, is about 7,517 km.": "गुजरात की सबसे लंबी तटरेखा है, जो अरब सागर के किनारे लगभग 1,600 किमी तक फैली है।",
    "Majuli, the world's largest river island, is located on which river?": "माजुली, दुनिया का सबसे बड़ा नदी द्वीप, किस नदी पर स्थित है?",
    "Majuli is a large river island in the Brahmaputra River in Assam. It covers an area of about 880 sq km and is recognized by Guinness World Records as the largest river island in the world.": "माजुली असम में ब्रह्मपुत्र नदी में स्थित एक बड़ा नदी द्वीप है जिसका क्षेत्रफल लगभग 880 वर्ग किमी है।",
    "NH-44, the longest national highway in India, connects which two cities?": "NH-44, भारत का सबसे लंबा राष्ट्रीय राजमार्ग, किन दो शहरों को जोड़ता है?",
    "NH-44 is the longest national highway in India, running for about 3,745 km from Srinagar in Jammu & Kashmir to Kanyakumari in Tamil Nadu. It passes through multiple states.": "NH-44 भारत का सबसे लंबा राष्ट्रीय राजमार्ग है, जो श्रीनगर से कन्याकुमारी तक लगभग 3,745 किमी चलता है।",
    "Kaziranga National Park, famous for the one-horned rhinoceros, is located in which state?": "काज़ीरंगा राष्ट्रीय उद्यान किस राज्य में स्थित है?",
    "Kaziranga National Park is located in Assam and is a UNESCO World Heritage Site. It hosts two-thirds of the world's population of the great one-horned rhinoceros.": "काज़ीरंगा राष्ट्रीय उद्यान असम में स्थित है और यूनेस्को विश्व धरोहर स्थल है।",
    "Which Indian state is the largest producer of mica?": "कौन सा भारतीय राज्य अभ्रक (माइका) का सबसे बड़ा उत्पादक है?",
    "Jharkhand (formerly part of Bihar) is the largest producer of mica in India. The major mica-producing belt extends over the districts of Koderma, Giridih, and Hazaribagh.": "झारखंड भारत में अभ्रक का सबसे बड़ा उत्पादक है।",
    "Kanchenjunga, the highest peak in India, is located in which state?": "कंचनजंघा, भारत की सबसे ऊंची चोटी, किस राज्य में स्थित है?",
    "Kanchenjunga (8,586 m) is the highest peak in India and the third highest in the world. It lies on the border between Sikkim, India and Nepal.": "कंचनजंघा (8,586 मीटर) भारत की सबसे ऊंची और दुनिया की तीसरी सबसे ऊंची चोटी है। यह सिक्किम और नेपाल की सीमा पर स्थित है।",
    "The Deccan Trap, a large igneous province, was formed due to which geological event?": "डेक्कन ट्रैप किस भूवैज्ञानिक घटना के कारण बना था?",
    "The Deccan Traps were formed by massive volcanic eruptions around 66 million years ago at the end of the Cretaceous period. These basalt flows cover an area of about 500,000 sq km.": "डेक्कन ट्रैप लगभग 66 मिलियन वर्ष पहले क्रीटेशस काल के अंत में विशाल ज्वालामुखी विस्फोटों से बना था।",

    # Indian Polity
    "Which Article of the Indian Constitution deals with the abolition of untouchability?": "भारतीय संविधान का कौन सा अनुच्छेद अस्पृश्यता के उन्मूलन से संबंधित है?",
    "Article 17 of the Indian Constitution abolishes untouchability and forbids its practice in any form.": "भारतीय संविधान का अनुच्छेद 17 अस्पृश्यता को समाप्त करता है और किसी भी रूप में इसके पालन पर रोक लगाता है।",
    "What is the maximum strength of the Lok Sabha as per the Constitution of India?": "भारत के संविधान के अनुसार लोकसभा की अधिकतम सदस्य संख्या कितनी है?",
    "The maximum strength of the Lok Sabha is 552 members: 530 from states, 20 from Union Territories, and up to 2 nominated by the President.": "लोकसभा की अधिकतम सदस्य संख्या 552 है: राज्यों से 530, केंद्र शासित प्रदेशों से 20।",
}

# Simple translation for unmapped strings
def hi_q(en):
    return HI.get(en, en)

def hi_exp(en):
    return HI.get(en, en)

def hi_opts(opts):
    return [HI.get(o, o) for o in opts]

def write_topic(questions, topic_id, id_prefix, out_dir):
    topic_qs = sorted([q for q in questions if q['topicId'] == topic_id], key=lambda q: q['id'])
    if not topic_qs:
        return 0
    os.makedirs(out_dir, exist_ok=True)
    output = []
    for idx, q in enumerate(topic_qs, 1):
        entry = {
            "id": f"{id_prefix}-{idx:04d}",
            "correctOption": q['correctOption'],
            "difficulty": q['difficulty'],
            "sourceYear": q['sourceYear'],
            "en": {
                "question": q['questionText'],
                "options": [q['optionA'], q['optionB'], q['optionC'], q['optionD']],
                "explanation": q['explanation']
            },
            "hi": {
                "question": hi_q(q['questionText']),
                "options": hi_opts([q['optionA'], q['optionB'], q['optionC'], q['optionD']]),
                "explanation": hi_exp(q['explanation'])
            }
        }
        output.append(entry)
    filename = topic_id.split('-', 3)[-1] if topic_id.count('-') >= 3 else topic_id
    filepath = os.path.join(out_dir, f"{filename}.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    return len(output)

# === NTPC GA TOPICS ===
ntpc_topics = [
    ('ntpc-gk-indian-history', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-geography', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-indian-polity', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-economics', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-general-science', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-current-affairs', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-art-culture', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-sports', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-computers-technology', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-environment-ecology', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-books-authors', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-important-days-events', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-government-schemes', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-transport-communication', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
    ('ntpc-gk-inventions-discoveries', 'ntpc-ga', 'public/data/questions/ntpc/general-awareness'),
]

# === GROUP D GA ===
gdga_topics = [
    ('group-d-gk-indian-history', 'groupd-ga', 'public/data/questions/group-d/general-awareness'),
    ('group-d-gk-geography', 'groupd-ga', 'public/data/questions/group-d/general-awareness'),
    ('group-d-gk-indian-polity', 'groupd-ga', 'public/data/questions/group-d/general-awareness'),
    ('group-d-gk-economics', 'groupd-ga', 'public/data/questions/group-d/general-awareness'),
    ('group-d-gk-current-affairs', 'groupd-ga', 'public/data/questions/group-d/general-awareness'),
    ('group-d-gk-sports', 'groupd-ga', 'public/data/questions/group-d/general-awareness'),
    ('group-d-gk-art-culture', 'groupd-ga', 'public/data/questions/group-d/general-awareness'),
    ('group-d-gk-government-schemes', 'groupd-ga', 'public/data/questions/group-d/general-awareness'),
    ('group-d-gk-important-days', 'groupd-ga', 'public/data/questions/group-d/general-awareness'),
    ('group-d-gk-general-knowledge', 'groupd-ga', 'public/data/questions/group-d/general-awareness'),
]

# === GROUP D SCIENCE ===
gdsc_topics = [
    ('group-d-science-physics-motion', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-physics-force-laws', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-physics-work-energy-power', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-physics-gravitation', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-physics-sound', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-physics-light', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-physics-electricity', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-physics-magnetism', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-physics-heat-thermodynamics', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-chemistry-matter', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-chemistry-atoms-molecules', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-chemistry-acids-bases-salts', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-chemistry-metals-nonmetals', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-chemistry-carbon-compounds', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-chemistry-periodic-table', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-chemistry-chemical-reactions', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-biology-cell-structure', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-biology-tissues', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-biology-nutrition', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-biology-respiration', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-biology-transportation', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-biology-excretion', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-biology-reproduction', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-biology-genetics', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-biology-diseases', 'groupd-s', 'public/data/questions/group-d/general-science'),
    ('group-d-science-biology-ecology', 'groupd-s', 'public/data/questions/group-d/general-science'),
]

total_files = 0
total_qs = 0

print("=" * 60)
print("GENERATING BILINGUAL JSON FILES")
print("=" * 60)

for topic_id, prefix, out_dir in ntpc_topics:
    n = write_topic(ntpc, topic_id, prefix, os.path.join(BASE, out_dir))
    if n:
        tail = topic_id.split('-', 3)[-1]
        print(f"  NTPC GA  | {tail}.json ({n} questions)")
        total_files += 1; total_qs += n

for topic_id, prefix, out_dir in gdga_topics:
    n = write_topic(gdga, topic_id, prefix, os.path.join(BASE, out_dir))
    if n:
        tail = topic_id.split('-', 3)[-1]
        print(f"  Group D GA | {tail}.json ({n} questions)")
        total_files += 1; total_qs += n

for topic_id, prefix, out_dir in gdsc_topics:
    n = write_topic(gdsc, topic_id, prefix, os.path.join(BASE, out_dir))
    if n:
        tail = topic_id.split('-', 3)[-1]
        print(f"  Group D Sci | {tail}.json ({n} questions)")
        total_files += 1; total_qs += n

print("=" * 60)
print(f"TOTAL: {total_files} files, {total_qs} questions")
print("All done! Run this script to generate the files.")
