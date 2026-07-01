#!/usr/bin/env python3
"""
RRB NTPC General Awareness - Question Expander
Generates ~975 new bilingual questions across 15 JSON files.
"""

import json, os

BASE = r"C:\Users\core\rrb-exam-prep\public\data\questions\ntpc\general-awareness"

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def q(correct, difficulty, year, enq, enopts, enexp, hiq, hiopts, hiexp):
    """Create a question dict (id assigned later)."""
    return {
        "correctOption": correct,
        "difficulty": difficulty,
        "sourceYear": year,
        "en": {"question": enq, "options": enopts, "explanation": enexp},
        "hi": {"question": hiq, "options": hiopts, "explanation": hiexp}
    }

def assign_ids(items, start_num):
    for i, item in enumerate(items):
        item["id"] = f"ntpc-ga-{start_num + i:04d}"
    return items

def expand_file(filename, new_questions):
    path = os.path.join(BASE, filename)
    existing = load_json(path)
    last_num = 0
    if existing:
        last_id = existing[-1]["id"]
        last_num = int(last_id.split("-")[-1])
    next_num = last_num + 1
    assign_ids(new_questions, next_num)
    existing.extend(new_questions)
    save_json(path, existing)
    print(f"  {filename}: {len(existing)} total questions ({len(new_questions)} new)")

# ================================================================
# FILE 1: indian-history.json (10 existing, adding 65 new = 75 total)
# ================================================================
indian_history = [
    # Indus Valley
    q("C","easy",2024,"Which is the largest site of the Indus Valley Civilization?",["Mohenjo-daro","Harappa","Rakhigarhi","Dholavira"],"Rakhigarhi in Haryana is the largest Indus Valley site, spanning over 350 hectares.","सिंधु घाटी सभ्यता का सबसे बड़ा स्थल कौन सा है?",["मोहनजोदड़ो","हड़प्पा","राखीगढ़ी","धोलावीरा"],"हरियाणा में राखीगढ़ी 350 हेक्टेयर से अधिक क्षेत्र में फैला सबसे बड़ा सिंधु घाटी स्थल है।"),
    q("B","medium",2024,"The Great Bath of the Indus Valley was discovered at which site?",["Harappa","Mohenjo-daro","Lothal","Kalibangan"],"The Great Bath at Mohenjo-daro is a large rectangular water tank, possibly used for ritual bathing.","सिंधु घाटी का महान स्नानागार किस स्थल पर खोजा गया?",["हड़प्पा","मोहनजोदड़ो","लोथल","कालीबंगा"],"मोहनजोदड़ो का महान स्नानागार एक बड़ा आयताकार जल कुंड है, जो संभवतः अनुष्ठान स्नान के लिए उपयोग होता था।"),
    q("D","medium",2024,"Which Indus Valley site is famous for its dockyard?",["Mohenjo-daro","Harappa","Kalibangan","Lothal"],"Lothal in Gujarat had a dockyard connected to the Sabarmati River, showing maritime trade capability.","सिंधु घाटी का कौन सा स्थल अपने बंदरगाह के लिए प्रसिद्ध है?",["मोहनजोदड़ो","हड़प्पा","कालीबंगा","लोथल"],"गुजरात में लोथल में साबरमती नदी से जुड़ा एक बंदरगाह था, जो समुद्री व्यापार क्षमता दर्शाता है।"),
    q("A","easy",2024,"The Indus Valley people worshipped which deity form?",["Pashupati (Proto-Shiva)","Vishnu","Brahma","Indra"],"The Pashupati seal shows a seated figure surrounded by animals, considered a proto-Shiva figure.","सिंधु घाटी के लोग किस देवता रूप की पूजा करते थे?",["पशुपति (आदि-शिव)","विष्णु","ब्रह्मा","इंद्र"],"पशुपति मुहर में पशुओं से घिरी बैठी आकृति आदि-शिव मानी जाती है।"),
    q("C","hard",2024,"The Indus script is written in which style?",["Left to right","Top to bottom","Boustrophedon (alternating directions)","Circular"],"The Indus script used Boustrophedon style - right to left then left to right alternately. It remains undeciphered.","सिंधु लिपि किस शैली में लिखी जाती है?",["बाएं से दाएं","ऊपर से नीचे","बूस्ट्रोफेडन (बारी-बारी दिशाएं)","गोलाकार"],"सिंधु लिपि बूस्ट्रोफेडन शैली में लिखी जाती थी। यह अभी तक पढ़ी नहीं जा सकी है।"),
    q("B","medium",2024,"Which metal was NOT known to the Indus Valley people?",["Copper","Iron","Bronze","Gold"],"Iron was unknown to Indus Valley people. They used copper, bronze, gold, silver, and lead but not iron.","सिंधु घाटी के लोग किस धातु से परिचित नहीं थे?",["तांबा","लोहा","कांसा","सोना"],"सिंधु घाटी के लोग लोहे से परिचित नहीं थे। वे तांबा, कांसा, सोना, चांदी और सीसा का उपयोग करते थे।"),
    # Vedic Period
    q("A","easy",2024,"Which is the oldest Veda?",["Rigveda","Samaveda","Yajurveda","Atharvaveda"],"Rigveda (c.1500-1200 BCE) is the oldest, containing 1,028 hymns in 10 mandalas.","सबसे पुराना वेद कौन सा है?",["ऋग्वेद","सामवेद","यजुर्वेद","अथर्ववेद"],"ऋग्वेद (लगभग 1500-1200 ई.पू.) सबसे पुराना है, जिसमें 10 मंडलों में 1,028 सूक्त हैं।"),
    q("C","medium",2024,"The Gayatri Mantra is found in which Veda?",["Samaveda","Yajurveda","Rigveda","Atharvaveda"],"Gayatri Mantra is in Rigveda Mandala 3, Hymn 62, Verse 10, dedicated to solar deity Savitr.","गायत्री मंत्र किस वेद में है?",["सामवेद","यजुर्वेद","ऋग्वेद","अथर्ववेद"],"गायत्री मंत्र ऋग्वेद मंडल 3, सूक्त 62, श्लोक 10 में है, जो सौर देवता सविता को समर्पित है।"),
    q("B","easy",2024,"Which Rishi composed hymns including the Gayatri Mantra?",["Vasishta","Vishwamitra","Atri","Agastya"],"Vishwamitra composed several Rigvedic hymns including Gayatri Mantra.","किस ऋषि ने गायत्री मंत्र सहित सूक्तों की रचना की?",["वसिष्ठ","विश्वामित्र","अत्रि","अगस्त्य"],"विश्वामित्र ने गायत्री मंत्र सहित कई ऋग्वैदिक सूक्तों की रचना की।"),
    q("D","hard",2023,"The Battle of Ten Kings (Dasarajna) was fought on which river?",["Ganga","Yamuna","Saraswati","Ravi (Parushni)"],"Fought on Ravi river banks between King Sudas (Bharata) and ten tribes. Sudas won.","दस राजाओं का युद्ध (दाशराज्ञ) किस नदी पर लड़ा गया?",["गंगा","यमुना","सरस्वती","रावी (परुष्णी)"],"राजा सुदास (भरत) और दस जनजातियों के बीच रावी नदी के तट पर लड़ा गया। सुदास विजयी हुए।"),
    q("B","medium",2024,"Which Veda is known as the 'Book of Chants'?",["Rigveda","Samaveda","Yajurveda","Atharvaveda"],"Samaveda contains melodies and chants, setting Rigvedic hymns to music for sacrificial rituals.","किस वेद को 'गानों की पुस्तक' कहा जाता है?",["ऋग्वेद","सामवेद","यजुर्वेद","अथर्ववेद"],"सामवेद में गान और संगीतमय मंत्र हैं, जो यज्ञ अनुष्ठानों के लिए ऋग्वैदिक सूक्तों को संगीतबद्ध करते हैं।"),
    # Mahajanapadas & Mauryas
    q("C","medium",2024,"How many Mahajanapadas existed in ancient India during the 6th century BCE?",["12","14","16","18"],"16 Mahajanapadas existed as per Buddhist text Anguttara Nikaya. Magadha emerged as the most powerful.","छठी शताब्दी ई.पू. में प्राचीन भारत में कितने महाजनपद थे?",["12","14","16","18"],"बौद्ध ग्रंथ अंगुत्तर निकाय के अनुसार 16 महाजनपद थे। मगध सबसे शक्तिशाली बनकर उभरा।"),
    q("B","easy",2024,"Chandragupta Maurya was succeeded by?",["Ashoka","Bindusara","Samprati","Dasharatha"],"Bindusara (297-273 BCE) succeeded Chandragupta and was called Amitraghata (slayer of enemies).","चंद्रगुप्त मौर्य का उत्तराधिकारी कौन था?",["अशोक","बिंदुसार","संप्रति","दशरथ"],"बिंदुसार (297-273 ई.पू.) चंद्रगुप्त के उत्तराधिकारी थे, जिन्हें अमित्रघात (शत्रुओं का विनाशक) कहा जाता था।"),
    q("C","medium",2024,"The Kalinga War was fought in which year?",["273 BCE","269 BCE","261 BCE","250 BCE"],"The Kalinga War in 261 BCE turned Ashoka to Buddhism and the policy of Dhamma.","कलिंग युद्ध किस वर्ष लड़ा गया?",["273 ई.पू.","269 ई.पू.","261 ई.पू.","250 ई.पू."],"261 ई.पू. में कलिंग युद्ध ने अशोक को बौद्ध धर्म और धम्म की नीति की ओर मोड़ दिया।"),
    q("D","medium",2024,"Megasthenes was ambassador to which Mauryan court?",["Ashoka","Bindusara","Samprati","Chandragupta Maurya"],"Megasthenes, sent by Seleucus Nicator, wrote 'Indica' about Mauryan India.","मेगस्थनीज़ किस मौर्य दरबार में राजदूत था?",["अशोक","बिंदुसार","संप्रति","चंद्रगुप्त मौर्य"],"सेल्यूकस निकेटर द्वारा भेजे गए मेगस्थनीज़ ने मौर्य भारत पर 'इंडिका' लिखी।"),
    q("A","medium",2024,"Who was the last Mauryan ruler?",["Brihadratha","Ashoka","Dasharatha","Samprati"],"Brihadratha was assassinated by Pushyamitra Shunga in 185 BCE, ending Mauryan rule.","अंतिम मौर्य शासक कौन था?",["बृहद्रथ","अशोक","दशरथ","संप्रति"],"बृहद्रथ की 185 ई.पू. में पुष्यमित्र शुंग ने हत्या कर मौर्य शासन समाप्त किया।"),
    q("B","hard",2024,"The Arthashastra, an ancient treatise on statecraft, was written by?",["Megasthenes","Kautilya (Chanakya)","Kalidasa","Panini"],"Kautilya/Chanakya wrote Arthashastra, covering politics, economics, military strategy, and law.","अर्थशास्त्र, राजकाज पर प्राचीन ग्रंथ, किसने लिखा?",["मेगस्थनीज़","कौटिल्य (चाणक्य)","कालिदास","पाणिनि"],"कौटिल्य/चाणक्य ने राजनीति, अर्थशास्त्र, सैन्य रणनीति और कानून पर अर्थशास्त्र लिखा।"),
    # Guptas
    q("C","easy",2024,"Who is known as the 'Napoleon of India'?",["Chandragupta Maurya","Ashoka","Samudragupta","Harshavardhana"],"Samudragupta is called Napoleon of India for his extensive conquests.","भारत का नेपोलियन किसे कहा जाता है?",["चंद्रगुप्त मौर्य","अशोक","समुद्रगुप्त","हर्षवर्धन"],"समुद्रगुप्त को उनके व्यापक सैन्य अभियानों के लिए भारत का नेपोलियन कहा जाता है।"),
    q("B","medium",2024,"The Iron Pillar at Mehrauli is associated with which Gupta ruler?",["Samudragupta","Chandragupta II Vikramaditya","Kumaragupta I","Skandagupta"],"The rust-resistant Iron Pillar bears an inscription of Chandragupta II.","महरौली का लौह स्तंभ किस गुप्त शासक से जुड़ा है?",["समुद्रगुप्त","चंद्रगुप्त द्वितीय विक्रमादित्य","कुमारगुप्त प्रथम","स्कंदगुप्त"],"जंग-रोधी लौह स्तंभ पर चंद्रगुप्त द्वितीय का शिलालेख है।"),
    q("D","hard",2024,"Chinese pilgrim Fa-Hien visited during whose reign?",["Samudragupta","Kumaragupta","Skandagupta","Chandragupta II"],"Fa-Hien (399-414 CE) visited during Chandragupta II's reign, describing Gupta prosperity.","चीनी यात्री फाहियान किसके शासनकाल में आए?",["समुद्रगुप्त","कुमारगुप्त","स्कंदगुप्त","चंद्रगुप्त द्वितीय"],"फाहियान (399-414 ई.) चंद्रगुप्त द्वितीय के शासनकाल में आए और गुप्त समृद्धि का वर्णन किया।"),
    q("A","medium",2024,"Which Gupta ruler assumed the title 'Maharajadhiraja'?",["Chandragupta I","Samudragupta","Chandragupta II","Skandagupta"],"Chandragupta I assumed the title Maharajadhiraja and started the Gupta Era (319-320 CE).","किस गुप्त शासक ने 'महाराजाधिराज' की उपाधि धारण की?",["चंद्रगुप्त प्रथम","समुद्रगुप्त","चंद्रगुप्त द्वितीय","स्कंदगुप्त"],"चंद्रगुप्त प्रथम ने महाराजाधिराज की उपाधि धारण की और गुप्त संवत (319-320 ई.) शुरू किया।"),
    q("C","hard",2023,"Navratnas (Nine Gems) adorned the court of which Gupta ruler?",["Samudragupta","Kumaragupta","Chandragupta II Vikramaditya","Skandagupta"],"Chandragupta II's court had Navratnas including Kalidasa, Varahamihira, and Amarasimha.","नवरत्न किस गुप्त शासक के दरबार में थे?",["समुद्रगुप्त","कुमारगुप्त","चंद्रगुप्त द्वितीय विक्रमादित्य","स्कंदगुप्त"],"चंद्रगुप्त द्वितीय के दरबार में कालिदास, वराहमिहिर और अमरसिंह सहित नवरत्न थे।"),
    q("B","easy",2024,"Kalidasa, the great Sanskrit poet, lived during which period?",["Mauryan","Gupta","Kushan","Harsha"],"Kalidasa flourished during the Gupta period (Chandragupta II's court), writing Abhijnanashakuntalam and Meghaduta.","महान संस्कृत कवि कालिदास किस काल में रहते थे?",["मौर्य","गुप्त","कुषाण","हर्ष"],"कालिदास गुप्त काल (चंद्रगुप्त द्वितीय के दरबार) में रचनाकार थे, जिन्होंने अभिज्ञानशाकुंतलम और मेघदूत लिखा।"),
    # Harsha
    q("C","medium",2024,"Harshavardhana's capital was at?",["Pataliputra","Ujjain","Kannauj","Taxila"],"Harshavardhana made Kannauj his capital. His reign is documented by Banabhatta and Chinese pilgrim Hiuen Tsang.","हर्षवर्धन की राजधानी कहां थी?",["पाटलिपुत्र","उज्जैन","कन्नौज","तक्षशिला"],"हर्षवर्धन ने कन्नौज को अपनी राजधानी बनाया। उनके शासन का वर्णन बाणभट्ट और चीनी यात्री ह्वेनसांग ने किया।"),
    q("D","hard",2024,"Hiuen Tsang visited India during whose reign?",["Ashoka","Chandragupta II","Samudragupta","Harshavardhana"],"Hiuen Tsang (Xuanzang) visited India (630-644 CE) during Harsha's reign, studying at Nalanda.","ह्वेनसांग किसके शासनकाल में भारत आए?",["अशोक","चंद्रगुप्त द्वितीय","समुद्रगुप्त","हर्षवर्धन"],"ह्वेनसांग (जुआनज़ांग) हर्ष के शासनकाल में (630-644 ई.) भारत आए और नालंदा में अध्ययन किया।"),
]

# ... lots more questions needed for all 15 files ...

print("Script structure established. Need to complete all question data arrays.")
