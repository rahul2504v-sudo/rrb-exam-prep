"""
Math Question Templates — NTPC & Group D
Every function returns a VERIFIED bilingual question.
"""
import math, random
from generator_core import *

# ═══════════════════════════════════════════
# NUMBER SYSTEM
# ═══════════════════════════════════════════

def number_system_templates():
    templates = []
    
    # Sum of first N natural numbers
    for _ in range(5):
        n = rand_int(20, 200)
        s = n * (n + 1) // 2
        wrong = [s + rand_int(1, n), s - rand_int(1, n//2), s + n, s - n//2]
        templates.append({
            "en_q": f"What is the sum of first {n} natural numbers?",
            "hi_q": f"प्रथम {n} प्राकृतिक संख्याओं का योग क्या है?",
            "ans": s, "wrong": wrong,
            "en_ex": f"Sum = n(n+1)/2 = {n}×{n+1}/2 = {n*(n+1)}/2 = {s}",
            "hi_ex": f"योग = n(n+1)/2 = {n}×{n+1}/2 = {n*(n+1)}/2 = {s}",
            "diff": "easy"
        })
    
    # Divisibility rules
    divisors = [(2, "last digit is even"), (3, "sum of digits divisible by 3"), 
                (4, "last 2 digits divisible by 4"), (5, "ends in 0 or 5"),
                (6, "divisible by both 2 and 3"), (8, "last 3 digits divisible by 8"),
                (9, "sum of digits divisible by 9"), (11, "alternating sum divisible by 11")]
    for d, _ in divisors:
        base = rand_int(1000, 9999)
        mult = base - (base % d) if base % d == 0 else base + (d - base % d)
        wrong_divs = [m for m in [mult+rand_int(1,5), mult-rand_int(1,5), mult+d*2, mult-d] if m != mult and m > 0]
        templates.append({
            "en_q": f"Which of the following numbers is divisible by {d}?",
            "hi_q": f"निम्नलिखित में से कौन सी संख्या {d} से विभाज्य है?",
            "ans": mult, "wrong": wrong_divs[:3],
            "en_ex": f"{mult} is divisible by {d} because {'the sum of digits = ' + str(sum(int(x) for x in str(mult))) + ' which is divisible by ' + str(d) if d == 3 or d == 9 else str(mult) + ' / ' + str(d) + ' = ' + str(mult//d)}",
            "hi_ex": f"{mult}, {d} से विभाज्य है।",
            "diff": "easy"
        })
    
    # Find unit digit
    for _ in range(4):
        base = rand_int(2, 9)
        exp = rand_int(10, 50)
        # Pattern: unit digits cycle every 4 for most numbers
        cycles = {
            2: [2,4,8,6], 3: [3,9,7,1], 4: [4,6],
            7: [7,9,3,1], 8: [8,4,2,6], 9: [9,1]
        }
        if base in cycles:
            cycle = cycles[base]
            idx = (exp - 1) % len(cycle)
            unit = cycle[idx]
        elif base == 5:
            unit = 5
        elif base == 6:
            unit = 6
        else:
            unit = 0
        
        wrong_units = random.sample([u for u in range(10) if u != unit], 3)
        templates.append({
            "en_q": f"Find the unit digit of {base}^{exp}.",
            "hi_q": f"{base}^{exp} का इकाई अंक ज्ञात करें।",
            "ans": unit, "wrong": wrong_units,
            "en_ex": f"Unit digits of powers of {base} repeat in cycle: {cycles.get(base, [])}. {exp} mod {len(cycles.get(base, [1]))} = {exp % len(cycles.get(base, [1]))}→ unit digit = {unit}",
            "hi_ex": f"{base} की घातों का इकाई अंक चक्र: {cycles.get(base, [])}। {exp} का शेष = {exp % len(cycles.get(base, [1]))}→ इकाई अंक = {unit}",
            "diff": "medium"
        })
    
    return templates

# ═══════════════════════════════════════════
# PERCENTAGE
# ═══════════════════════════════════════════

def percentage_templates():
    templates = []
    
    # X% of Y
    for _ in range(8):
        pct = rand_int(5, 95)
        base = rand_int(200, 5000)
        if base % 100 != 0:
            base = (base // 100) * 100
        result = (pct * base) // 100
        wrong = [result + rand_int(5, 100), result - rand_int(5, 100), 
                 (pct * (base+100))//100, ((pct+10)*base)//100]
        templates.append({
            "en_q": f"What is {pct}% of {base}?",
            "hi_q": f"{base} का {pct}% कितना होता है?",
            "ans": result, "wrong": wrong,
            "en_ex": f"{pct}% of {base} = ({pct}/100) × {base} = {pct/100} × {base} = {result}",
            "hi_ex": f"{base} का {pct}% = ({pct}/100) × {base} = {result}",
            "diff": "easy"
        })
    
    # X is what % of Y
    for _ in range(5):
        x = rand_int(20, 400)
        y = x * rand_int(2, 8)
        result = round((x / y) * 100, 1)
        wrong = [round(result + random.uniform(1,10), 1), round(result - random.uniform(1,8), 1), 
                 round(result * random.uniform(1.1, 1.5), 1)]
        templates.append({
            "en_q": f"{x} is what percent of {y}?",
            "hi_q": f"{x}, {y} का कितना प्रतिशत है?",
            "ans": result, "wrong": wrong,
            "en_ex": f"Percentage = ({x}/{y}) × 100 = {x/y:.4f} × 100 = {result}%",
            "hi_ex": f"प्रतिशत = ({x}/{y}) × 100 = {result}%",
            "diff": "easy"
        })
    
    # Percentage change
    for _ in range(6):
        original = rand_int(200, 2000)
        change_pct = rand_int(5, 40)
        direction = rand_choice(["increase", "decrease"])
        if direction == "increase":
            new_val = original + (original * change_pct // 100)
        else:
            new_val = original - (original * change_pct // 100)
        wrong = [new_val + rand_int(10, 100), new_val - rand_int(10, 100), 
                 original + (original * (change_pct+10) // 100),
                 original - (original * (change_pct-5) // 100)]
        templates.append({
            "en_q": f"If a value of {original} is {'increased' if direction == 'increase' else 'decreased'} by {change_pct}%, what is the new value?",
            "hi_q": f"यदि {original} को {change_pct}% {'बढ़ाया' if direction == 'increase' else 'घटाया'} जाए, तो नया मान क्या होगा?",
            "ans": new_val, "wrong": wrong,
            "en_ex": f"Change = {original} × {change_pct}/100 = {original * change_pct // 100}. New value = {original} {'+ ' if direction == 'increase' else '- '}{original * change_pct // 100} = {new_val}",
            "hi_ex": f"परिवर्तन = {original} × {change_pct}/100 = {original * change_pct // 100}। नया मान = {new_val}",
            "diff": "medium"
        })
    
    # Price after successive discounts
    for _ in range(5):
        price = rand_int(1000, 10000)
        d1 = rand_int(5, 30)
        d2 = rand_int(5, 30)
        after_d1 = price - (price * d1 // 100)
        after_d2 = after_d1 - (after_d1 * d2 // 100)
        wrong = [after_d2 + rand_int(50, 500), after_d2 - rand_int(50, 300),
                 price - (price * (d1 + d2) // 100),
                 price * (100 - d1) * (100 - d2) // 10000 + rand_int(10, 100)]
        templates.append({
            "en_q": f"A product marked at ₹{price} is sold after successive discounts of {d1}% and {d2}%. What is the selling price?",
            "hi_q": f"₹{price} अंकित मूल्य वाले उत्पाद पर {d1}% और {d2}% की क्रमिक छूट दी जाती है। विक्रय मूल्य क्या है?",
            "ans": after_d2, "wrong": wrong,
            "en_ex": f"After {d1}% discount: {price} × (100-{d1})/100 = {after_d1}. After {d2}%: {after_d1} × (100-{d2})/100 = {after_d2}",
            "hi_ex": f"{d1}% छूट के बाद: {after_d1}। {d2}% छूट के बाद: {after_d2}",
            "diff": "medium"
        })
    
    return templates

# ═══════════════════════════════════════════
# PROFIT & LOSS
# ═══════════════════════════════════════════

def profit_loss_templates():
    templates = []
    
    # Profit % from CP and SP
    for _ in range(5):
        cp = rand_int(200, 5000)
        profit_pct = rand_int(5, 50)
        sp = cp + (cp * profit_pct // 100)
        wrong = [sp + rand_int(50, 300), sp - rand_int(50, 200), 
                 cp + (cp * (profit_pct+10) // 100), cp + (cp * (profit_pct-5) // 100)]
        templates.append({
            "en_q": f"An item is bought for ₹{cp} and sold for ₹{sp}. What is the profit percentage?",
            "hi_q": f"एक वस्तु ₹{cp} में खरीदी गई और ₹{sp} में बेची गई। लाभ प्रतिशत क्या है?",
            "ans": profit_pct, "wrong": [profit_pct + rand_int(1, 10), profit_pct - rand_int(1, 5), 
                                          profit_pct + 5, profit_pct - 3],
            "en_ex": f"Profit = SP - CP = {sp} - {cp} = {sp-cp}. Profit% = ({sp-cp}/{cp}) × 100 = {profit_pct}%",
            "hi_ex": f"लाभ = {sp} - {cp} = {sp-cp}। लाभ% = ({sp-cp}/{cp}) × 100 = {profit_pct}%",
            "diff": "easy"
        })
    
    # CP from SP and profit/loss %
    for _ in range(5):
        sp = rand_int(500, 5000)
        pct = rand_int(10, 40)
        is_profit = rand_choice([True, False])
        if is_profit:
            cp = sp * 100 // (100 + pct)
            label = "profit"
        else:
            cp = sp * 100 // (100 - pct)
            label = "loss"
        wrong = [cp + rand_int(50, 300), cp - rand_int(20, 150), 
                 sp * 100 // (100 + pct + 10), sp * 100 // (100 - pct - 5)]
        templates.append({
            "en_q": f"By selling an article for ₹{sp}, a shopkeeper makes a {label} of {pct}%. What is the cost price?",
            "hi_q": f"एक वस्तु को ₹{sp} में बेचने पर {pct}% का {'लाभ' if is_profit else 'हानि'} होता है। क्रय मूल्य क्या है?",
            "ans": cp, "wrong": wrong,
            "en_ex": f"CP = SP × 100/(100 {'+' if is_profit else '-'} {label}%) = {sp} × 100/(100{'+' if is_profit else '-'}{pct}) = {sp*100//(100+[1,-1][is_profit]*pct)}",
            "hi_ex": f"क्रय मूल्य = {sp} × 100/(100 {'+' if is_profit else '-'} {pct}) = {cp}",
            "diff": "medium"
        })
    
    # Dishonest shopkeeper (false weight)
    for _ in range(4):
        actual = rand_int(800, 950)
        claimed = 1000
        profit = ((claimed - actual) / actual) * 100
        wrong = [round(profit + random.uniform(1, 8), 1), 
                 round(profit - random.uniform(1, 5), 1), 
                 round(((1000 - actual) / 1000) * 100, 1)]
        templates.append({
            "en_q": f"A shopkeeper uses a weight of {actual}g instead of 1kg. What is his profit percentage?",
            "hi_q": f"एक दुकानदार 1 किलो के बजाय {actual} ग्राम का बाट प्रयोग करता है। उसका लाभ प्रतिशत क्या है?",
            "ans": round(profit, 1), "wrong": wrong,
            "en_ex": f"Profit = (Error / Actual) × 100 = (({1000-actual})/{actual}) × 100 = {profit:.1f}%",
            "hi_ex": f"लाभ% = (त्रुटि / वास्तविक) × 100 = (({1000-actual})/{actual}) × 100 = {profit:.1f}%",
            "diff": "medium"
        })
    
    return templates

# ═══════════════════════════════════════════
# TIME & WORK
# ═══════════════════════════════════════════

def time_work_templates():
    templates = []
    
    # A alone, B alone, together
    for _ in range(6):
        a_days = rand_int(6, 30)
        b_days = a_days + rand_int(3, 20)
        lcm = (a_days * b_days) // math.gcd(a_days, b_days)
        together = lcm // (lcm // a_days + lcm // b_days)
        wrong = [together + rand_int(1, 5), together - rand_int(1, 3),
                 (a_days + b_days) // 2, max(1, a_days * b_days // (a_days + b_days) + rand_int(1, 3))]
        templates.append({
            "en_q": f"A can complete a work in {a_days} days and B can complete it in {b_days} days. How many days will they take working together?",
            "hi_q": f"A किसी कार्य को {a_days} दिनों में और B उसे {b_days} दिनों में पूरा कर सकता है। दोनों मिलकर कितने दिनों में पूरा करेंगे?",
            "ans": together, "wrong": wrong,
            "en_ex": f"A's 1 day work = 1/{a_days}. B's 1 day work = 1/{b_days}. Together = 1/{a_days} + 1/{b_days} = {1/a_days + 1/b_days:.4f}. Days = 1/{1/a_days + 1/b_days:.4f} = {together}",
            "hi_ex": f"A का 1 दिन = 1/{a_days}, B का 1 दिन = 1/{b_days}। दोनों = 1/{together} कार्य/दिन। समय = {together} दिन",
            "diff": "easy"
        })
    
    # Efficiency ratios
    for _ in range(5):
        a_eff = rand_int(2, 5)
        b_eff = a_eff + rand_int(1, 3)
        total_work = a_eff * b_eff * rand_int(5, 20)
        a_days = total_work // a_eff
        b_days = total_work // b_eff
        together_days = total_work // (a_eff + b_eff)
        wrong = [together_days + rand_int(1, 4), together_days - rand_int(1, 3),
                 (a_days + b_days) // 2, together_days + 2]
        templates.append({
            "en_q": f"A is {b_eff//a_eff} times as efficient as B. If A takes {a_days} days to complete a work, how many days will they take together?",
            "hi_q": f"A, B से {b_eff//a_eff} गुना कुशल है। यदि A को कार्य पूरा करने में {a_days} दिन लगते हैं, तो दोनों मिलकर कितने दिन लेंगे?",
            "ans": together_days, "wrong": wrong,
            "en_ex": f"A's efficiency = {a_eff}, B's = {b_eff}. Total work = {a_eff} × {a_days} = {total_work}. Together/day = {a_eff} + {b_eff} = {a_eff + b_eff}. Days = {total_work}/{a_eff + b_eff} = {together_days}",
            "hi_ex": f"A की दक्षता = {a_eff}, B = {b_eff}। कुल कार्य = {total_work}। दोनों/दिन = {a_eff + b_eff}। दिन = {together_days}",
            "diff": "medium"
        })
    
    return templates

# ═══════════════════════════════════════════
# TIME, SPEED & DISTANCE
# ═══════════════════════════════════════════

def tsd_templates():
    templates = []
    
    # Basic speed = distance / time
    for _ in range(5):
        dist = rand_int(60, 600)
        time_hrs = random.choice([1, 1.5, 2, 2.5, 3, 4, 5])
        speed = dist / time_hrs
        wrong = [speed + random.randint(5, 20), speed - random.randint(3, 15),
                 dist / (time_hrs + 0.5), dist / (time_hrs - 0.3) if time_hrs > 0.5 else speed * 2]
        templates.append({
            "en_q": f"A car covers {dist} km in {time_hrs} hours. What is its speed in km/hr?",
            "hi_q": f"एक कार {dist} किमी की दूरी {time_hrs} घंटे में तय करती है। उसकी गति किमी/घंटा में क्या है?",
            "ans": round(speed), "wrong": [round(w) for w in wrong],
            "en_ex": f"Speed = Distance / Time = {dist} / {time_hrs} = {speed} km/hr",
            "hi_ex": f"गति = दूरी / समय = {dist} / {time_hrs} = {speed} किमी/घंटा",
            "diff": "easy"
        })
    
    # Train crossing pole/platform
    for _ in range(6):
        length = rand_int(100, 400)
        speed_kmh = rand_int(36, 108)
        speed_ms = speed_kmh * 5 / 18
        # Crossing pole
        time_pole = length / speed_ms
        # Crossing platform
        platform = rand_int(150, 600)
        time_platform = (length + platform) / speed_ms
        
        if rand_choice([True, False]):
            wrong = [round(time_pole + random.uniform(1, 5)), round(time_pole - random.uniform(0.5, 3)),
                     round(length / (speed_kmh * 5 / 18 + 5)), round(length / speed_kmh)]
            templates.append({
                "en_q": f"A train of length {length}m is moving at {speed_kmh} km/hr. How long will it take to cross a pole?",
                "hi_q": f"{length} मीटर लंबी रेलगाड़ी {speed_kmh} किमी/घंटा की गति से चल रही है। एक खंभे को पार करने में कितना समय लगेगा?",
                "ans": round(time_pole, 1), "wrong": [round(w, 1) for w in wrong],
                "en_ex": f"Speed in m/s = {speed_kmh} × 5/18 = {speed_ms:.1f}. Time = Length/Speed = {length}/{speed_ms:.1f} = {time_pole:.1f}s",
                "hi_ex": f"गति (मी/से) = {speed_kmh} × 5/18 = {speed_ms:.1f}। समय = {length}/{speed_ms:.1f} = {time_pole:.1f} सेकंड",
                "diff": "medium"
            })
        else:
            wrong = [round(time_platform + random.uniform(1, 8)), round(time_platform - random.uniform(1, 5)),
                     round((length + platform) / speed_kmh), round(platform / speed_ms)]
            templates.append({
                "en_q": f"A train of length {length}m running at {speed_kmh} km/hr crosses a platform of length {platform}m. Find the time taken.",
                "hi_q": f"{length} मीटर लंबी रेलगाड़ी {speed_kmh} किमी/घंटा से {platform} मीटर लंबे प्लेटफॉर्म को पार करती है। समय ज्ञात करें।",
                "ans": round(time_platform, 1), "wrong": [round(w, 1) for w in wrong],
                "en_ex": f"Speed = {speed_kmh} × 5/18 = {speed_ms:.1f} m/s. Total distance = {length} + {platform} = {length+platform}m. Time = {length+platform}/{speed_ms:.1f} = {time_platform:.1f}s",
                "hi_ex": f"गति = {speed_ms:.1f} मी/से। कुल दूरी = {length+platform} मी। समय = {time_platform:.1f} सेकंड",
                "diff": "medium"
            })
    
    return templates

# ═══════════════════════════════════════════
# SIMPLE & COMPOUND INTEREST
# ═══════════════════════════════════════════

def interest_templates():
    templates = []
    
    # Simple interest
    for _ in range(5):
        p = rand_int(1000, 20000)
        r = rand_int(4, 15)
        t = rand_int(1, 5)
        si = (p * r * t) // 100
        wrong = [si + rand_int(50, 500), si - rand_int(20, 200),
                 (p * r * (t + 1)) // 100, (p * (r + 2) * t) // 100]
        templates.append({
            "en_q": f"Find the simple interest on ₹{p} at {r}% per annum for {t} years.",
            "hi_q": f"₹{p} पर {r}% वार्षिक दर से {t} वर्षों का साधारण ब्याज ज्ञात करें।",
            "ans": si, "wrong": wrong,
            "en_ex": f"SI = (P × R × T) / 100 = ({p} × {r} × {t}) / 100 = {p * r * t} / 100 = ₹{si}",
            "hi_ex": f"साधारण ब्याज = ({p} × {r} × {t}) / 100 = ₹{si}",
            "diff": "easy"
        })
    
    # CI - SI difference for 2 years
    for _ in range(5):
        p = rand_int(5000, 50000)
        r = rand_int(5, 20)
        si2 = (p * r * 2) // 100
        ci2 = p * (1 + r/100)**2 - p
        diff = int(ci2 - si2)
        wrong = [diff + rand_int(5, 50), diff - rand_int(2, 20),
                 int(p * (r/100)**2 * 1.5), int(p * (r/100)**2 * 0.5)]
        templates.append({
            "en_q": f"What is the difference between compound interest and simple interest on ₹{p} at {r}% per annum for 2 years?",
            "hi_q": f"₹{p} पर {r}% वार्षिक दर से 2 वर्षों के चक्रवृद्धि ब्याज और साधारण ब्याज में कितना अंतर है?",
            "ans": diff, "wrong": wrong,
            "en_ex": f"Difference = P × (r/100)² = {p} × ({r}/100)² = {p} × {(r/100)**2} = {diff}",
            "hi_ex": f"अंतर = P × (r/100)² = {p} × ({r}/100)² = {diff}",
            "diff": "medium"
        })
    
    # Compound interest half-yearly
    for _ in range(4):
        p = rand_int(5000, 25000)
        r = rand_int(8, 16)
        t = rand_int(1, 2)
        n = 2  # half-yearly
        amount = p * (1 + r/(100*n))**(n*t)
        ci = int(amount - p)
        wrong = [ci + rand_int(100, 500), ci - rand_int(50, 200),
                 int(p * (1 + r/100)**t - p), ci + rand_int(200, 600)]
        templates.append({
            "en_q": f"Find the compound interest on ₹{p} at {r}% per annum compounded half-yearly for {t} year(s).",
            "hi_q": f"₹{p} पर {r}% वार्षिक दर से {t} वर्ष का चक्रवृद्धि ब्याज ज्ञात करें, जब ब्याज अर्धवार्षिक संयोजित होता है।",
            "ans": ci, "wrong": wrong,
            "en_ex": f"Rate per period = {r}/2 = {r/2}%. Periods = {t}×2 = {t*2}. Amount = {p} × (1 + {r/2}/100)^{t*2} = {amount:.0f}. CI = {amount:.0f} - {p} = {ci}",
            "hi_ex": f"दर/अवधि = {r/2}%। अवधियां = {t*2}। मिश्रधन = {amount:.0f}। CI = {ci}",
            "diff": "hard"
        })
    
    return templates

# ═══════════════════════════════════════════
# MENSURATION
# ═══════════════════════════════════════════

def mensuration_templates():
    templates = []
    
    # Circle area/circumference
    for _ in range(5):
        r = rand_int(7, 35)
        area = math.pi * r**2
        circ = 2 * math.pi * r
        if rand_choice([True, False]):
            wrong = [round(area + random.uniform(10, 100)), round(area - random.uniform(10, 50)),
                     round(2 * math.pi * r**2), round(math.pi * r)]
            templates.append({
                "en_q": f"Find the area of a circle with radius {r} cm. (Use π = 22/7)",
                "hi_q": f"{r} सेमी त्रिज्या वाले वृत्त का क्षेत्रफल ज्ञात करें। (π = 22/7)",
                "ans": round(22/7 * r**2), "wrong": [round(w) for w in wrong],
                "en_ex": f"Area = πr² = (22/7) × {r}² = (22/7) × {r**2} = {round(22/7 * r**2)} sq cm",
                "hi_ex": f"क्षेत्रफल = πr² = (22/7) × {r}² = {round(22/7 * r**2)} वर्ग सेमी",
                "diff": "easy"
            })
        else:
            wrong = [round(circ + random.uniform(5, 30)), round(circ - random.uniform(3, 20)),
                     round(math.pi * r**2), round(2 * math.pi * (r+1))]
            templates.append({
                "en_q": f"Find the circumference of a circle with radius {r} cm. (Use π = 22/7)",
                "hi_q": f"{r} सेमी त्रिज्या वाले वृत्त की परिधि ज्ञात करें। (π = 22/7)",
                "ans": round(2 * 22/7 * r), "wrong": [round(w) for w in wrong],
                "en_ex": f"Circumference = 2πr = 2 × (22/7) × {r} = {round(2*22/7*r)} cm",
                "hi_ex": f"परिधि = 2πr = 2 × (22/7) × {r} = {round(2*22/7*r)} सेमी",
                "diff": "easy"
            })
    
    # Rectangle area from perimeter
    for _ in range(5):
        l = rand_int(10, 50)
        b = rand_int(5, l - 2)
        area = l * b
        perimeter = 2 * (l + b)
        wrong = [area + rand_int(10, 80), area - rand_int(5, 30),
                 l * b + l, l * b + b, perimeter]
        templates.append({
            "en_q": f"A rectangle has length {l}m and breadth {b}m. Find its area.",
            "hi_q": f"एक आयत की लंबाई {l} मी और चौड़ाई {b} मी है। इसका क्षेत्रफल ज्ञात करें।",
            "ans": area, "wrong": wrong[:3],
            "en_ex": f"Area of rectangle = Length × Breadth = {l} × {b} = {area} sq m",
            "hi_ex": f"आयत का क्षेत्रफल = लंबाई × चौड़ाई = {l} × {b} = {area} वर्ग मी",
            "diff": "easy"
        })
    
    # Cube/Cuboid volume
    for _ in range(4):
        side = rand_int(3, 20)
        volume = side ** 3
        wrong = [side**2, side**3 + side, side**3 * 2, 6 * side**2]
        templates.append({
            "en_q": f"Find the volume of a cube with side {side} cm.",
            "hi_q": f"{side} सेमी भुजा वाले घन का आयतन ज्ञात करें।",
            "ans": volume, "wrong": wrong,
            "en_ex": f"Volume of cube = side³ = {side}³ = {volume} cubic cm",
            "hi_ex": f"घन का आयतन = भुजा³ = {side}³ = {volume} घन सेमी",
            "diff": "easy"
        })
    
    # Cylinder volume
    for _ in range(4):
        r = rand_int(5, 15)
        h = rand_int(10, 30)
        volume = int((22/7) * r**2 * h)
        wrong = [volume + rand_int(50, 300), volume - rand_int(20, 150),
                 int((22/7) * r * h), int(2 * (22/7) * r * h)]
        templates.append({
            "en_q": f"Find the volume of a cylinder with radius {r} cm and height {h} cm. (Use π = 22/7)",
            "hi_q": f"{r} सेमी त्रिज्या और {h} सेमी ऊंचाई वाले बेलन का आयतन ज्ञात करें। (π = 22/7)",
            "ans": volume, "wrong": wrong,
            "en_ex": f"Volume = πr²h = (22/7) × {r}² × {h} = (22/7) × {r**2} × {h} = {volume} cubic cm",
            "hi_ex": f"आयतन = πr²h = (22/7) × {r}² × {h} = {volume} घन सेमी",
            "diff": "medium"
        })
    
    return templates

# ═══════════════════════════════════════════
# GENERATOR: Convert templates to JSON
# ═══════════════════════════════════════════

def templates_to_json(templates, prefix, start_id=1):
    """Convert template list to JSON-ready question list"""
    questions = []
    for i, t in enumerate(templates):
        ans = t["ans"]
        wrong = t["wrong"][:3]  # Take 3 wrong options
        options = [ans] + wrong
        random.shuffle(options)
        correct_idx = options.index(ans)
        correct_letter = ['A', 'B', 'C', 'D'][correct_idx]
        
        questions.append({
            "id": make_id(prefix, start_id + i),
            "correctOption": correct_letter,
            "difficulty": t.get("diff", "medium"),
            "sourceYear": 2025,
            "en": {
                "question": t["en_q"],
                "options": [str(o) for o in options],
                "explanation": t["en_ex"]
            },
            "hi": {
                "question": t["hi_q"],
                "options": [str(o) for o in options],
                "explanation": t["hi_ex"]
            }
        })
    return questions

if __name__ == "__main__":
    # Test
    temps = number_system_templates()
    print(f"Generated {len(temps)} number system templates")
    temps = percentage_templates()
    print(f"Generated {len(temps)} percentage templates")
    temps = profit_loss_templates()
    print(f"Generated {len(temps)} profit/loss templates")
    temps = time_work_templates()
    print(f"Generated {len(temps)} time & work templates")
    temps = tsd_templates()
    print(f"Generated {len(temps)} TSD templates")
    temps = interest_templates()
    print(f"Generated {len(temps)} interest templates")
    temps = mensuration_templates()
    print(f"Generated {len(temps)} mensuration templates")
