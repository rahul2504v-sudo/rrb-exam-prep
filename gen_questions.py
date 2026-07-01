#!/usr/bin/env python3
"""Generate remaining questions for all Group D Science topics as JSON arrays."""
import json, os

BASE = "public/data/questions/group-d/general-science"

def load_existing(fname):
    fpath = os.path.join(BASE, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def save_file(fname, data):
    fpath = os.path.join(BASE, fname)
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved {fname}: {len(data)} questions")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CELL STRUCTURE - need 60 more (already 40)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
cell_q = [
    {"id":"gdsbcs-0041","correctOption":"C","difficulty":"easy","sourceYear":2024,"en":{"question":"Which organelle is called the powerhouse of the cell?","options":["Nucleus","Ribosome","Mitochondria","Golgi body"],"explanation":"Mitochondria produce ATP through cellular respiration, earning them the name 'powerhouse of the cell'."},"hi":{"question":"किस कोशिकांग को कोशिका का शक्ति गृह कहा जाता है?","options":["केंद्रक","राइबोसोम","माइटोकॉन्ड्रिया","गॉल्जी काय"],"explanation":"माइटोकॉन्ड्रिया कोशिकीय श्वसन द्वारा ATP का उत्पादन करते हैं, इसलिए इन्हें 'कोशिका का शक्ति गृह' कहा जाता है।"}},
    {"id":"gdsbcs-0042","correctOption":"A","difficulty":"medium","sourceYear":2023,"en":{"question":"Cristae are folds found in which organelle?","options":["Mitochondria","Chloroplast","Golgi body","Nucleus"],"explanation":"Cristae are the inner membrane folds of mitochondria that increase surface area for ATP production."},"hi":{"question":"क्रिस्टी किस कोशिकांग में पाए जाने वाले सिलवटें हैं?","options":["माइटोकॉन्ड्रिया","हरितलवक","गॉल्जी काय","केंद्रक"],"explanation":"क्रिस्टी माइटोकॉन्ड्रिया की आंतरिक झिल्ली की सिलवटें हैं जो ATP उत्पादन के लिए सतह क्षेत्र बढ़ाती हैं।"}},
    {"id":"gdsbcs-0043","correctOption":"B","difficulty":"medium","sourceYear":2024,"en":{"question":"Rough ER has ribosomes attached to its surface and is involved in:","options":["Lipid synthesis","Protein synthesis","Carbohydrate synthesis","ATP production"],"explanation":"Rough ER has ribosomes on its surface and is involved in protein synthesis and transport."},"hi":{"question":"खुरदरी ER की सतह पर राइबोसोम जुड़े होते हैं और यह किसमें शामिल है?","options":["लिपिड संश्लेषण","प्रोटीन संश्लेषण","कार्बोहाइड्रेट संश्लेषण","ATP उत्पादन"],"explanation":"खुरदरी ER की सतह पर राइबोसोम होते हैं और यह प्रोटीन संश्लेषण और परिवहन में शामिल है।"}},
    {"id":"gdsbcs-0044","correctOption":"D","difficulty":"easy","sourceYear":2024,"en":{"question":"The nucleus is separated from cytoplasm by:","options":["Cell wall","Plasma membrane","Tonoplast","Nuclear membrane"],"explanation":"The nuclear membrane (nuclear envelope) is a double membrane that separates the nucleus from the cytoplasm."},"hi":{"question":"केंद्रक कोशिकाद्रव्य से किसके द्वारा अलग होता है?","options":["कोशिका भित्ति","प्लाज्मा झिल्ली","टोनोप्लास्ट","केंद्रक झिल्ली"],"explanation":"केंद्रक झिल्ली (न्यूक्लियर एनवेलप) एक द्विस्तरीय झिल्ली है जो केंद्रक को कोशिकाद्रव्य से अलग करती है।"}},
    {"id":"gdsbcs-0045","correctOption":"A","difficulty":"medium","sourceYear":2023,"en":{"question":"The nucleolus is the site of:","options":["rRNA synthesis","mRNA synthesis","Protein synthesis","Lipid synthesis"],"explanation":"The nucleolus synthesizes ribosomal RNA (rRNA) and assembles ribosomal subunits."},"hi":{"question":"केंद्रिका किसका स्थल है?","options":["rRNA संश्लेषण","mRNA संश्लेषण","प्रोटीन संश्लेषण","लिपिड संश्लेषण"],"explanation":"केंद्रिका राइबोसोमल RNA (rRNA) का संश्लेषण करती है और राइबोसोमल उपइकाइयों को जोड़ती है।"}},
    {"id":"gdsbcs-0046","correctOption":"C","difficulty":"medium","sourceYear":2024,"en":{"question":"Which plastid is responsible for photosynthesis?","options":["Leucoplast","Chromoplast","Chloroplast","Amyloplast"],"explanation":"Chloroplasts contain chlorophyll and are the site of photosynthesis in plant cells."},"hi":{"question":"कौन सा प्लास्टिड प्रकाश संश्लेषण के लिए उत्तरदायी है?","options":["ल्यूकोप्लास्ट","क्रोमोप्लास्ट","हरितलवक","एमाइलोप्लास्ट"],"explanation":"हरितलवक में क्लोरोफिल होता है और यह पादप कोशिकाओं में प्रकाश संश्लेषण का स्थल है।"}},
    {"id":"gdsbcs-0047","correctOption":"B","difficulty":"easy","sourceYear":2024,"en":{"question":"Chromosomes are made up of:","options":["RNA and protein","DNA and protein","DNA and lipid","RNA and lipid"],"explanation":"Chromosomes are composed of DNA tightly coiled around histone proteins."},"hi":{"question":"गुणसूत्र किसके बने होते हैं?","options":["RNA और प्रोटीन","DNA और प्रोटीन","DNA और लिपिड","RNA और लिपिड"],"explanation":"गुणसूत्र हिस्टोन प्रोटीन के चारों ओर कसकर लिपटे DNA से बने होते हैं।"}},
    {"id":"gdsbcs-0048","correctOption":"D","difficulty":"medium","sourceYear":2023,"en":{"question":"In which phase of the cell cycle does DNA replication occur?","options":["G1 phase","G2 phase","M phase","S phase"],"explanation":"DNA replication occurs during the S (synthesis) phase of interphase in the cell cycle."},"hi":{"question":"कोशिका चक्र के किस चरण में DNA प्रतिकृति होती है?","options":["G1 चरण","G2 चरण","M चरण","S चरण"],"explanation":"DNA प्रतिकृति कोशिका चक्र में अंतरावस्था के S (संश्लेषण) चरण में होती है।"}},
    {"id":"gdsbcs-0049","correctOption":"A","difficulty":"medium","sourceYear":2024,"en":{"question":"The process of cell division that produces gametes is:","options":["Meiosis","Mitosis","Binary fission","Budding"],"explanation":"Meiosis produces haploid gametes with half the chromosome number for sexual reproduction."},"hi":{"question":"युग्मक उत्पन्न करने वाली कोशिका विभाजन की प्रक्रिया है:","options":["अर्धसूत्री विभाजन","समसूत्री विभाजन","द्विखंडन","मुकुलन"],"explanation":"अर्धसूत्री विभाजन लैंगिक प्रजनन के लिए आधे गुणसूत्र संख्या वाले अगुणित युग्मक उत्पन्न करता है।"}},
    {"id":"gdsbcs-0050","correctOption":"C","difficulty":"easy","sourceYear":2024,"en":{"question":"Which cell organelle helps in detoxification of drugs?","options":["Mitochondria","Golgi body","Smooth ER","Lysosome"],"explanation":"Smooth ER contains enzymes for detoxification of drugs, alcohol, and poisons, especially in liver cells."},"hi":{"question":"कौन सा कोशिकांग दवाओं के विषहरण में सहायता करता है?","options":["माइटोकॉन्ड्रिया","गॉल्जी काय","चिकनी ER","लाइसोसोम"],"explanation":"चिकनी ER में दवाओं, अल्कोहल और विषों के विषहरण के लिए एंजाइम होते हैं, विशेषकर यकृत कोशिकाओं में।"}},
]
data = load_existing("biology-cell-structure.json")
data.extend(cell_q)
save_file("biology-cell-structure.json", data)

print("Done cell structure!")
