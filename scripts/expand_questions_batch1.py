#!/usr/bin/env python3
"""Batch 1: Expand indian-history, geography, indian-polity, economics, general-science JSON files"""

import json
import os

BASE = r"C:\Users\core\rrb-exam-prep\public\data\questions\ntpc\general-awareness"

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_last_num(items):
    if not items:
        return 0
    last_id = items[-1]['id']
    return int(last_id.split('-')[-1])

def make_q(num, correct, difficulty, sourceYear, en_q, en_opts, en_expl, hi_q, hi_opts, hi_expl):
    return {
        "id": f"ntpc-ga-{num:04d}",
        "correctOption": correct,
        "difficulty": difficulty,
        "sourceYear": sourceYear,
        "en": {
            "question": en_q,
            "options": en_opts,
            "explanation": en_expl
        },
        "hi": {
            "question": hi_q,
            "options": hi_opts,
            "explanation": hi_expl
        }
    }

# =============================================================
# 1. INDIAN HISTORY (65 new questions, start at 0011)
# =============================================================
indian_history_new = [
    # Indus Valley Civilization
    make_q(11, "C", "easy", 2024,
        "Which is the largest site of the Indus Valley Civilization?",
        ["Mohenjo-daro", "Harappa", "Rakhigarhi", "Dholavira"],
        "Rakhigarhi in Haryana is now considered the largest Indus Valley site, spanning over 350 hectares. Mohenjo-daro and Harappa were previously thought to be the largest.",
        "सिंधु घाटी सभ्यता का सबसे बड़ा स्थल कौन सा है?",
        ["मोहनजोदड़ो", "हड़प्पा", "राखीगढ़ी", "धोलावीरा"],
        "हरियाणा में राखीगढ़ी अब 350 हेक्टेयर से अधिक क्षेत्र में फैला सबसे बड़ा सिंधु घाटी स्थल माना जाता है। पहले मोहनजोदड़ो और हड़प्पा को सबसे बड़ा माना जाता था।"
    ),
    make_q(12, "B", "medium", 2024,
        "The Great Bath of the Indus Valley Civilization was discovered at which site?",
        ["Harappa", "Mohenjo-daro", "Lothal", "Kalibangan"],
        "The Great Bath, a large rectangular water tank, was discovered at Mohenjo-daro. It is considered an early example of public water architecture and possibly used for ritual bathing.",
        "सिंधु घाटी सभ्यता का महान स्नानागार किस स्थल पर खोजा गया था?",
        ["हड़प्पा", "मोहनजोदड़ो", "लोथल", "कालीबंगा"],
        "महान स्नानागार, एक बड़ा आयताकार जल कुंड, मोहनजोदड़ो में खोजा गया था। इसे सार्वजनिक जल वास्तुकला का प्रारंभिक उदाहरण माना जाता है।"
    ),
    make_q(13, "D", "medium", 2024,
        "Which Indus Valley site is famous for its dockyard?",
        ["Mohenjo-daro", "Harappa", "Kalibangan", "Lothal"],
        "Lothal in Gujarat had a remarkable dockyard connected to an ancient course of the Sabarmati River, showing the civilization's maritime trade capability.",
        "कौन सा सिंधु घाटी स्थल अपने बंदरगाह के लिए प्रसिद्ध है?",
        ["मोहनजोदड़ो", "हड़प्पा", "कालीबंगा", "लोथल"],
        "गुजरात में लोथल में साबरमती नदी के प्राचीन मार्ग से जुड़ा एक उल्लेखनीय बंदरगाह था, जो सभ्यता की समुद्री व्यापार क्षमता को दर्शाता है।"
    ),
    make_q(14, "A", "easy", 2024,
        "The Indus Valley people worshipped which of the following?",
        ["Pashupati (Proto-Shiva)", "Vishnu", "Brahma", "Indra"],
        "The Pashupati seal found at Mohenjo-daro shows a seated figure surrounded by animals, considered a proto-Shiva figure. They also worshipped mother goddess and trees like Peepal.",
        "सिंधु घाटी के लोग किसकी पूजा करते थे?",
        ["पशुपति (आदि-शिव)", "विष्णु", "ब्रह्मा", "इंद्र"],
        "मोहनजोदड़ो में मिली पशुपति मुहर में पशुओं से घिरी एक बैठी आकृति दिखती है, जिसे आदि-शिव माना जाता है। वे मातृदेवी और पीपल जैसे वृक्षों की भी पूजा करते थे।"
    ),
    make_q(15, "C", "medium", 2024,
        "The Indus Valley script was written in which direction?",
        ["Left to right only", "Top to bottom", "Right to left (Boustrophedon)", "Circular"],
        "The Indus script was written in Boustrophedon style - right to left in the first line, then left to right in the next, and so on. The script remains undeciphered.",
        "सिंधु घाटी की लिपि किस दिशा में लिखी जाती थी?",
        ["केवल बाएं से दाएं", "ऊपर से नीचे", "दाएं से बाएं (बूस्ट्रोफेडन)", "गोलाकार"],
        "सिंधु लिपि बूस्ट्रोफेडन शैली में लिखी जाती थी - पहली पंक्ति में दाएं से बाएं, फिर अगली में बाएं से दाएं। यह लिपि अभी तक पढ़ी नहीं जा सकी है।"
    ),
    # Vedic Period
    make_q(16, "A", "easy", 2024,
        "Which is the oldest Veda?",
        ["Rigveda", "Samaveda", "Yajurveda", "Atharvaveda"],
        "The Rigveda is the oldest Veda, composed around 1500-1200 BCE. It contains 1,028 hymns (suktas) divided into 10 mandalas, mostly praising various deities.",
        "सबसे पुराना वेद कौन सा है?",
        ["ऋग्वेद", "सामवेद", "यजुर्वेद", "अथर्ववेद"],
        "ऋग्वेद सबसे पुराना वेद है, जो लगभग 1500-1200 ईसा पूर्व रचा गया। इसमें 10 मंडलों में विभाजित 1,028 सूक्त हैं, जो विभिन्न देवताओं की स्तुति करते हैं।"
    ),
    make_q(17, "C", "medium", 2024,
        "The Gayatri Mantra is found in which Veda?",
        ["Samaveda", "Yajurveda", "Rigveda", "Atharvaveda"],
        "The Gayatri Mantra is found in the Rigveda (Mandala 3, Hymn 62, Verse 10). It is dedicated to the solar deity Savitr.",
        "गायत्री मंत्र किस वेद में पाया जाता है?",
        ["सामवेद", "यजुर्वेद", "ऋग्वेद", "अथर्ववेद"],
        "गायत्री मंत्र ऋग्वेद (मंडल 3, सूक्त 62, श्लोक 10) में पाया जाता है। यह सौर देवता सविता को समर्पित है।"
    ),
    make_q(18, "B", "easy", 2024,
        "Who among the following was a famous scholar during the Vedic period who composed hymns in the Rigveda?",
        ["Manu", "Vishwamitra", "Chanakya", "Valmiki"],
        "Vishwamitra was a celebrated Rishi who composed several hymns of the Rigveda, including the Gayatri Mantra (Mandala 3). Other major Rigvedic rishis include Vasishta, Atri, and Agastya.",
        "वैदिक काल में प्रसिद्ध विद्वान कौन थे जिन्होंने ऋग्वेद में सूक्त रचे?",
        ["मनु", "विश्वामित्र", "चाणक्य", "वाल्मीकि"],
        "विश्वामित्र एक प्रसिद्ध ऋषि थे जिन्होंने ऋग्वेद के कई सूक्तों की रचना की, जिसमें गायत्री मंत्र (मंडल 3) भी शामिल है। वसिष्ठ, अत्रि और अगस्त्य अन्य प्रमुख ऋग्वैदिक ऋषि हैं।"
    ),
    make_q(19, "D", "hard", 2023,
        "The Battle of the Ten Kings (Dasarajna) was fought on the banks of which river?",
        ["Ganga", "Yamuna", "Saraswati", "Ravi (Parushni)"],
        "The Battle of the Ten Kings, mentioned in Rigveda Mandala 7, was fought between King Sudas of the Bharata tribe and a confederacy of ten tribes on the banks of the Ravi (Parushni) river. Sudas emerged victorious.",
        "दस राजाओं का युद्ध (दाशराज्ञ) किस नदी के तट पर लड़ा गया था?",
        ["गंगा", "यमुना", "सरस्वती", "रावी (परुष्णी)"],
        "ऋग्वेद मंडल 7 में वर्णित दस राजाओं का युद्ध भरत जनजाति के राजा सुदास और दस जनजातियों के संघ के बीच रावी (परुष्णी) नदी के तट पर लड़ा गया था। सुदास विजयी हुए।"
    ),
    # Mauryan Empire
    make_q(20, "B", "easy", 2024,
        "Chandragupta Maurya was succeeded by which ruler?",
        ["Ashoka", "Bindusara", "Samprati", "Dasharatha"],
        "After Chandragupta Maurya abdicated to become a Jain monk, his son Bindusara ruled from about 297-273 BCE. Bindusara was called Amitraghata (slayer of enemies).",
        "चंद्रगुप्त मौर्य के बाद किस शासक ने शासन किया?",
        ["अशोक", "बिंदुसार", "संप्रति", "दशरथ"],
        "चंद्रगुप्त मौर्य द्वारा जैन भिक्षु बनने के लिए त्याग करने के बाद, उनके पुत्र बिंदुसार ने लगभग 297-273 ईसा पूर्व तक शासन किया। बिंदुसार को अमित्रघात (शत्रुओं का विनाशक) कहा जाता था।"
    ),
    make_q(21, "C", "medium", 2024,
        "The famous Kalinga War was fought in which year?",
        ["273 BCE", "269 BCE", "261 BCE", "250 BCE"],
        "The Kalinga War was fought in 261 BCE during Ashoka's reign. The massive bloodshed and suffering caused Ashoka to embrace Buddhism and the policy of Dhamma.",
        "प्रसिद्ध कलिंग युद्ध किस वर्ष लड़ा गया था?",
        ["273 ईसा पूर्व", "269 ईसा पूर्व", "261 ईसा पूर्व", "250 ईसा पूर्व"],
        "कलिंग युद्ध 261 ईसा पूर्व में अशोक के शासनकाल में लड़ा गया था। भारी रक्तपात और पीड़ा ने अशोक को बौद्ध धर्म और धम्म की नीति अपनाने के लिए प्रेरित किया।"
    ),
    make_q(22, "D", "medium", 2024,
        "Megasthenes was an ambassador to which Mauryan ruler's court?",
        ["Ashoka", "Bindusara", "Samprati", "Chandragupta Maurya"],
        "Megasthenes was a Greek ambassador sent by Seleucus Nicator to the court of Chandragupta Maurya. He wrote 'Indica', a detailed account of Mauryan India.",
        "मेगस्थनीज़ किस मौर्य शासक के दरबार में राजदूत था?",
        ["अशोक", "बिंदुसार", "संप्रति", "चंद्रगुप्त मौर्य"],
        "मेगस्थनीज़ सेल्यूकस निकेटर द्वारा चंद्रगुप्त मौर्य के दरबार में भेजा गया यूनानी राजदूत था। उसने मौर्य भारत का विस्तृत विवरण 'इंडिका' लिखा।"
    ),
    make_q(23, "A", "medium", 2024,
        "Who was the last Mauryan ruler?",
        ["Brihadratha", "Ashoka", "Dasharatha", "Samprati"],
        "Brihadratha was the last Mauryan emperor, assassinated by his commander-in-chief Pushyamitra Shunga in 185 BCE, who then established the Shunga dynasty.",
        "अंतिम मौर्य शासक कौन था?",
        ["बृहद्रथ", "अशोक", "दशरथ", "संप्रति"],
        "बृहद्रथ अंतिम मौर्य सम्राट था, जिसकी 185 ईसा पूर्व में उसके सेनापति पुष्यमित्र शुंग ने हत्या कर दी, जिसने फिर शुंग राजवंश की स्थापना की।"
    ),
    # Gupta Empire
    make_q(24, "C", "easy", 2024,
        "Who is known as the 'Napoleon of India'?",
        ["Chandragupta Maurya", "Ashoka", "Samudragupta", "Harshavardhana"],
        "Samudragupta is known as the Napoleon of India for his extensive military conquests. The Allahabad Pillar inscription by Harisena provides details of his campaigns.",
        "भारत का नेपोलियन किसे कहा जाता है?",
        ["चंद्रगुप्त मौर्य", "अशोक", "समुद्रगुप्त", "हर्षवर्धन"],
        "समुद्रगुप्त को उनके व्यापक सैन्य अभियानों के लिए भारत का नेपोलियन कहा जाता है। हरिषेण द्वारा इलाहाबाद स्तंभ शिलालेख उनके अभियानों का विवरण देता है।"
    ),
    make_q(25, "B", "medium", 2024,
        "The Iron Pillar at Mehrauli is associated with which Gupta ruler?",
        ["Samudragupta", "Chandragupta II (Vikramaditya)", "Kumaragupta I", "Skandagupta"],
        "The Iron Pillar at Mehrauli (Delhi) bears an inscription of Chandragupta II Vikramaditya. It is famous for its rust-resistant iron, showing advanced metallurgical skills.",
        "महरौली का लौह स्तंभ किस गुप्त शासक से जुड़ा है?",
        ["समुद्रगुप्त", "चंद्रगुप्त द्वितीय (विक्रमादित्य)", "कुमारगुप्त प्रथम", "स्कंदगुप्त"],
        "महरौली (दिल्ली) के लौह स्तंभ पर चंद्रगुप्त द्वितीय विक्रमादित्य का शिलालेख है। यह जंग-रोधी लोहे के लिए प्रसिद्ध है, जो उन्नत धातुकर्म कौशल दर्शाता है।"
    ),
    make_q(26, "D", "hard", 2024,
        "The famous Chinese pilgrim Fa-Hien visited India during the reign of which Gupta emperor?",
        ["Samudragupta", "Kumaragupta", "Skandagupta", "Chandragupta II"],
        "Fa-Hien visited India during the reign of Chandragupta II (Vikramaditya) around 399-414 CE. He came to study Buddhism and described the prosperity and peaceful nature of Gupta rule.",
        "प्रसिद्ध चीनी यात्री फाहियान ने किस गुप्त सम्राट के शासनकाल में भारत का दौरा किया?",
        ["समुद्रगुप्त", "कुमारगुप्त", "स्कंदगुप्त", "चंद्रगुप्त द्वितीय"],
        "फाहियान ने चंद्रगुप्त द्वितीय (विक्रमादित्य) के शासनकाल में लगभग 399-414 ईस्वी में भारत का दौरा किया। वे बौद्ध धर्म का अध्ययन करने आए और गुप्त शासन की समृद्धि व शांतिपूर्ण प्रकृति का वर्णन किया।"
    ),
    # Delhi Sultanate
    make_q(27, "A", "easy", 2024,
        "Who founded the Delhi Sultanate?",
        ["Qutb-ud-din Aibak", "Iltutmish", "Alauddin Khilji", "Muhammad bin Tughlaq"],
        "Qutb-ud-din Aibak, a slave general of Muhammad Ghori, founded the Slave (Mamluk) dynasty in 1206 CE, marking the beginning of the Delhi Sultanate.",
        "दिल्ली सल्तनत की स्थापना किसने की?",
        ["कुतुब-उद-दीन ऐबक", "इल्तुतमिश", "अलाउद्दीन खिलजी", "मुहम्मद बिन तुगलक"],
        "मुहम्मद गौरी के गुलाम सेनापति कुतुब-उद-दीन ऐबक ने 1206 ईस्वी में गुलाम (ममलूक) राजवंश की स्थापना की, जो दिल्ली सल्तनत की शुरुआत थी।"
    ),
    make_q(28, "B", "medium", 2024,
        "Which Delhi Sultan introduced the token currency system?",
        ["Alauddin Khilji", "Muhammad bin Tughlaq", "Firoz Shah Tughlaq", "Iltutmish"],
        "Muhammad bin Tughlaq introduced token currency made of brass and copper in place of silver coins in 1330. The experiment failed due to widespread forgery.",
        "किस दिल्ली सुल्तान ने सांकेतिक मुद्रा प्रणाली शुरू की?",
        ["अलाउद्दीन खिलजी", "मुहम्मद बिन तुगलक", "फिरोज शाह तुगलक", "इल्तुतमिश"],
        "मुहम्मद बिन तुगलक ने 1330 में चांदी के सिक्कों के स्थान पर पीतल और तांबे की सांकेतिक मुद्रा शुरू की। व्यापक जालसाजी के कारण यह प्रयोग विफल रहा।"
    ),
    make_q(29, "C", "hard", 2023,
        "The market control policy (price regulations) was introduced by which Delhi Sultan?",
        ["Iltutmish", "Balban", "Alauddin Khilji", "Muhammad bin Tughlaq"],
        "Alauddin Khilji established a comprehensive market control system with fixed prices for all commodities. He set up separate markets (mandis) and appointed Shahna-i-Mandi to regulate prices.",
        "बाजार नियंत्रण नीति (मूल्य विनियमन) किस दिल्ली सुल्तान ने शुरू की?",
        ["इल्तुतमिश", "बलबन", "अलाउद्दीन खिलजी", "मुहम्मद बिन तुगलक"],
        "अलाउद्दीन खिलजी ने सभी वस्तुओं के निश्चित मूल्यों के साथ एक व्यापक बाजार नियंत्रण प्रणाली स्थापित की। उसने अलग बाजार (मंडियां) स्थापित किए और मूल्यों के नियमन के लिए शहना-ए-मंडी नियुक्त किए।"
    ),
    make_q(30, "A", "medium", 2024,
        "The correct chronological order of Delhi Sultanate dynasties is:",
        ["Slave → Khilji → Tughlaq → Sayyid → Lodi", "Khilji → Slave → Tughlaq → Lodi → Sayyid", "Slave → Tughlaq → Khilji → Lodi → Sayyid", "Tughlaq → Slave → Khilji → Sayyid → Lodi"],
        "The Delhi Sultanate had five dynasties in order: Slave/Mamluk (1206-1290), Khilji (1290-1320), Tughlaq (1320-1414), Sayyid (1414-1451), and Lodi (1451-1526).",
        "दिल्ली सल्तनत के राजवंशों का सही कालक्रम है:",
        ["गुलाम → खिलजी → तुगलक → सैयद → लोदी", "खिलजी → गुलाम → तुगलक → लोदी → सैयद", "गुलाम → तुगलक → खिलजी → लोदी → सैयद", "तुगलक → गुलाम → खिलजी → सैयद → लोदी"],
        "दिल्ली सल्तनत में क्रमानुसार पांच राजवंश थे: गुलाम/ममलूक (1206-1290), खिलजी (1290-1320), तुगलक (1320-1414), सैयद (1414-1451), और लोदी (1451-1526)।"
    ),
    # Mughal Empire
    make_q(31, "C", "easy", 2024,
        "The First Battle of Panipat (1526) was fought between Babur and whom?",
        ["Rana Sanga", "Hem Chandra Vikramaditya", "Ibrahim Lodi", "Sher Shah Suri"],
        "The First Battle of Panipat was fought on April 21, 1526 between Babur and Ibrahim Lodi. Babur's use of artillery (Ottoman cannons) and Tuluguma tactics helped him defeat the larger Lodi army.",
        "पानीपत का पहला युद्ध (1526) बाबर और किसके बीच लड़ा गया था?",
        ["राणा सांगा", "हेम चंद्र विक्रमादित्य", "इब्राहिम लोदी", "शेर शाह सूरी"],
        "पानीपत का पहला युद्ध 21 अप्रैल 1526 को बाबर और इब्राहिम लोदी के बीच लड़ा गया। बाबर की तोपखाने (उस्मानी तोपों) और तुलुगुमा रणनीति ने बड़ी लोदी सेना को हराने में मदद की।"
    ),
    make_q(32, "A", "medium", 2024,
        "The Mansabdari system was introduced by which Mughal emperor?",
        ["Akbar", "Babur", "Humayun", "Shah Jahan"],
        "Akbar introduced the Mansabdari system around 1570. It was a military-cum-administrative system where officers (mansabdars) were ranked based on zat (personal rank) and sawar (cavalry maintained).",
        "मनसबदारी प्रणाली किस मुगल सम्राट ने शुरू की थी?",
        ["अकबर", "बाबर", "हुमायूं", "शाहजहां"],
        "अकबर ने लगभग 1570 में मनसबदारी प्रणाली शुरू की। यह एक सैन्य-सह-प्रशासनिक प्रणाली थी जहां अधिकारियों (मनसबदारों) को जात (व्यक्तिगत रैंक) और सवार (अनुरक्षित घुड़सवार) के आधार पर रैंक दिया जाता था।"
    ),
    make_q(33, "B", "medium", 2024,
        "Din-i-Ilahi, a syncretic religion, was started by which Mughal emperor?",
        ["Jahangir", "Akbar", "Shah Jahan", "Aurangzeb"],
        "Akbar founded Din-i-Ilahi (Divine Faith) in 1582, combining elements of various religions including Hinduism, Islam, Christianity, and Zoroastrianism. It had very few followers.",
        "दीन-ए-इलाही, एक समन्वयवादी धर्म, किस मुगल सम्राट ने शुरू किया था?",
        ["जहांगीर", "अकबर", "शाहजहां", "औरंगज़ेब"],
        "अकबर ने 1582 में दीन-ए-इलाही (ईश्वरीय धर्म) की स्थापना की, जिसमें हिंदू धर्म, इस्लाम, ईसाई धर्म और पारसी धर्म सहित विभिन्न धर्मों के तत्व शामिल थे। इसके बहुत कम अनुयायी थे।"
    ),
    make_q(34, "D", "easy", 2024,
        "The Taj Mahal was built by Shah Jahan in memory of whom?",
        ["Nur Jahan", "Jahanara", "Mumtaz Begum", "Mumtaz Mahal"],
        "Shah Jahan built the Taj Mahal in Agra in memory of his beloved wife Mumtaz Mahal (originally Arjumand Banu Begum). Construction began in 1632 and took about 22 years to complete.",
        "ताजमहल शाहजहां ने किसकी याद में बनवाया था?",
        ["नूरजहां", "जहांआरा", "मुमताज बेगम", "मुमताज महल"],
        "शाहजहां ने अपनी प्रिय पत्नी मुमताज महल (मूल नाम अर्जुमंद बानू बेगम) की याद में आगरा में ताजमहल बनवाया। निर्माण 1632 में शुरू हुआ और लगभग 22 वर्षों में पूरा हुआ।"
    ),
    make_q(35, "C", "hard", 2024,
        "Which Mughal emperor is known as 'Zinda Pir' (Living Saint)?",
        ["Akbar", "Jahangir", "Aurangzeb", "Shah Jahan"],
        "Aurangzeb was called Zinda Pir due to his strict adherence to Islamic orthodoxy. He re-introduced Jizya tax, banned music in court, and executed Guru Tegh Bahadur.",
        "किस मुगल सम्राट को 'जिंदा पीर' (जीवित संत) कहा जाता है?",
        ["अकबर", "जहांगीर", "औरंगज़ेब", "शाहजहां"],
        "औरंगज़ेब को उनकी सख्त इस्लामी रूढ़िवादिता के कारण जिंदा पीर कहा जाता था। उन्होंने जजिया कर पुनः लागू किया, दरबार में संगीत पर प्रतिबंध लगाया और गुरु तेग बहादुर को मृत्युदंड दिया।"
    ),
    # Marathas
    make_q(36, "B", "medium", 2024,
        "Shivaji was crowned as Chhatrapati in which year?",
        ["1670", "1674", "1680", "1646"],
        "Shivaji Maharaj was formally crowned Chhatrapati on June 6, 1674 at Raigad Fort. The ceremony was conducted by the famous scholar Gaga Bhatt.",
        "शिवाजी का छत्रपति के रूप में राज्याभिषेक किस वर्ष हुआ?",
        ["1670", "1674", "1680", "1646"],
        "शिवाजी महाराज का 6 जून 1674 को रायगढ़ किले में विधिवत छत्रपति के रूप में राज्याभिषेक हुआ। यह समारोह प्रसिद्ध विद्वान गागा भट्ट द्वारा संपन्न कराया गया।"
    ),
    make_q(37, "D", "hard", 2023,
        "The Third Battle of Panipat (1761) was fought between the Marathas and whom?",
        ["British", "Mughals", "Sikhs", "Ahmad Shah Abdali (Durrani)"],
        "The Third Battle of Panipat was fought on January 14, 1761 between the Maratha Empire under Sadashivrao Bhau and Ahmad Shah Abdali. The Marathas suffered a devastating defeat, which altered the power balance in India.",
        "पानीपत का तीसरा युद्ध (1761) मराठों और किसके बीच लड़ा गया था?",
        ["अंग्रेज़", "मुगल", "सिख", "अहमद शाह अब्दाली (दुर्रानी)"],
        "पानीपत का तीसरा युद्ध 14 जनवरी 1761 को सदाशिवराव भाऊ के नेतृत्व में मराठा साम्राज्य और अहमद शाह अब्दाली के बीच लड़ा गया। मराठों को विनाशकारी हार का सामना करना पड़ा, जिसने भारत में शक्ति संतुलन बदल दिया।"
    ),
    # 1857 Revolt
    make_q(38, "C", "easy", 2024,
        "The Revolt of 1857 began at which place?",
        ["Delhi", "Kanpur", "Meerut", "Lucknow"],
        "The Revolt of 1857 began on May 10, 1857 at Meerut when sepoys refused to use the new greased cartridges rumored to be coated with cow/pig fat. The rebels then marched to Delhi.",
        "1857 का विद्रोह किस स्थान पर शुरू हुआ?",
        ["दिल्ली", "कानपुर", "मेरठ", "लखनऊ"],
        "1857 का विद्रोह 10 मई 1857 को मेरठ में शुरू हुआ जब सिपाहियों ने गाय/सूअर की चर्बी लगे नए कारतूसों का उपयोग करने से इनकार कर दिया। विद्रोही फिर दिल्ली की ओर बढ़े।"
    ),
    make_q(39, "A", "medium", 2024,
        "Who led the 1857 revolt at Kanpur?",
        ["Nana Sahib", "Tantia Tope", "Rani Lakshmibai", "Kunwar Singh"],
        "Nana Sahib (Dhondu Pant) led the revolt at Kanpur. He was the adopted son of the last Peshwa Baji Rao II. Tantia Tope was his military commander.",
        "कानपुर में 1857 के विद्रोह का नेतृत्व किसने किया?",
        ["नाना साहब", "तांत्या टोपे", "रानी लक्ष्मीबाई", "कुंवर सिंह"],
        "नाना साहब (धोंडू पंत) ने कानपुर में विद्रोह का नेतृत्व किया। वे अंतिम पेशवा बाजीराव द्वितीय के दत्तक पुत्र थे। तांत्या टोपे उनके सैन्य कमांडर थे।"
    ),
    make_q(40, "B", "easy", 2024,
        "Rani Lakshmibai was associated with which center of the 1857 revolt?",
        ["Kanpur", "Jhansi", "Delhi", "Bareilly"],
        "Rani Lakshmibai led the revolt at Jhansi. She died fighting British forces at Gwalior on June 17, 1858. She was one of the most prominent female leaders of the rebellion.",
        "रानी लक्ष्मीबाई 1857 के विद्रोह के किस केंद्र से जुड़ी थीं?",
        ["कानपुर", "झांसी", "दिल्ली", "बरेली"],
        "रानी लक्ष्मीबाई ने झांसी में विद्रोह का नेतृत्व किया। वे 17 जून 1858 को ग्वालियर में ब्रिटिश सेना से लड़ते हुए शहीद हुईं। वे विद्रोह की सबसे प्रमुख महिला नेत्रियों में से एक थीं।"
    ),
    # INC & Freedom Movement
    make_q(41, "A", "medium", 2024,
        "The Indian National Congress was founded in which year?",
        ["1885", "1890", "1900", "1882"],
        "The INC was founded on December 28, 1885 at Gokuldas Tejpal Sanskrit College in Bombay (Mumbai). The first session was presided over by W.C. Bonnerjee and attended by 72 delegates.",
        "भारतीय राष्ट्रीय कांग्रेस की स्थापना किस वर्ष हुई?",
        ["1885", "1890", "1900", "1882"],
        "INC की स्थापना 28 दिसंबर 1885 को बॉम्बे (मुंबई) के गोकुलदास तेजपाल संस्कृत कॉलेज में हुई। पहले अधिवेशन की अध्यक्षता डब्ल्यू.सी. बनर्जी ने की और 72 प्रतिनिधियों ने भाग लिया।"
    ),
    make_q(42, "D", "hard", 2023,
        "Who presided over the Lahore session of INC in 1929 where Purna Swaraj was declared?",
        ["Mahatma Gandhi", "Motilal Nehru", "Subhas Chandra Bose", "Jawaharlal Nehru"],
        "Jawaharlal Nehru presided over the historic Lahore session of INC in December 1929. The session passed the Purna Swaraj resolution, and January 26, 1930 was celebrated as the first Independence Day.",
        "1929 में INC के लाहौर अधिवेशन की अध्यक्षता किसने की जहां पूर्ण स्वराज की घोषणा हुई?",
        ["महात्मा गांधी", "मोतीलाल नेहरू", "सुभाष चंद्र बोस", "जवाहरलाल नेहरू"],
        "जवाहरलाल नेहरू ने दिसंबर 1929 में INC के ऐतिहासिक लाहौर अधिवेशन की अध्यक्षता की। इस अधिवेशन ने पूर्ण स्वराज प्रस्ताव पारित किया और 26 जनवरी 1930 को पहला स्वतंत्रता दिवस मनाया गया।"
    ),
    make_q(43, "C", "easy", 2024,
        "Who gave the slogan 'Do or Die' during the Quit India Movement?",
        ["Subhas Chandra Bose", "Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel"],
        "Mahatma Gandhi gave the slogan 'Do or Die' (Karo ya Maro) at the Bombay session of AICC on August 8, 1942, launching the Quit India Movement against British rule.",
        "भारत छोड़ो आंदोलन के दौरान 'करो या मरो' का नारा किसने दिया?",
        ["सुभाष चंद्र बोस", "जवाहरलाल नेहरू", "महात्मा गांधी", "सरदार पटेल"],
        "महात्मा गांधी ने 8 अगस्त 1942 को AICC के बॉम्बे अधिवेशन में 'करो या मरो' का नारा दिया, जिसने ब्रिटिश शासन के खिलाफ भारत छोड़ो आंदोलन शुरू किया।"
    ),
    make_q(44, "B", "medium", 2024,
        "The Dandi March (Salt Satyagraha) began on which date?",
        ["March 12, 1931", "March 12, 1930", "April 6, 1930", "April 12, 1930"],
        "The Dandi March began on March 12, 1930 from Sabarmati Ashram. Gandhi and 78 followers marched 241 miles to Dandi, reaching on April 6, 1930, where he broke the salt law.",
        "दांडी मार्च (नमक सत्याग्रह) किस तारीख को शुरू हुआ?",
        ["12 मार्च 1931", "12 मार्च 1930", "6 अप्रैल 1930", "12 अप्रैल 1930"],
        "दांडी मार्च 12 मार्च 1930 को साबरमती आश्रम से शुरू हुआ। गांधी और 78 अनुयायियों ने 241 मील पैदल चलकर 6 अप्रैल 1930 को दांडी पहुंचे, जहां उन्होंने नमक कानून तोड़ा।"
    ),
    make_q(45, "A", "hard", 2024,
        "Who founded the Indian National Army (INA) in 1942?",
        ["Subhas Chandra Bose", "Mohan Singh", "Rash Behari Bose", "Capt. Lakshmi Sahgal"],
        "The INA was first formed by Captain Mohan Singh in 1942 with Japanese help. Subhas Chandra Bose revived it in 1943, giving the famous call 'Give me blood, I will give you freedom'.",
        "1942 में भारतीय राष्ट्रीय सेना (INA) की स्थापना किसने की?",
        ["सुभाष चंद्र बोस", "मोहन सिंह", "रास बिहारी बोस", "कैप्टन लक्ष्मी सहगल"],
        "INA पहली बार 1942 में कैप्टन मोहन सिंह द्वारा जापानी सहायता से बनाई गई। सुभाष चंद्र बोस ने 1943 में इसे पुनर्जीवित किया और 'तुम मुझे खून दो, मैं तुम्हें आज़ादी दूंगा' का प्रसिद्ध आह्वान दिया।"
    ),
    # Partition & Independence
    make_q(46, "B", "easy", 2024,
        "Who was the Prime Minister of Britain when India got independence?",
        ["Winston Churchill", "Clement Attlee", "Neville Chamberlain", "Harold Macmillan"],
        "Clement Attlee was the British Prime Minister (Labour Party) when India gained independence in 1947. He sent the Cabinet Mission in 1946 and appointed Lord Mountbatten as the last Viceroy.",
        "भारत को स्वतंत्रता मिलने के समय ब्रिटेन के प्रधानमंत्री कौन थे?",
        ["विंस्टन चर्चिल", "क्लेमेंट एटली", "नेविल चैंबरलेन", "हेरोल्ड मैकमिलन"],
        "1947 में भारत को स्वतंत्रता मिलने के समय क्लेमेंट एटली (लेबर पार्टी) ब्रिटिश प्रधानमंत्री थे। उन्होंने 1946 में कैबिनेट मिशन भेजा और लॉर्ड माउंटबेटन को अंतिम वायसराय नियुक्त किया।"
    ),
    make_q(47, "C", "medium", 2024,
        "Who drew the Radcliffe Line that partitioned India and Pakistan?",
        ["Lord Mountbatten", "Stafford Cripps", "Cyril Radcliffe", "A.V. Alexander"],
        "Sir Cyril Radcliffe chaired the Boundary Commission that drew the Radcliffe Line on August 17, 1947, dividing Punjab and Bengal between India and Pakistan.",
        "भारत और पाकिस्तान को विभाजित करने वाली रैडक्लिफ रेखा किसने खींची?",
        ["लॉर्ड माउंटबेटन", "स्टैफोर्ड क्रिप्स", "सिरिल रैडक्लिफ", "ए.वी. अलेक्जेंडर"],
        "सर सिरिल रैडक्लिफ ने सीमा आयोग की अध्यक्षता की जिसने 17 अगस्त 1947 को रैडक्लिफ रेखा खींची, जो भारत और पाकिस्तान के बीच पंजाब और बंगाल का विभाजन करती थी।"
    ),
    make_q(48, "D", "medium", 2024,
        "Who was known as the 'Iron Man of India'?",
        ["Mahatma Gandhi", "Jawaharlal Nehru", "B.R. Ambedkar", "Sardar Vallabhbhai Patel"],
        "Sardar Vallabhbhai Patel is known as the Iron Man of India for his role in integrating over 560 princely states into the Indian Union after independence.",
        "भारत का लौह पुरुष किसे कहा जाता है?",
        ["महात्मा गांधी", "जवाहरलाल नेहरू", "बी.आर. अंबेडकर", "सरदार वल्लभभाई पटेल"],
        "स्वतंत्रता के बाद 560 से अधिक रियासतों को भारतीय संघ में शामिल करने की भूमिका के लिए सरदार वल्लभभाई पटेल को भारत का लौह पुरुष कहा जाता है।"
    ),
]
# Fill remaining IDs up to ~75 for indian-history (current max=10, need 65 new = IDs 11-75)
# We have 22 questions above (IDs 11-32). Need ~43 more to reach 65.
# IDs already used: 11-32. Let me continue...

# ... (continued in next section)
]

# The above is just the beginning. For the full implementation,
# I'll use a different approach - write all questions in a data file
# and process them.

print("Batch 1 script template created.")
print("This is a structural template - full content generation to follow.")
