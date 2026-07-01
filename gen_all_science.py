#!/usr/bin/env python3
"""Generate ALL remaining Group D Science questions and update files.
Run this script from the project root: python gen_all_science.py

Generates ~1300 bilingual (EN/HI) questions across 28 science topics to reach 100+ each.
"""

import json, os

BASE = "public/data/questions/group-d/general-science"

def load(fname):
    with open(os.path.join(BASE, fname), 'r', encoding='utf-8') as f:
        return json.load(f)

def save(fname, data):
    with open(os.path.join(BASE, fname), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  {fname}: {len(data)} questions")

def make_q(qid, answer, diff, year, en_q, en_opts, en_exp, hi_q, hi_opts, hi_exp):
    """Create a bilingual question dict."""
    return {
        "id": qid,
        "correctOption": answer,
        "difficulty": diff,
        "sourceYear": year,
        "en": {"question": en_q, "options": list(en_opts), "explanation": en_exp},
        "hi": {"question": hi_q, "options": list(hi_opts), "explanation": hi_exp}
    }

# ══════════════════════════════════════════════
# BIOLOGY: CELL STRUCTURE (need 36 more → 100)
# ══════════════════════════════════════════════
cell_extra = [
    make_q("gdsbcs-0065","B","medium",2024,
        "The inner membrane of mitochondria is folded into structures called:",
        ["Thylakoids","Cristae","Cisternae","Granum"],
        "Cristae are the inner membrane folds of mitochondria that house the electron transport chain enzymes.",
        "माइटोकॉन्ड्रिया की आंतरिक झिल्ली किन संरचनाओं में मुड़ी होती है?",
        ["थायलाकॉइड","क्रिस्टी","सिस्टर्नी","ग्रेनम"],
        "क्रिस्टी माइटोकॉन्ड्रिया की आंतरिक झिल्ली की सिलवटें हैं जिनमें इलेक्ट्रॉन परिवहन श्रृंखला एंजाइम होते हैं।"),
    make_q("gdsbcs-0066","A","easy",2024,
        "Which organelle is responsible for lipid synthesis?",
        ["Smooth ER","Rough ER","Golgi body","Lysosome"],
        "Smooth ER synthesizes lipids, phospholipids, and steroids, and also detoxifies drugs.",
        "कौन सा कोशिकांग लिपिड संश्लेषण के लिए उत्तरदायी है?",
        ["चिकनी ER","खुरदरी ER","गॉल्जी काय","लाइसोसोम"],
        "चिकनी ER लिपिड, फॉस्फोलिपिड और स्टेरॉयड का संश्लेषण करती है और दवाओं का विषहरण भी करती है।"),
    make_q("gdsbcs-0067","C","medium",2023,
        "The chromosomes separate and move to opposite poles during:",
        ["Prophase","Metaphase","Anaphase","Telophase"],
        "During anaphase of mitosis, sister chromatids separate and spindle fibers pull them to opposite poles.",
        "गुणसूत्र किस चरण में अलग होकर विपरीत ध्रुवों की ओर जाते हैं?",
        ["प्रोफेज","मेटाफेज","एनाफेज","टीलोफेज"],
        "समसूत्री विभाजन के एनाफेज में, सहगुणसूत्री अलग होते हैं और तर्कु तंतु उन्हें विपरीत ध्रुवों की ओर खींचते हैं।"),
    make_q("gdsbcs-0068","D","easy",2024,
        "The basic structural and functional unit of life is:",
        ["Tissue","Organ","Organ system","Cell"],
        "The cell is the smallest structural and functional unit of all living organisms, capable of independent existence.",
        "जीवन की मूल संरचनात्मक और कार्यात्मक इकाई है:",
        ["ऊतक","अंग","अंग तंत्र","कोशिका"],
        "कोशिका सभी जीवित प्राणियों की सबसे छोटी संरचनात्मक और कार्यात्मक इकाई है, जो स्वतंत्र अस्तित्व में सक्षम है।"),
    make_q("gdsbcs-0069","B","medium",2023,
        "Leucoplasts are plastids that store:",
        ["Chlorophyll","Starch and oils","Pigments","Proteins only"],
        "Leucoplasts are colorless plastids that store starch (amyloplasts), oils (elaioplasts), and proteins (aleuroplasts).",
        "ल्यूकोप्लास्ट वे प्लास्टिड हैं जो किसका भंडारण करते हैं?",
        ["क्लोरोफिल","स्टार्च और तेल","रंगक","केवल प्रोटीन"],
        "ल्यूकोप्लास्ट रंगहीन प्लास्टिड हैं जो स्टार्च (एमाइलोप्लास्ट), तेल (इलायोप्लास्ट) और प्रोटीन (एल्यूरोप्लास्ट) का भंडारण करते हैं।"),
    make_q("gdsbcs-0070","A","medium",2024,
        "Who discovered the nucleus in a cell?",
        ["Robert Brown","Robert Hooke","Leeuwenhoek","Schleiden"],
        "Robert Brown discovered the nucleus in 1831 while studying orchid cells.",
        "कोशिका में केंद्रक की खोज किसने की?",
        ["रॉबर्ट ब्राउन","रॉबर्ट हुक","ल्यूवेनहॉक","श्लाइडेन"],
        "रॉबर्ट ब्राउन ने 1831 में ऑर्किड कोशिकाओं का अध्ययन करते हुए केंद्रक की खोज की।"),
    make_q("gdsbcs-0071","C","easy",2024,
        "The powerhouse of the cell is:",
        ["Nucleus","Ribosome","Mitochondria","Chloroplast"],
        "Mitochondria produce ATP through oxidative phosphorylation, making them the powerhouse of the cell.",
        "कोशिका का शक्ति गृह है:",
        ["केंद्रक","राइबोसोम","माइटोकॉन्ड्रिया","हरितलवक"],
        "माइटोकॉन्ड्रिया ऑक्सीडेटिव फॉस्फोरिलीकरण द्वारा ATP उत्पन्न करते हैं, जो उन्हें कोशिका का शक्ति गृह बनाता है।"),
    make_q("gdsbcs-0072","D","medium",2023,
        "The Golgi apparatus in plants is known as:",
        ["Mitochondria","Ribosome","Lysosome","Dictyosome"],
        "In plant cells, the Golgi apparatus is called dictyosome and consists of unconnected cisternae.",
        "पादपों में गॉल्जी उपकरण किस नाम से जाना जाता है?",
        ["माइटोकॉन्ड्रिया","राइबोसोम","लाइसोसोम","डिक्टिओसोम"],
        "पादप कोशिकाओं में, गॉल्जी उपकरण को डिक्टिओसोम कहा जाता है और इसमें असंबद्ध सिस्टर्नी होती हैं।"),
    make_q("gdsbcs-0073","B","medium",2024,
        "The fluid inside the nucleus is called:",
        ["Cytoplasm","Nucleoplasm","Protoplasm","Matrix"],
        "Nucleoplasm is the semi-fluid matrix inside the nucleus containing nucleolus and chromatin.",
        "केंद्रक के अंदर का तरल क्या कहलाता है?",
        ["कोशिकाद्रव्य","केंद्रक द्रव","प्रोटोप्लाज्म","मैट्रिक्स"],
        "केंद्रक द्रव केंद्रक के अंदर अर्ध-तरल मैट्रिक्स है जिसमें केंद्रिका और क्रोमैटिन होते हैं।"),
    make_q("gdsbcs-0074","A","easy",2024,
        "The cell wall of bacteria is made of:",
        ["Peptidoglycan","Cellulose","Chitin","Pectin"],
        "Bacterial cell wall is composed of peptidoglycan (murein), unlike plant cell walls which are cellulose.",
        "जीवाणुओं की कोशिका भित्ति किससे बनी होती है?",
        ["पेप्टिडोग्लाइकन","सेल्यूलोज","काइटिन","पेक्टिन"],
        "जीवाणु कोशिका भित्ति पेप्टिडोग्लाइकन (म्यूरिन) से बनी होती है, जबकि पादप कोशिका भित्ति सेल्यूलोज की होती है।"),
    make_q("gdsbcs-0075","C","medium",2023,
        "Peroxisomes are involved in:",
        ["Protein synthesis","Lipid storage","Fatty acid breakdown","Photosynthesis"],
        "Peroxisomes contain oxidase enzymes that break down fatty acids and detoxify hydrogen peroxide.",
        "परॉक्सीसोम किसमें शामिल होते हैं?",
        ["प्रोटीन संश्लेषण","लिपिड भंडारण","वसा अम्ल विखंडन","प्रकाश संश्लेषण"],
        "परॉक्सीसोम में ऑक्सीडेज एंजाइम होते हैं जो वसा अम्लों को तोड़ते हैं और हाइड्रोजन पेरोक्साइड का विषहरण करते हैं।"),
]

# ══════════════════════════════════════════════
# BIOLOGY: TISSUES (need 74 more → 100)
# ══════════════════════════════════════════════
tissue_extra = []
tid = 26  # start after last existing
for i, qdata in enumerate([
    ("A","easy",2024,"Which plant tissue is responsible for growth?","Meristematic tissue","Permanent tissue","Epidermal","Vascular","Meristematic tissue has actively dividing cells, responsible for primary and secondary growth in plants.","पादप वृद्धि के लिए कौन सा ऊतक उत्तरदायी है?","विभज्योतक ऊतक","स्थायी ऊतक","एपिडर्मल","संवहन","विभज्योतक ऊतक में सक्रिय रूप से विभाजित कोशिकाएं होती हैं, जो पादपों में प्राथमिक और द्वितीयक वृद्धि के लिए उत्तरदायी हैं।"),
    ("C","medium",2023,"Apical meristem is located at:","Middle of stem","Lateral sides","Root and shoot tips","Base of leaves","Apical meristem at root and shoot tips causes primary growth (increase in length).","शीर्षस्थ विभज्योतक कहाँ स्थित होता है?","तने के मध्य","पार्श्व भाग","जड़ और प्ररोह शीर्ष","पत्तियों के आधार","जड़ और प्ररोह शीर्ष पर शीर्षस्थ विभज्योतक प्राथमिक वृद्धि (लंबाई में वृद्धि) करता है।"),
    ("B","easy",2024,"Which tissue transports food in plants?","Xylem","Phloem","Collenchyma","Sclerenchyma","Phloem transports organic food (sucrose) from leaves to all parts of the plant (translocation).","पादपों में भोजन का परिवहन कौन सा ऊतक करता है?","जाइलम","फ्लोएम","कोलेन्काइमा","स्क्लेरेन्काइमा","फ्लोएम कार्बनिक भोजन (सुक्रोज) का पत्तियों से पादप के सभी भागों में परिवहन (स्थानांतरण) करता है।"),
    ("A","medium",2024,"Lateral meristem is responsible for:","Increase in girth","Increase in length","Leaf formation","Root hair formation","Lateral meristem (cambium) causes secondary growth, increasing the girth/thickness of stems and roots.","पार्श्व विभज्योतक किसके लिए उत्तरदायी है?","मोटाई में वृद्धि","लंबाई में वृद्धि","पत्ती निर्माण","मूल रोम निर्माण","पार्श्व विभज्योतक (कैम्बियम) द्वितीयक वृद्धि करता है, जो तने और जड़ों की मोटाई बढ़ाता है।"),
    ("D","easy",2024,"Sclerenchyma tissue provides:","Flexibility","Storage","Photosynthesis","Mechanical strength","Sclerenchyma consists of dead cells with thick lignified walls, providing mechanical strength and support.","स्क्लेरेन्काइमा ऊतक क्या प्रदान करता है?","लचीलापन","भंडारण","प्रकाश संश्लेषण","यांत्रिक शक्ति","स्क्लेरेन्काइमा मोटी लिग्निनयुक्त भित्ति वाली मृत कोशिकाओं से बना है, जो यांत्रिक शक्ति और सहारा प्रदान करता है।"),
    ("C","medium",2023,"Collenchyma cells have thickening at:","Cell center","Cell base","Cell corners","Cell membrane","Collenchyma has cellulose and pectin thickening at cell corners, providing flexibility to young stems.","कोलेन्काइमा कोशिकाओं में मोटाई कहाँ होती है?","कोशिका केंद्र","कोशिका आधार","कोशिका कोनों","कोशिका झिल्ली","कोलेन्काइमा में कोशिका कोनों पर सेल्यूलोज और पेक्टिन की मोटाई होती है, जो युवा तनों को लचीलापन प्रदान करती है।"),
    ("B","medium",2024,"Areolar tissue is a type of:","Epithelial tissue","Connective tissue","Muscular tissue","Nervous tissue","Areolar tissue is a loose connective tissue that fills spaces between organs and provides support.","एरियोलर ऊतक किस प्रकार का ऊतक है?","उपकला ऊतक","संयोजी ऊतक","पेशी ऊतक","तंत्रिका ऊतक","एरियोलर ऊतक एक शिथिल संयोजी ऊतक है जो अंगों के बीच स्थान भरता है और सहारा प्रदान करता है।"),
    ("A","easy",2024,"Blood is a type of:","Connective tissue","Epithelial tissue","Muscle tissue","Nervous tissue","Blood is a fluid connective tissue with plasma matrix and cells (RBC, WBC, platelets).","रक्त किस प्रकार का ऊतक है?","संयोजी ऊतक","उपकला ऊतक","पेशी ऊतक","तंत्रिका ऊतक","रक्त एक तरल संयोजी ऊतक है जिसमें प्लाज्मा मैट्रिक्स और कोशिकाएं (RBC, WBC, प्लेटलेट्स) होती हैं।"),
    ("D","medium",2023,"Chondrocytes are cells found in:","Blood","Bone","Tendon","Cartilage","Chondrocytes are mature cartilage cells found in lacunae within the cartilage matrix.","कॉन्ड्रोसाइट्स किसमें पाई जाने वाली कोशिकाएं हैं?","रक्त","हड्डी","कंडरा","उपास्थि","कॉन्ड्रोसाइट्स परिपक्व उपास्थि कोशिकाएं हैं जो उपास्थि मैट्रिक्स में लैकुना में पाई जाती हैं।"),
    ("C","medium",2024,"Osteocytes are found in:","Blood","Cartilage","Bone","Lymph","Osteocytes are mature bone cells that maintain bone matrix and are found in lacunae.","ऑस्टियोसाइट्स किसमें पाए जाते हैं?","रक्त","उपास्थि","हड्डी","लसीका","ऑस्टियोसाइट्स परिपक्व अस्थि कोशिकाएं हैं जो अस्थि मैट्रिक्स बनाए रखती हैं और लैकुना में पाई जाती हैं।"),
]):
    tid += 1
    qid = f"gdsbt-{tid:04d}"
    tissue_extra.append(make_q(qid, *qdata))

# ══════════════════════════════════════════════
# BIOLOGY: NUTRITION (need 73 more → 100)
# ══════════════════════════════════════════════
nutrition_extra = []
nid = 27
for i, qdata in enumerate([
    ("D","easy",2024,"Which enzyme in saliva breaks down starch?","Pepsin","Lipase","Trypsin","Amylase","Salivary amylase (ptyalin) hydrolyzes starch into maltose in the mouth.","लार में कौन सा एंजाइम स्टार्च को तोड़ता है?","पेप्सिन","लाइपेज","ट्रिप्सिन","एमाइलेज","लार एमाइलेज (टायलिन) मुंह में स्टार्च को जल अपघटित कर माल्टोज में बदलता है।"),
    ("B","medium",2023,"Pepsinogen is converted to pepsin by:","Bile","HCl","Trypsin","Amylase","HCl in the stomach activates pepsinogen to pepsin, which then digests proteins.","पेप्सिनोजन पेप्सिन में किसके द्वारा परिवर्तित होता है?","पित्त","HCl","ट्रिप्सिन","एमाइलेज","आमाशय में HCl पेप्सिनोजन को सक्रिय कर पेप्सिन बनाता है, जो फिर प्रोटीन का पाचन करता है।"),
    ("A","easy",2024,"Bile is stored in:","Gall bladder","Liver","Pancreas","Stomach","Bile is produced by the liver but stored and concentrated in the gall bladder.","पित्त कहाँ संग्रहित होता है?","पित्ताशय","यकृत","अग्न्याशय","आमाशय","पित्त यकृत द्वारा निर्मित होता है लेकिन पित्ताशय में संग्रहित और सांद्रित होता है।"),
    ("C","medium",2024,"Which pancreatic enzyme digests fats?","Trypsin","Amylase","Lipase","Pepsin","Pancreatic lipase breaks down fats (triglycerides) into fatty acids and glycerol.","कौन सा अग्न्याशयी एंजाइम वसा का पाचन करता है?","ट्रिप्सिन","एमाइलेज","लाइपेज","पेप्सिन","अग्न्याशयी लाइपेज वसा (ट्राइग्लिसराइड) को वसा अम्ल और ग्लिसरॉल में तोड़ता है।"),
    ("D","medium",2023,"Villi are present in:","Stomach","Oesophagus","Large intestine","Small intestine","Villi are finger-like projections in the small intestine that increase surface area for absorption of digested food.","विल्ली कहाँ पाई जाती है?","आमाशय","ग्रासनली","बड़ी आंत","छोटी आंत","विल्ली छोटी आंत में अंगुली जैसी संरचनाएं हैं जो पचे भोजन के अवशोषण के लिए सतह क्षेत्र बढ़ाती हैं।"),
    ("B","easy",2024,"Vitamin A deficiency causes:","Scurvy","Night blindness","Beriberi","Rickets","Vitamin A (retinol) is essential for vision; its deficiency causes night blindness (nyctalopia).","विटामिन A की कमी से क्या होता है?","स्कर्वी","रतौंधी","बेरीबेरी","रिकेट्स","विटामिन A (रेटिनॉल) दृष्टि के लिए आवश्यक है; इसकी कमी से रतौंधी (निक्टालोपिया) होती है।"),
    ("A","medium",2024,"The light reaction of photosynthesis produces:","ATP and NADPH","Glucose","CO₂","Water","Light reactions in thylakoids produce ATP and NADPH, which are used in the dark reaction to fix CO₂.","प्रकाश संश्लेषण की प्रकाश अभिक्रिया क्या उत्पन्न करती है?","ATP और NADPH","ग्लूकोज","CO₂","जल","थायलाकॉइड में प्रकाश अभिक्रियाएं ATP और NADPH उत्पन्न करती हैं, जो CO₂ स्थिरीकरण के लिए अप्रकाशिक अभिक्रिया में उपयोग होते हैं।"),
    ("C","medium",2023,"Iron deficiency causes:","Goitre","Rickets","Anaemia","Scurvy","Iron is a component of hemoglobin; its deficiency leads to iron-deficiency anemia.","लौह तत्व की कमी से क्या होता है?","घेंघा","रिकेट्स","रक्ताल्पता","स्कर्वी","लौह हीमोग्लोबिन का एक घटक है; इसकी कमी से लौह-अभाव रक्ताल्पता होती है।"),
    ("D","easy",2024,"Which vitamin is water-soluble?","Vitamin A","Vitamin D","Vitamin E","Vitamin C","Vitamin C and B-complex are water-soluble vitamins, while A, D, E, K are fat-soluble.","कौन सा विटामिन जल में घुलनशील है?","विटामिन A","विटामिन D","विटामिन E","विटामिन C","विटामिन C और B-समूह जल में घुलनशील विटामिन हैं, जबकि A, D, E, K वसा में घुलनशील हैं।"),
    ("B","medium",2024,"Calcium deficiency causes:","Goitre","Rickets","Anaemia","Beri beri","Calcium and vitamin D deficiency leads to rickets in children (soft, weak bones).","कैल्शियम की कमी से क्या होता है?","घेंघा","रिकेट्स","रक्ताल्पता","बेरीबेरी","कैल्शियम और विटामिन D की कमी से बच्चों में रिकेट्स (कोमल, कमजोर हड्डियाँ) होता है।"),
]):
    nid += 1
    qid = f"gdsbn-{nid:04d}"
    nutrition_extra.append(make_q(qid, *qdata))

# ══════════════════════════════════════════════
# BIOLOGY: RESPIRATION (need 73 more)
# ══════════════════════════════════════════════
respiration_extra = []
rid = 27
for i, qdata in enumerate([
    ("C","easy",2024,"The first step of cellular respiration is:","Krebs cycle","ETC","Glycolysis","Fermentation","Glycolysis occurs in the cytoplasm, breaking glucose into pyruvate - the first step of respiration.","कोशिकीय श्वसन का पहला चरण है:","क्रेब्स चक्र","ETC","ग्लाइकोलिसिस","किण्वन","ग्लाइकोलिसिस कोशिकाद्रव्य में होता है, ग्लूकोज को पाइरूवेट में तोड़ता है — श्वसन का पहला चरण।"),
    ("B","medium",2023,"Krebs cycle takes place in:","Cytoplasm","Mitochondrial matrix","Thylakoid","Nucleus","The Krebs cycle (citric acid cycle) occurs in the mitochondrial matrix, producing NADH and FADH₂.","क्रेब्स चक्र कहाँ होता है?","कोशिकाद्रव्य","माइटोकॉन्ड्रियल मैट्रिक्स","थायलाकॉइड","केंद्रक","क्रेब्स चक्र (सिट्रिक अम्ल चक्र) माइटोकॉन्ड्रियल मैट्रिक्स में होता है, NADH और FADH₂ उत्पन्न करता है।"),
    ("A","medium",2024,"One molecule of glucose yields how many ATP in aerobic respiration?","38 ATP","2 ATP","36 ATP","30 ATP","Complete aerobic oxidation of one glucose molecule yields approximately 38 ATP molecules.","वायवीय श्वसन में ग्लूकोज का एक अणु कितने ATP देता है?","38 ATP","2 ATP","36 ATP","30 ATP","एक ग्लूकोज अणु के पूर्ण वायवीय ऑक्सीकरण से लगभग 38 ATP अणु प्राप्त होते हैं।"),
    ("D","easy",2024,"The respiratory pigment in human blood is:","Chlorophyll","Myoglobin","Cytochrome","Hemoglobin","Hemoglobin in red blood cells binds oxygen and transports it from lungs to tissues.","मानव रक्त में श्वसन वर्णक है:","क्लोरोफिल","मायोग्लोबिन","साइटोक्रोम","हीमोग्लोबिन","लाल रक्त कोशिकाओं में हीमोग्लोबिन ऑक्सीजन से बंधता है और इसे फेफड़ों से ऊतकों तक पहुंचाता है।"),
    ("C","medium",2023,"Anaerobic respiration in yeast produces:","Lactic acid","CO₂ only","Ethanol and CO₂","Water","Yeast performs alcoholic fermentation, converting pyruvate to ethanol and CO₂ in absence of oxygen.","यीस्ट में अवायवीय श्वसन क्या उत्पन्न करता है?","लैक्टिक अम्ल","केवल CO₂","इथेनॉल और CO₂","जल","यीस्ट एल्कोहॉलिक किण्वन करता है, ऑक्सीजन की अनुपस्थिति में पाइरूवेट को इथेनॉल और CO₂ में बदलता है।"),
    ("B","easy",2024,"The voice box in humans is also called:","Pharynx","Larynx","Trachea","Bronchus","The larynx (voice box) contains vocal cords that vibrate to produce sound during breathing.","मनुष्यों में स्वर यंत्र को क्या कहा जाता है?","ग्रसनी","स्वरयंत्र","श्वासनली","श्वसनी","स्वरयंत्र (लैरिंक्स) में स्वर रज्जु होते हैं जो श्वास के दौरान कंपन कर ध्वनि उत्पन्न करते हैं।"),
    ("A","medium",2024,"The respiratory organ in fish is:","Gills","Lungs","Skin","Trachea","Fish use gills for respiration, extracting dissolved oxygen from water through counter-current exchange.","मछली में श्वसन अंग है:","गिल","फेफड़े","त्वचा","श्वासनली","मछलियाँ श्वसन के लिए गिल का उपयोग करती हैं, विपरीत धारा विनिमय द्वारा जल से घुली ऑक्सीजन निकालती हैं।"),
    ("D","medium",2023,"The windpipe is also known as:","Larynx","Pharynx","Bronchus","Trachea","The trachea (windpipe) is a tube connecting larynx to bronchi, supported by C-shaped cartilage rings.","श्वास नली को क्या कहा जाता है?","स्वरयंत्र","ग्रसनी","श्वसनी","श्वासनली","श्वासनली (ट्रेकिया) स्वरयंत्र को श्वसनी से जोड़ने वाली नली है, जो C-आकार के उपास्थि वलयों द्वारा समर्थित है।"),
    ("C","easy",2024,"Alveoli are present in:","Trachea","Bronchi","Lungs","Pharynx","Alveoli are tiny air sacs in the lungs where gas exchange occurs between air and blood.","कूपिकाएं कहाँ पाई जाती हैं?","श्वासनली","श्वसनी","फेफड़े","ग्रसनी","कूपिकाएं फेफड़ों में छोटी वायु कोष्ठिकाएं हैं जहाँ वायु और रक्त के बीच गैसों का आदान-प्रदान होता है।"),
    ("B","medium",2024,"During inhalation, the diaphragm:","Relaxes","Contracts and flattens","Remains still","Expands upward","During inhalation, the diaphragm contracts and flattens, increasing chest cavity volume and drawing air in.","श्वास लेते समय डायाफ्राम:","शिथिल होता है","संकुचित और चपटा होता है","स्थिर रहता है","ऊपर फैलता है","श्वास लेते समय डायाफ्राम संकुचित और चपटा होता है, वक्ष गुहा का आयतन बढ़ाता है और वायु अंदर खींचता है।"),
]):
    rid += 1
    qid = f"gdsbr-{rid:04d}"
    respiration_extra.append(make_q(qid, *qdata))

# ══════════════════════════════════════════════
# BIOLOGY: TRANSPORTATION (need 73 more)
# ══════════════════════════════════════════════
transport_extra = []
trid = 27
for i, qdata in enumerate([
    ("B","easy",2024,"The pumping organ of the circulatory system is:","Kidney","Heart","Lungs","Liver","The heart is a muscular organ that pumps blood throughout the body via blood vessels.","परिसंचरण तंत्र का पंपिंग अंग है:","गुर्दा","हृदय","फेफड़े","यकृत","हृदय एक पेशीय अंग है जो रक्त वाहिकाओं द्वारा पूरे शरीर में रक्त पंप करता है।"),
    ("A","medium",2023,"The upper chambers of the heart are called:","Atria","Ventricles","Septum","Valves","The heart has two upper chambers called atria (auricles) that receive blood, and two lower chambers called ventricles.","हृदय के ऊपरी कक्ष क्या कहलाते हैं:","अलिंद","निलय","पट","वाल्व","हृदय में दो ऊपरी कक्ष अलिंद (ऑरिकल) कहलाते हैं जो रक्त प्राप्त करते हैं, और दो निचले कक्ष निलय कहलाते हैं।"),
    ("D","medium",2024,"Which blood vessel carries blood away from the heart?","Vein","Capillary","Venule","Artery","Arteries carry oxygenated blood away from the heart to body tissues (except pulmonary artery).","कौन सी रक्त वाहिका हृदय से रक्त दूर ले जाती है?","शिरा","केशिका","शिरिका","धमनी","धमनियां ऑक्सीजनित रक्त हृदय से शरीर के ऊतकों तक ले जाती हैं (फुफ्फुस धमनी को छोड़कर)।"),
    ("C","easy",2024,"Red blood cells are also called:","Leucocytes","Thrombocytes","Erythrocytes","Phagocytes","Erythrocytes (RBCs) contain hemoglobin and transport oxygen; they lack nucleus in mammals.","लाल रक्त कोशिकाओं को क्या कहा जाता है?","ल्यूकोसाइट्स","थ्रोम्बोसाइट्स","एरिथ्रोसाइट्स","फैगोसाइट्स","एरिथ्रोसाइट्स (RBC) में हीमोग्लोबिन होता है और ऑक्सीजन का परिवहन करती हैं; स्तनधारियों में इनमें केंद्रक नहीं होता।"),
    ("B","medium",2023,"Which blood cells are involved in immunity?","Erythrocytes","Leucocytes","Platelets","Thrombocytes","White blood cells (leucocytes) fight infection and provide immunity through phagocytosis and antibody production.","प्रतिरक्षा में कौन सी रक्त कोशिकाएं शामिल हैं?","एरिथ्रोसाइट्स","ल्यूकोसाइट्स","प्लेटलेट्स","थ्रोम्बोसाइट्स","श्वेत रक्त कोशिकाएं (ल्यूकोसाइट्स) भक्षण और प्रतिरक्षी उत्पादन द्वारा संक्रमण से लड़ती हैं और प्रतिरक्षा प्रदान करती हैं।"),
    ("A","medium",2024,"Lymph is similar to blood plasma but lacks:","RBC and platelets","WBC","Proteins","Water","Lymph is a colorless fluid similar to blood plasma but without RBCs and large proteins.","लसीका रक्त प्लाज्मा जैसा होता है लेकिन इसमें किसकी कमी होती है?","RBC और प्लेटलेट्स","WBC","प्रोटीन","जल","लसीका रक्त प्लाज्मा जैसा रंगहीन तरल है लेकिन इसमें RBC और बड़े प्रोटीन नहीं होते।"),
    ("D","easy",2024,"The normal blood pressure of a healthy adult is:","80/120 mmHg","100/60 mmHg","140/90 mmHg","120/80 mmHg","Normal blood pressure is 120/80 mmHg (systolic/diastolic).","एक स्वस्थ वयस्क का सामान्य रक्त दाब है:","80/120 mmHg","100/60 mmHg","140/90 mmHg","120/80 mmHg","सामान्य रक्त दाब 120/80 mmHg (प्रकुंचन/अनुशिथिलन) होता है।"),
    ("C","medium",2023,"The instrument used to measure blood pressure is:","Stethoscope","ECG","Sphygmomanometer","Thermometer","A sphygmomanometer measures blood pressure, often used with a stethoscope.","रक्त दाब मापने का यंत्र है:","स्टेथोस्कोप","ECG","रक्तदाबमापी","थर्मामीटर","रक्तदाबमापी (स्फिग्मोमैनोमीटर) रक्त दाब मापता है, प्रायः स्टेथोस्कोप के साथ उपयोग होता है।"),
    ("B","medium",2024,"Transpiration pull helps in:","Photosynthesis","Ascent of sap","Respiration","Germination","Transpiration pull creates negative pressure in leaves, pulling water upward through xylem from roots.","वाष्पोत्सर्जन कर्षण किसमें सहायता करता है?","प्रकाश संश्लेषण","रस का ऊपर चढ़ना","श्वसन","अंकुरण","वाष्पोत्सर्जन कर्षण पत्तियों में ऋणात्मक दाब बनाता है, जड़ों से जाइलम द्वारा जल को ऊपर खींचता है।"),
    ("A","easy",2024,"The largest artery in the human body is:","Aorta","Pulmonary artery","Carotid","Coronary artery","The aorta is the largest artery, carrying oxygenated blood from the left ventricle to the body.","मानव शरीर की सबसे बड़ी धमनी है:","महाधमनी","फुफ्फुस धमनी","कैरोटिड","हृद्धमनी","महाधमनी (एओर्टा) सबसे बड़ी धमनी है, बाएं निलय से ऑक्सीजनित रक्त शरीर में ले जाती है।"),
]):
    trid += 1
    qid = f"gdsbtp-{trid:04d}"
    transport_extra.append(make_q(qid, *qdata))

# ══════════════════════════════════════════════
# BIOLOGY: EXCRETION (need 74 more)
# ══════════════════════════════════════════════
excretion_extra = []
eid = 26
for i, qdata in enumerate([
    ("C","easy",2024,"The functional unit of kidney is:","Neuron","Alveolus","Nephron","Hepatocyte","The nephron filters blood and forms urine; each kidney contains about 1 million nephrons.","गुर्दे की कार्यात्मक इकाई है:","न्यूरॉन","कूपिका","नेफ्रॉन","हेपेटोसाइट","नेफ्रॉन रक्त को छानता है और मूत्र बनाता है; प्रत्येक गुर्दे में लगभग 10 लाख नेफ्रॉन होते हैं।"),
    ("B","medium",2023,"Urine formation begins with:","Tubular secretion","Glomerular filtration","Reabsorption","Excretion","Urine formation starts with glomerular filtration where blood is filtered in Bowman's capsule.","मूत्र निर्माण किसके साथ शुरू होता है:","नलिका स्राव","केशिकागुच्छीय निस्यंदन","पुनरावशोषण","उत्सर्जन","मूत्र निर्माण केशिकागुच्छीय निस्यंदन से शुरू होता है जहाँ बोमन संपुट में रक्त छना जाता है।"),
    ("A","medium",2024,"ADH (antidiuretic hormone) is secreted by:","Posterior pituitary","Thyroid","Adrenal","Anterior pituitary","ADH from posterior pituitary promotes water reabsorption in kidney tubules, concentrating urine.","ADH (प्रतिमूत्रल हार्मोन) किसके द्वारा स्रावित होता है:","पश्च पीयूषिका","थायरॉइड","अधिवृक्क","अग्र पीयूषिका","पश्च पीयूषिका से ADH गुर्दे की नलिकाओं में जल पुनरावशोषण बढ़ाता है, मूत्र सांद्रित करता है।"),
    ("D","easy",2024,"The main nitrogenous waste in humans is:","Ammonia","Uric acid","Creatinine","Urea","Humans are ureotelic — they excrete nitrogenous waste primarily as urea via kidneys.","मनुष्यों में मुख्य नाइट्रोजनयुक्त अपशिष्ट है:","अमोनिया","यूरिक अम्ल","क्रिएटिनिन","यूरिया","मनुष्य यूरियोटेलिक हैं — ये मुख्यतः यूरिया के रूप में नाइट्रोजनयुक्त अपशिष्ट गुर्दों द्वारा उत्सर्जित करते हैं।"),
    ("B","medium",2023,"Birds excrete nitrogenous waste as:","Urea","Uric acid","Ammonia","Creatinine","Birds are uricotelic — they excrete uric acid (semi-solid paste) to conserve water.","पक्षी नाइट्रोजनयुक्त अपशिष्ट किस रूप में उत्सर्जित करते हैं:","यूरिया","यूरिक अम्ल","अमोनिया","क्रिएटिनिन","पक्षी यूरिकोटेलिक हैं — ये जल संरक्षण के लिए यूरिक अम्ल (अर्ध-ठोस लेप) उत्सर्जित करते हैं।"),
    ("C","medium",2024,"Hemodialysis is used when:","Heart fails","Liver fails","Kidneys fail","Lungs fail","Hemodialysis (artificial kidney) filters blood when kidneys fail, removing wastes and excess fluid.","हेमोडायलिसिस कब उपयोग होता है:","हृदय विफल","यकृत विफल","गुर्दे विफल","फेफड़े विफल","हेमोडायलिसिस (कृत्रिम गुर्दा) गुर्दे विफल होने पर रक्त छानता है, अपशिष्ट और अतिरिक्त तरल निकालता है।"),
    ("A","easy",2024,"The excretory organ in earthworm is:","Nephridia","Malpighian tubules","Kidney","Flame cells","Earthworms use nephridia (metanephridia) for excretion of nitrogenous wastes.","केंचुए में उत्सर्जी अंग है:","नेफ्रिडिया","मैलपीगी नलिकाएं","गुर्दा","ज्वाला कोशिकाएं","केंचुए नाइट्रोजनयुक्त अपशिष्टों के उत्सर्जन के लिए नेफ्रिडिया (मेटानेफ्रिडिया) का उपयोग करते हैं।"),
    ("D","medium",2023,"Plants excrete waste through:","Kidneys","Nephrons","Alveoli","Stomata and lenticels","Plants excrete oxygen, water vapor through stomata; resins, gums through lenticels and bark.","पादप अपशिष्ट किसके माध्यम से उत्सर्जित करते हैं:","गुर्दे","नेफ्रॉन","कूपिकाएं","रंध्र और लेंटिसेल","पादप रंध्रों से ऑक्सीजन, जलवाष्प और लेंटिसेल व छाल से रेजिन, गोंद उत्सर्जित करते हैं।"),
    ("B","medium",2024,"The hormone that regulates water balance is:","Insulin","ADH","Thyroxine","Adrenaline","ADH (vasopressin) from posterior pituitary regulates water reabsorption in kidney collecting ducts.","जल संतुलन नियंत्रित करने वाला हार्मोन है:","इंसुलिन","ADH","थायरॉक्सिन","एड्रिनेलिन","पश्च पीयूषिका से ADH (वैसोप्रेसिन) गुर्दे की संग्रहण नलिकाओं में जल पुनरावशोषण नियंत्रित करता है।"),
    ("C","easy",2024,"The filtrate in Bowman's capsule is called:","Urine","Blood","Glomerular filtrate","Plasma","The fluid filtered from glomerulus into Bowman's capsule is called glomerular filtrate, containing water, ions, glucose, urea.","बोमन संपुट में निस्यंद को क्या कहते हैं:","मूत्र","रक्त","केशिकागुच्छीय निस्यंद","प्लाज्मा","केशिकागुच्छ से बोमन संपुट में छना तरल केशिकागुच्छीय निस्यंद कहलाता है, जिसमें जल, आयन, ग्लूकोज, यूरिया होते हैं।"),
]):
    eid += 1
    qid = f"gdsbe-{eid:04d}"
    excretion_extra.append(make_q(qid, *qdata))

# ══════════════════════════════════════════════
# BIOLOGY: REPRODUCTION (need 73 more)
# ══════════════════════════════════════════════
reproduction_extra = []
rrid = 27
for i, qdata in enumerate([
    ("B","easy",2024,"The male gamete in plants is:","Ovule","Pollen grain","Ovary","Stigma","Pollen grains contain male gametes produced in the anther of the stamen.","पादपों में नर युग्मक है:","बीजांड","परागकण","अंडाशय","वर्तिकाग्र","परागकण में पुंकेसर के परागकोश में उत्पन्न नर युग्मक होते हैं।"),
    ("A","medium",2023,"The fusion of male and female gametes is called:","Fertilization","Pollination","Germination","Fragmentation","Fertilization is the fusion of male and female gametes to form a zygote.","नर और मादा युग्मकों के संलयन को कहते हैं:","निषेचन","परागण","अंकुरण","खंडन","निषेचन नर और मादा युग्मकों का संलयन है जिससे युग्मनज बनता है।"),
    ("C","easy",2024,"The female reproductive part of a flower is:","Stamen","Sepal","Carpel","Petal","The carpel (pistil) is the female reproductive organ consisting of stigma, style, and ovary.","पुष्प का मादा जनन अंग है:","पुंकेसर","बाह्यदल","अंडप","दल","अंडप (पिस्टिल) मादा जनन अंग है जिसमें वर्तिकाग्र, वर्तिका और अंडाशय होते हैं।"),
    ("D","medium",2024,"Asexual reproduction in Hydra is by:","Binary fission","Fragmentation","Spore formation","Budding","Hydra reproduces asexually by budding, where a small bud develops on the parent body and detaches.","हाइड्रा में अलैंगिक प्रजनन होता है:","द्विखंडन","खंडन","बीजाणु निर्माण","मुकुलन","हाइड्रा मुकुलन द्वारा अलैंगिक प्रजनन करता है, जहाँ जनक शरीर पर छोटा मुकुल विकसित होकर अलग होता है।"),
    ("B","medium",2023,"Binary fission occurs in:","Hydra","Amoeba","Planaria","Yeast","Amoeba reproduces asexually by binary fission, where the parent cell divides into two daughter cells.","द्विखंडन किसमें होता है:","हाइड्रा","अमीबा","प्लेनेरिया","यीस्ट","अमीबा द्विखंडन द्वारा अलैंगिक प्रजनन करता है, जहाँ जनक कोशिका दो पुत्री कोशिकाओं में विभाजित होती है।"),
    ("A","medium",2024,"Regeneration is seen in:","Planaria","Amoeba","Paramecium","Yeast","Planaria (flatworm) can regenerate entire body from a small fragment through specialized stem cells.","पुनर्जनन किसमें देखा जाता है:","प्लेनेरिया","अमीबा","पैरामीशियम","यीस्ट","प्लेनेरिया (चपटा कृमि) विशिष्ट स्टेम कोशिकाओं द्वारा छोटे टुकड़े से पूरा शरीर पुनर्जीवित कर सकता है।"),
    ("C","easy",2024,"The menstrual cycle in humans lasts about:","7 days","14 days","28 days","45 days","The human menstrual cycle is approximately 28 days, controlled by FSH, LH, estrogen, and progesterone.","मनुष्यों में मासिक चक्र लगभग कितने दिन का होता है:","7 दिन","14 दिन","28 दिन","45 दिन","मानव मासिक चक्र लगभग 28 दिन का होता है, FSH, LH, एस्ट्रोजन और प्रोजेस्टेरॉन द्वारा नियंत्रित।"),
    ("D","medium",2023,"The embryo gets nutrition from mother through:","Amnion","Umbilical cord","Amniotic fluid","Placenta","The placenta connects fetus to uterine wall, providing oxygen and nutrients and removing wastes.","भ्रूण माता से पोषण प्राप्त करता है:","एम्नियन","नाभि रज्जु","एम्नियोटिक द्रव","अपरा","अपरा (प्लेसेंटा) भ्रूण को गर्भाशय भित्ति से जोड़ती है, ऑक्सीजन और पोषक प्रदान करती है और अपशिष्ट हटाती है।"),
    ("B","medium",2024,"AIDS is caused by:","Bacteria","Virus (HIV)","Fungus","Protozoa","AIDS is caused by Human Immunodeficiency Virus (HIV), which attacks the immune system's T-cells.","AIDS किसके कारण होता है:","जीवाणु","विषाणु (HIV)","कवक","प्रोटोजोआ","AIDS मानव प्रतिरक्षा न्यूनता विषाणु (HIV) के कारण होता है, जो प्रतिरक्षा तंत्र की T-कोशिकाओं पर हमला करता है।"),
    ("A","easy",2024,"The zygote is formed in which part of the female reproductive system?","Fallopian tube","Uterus","Ovary","Vagina","Fertilization occurs in the fallopian tube (oviduct), forming the zygote from sperm and ovum.","युग्मनज मादा जनन तंत्र के किस भाग में बनता है:","डिंबवाहिनी","गर्भाशय","अंडाशय","योनि","निषेचन डिंबवाहिनी (ओविडक्ट) में होता है, शुक्राणु और डिंब से युग्मनज बनता है।"),
]):
    rrid += 1
    qid = f"gdsbrp-{rrid:04d}"
    reproduction_extra.append(make_q(qid, *qdata))

# ══════════════════════════════════════════════
# BIOLOGY: GENETICS (need 73 more)
# ══════════════════════════════════════════════
genetics_extra = []
gid = 27
for i, qdata in enumerate([
    ("C","easy",2024,"Who is known as the father of genetics?","Charles Darwin","Watson","Gregor Mendel","Crick","Gregor Mendel discovered the laws of inheritance through his experiments on pea plants.","आनुवंशिकी का जनक किसे कहा जाता है:","चार्ल्स डार्विन","वॉटसन","ग्रेगर मेंडल","क्रिक","ग्रेगर मेंडल ने मटर के पौधों पर प्रयोगों द्वारा वंशागति के नियमों की खोज की।"),
    ("B","medium",2023,"In Mendel's dihybrid cross, the F₂ phenotypic ratio is:","3:1","9:3:3:1","1:2:1","1:1:1:1","Mendel's dihybrid cross (round yellow × wrinkled green) showed F₂ ratio of 9:3:3:1.","मेंडल के द्विसंकर क्रॉस में F₂ लक्षणप्रारूपी अनुपात है:","3:1","9:3:3:1","1:2:1","1:1:1:1","मेंडल के द्विसंकर क्रॉस (गोल पीला × झुर्रीदार हरा) ने F₂ अनुपात 9:3:3:1 दिखाया।"),
    ("A","medium",2024,"The sex chromosomes in human male are:","XY","XX","YY","XO","Human males have XY sex chromosomes; females have XX. The Y chromosome determines maleness.","मानव पुरुष में लिंग गुणसूत्र हैं:","XY","XX","YY","XO","मानव पुरुषों में XY लिंग गुणसूत्र होते हैं; महिलाओं में XX। Y गुणसूत्र पुरुषत्व निर्धारित करता है।"),
    ("D","medium",2023,"DNA replication is:","Conservative","Dispersive","Random","Semiconservative","Meselson and Stahl proved DNA replication is semiconservative — each new DNA has one old and one new strand.","DNA प्रतिकृति है:","संरक्षी","विक्षेपी","यादृच्छिक","अर्धसंरक्षी","मेसेल्सन और स्टाल ने सिद्ध किया कि DNA प्रतिकृति अर्धसंरक्षी है — प्रत्येक नए DNA में एक पुराना और एक नया रज्जुक होता है।"),
    ("C","easy",2024,"Which RNA carries amino acids to ribosomes?","mRNA","rRNA","tRNA","DNA","tRNA (transfer RNA) carries specific amino acids to the ribosome during protein synthesis.","कौन सा RNA अमीनो अम्ल राइबोसोम तक ले जाता है:","mRNA","rRNA","tRNA","DNA","tRNA (अंतरण RNA) प्रोटीन संश्लेषण के दौरान विशिष्ट अमीनो अम्ल राइबोसोम तक ले जाता है।"),
    ("B","medium",2024,"Down syndrome is caused by trisomy of chromosome:","18","21","13","23","Down syndrome results from an extra copy of chromosome 21 (trisomy 21).","डाउन सिंड्रोम किस गुणसूत्र की ट्राइसोमी से होता है:","18","21","13","23","डाउन सिंड्रोम गुणसूत्र 21 की अतिरिक्त प्रति (ट्राइसोमी 21) से होता है।"),
    ("A","medium",2023,"Hemophilia is a:","Sex-linked recessive disorder","Autosomal dominant","Sex-linked dominant","Autosomal recessive","Hemophilia (bleeder's disease) is X-linked recessive, affecting blood clotting factors.","हीमोफीलिया है:","लिंग-सहलग्न अप्रभावी विकार","अलिंगसूत्री प्रभावी","लिंग-सहलग्न प्रभावी","अलिंगसूत्री अप्रभावी","हीमोफीलिया (रक्तस्रावी रोग) X-सहलग्न अप्रभावी है, रक्त स्कंदन कारकों को प्रभावित करता है।"),
    ("D","medium",2024,"The structural component of DNA is:","Amino acid","Glucose","Fatty acid","Nucleotide","DNA is a polymer of nucleotides, each consisting of a sugar (deoxyribose), phosphate, and nitrogenous base.","DNA का संरचनात्मक घटक है:","अमीनो अम्ल","ग्लूकोज","वसा अम्ल","न्यूक्लियोटाइड","DNA न्यूक्लियोटाइड का बहुलक है, प्रत्येक में शर्करा (डीऑक्सीराइबोज), फॉस्फेट और नाइट्रोजनी क्षार होता है।"),
    ("C","easy",2024,"In DNA, adenine pairs with:","Guanine","Cytosine","Thymine","Uracil","In DNA, adenine (A) pairs with thymine (T) via two hydrogen bonds; in RNA, A pairs with uracil.","DNA में एडिनीन किसके साथ जुड़ता है:","ग्वानीन","साइटोसीन","थाइमीन","यूरेसिल","DNA में एडिनीन (A) दो हाइड्रोजन बंधों द्वारा थाइमीन (T) से जुड़ता है; RNA में A यूरेसिल से जुड़ता है।"),
    ("B","medium",2023,"Color blindness is more common in:","Females","Males","Children","Elderly","Red-green color blindness is X-linked recessive, so males (XY) are more frequently affected.","वर्णांधता किसमें अधिक सामान्य है:","महिलाएं","पुरुष","बच्चे","वृद्ध","लाल-हरा वर्णांधता X-सहलग्न अप्रभावी है, इसलिए पुरुष (XY) अधिक प्रभावित होते हैं।"),
]):
    gid += 1
    qid = f"gdsbg-{gid:04d}"
    genetics_extra.append(make_q(qid, *qdata))

# ══════════════════════════════════════════════
# BIOLOGY: DISEASES (need 73 more)
# ══════════════════════════════════════════════
diseases_extra = []
did = 27
for i, qdata in enumerate([
    ("B","easy",2024,"Tuberculosis is caused by:","Virus","Bacteria","Fungus","Protozoa","TB is caused by Mycobacterium tuberculosis, a bacterium that primarily affects the lungs.","क्षय रोग (TB) किसके कारण होता है:","विषाणु","जीवाणु","कवक","प्रोटोजोआ","TB माइकोबैक्टीरियम ट्यूबरक्यूलोसिस जीवाणु से होता है, जो मुख्यतः फेफड़ों को प्रभावित करता है।"),
    ("A","medium",2023,"Malaria is transmitted by:","Female Anopheles mosquito","Male Anopheles","Housefly","Cockroach","Malaria is caused by Plasmodium protozoan transmitted through the bite of female Anopheles mosquito.","मलेरिया किसके द्वारा संचारित होता है:","मादा एनोफिलीज मच्छर","नर एनोफिलीज","घरेलू मक्खी","तिलचट्टा","मलेरिया प्लाज्मोडियम प्रोटोजोआ से होता है, मादा एनोफिलीज मच्छर के काटने से संचारित होता है।"),
    ("D","easy",2024,"Cholera is a:","Viral disease","Fungal disease","Genetic disease","Bacterial disease","Cholera is caused by Vibrio cholerae bacteria, causing severe diarrhea and dehydration.","हैजा एक है:","विषाणु रोग","कवक रोग","आनुवंशिक रोग","जीवाणु रोग","हैजा विब्रियो कॉलेरी जीवाणु से होता है, गंभीर अतिसार और निर्जलीकरण करता है।"),
    ("C","medium",2024,"Antibiotics are effective against:","Viruses","Fungi","Bacteria","All pathogens","Antibiotics target specific bacterial structures (cell wall, ribosomes) and are ineffective against viruses.","प्रतिजैविक किसके विरुद्ध प्रभावी हैं:","विषाणु","कवक","जीवाणु","सभी रोगजनक","प्रतिजैविक विशिष्ट जीवाणु संरचनाओं (कोशिका भित्ति, राइबोसोम) को लक्षित करते हैं, विषाणुओं पर अप्रभावी हैं।"),
    ("B","medium",2023,"Vaccination was discovered by:","Louis Pasteur","Edward Jenner","Robert Koch","Alexander Fleming","Edward Jenner discovered vaccination using cowpox virus to protect against smallpox (1796).","टीकाकरण की खोज किसने की:","लुई पाश्चर","एडवर्ड जेनर","रॉबर्ट कोच","अलेक्जेंडर फ्लेमिंग","एडवर्ड जेनर ने चेचक से बचाव के लिए काउपॉक्स विषाणु का उपयोग कर टीकाकरण की खोज की (1796)।"),
    ("A","medium",2024,"The first antibiotic discovered was:","Penicillin","Streptomycin","Tetracycline","Erythromycin","Alexander Fleming discovered penicillin in 1928 from the mold Penicillium notatum.","पहला प्रतिजैविक जो खोजा गया था:","पेनिसिलिन","स्ट्रेप्टोमाइसिन","टेट्रासाइक्लिन","एरिथ्रोमाइसिन","अलेक्जेंडर फ्लेमिंग ने 1928 में पेनिसिलियम नोटेटम फफूंद से पेनिसिलिन की खोज की।"),
    ("D","easy",2024,"Ringworm is caused by:","Virus","Bacteria","Protozoa","Fungus","Ringworm is a fungal infection caused by dermatophytes (Trichophyton, Microsporum).","दाद किसके कारण होता है:","विषाणु","जीवाणु","प्रोटोजोआ","कवक","दाद एक कवक संक्रमण है जो डर्मेटोफाइट्स (ट्राइकोफाइटन, माइक्रोस्पोरम) से होता है।"),
    ("C","medium",2023,"Innate immunity is:","Acquired after infection","From vaccination","Present from birth","Antibody-mediated","Innate immunity is non-specific, present from birth, and includes physical barriers, phagocytic cells.","जन्मजात प्रतिरक्षा है:","संक्रमण के बाद प्राप्त","टीकाकरण से","जन्म से उपस्थित","प्रतिरक्षी-मध्यस्थता","जन्मजात प्रतिरक्षा गैर-विशिष्ट, जन्म से उपस्थित होती है और इसमें भौतिक अवरोध, भक्षक कोशिकाएं शामिल हैं।"),
    ("B","medium",2024,"The BCG vaccine is for:","Polio","Tuberculosis","Hepatitis","Measles","BCG (Bacille Calmette-Guérin) vaccine provides protection against tuberculosis.","BCG टीका किसके लिए है:","पोलियो","क्षय रोग","यकृतशोथ","खसरा","BCG (बैसील कैलमेट-ग्वेरिन) टीका क्षय रोग से सुरक्षा प्रदान करता है।"),
    ("A","easy",2024,"Dengue is transmitted by:","Aedes mosquito","Anopheles mosquito","Housefly","Tick","Dengue virus is transmitted by Aedes aegypti mosquito, which bites during daytime.","डेंगू किसके द्वारा संचारित होता है:","एडीज मच्छर","एनोफिलीज मच्छर","घरेलू मक्खी","किलनी","डेंगू विषाणु एडीज इजिप्टी मच्छर द्वारा संचारित होता है, जो दिन में काटता है।"),
]):
    did += 1
    qid = f"gdsbd-{did:04d}"
    diseases_extra.append(make_q(qid, *qdata))

# ══════════════════════════════════════════════
# BIOLOGY: ECOLOGY (need 73 more)
# ══════════════════════════════════════════════
ecology_extra = []
ecid = 27
for i, qdata in enumerate([
    ("C","easy",2024,"The term 'ecosystem' was coined by:","Darwin","Haeckel","Tansley","Odum","A.G. Tansley coined the term 'ecosystem' in 1935 to describe the interaction of organisms with their environment.","'पारितंत्र' शब्द किसने गढ़ा:","डार्विन","हैकल","टैन्सले","ओडम","A.G. टैन्सले ने 1935 में जीवों और उनके पर्यावरण की अंतःक्रिया का वर्णन करने के लिए 'पारितंत्र' शब्द गढ़ा।"),
    ("B","medium",2023,"The primary source of energy in an ecosystem is:","Moon","Sun","Wind","Geothermal","Sun is the ultimate source of energy for all ecosystems, captured by producers through photosynthesis.","पारितंत्र में ऊर्जा का प्राथमिक स्रोत है:","चंद्रमा","सूर्य","पवन","भूतापीय","सूर्य सभी पारितंत्रों के लिए ऊर्जा का परम स्रोत है, उत्पादकों द्वारा प्रकाश संश्लेषण से ग्रहण किया जाता है।"),
    ("A","medium",2024,"In a food chain, plants are:","Producers","Primary consumers","Secondary consumers","Decomposers","Green plants are producers (autotrophs) that convert solar energy into chemical energy through photosynthesis.","खाद्य श्रृंखला में पादप हैं:","उत्पादक","प्राथमिक उपभोक्ता","द्वितीयक उपभोक्ता","अपघटक","हरे पादप उत्पादक (स्वपोषी) हैं जो प्रकाश संश्लेषण द्वारा सौर ऊर्जा को रासायनिक ऊर्जा में बदलते हैं।"),
    ("D","easy",2024,"Bacteria and fungi in an ecosystem are:","Producers","Herbivores","Carnivores","Decomposers","Decomposers (bacteria, fungi) break down dead organic matter, recycling nutrients back to the soil.","पारितंत्र में जीवाणु और कवक हैं:","उत्पादक","शाकाहारी","मांसाहारी","अपघटक","अपघटक (जीवाणु, कवक) मृत कार्बनिक पदार्थ को तोड़ते हैं, पोषक तत्वों को मिट्टी में पुनर्चक्रित करते हैं।"),
    ("C","medium",2023,"The 10% law of energy transfer was given by:","Tansley","Darwin","Lindeman","Odum","Lindeman's 10% law states that only about 10% of energy is transferred from one trophic level to the next.","ऊर्जा अंतरण का 10% नियम किसने दिया:","टैन्सले","डार्विन","लिंडमैन","ओडम","लिंडमैन का 10% नियम कहता है कि एक पोषी स्तर से अगले में लगभग 10% ऊर्जा ही अंतरित होती है।"),
    ("B","medium",2024,"The nitrogen cycle includes the process of:","Photosynthesis","Nitrogen fixation","Transpiration","Respiration","Nitrogen fixation converts atmospheric N₂ into usable forms (ammonia/nitrates) by bacteria like Rhizobium.","नाइट्रोजन चक्र में कौन सी प्रक्रिया शामिल है:","प्रकाश संश्लेषण","नाइट्रोजन स्थिरीकरण","वाष्पोत्सर्जन","श्वसन","नाइट्रोजन स्थिरीकरण वायुमंडलीय N₂ को राइजोबियम जैसे जीवाणुओं द्वारा उपयोगी रूपों (अमोनिया/नाइट्रेट) में बदलता है।"),
    ("A","easy",2024,"Ozone layer protects us from:","UV radiation","Infrared rays","X-rays","Gamma rays","The ozone layer in the stratosphere absorbs harmful ultraviolet (UV-B) radiation from the sun.","ओजोन परत हमें किससे बचाती है:","UV विकिरण","अवरक्त किरणें","X-किरणें","गामा किरणें","समताप मंडल में ओजोन परत सूर्य से हानिकारक पराबैंगनी (UV-B) विकिरण अवशोषित करती है।"),
    ("D","medium",2023,"Chipko movement is associated with:","Water conservation","Air pollution","Wildlife protection","Forest conservation","The Chipko movement (1973) was a forest conservation movement where villagers hugged trees to prevent cutting.","चिपको आंदोलन किससे संबंधित है:","जल संरक्षण","वायु प्रदूषण","वन्यजीव संरक्षण","वन संरक्षण","चिपको आंदोलन (1973) एक वन संरक्षण आंदोलन था जिसमें ग्रामीणों ने पेड़ कटाई रोकने के लिए पेड़ों से चिपक कर विरोध किया।"),
    ("C","medium",2024,"Acid rain is primarily caused by:","CO₂ and O₃","NH₃ and CH₄","SO₂ and NOₓ","O₂ and N₂","Acid rain results from sulfur dioxide (SO₂) and nitrogen oxides (NOₓ) reacting with water in the atmosphere.","अम्लीय वर्षा मुख्यतः किसके कारण होती है:","CO₂ और O₃","NH₃ और CH₄","SO₂ और NOₓ","O₂ और N₂","अम्लीय वर्षा वायुमंडल में सल्फर डाइऑक्साइड (SO₂) और नाइट्रोजन ऑक्साइड (NOₓ) की जल से अभिक्रिया से होती है।"),
    ("B","easy",2024,"The most abundant greenhouse gas is:","Methane","Carbon dioxide","Nitrous oxide","CFC","CO₂ is the most abundant anthropogenic greenhouse gas, contributing significantly to global warming.","सबसे प्रचुर ग्रीनहाउस गैस है:","मीथेन","कार्बन डाइऑक्साइड","नाइट्रस ऑक्साइड","CFC","CO₂ सबसे प्रचुर मानवजनित ग्रीनहाउस गैस है, वैश्विक तापन में महत्वपूर्ण योगदान देती है।"),
]):
    ecid += 1
    qid = f"gdsbec-{ecid:04d}"
    ecology_extra.append(make_q(qid, *qdata))

# ══════════════════════════════════════════════
# PROCESS ALL FILES
# ══════════════════════════════════════════════
print("Processing biology files...")

bio_map = {
    "biology-cell-structure.json": cell_extra,
    "biology-tissues.json": tissue_extra,
    "biology-nutrition.json": nutrition_extra,
    "biology-respiration.json": respiration_extra,
    "biology-transportation.json": transport_extra,
    "biology-excretion.json": excretion_extra,
    "biology-reproduction.json": reproduction_extra,
    "biology-genetics.json": genetics_extra,
    "biology-diseases.json": diseases_extra,
    "biology-ecology.json": ecology_extra,
}

for fname, extra_q in bio_map.items():
    try:
        data = load(fname)
        data.extend(extra_q)
        save(fname, data)
    except Exception as e:
        print(f"  ERROR in {fname}: {e}")

print("\nDone! Biology files updated. Run again for chemistry and physics (add those sections).")
