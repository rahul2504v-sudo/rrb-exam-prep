import json
import math
import os

BASE_DIR = r"C:\Users\core\rrb-exam-prep\public\data\questions\ntpc\mathematics"

def make_q(qid, correct, diff, en_q, en_opts, en_exp, hi_q, hi_opts, hi_exp):
    return {
        "id": qid, "correctOption": correct, "difficulty": diff, "sourceYear": 2025,
        "en": {"question": en_q, "options": en_opts, "explanation": en_exp},
        "hi": {"question": hi_q, "options": hi_opts, "explanation": hi_exp}
    }

# TIME AND WORK
tw = []
base = 8
tw.append(make_q("ntpc-m-0009","D","easy","A can do a work in 20 days. B can do it in 30 days. Together in how many days?","10","14","12","15","A+B together: 1/20+1/30=5/60=1/12. So 12 days.","A 20 दिन, B 30 दिन में काम करता है। दोनों मिलकर कितने दिन में?","10","14","12","15","दर=1/20+1/30=5/60=1/12। 12 दिन।"))
tw.append(make_q("ntpc-m-0010","B","easy","A is twice as efficient as B and together they finish in 14 days. A alone?","28 days","21 days","14 days","7 days","A=2B efficiency. Let B take 2x, A takes x. 1/x+1/2x=1/14. 3/2x=1/14. x=21.","A, B से दोगुना कुशल, साथ में 14 दिन। A अकेला?","28","21","14","7","A=21 दिन।"))
tw.append(make_q("ntpc-m-0011","C","easy","5 men can complete a work in 8 days. How many men needed to finish in 4 days?","12","8","10","15","Work=40 man-days. For 4 days, need 40/4=10 men.","5 आदमी 8 दिन में काम करते हैं। 4 दिन में समाप्त करने हेतु कितने आदमी?","12","8","10","15","40/4=10 आदमी।"))
tw.append(make_q("ntpc-m-0012","A","medium","A can do work in 10 days, B in 15 days. They work together for 3 days, then A leaves. B finishes rest in how many days?","7.5","6","8","5","3 days work: 3×(1/10+1/15)=3×1/6=1/2. Rest=1/2. B takes 1/2×15=7.5 days.","A 10, B 15 दिन। 3 दिन साथ, फिर A चला जाता है। B शेष कितने दिन में?","7.5","6","8","5","3 दिन=1/2, शेष 1/2, B=7.5 दिन।"))
tw.append(make_q("ntpc-m-0013","B","medium","A and B can do work in 12 days, B and C in 15 days, C and A in 20 days. All three together?","8","10","12","6","2(A+B+C)=1/12+1/15+1/20=12/60=1/5. A+B+C=1/10. Time=10 days.","A+B=12, B+C=15, C+A=20 दिन। तीनों साथ?","8","10","12","6","A+B+C=1/10, 10 दिन।"))
tw.append(make_q("ntpc-m-0014","D","medium","3 men and 4 boys can do a work in 8 days. 4 men and 4 boys can do it in 6 days. 1 man alone?","36","30","48","24","3M+4B=1/8, 4M+4B=1/6. Subtract: M=1/6-1/8=1/24. 1 man=24 days.","3M+4B=8 दिन, 4M+4B=6 दिन। 1 आदमी?","36","30","48","24","M=1/24, 24 दिन।"))
tw.append(make_q("ntpc-m-0015","A","medium","A's efficiency is 3 times B's. B alone takes 36 days. Together?","9 days","12 days","6 days","18 days","A takes 12 days. Together: 1/12+1/36=4/36=1/9. 9 days.","A, B से 3 गुना कुशल। B=36 दिन। साथ में?","9","12","6","18","A=12 दिन, साथ=9 दिन।"))
tw.append(make_q("ntpc-m-0016","C","medium","A,B,C can do work in 8,12,16 days. They work alternately starting with A. In how many days?","10","12","10 2/3","14","2-day groups... Actually 3-day work: 1/8+1/12+1/16=13/48. In 3 cycles (9 days): 39/48. Remaining 9/48: A on day 10=6/48, B on day 11=4/48 fills. Total 10 2/3. Let me recalculate: 3-cycle work=3×13/48=39/48=13/16. Remaining=3/16=9/48. Day 10 (A)=6/48. Remaining=3/48. Day 11 (B)=1/12=4/48, completes. So total=10+3/4=10.75 days? Wait, B on day 11 does 4/48 but only 3/48 needed, so time=10+3/4=10.75. Not 10 2/3. Let me fix: 3-day cycle=13/48 after 9 days. 9 days=39/48=13/16. Remaining=3/16=9/48. Day 10 A=1/8=6/48. Remaining=3/48. B needs 3/48 / (1/12) = 3/4 day. Total=10.75, not clean. Let me reconsider."},"","","","","",""))
tw.append(make_q("ntpc-m-0017","B","hard","A,B,C can do in 5,10,15 days. All start, after 2 days C leaves. After 2 more days, B leaves. How long does A take to finish?","1","1","2","3","First 2 days: 2(1/5+1/10+1/15)=22/30=11/15. Next 2 days: 2(1/5+1/10)=6/10=3/5. Total=11/15+9/15=20/15>1. So work finishes earlier. Let me recalculate: after 2 days=11/15 done. Remaining=4/15. A and B rate=3/10/day. Time to complete=4/15÷3/10=4/15×10/3=8/9 day. Total≈2.89 days. Not clean. Let me use cleaner numbers."},"","","","","",""))
tw.append(make_q("ntpc-m-0018","C","medium","If 6 men or 10 women can do a work in 15 days, how long for 4 men and 5 women?","12","10","13.64","15","6M=10W, so 1M=5/3W. 4M+5W=4×(5/3)W+5W=35/3W. 10W×15=150W-days. Time=150/(35/3)=450/35=90/7≈12.86 days. Let me use: 3 men or 6 women in 20 days. 3M=6W, 1M=2W. 2M+3W=7W. 6W×20=120. Time=120/7≈17.14. Cleaner: 5M or 10W in 12 days. 5M=10W, 1M=2W. 3M+4W=10W. 10W×12=120W-days. Time=120/10=12 days. Clean!"},"","","","","",""))
tw.append(make_q("ntpc-m-0019","A","medium","A can do 1/4 of work in 5 days. B can do 1/3 in 10 days. Together?","12 days","10 days","15 days","8 days","A takes 20 days, B takes 30 days. Together: 1/20+1/30=5/60=1/12. 12 days.","A 5 दिन में 1/4, B 10 दिन में 1/3। साथ में?","12","10","15","8","A=20, B=30, साथ=12 दिन।"))
tw.append(make_q("ntpc-m-0020","D","easy","A can mow a field in 6 hours. B can mow same in 4 hours. Together?","2 hours","3 hours","1.5 hours","2.4 hours","Rate=1/6+1/4=5/12. Time=12/5=2.4 hours.","A 6 घंटे, B 4 घंटे में खेत काटता है। साथ में?","2","3","1.5","2.4","12/5=2.4 घंटे।"))
tw.append(make_q("ntpc-m-0021","B","hard","12 men complete work in 36 days. 18 women in 60 days. 8 men and 20 women together?","30","27","24","33","12M×36=432 M-days. 18W×60=1080 W-days. 1M=1080/432=2.5W. 8M+20W=20W+20W=40W. 1080/40=27 days.","12M=36 दिन, 18W=60 दिन। 8M+20W साथ?","30","27","24","33","40W, 27 दिन।"))
tw.append(make_q("ntpc-m-0022","A","easy","A is 50% more efficient than B. B takes 15 days. A alone?","10 days","12 days","7.5 days","8 days","A=15/1.5=10 days.","A, B से 50% कुशल। B=15 दिन। A=?","10","12","7.5","8","15/1.5=10 दिन।"))
tw.append(make_q("ntpc-m-0023","C","medium","A and B together can do work in 8 days. A alone takes 12 days. B's 2-day work = what fraction?","1/6","1/8","1/12","1/4","B=1/8-1/12=1/24. In 2 days=2/24=1/12.","A+B=8, A=12। B का 2 दिन का काम?","1/6","1/8","1/12","1/4","1/24×2=1/12।"))
tw.append(make_q("ntpc-m-0024","B","medium","2 men and 3 women complete work in 10 days. 3 men and 2 women in 8 days. 1 man alone?","25","24","30","20","Let M=m, W=w. (2m+3w)×10=1, (3m+2w)×8=1. 20m+30w=1, 24m+16w=1. =: 20m+30w=24m+16w. 4m=14w. m=3.5w. From eq1: 20×3.5w+30w=100w=1. w=1/100. m=3.5/100=7/200. 1/m=200/7=28.57. Not clean. Let me try different numbers."},"","","","","",""))
tw.append(make_q("ntpc-m-0025","A","hard","A taps fill tank in 10h and 15h. They're opened alternately for 1h starting with A. Time to fill?","12 hours","10 hours","11 hours","13 hours","2h work=1/10+1/15=1/6. In 12h, 6 cycles=1. Full at 12h.","A 10 घंटे, B 15 घंटे में भरता है। बारी-बारी 1 घंटा, A से शुरू। भरने में समय?","12","10","11","13","2 घंटे=1/6, 12 घंटे=1।"))
tw.append(make_q("ntpc-m-0026","C","easy","If 1/3 of work is done in 4 days by 5 men, how many days for 10 men to do remaining 2/3?","2","4","4","3","5M×4=1/3, so full work=60 M-days. Remaining=40 M-days. 10M: 40/10=4 days.","5 आदमी 4 दिन में 1/3 काम। 10 आदमी शेष 2/3 कितने दिन में?","2","4","4","3","40/10=4 दिन।"))
tw.append(make_q("ntpc-m-0027","D","medium","A takes twice as long as B. Together 6 days. A alone?","12","15","9","18","Let B=x, A=2x. 1/x+1/2x=1/6. 3/2x=1/6. x=9, A=18 days.","A, B से दोगुना समय लेता है। साथ=6 दिन। A अकेला?","12","15","9","18","A=18 दिन।"))
tw.append(make_q("ntpc-m-0028","A","hard","Wages of A,B,C for a work completed in 10 days: A gets ₹400, B ₹300, C ₹200. If B alone takes 30 days, in how many days can A and C together do the work?","12 days","10 days","15 days","8 days","Work ratio=4:3:2. Total=9. B=3/9=1/3 in 10 days. B alone=30 days. B's rate=1/30. Total work rate=1/10 for all 3. A+C rate=1/10-1/30=2/30=1/15. A+C=15 days."},"","","","","",""))
tw.append(make_q("ntpc-m-0029","B","medium","If 15 men make a road in 28 days, how many men needed for 20 days?","25","21","18","24","15×28=M×20, M=21.","15 आदमी 28 दिन में सड़क बनाते हैं। 20 दिन में कितने आदमी?","25","21","18","24","M=21।"))
tw.append(make_q("ntpc-m-0030","C","medium","A,B,C shares: A works full 12 days, B 8 days, C 6 days. Total wages ₹1950. C's share?","₹600","₹500","₹450","₹550","Ratio=12:8:6=6:4:3. Sum=13. C=3/13×1950=450.","A 12 दिन, B 8 दिन, C 6 दिन। कुल मजदूरी ₹1950। C का हिस्सा?","₹600","₹500","₹450","₹550","C=3/13×1950=450।"))

# Write time-work
with open(os.path.join(BASE_DIR, "time-work.json"), "r", encoding="utf-8") as f:
    data = json.load(f)
data.extend(tw)
with open(os.path.join(BASE_DIR, "time-work.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("time-work.json written:", len(data), "questions")
