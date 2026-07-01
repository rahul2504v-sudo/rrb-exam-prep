
import json, random, os, math
from pathlib import Path

BASE = Path("public/data/questions")

def randint(a, b): return random.randint(a, b)
def pick(arr): return random.choice(arr)

def format_options(correct, wrongs):
    opts = [str(correct)] + [str(w) for w in wrongs]
    random.shuffle(opts)
    correct_idx = opts.index(str(correct))
    return opts, ['A','B','C','D'][correct_idx]

def make_q(en_q, hi_q, correct, wrongs, en_expl, hi_expl, diff="medium"):
    opts, ans = format_options(correct, wrongs)
    return {
        "correctOption": ans, "difficulty": diff, "sourceYear": 2025,
        "en": {"question": en_q, "options": opts, "explanation": en_expl},
        "hi": {"question": hi_q, "options": opts, "explanation": hi_expl}
    }

def gen_percentage():
    qs = []
    for _ in range(50):
        p, base = randint(5,40), randint(200,5000)
        result = round(base*(1+p/100), 2)
        val = round(base*p/100, 2)
        r_str = str(int(result)) if result==int(result) else str(result)
        v_str = str(int(val)) if val==int(val) else str(val)
        if random.random() < 0.5:
            qs.append(make_q(
                f"A number increased by {p}% becomes {r_str}. Find the original number.",
                f"{p}% बढ़ने पर {r_str} हो जाती है। मूल संख्या ज्ञात करें।", str(base),
                [str(base+randint(10,100)), str(base-randint(10,100)), str(int(base*(1-p/100)))],
                f"Let x be original. x × (1+{p}/100) = {r_str}. x = {base}.", f"माना x मूल। x × (1+{p}/100) = {r_str}। x = {base}।", "medium"))
        else:
            qs.append(make_q(
                f"What is {p}% of {base}?", f"{base} का {p}% क्या है?", v_str,
                [str(base), str(base//2), str(base*2)],
                f"{p}% of {base} = {base} × {p}/100 = {v_str}.", f"{base} का {p}% = {base} × {p}/100 = {v_str}।", "easy"))
    return qs

def gen_profit_loss():
    qs = []
    for _ in range(50):
        cp, pct = randint(100,2000), randint(5,50)
        sp = round(cp*(1+pct/100), 2)
        sl = round(cp*(1-pct/100), 2)
        s_str = str(int(sp)) if sp==int(sp) else str(sp)
        sl_str = str(int(sl)) if sl==int(sl) else str(sl)
        if random.random() < 0.5:
            qs.append(make_q(f"Article CP Rs.{cp}, sold at {pct}% profit. Find SP.", f"{cp} रु. की वस्तु {pct}% लाभ पर बेची। वि.मू. ज्ञात करें।", s_str, [str(cp+randint(50,300)), str(cp), str(int(sp*0.9))], f"SP = CP×(1+profit%/100) = {cp}×{1+pct/100} = {sp}.", f"वि.मू. = {cp}×{1+pct/100} = {sp}।", "easy"))
        else:
            qs.append(make_q(f"Shopkeeper sells at {pct}% loss for Rs.{sl_str}. Find CP.", f"दुकानदार {pct}% हानि पर {sl_str} रु. में बेचता है। क्र.मू. ज्ञात करें।", str(cp), [str(cp+randint(50,200)), str(int(sl*1.1)), str(cp-randint(50,200))], f"CP = SP/(1-loss%/100) = {sl_str}/{1-pct/100} = {cp}.", f"क्र.मू. = {sl_str}/{1-pct/100} = {cp}।", "medium"))
    return qs

def gen_time_work():
    qs = []
    for _ in range(50):
        a, b = randint(5,30), randint(8,40)
        together = round(1/(1/a+1/b), 1)
        t_str = str(int(together)) if together==int(together) else str(together)
        if random.random() < 0.5:
            qs.append(make_q(f"A does work in {a} days, B in {b} days. Together?", f"A {a} दिन में, B {b} दिन में काम करता है। साथ मिलकर?", t_str, [str(round(together*1.5,1)), str(a+b), str(round(abs(a-b)/2,1))], f"1 day: 1/{a}+1/{b} = {round(1/a+1/b,4)}. Days = 1/({round(1/a+1/b,4)}) = {t_str}.", f"1 दिन: 1/{a}+1/{b} = {round(1/a+1/b,4)}। दिन = {t_str}।", "medium"))
        else:
            qs.append(make_q(f"A is twice as efficient as B. Together = {a} days. A alone?", f"A, B से दोगुना कुशल है। साथ = {a} दिन। A अकेला?", str(int(a*1.5)), [str(a*2), str(a), str(a*3)], f"B=1x, A=2x. Together=3x. 3x×{a}=1. x=1/{a*3}. A=1/(2x)={int(a*1.5)}.", f"B=1x, A=2x। दोनों=3x। 3x×{a}=1। x=1/{a*3}। A={int(a*1.5)} दिन।", "hard"))
    return qs

def gen_tsd():
    qs = []
    for _ in range(50):
        speed, t = randint(30,120), randint(1,8)
        dist = speed * t
        tl, pl = randint(100,500), randint(200,800)
        ts = randint(15,40)
        tt = round((tl+pl)/ts, 1)
        if random.random() < 0.5:
            qs.append(make_q(f"Car at {speed} km/hr for {t} hrs. Distance?", f"{speed} किमी/घंटा से {t} घंटे। दूरी?", f"{dist} km", [f"{dist*2} km", f"{dist//2} km", f"{speed+t} km"], f"Distance = Speed×Time = {speed}×{t} = {dist} km.", f"दूरी = {speed}×{t} = {dist} किमी।", "easy"))
        else:
            qs.append(make_q(f"Train {tl}m crosses platform {pl}m in {tt}s. Speed in km/hr?", f"{tl}मी ट्रेन {pl}मी प्लेटफॉर्म {tt}सेकंड में। चाल किमी/घंटा?", str(round((tl+pl)/tt*18/5,1)), [str(round((tl+pl)/tt*18/5*1.5,1)), "60", str(round((tl+pl)/tt,1))], f"Dist={tl}+{pl}={tl+pl}m. Speed={round((tl+pl)/tt,2)}m/s = {round((tl+pl)/tt*18/5,1)}km/hr.", f"दूरी={tl+pl}मी। चाल={round((tl+pl)/tt*18/5,1)}किमी/घंटा।", "medium"))
    return qs

def gen_si_ci():
    qs = []
    for _ in range(50):
        p, r, t = randint(1000,20000), randint(3,15), randint(1,5)
        si = round(p*r*t/100, 2)
        ci = round(p*(1+r/100)**t - p, 2)
        diff = round(ci-si, 2)
        si_s = str(int(si)) if si==int(si) else str(si)
        if random.random() < 0.5:
            qs.append(make_q(f"SI on Rs.{p} at {r}% for {t} years?", f"{p} रु. पर {r}% से {t} वर्ष का सा.ब्याज?", si_s, [str(p), str(int(si*1.5)), str(int(si*2))], f"SI = P×R×T/100 = {p}×{r}×{t}/100 = {si}.", f"सा.ब्याज = {p}×{r}×{t}/100 = {si}।", "easy"))
        else:
            qs.append(make_q(f"CI-SI difference on Rs.{p} at {r}% for {t} years?", f"{p} रु. पर {r}% से {t} वर्ष का च.ब्याज-सा.ब्याज अंतर?", str(diff), [str(round(diff*2,2)), str(round(diff*0.5,2)), str(si)], f"CI={p}×(1+{r}/100)^{t}-{p}={ci}. SI={si}. Diff={diff}.", f"च.ब्याज={ci}। सा.ब्याज={si}। अंतर={diff}।", "medium"))
    return qs

def gen_average():
    qs = []
    for _ in range(50):
        n = randint(5,20)
        vals = [randint(10,100) for _ in range(n)]
        avg = sum(vals)//n
        sub = vals[:6]
        a1 = round(sum(sub)/6,2)
        a1_s = str(int(a1)) if a1==int(a1) else str(a1)
        if random.random() < 0.5:
            qs.append(make_q(f"Average of: {', '.join(map(str,sub))}.", f"औसत: {', '.join(map(str,sub))}", a1_s, [str(randint(avg-20,avg-5)), str(randint(avg+5,avg+20)), str(max(sub))], f"Sum={sum(sub)}, Count=6, Avg={a1_s}.", f"योग={sum(sub)}, संख्या=6, औसत={a1_s}।", "easy"))
        else:
            na = round((sum(vals)-vals[0])/(n-1),2)
            na_s = str(int(na)) if na==int(na) else str(na)
            qs.append(make_q(f"{n} numbers avg={avg}. Remove {vals[0]}, new avg?", f"{n} संख्याओं का औसत={avg}। {vals[0]} हटाने पर नया औसत?", na_s, [str(avg), str(round(avg*0.9,2)), str(round(avg*1.1,2))], f"Sum={n}×{avg}={sum(vals)}. Remove {vals[0]}: sum={sum(vals)-vals[0]}, n={n-1}. Avg={na_s}.", f"योग={sum(vals)}। {vals[0]} हटाने पर: योग={sum(vals)-vals[0]}, n={n-1}। औसत={na_s}।", "medium"))
    return qs

def gen_ratio():
    qs = []
    for _ in range(50):
        r1, r2 = randint(2,8), randint(3,10)
        total = (r1+r2)*randint(10,100)
        p1, p2 = int(total*r1/(r1+r2)), total-int(total*r1/(r1+r2))
        if random.random() < 0.5:
            qs.append(make_q(f"Divide Rs.{total} in {r1}:{r2}. Larger share?", f"{total} रु. {r1}:{r2} में बांटें। बड़ा हिस्सा?", str(max(p1,p2)), [str(min(p1,p2)), str(total), str(total//2)], f"Parts={r1+r2}. {r1}/part: {p1}, {r2}/part: {p2}. Larger={max(p1,p2)}.", f"भाग={r1+r2}। हिस्से: {p1}, {p2}। बड़ा={max(p1,p2)}।", "easy"))
        else:
            r3 = randint(2,5)
            qs.append(make_q(f"A:B={r1}:{r2}, B:C={r2}:{r3}. A:C=?", f"A:B={r1}:{r2}, B:C={r2}:{r3}। A:C=?", f"{r1}:{r3}", [f"{r2}:{r1}", "1:1", f"{r1+r2}:{r1}"], f"B is {r2} in both. A:C = {r1}:{r3}.", f"B दोनों में {r2} है। A:C = {r1}:{r3}।", "medium"))
    return qs

def gen_mensuration():
    qs = []
    for _ in range(50):
        r = randint(7,30)
        l, b = randint(5,30), randint(4,25)
        area = round(22/7*r*r, 1)
        w = randint(1,3)
        path = 2*(l+b+2*w)*w
        if random.random() < 0.5:
            qs.append(make_q(f"Area of circle radius {r}cm (π=22/7)?", f"{r}सेमी त्रिज्या वृत्त का क्षेत्रफल (π=22/7)?", str(area), [str(round(2*22/7*r,1)), str(round(22/7*r,1)), str(r*r)], f"πr² = (22/7)×{r}² = {area} cm².", f"πr² = (22/7)×{r}² = {area} वर्ग सेमी।", "easy"))
        else:
            qs.append(make_q(f"Field {l}m×{b}m, {w}m path around. Path area?", f"{l}मी×{b}मी मैदान, {w}मी चौड़ा रास्ता। रास्ते का क्षेत्रफल?", str(path), [str(l*b), str(2*(l+b)), str((l+2*w)*(b+2*w))], f"Outer: {l+2*w}×{b+2*w}={(l+2*w)*(b+2*w)}. Inner: {l*b}. Path: {(l+2*w)*(b+2*w)-l*b}={path} m².", f"बाहरी={(l+2*w)*(b+2*w)}। भीतरी={l*b}। रास्ता={path} वर्ग मी।", "medium"))
    return qs

def gen_algebra():
    qs = []
    for _ in range(50):
        a = randint(1,15)
        x = randint(2,20)
        c = randint(5,30)
        rhs = a*x + c
        qs.append(make_q(f"Solve: {a}x + {c} = {rhs}. Find x.", f"हल करें: {a}x + {c} = {rhs}। x ज्ञात करें।", str(x), [str(x+randint(1,5)), str(x-randint(1,3)), str(rhs)], f"{a}x+{c}={rhs} → {a}x={rhs-c}={a*x} → x={x}.", f"{a}x+{c}={rhs} → {a}x={a*x} → x={x}।", "easy"))
    return qs

def gen_number_system():
    qs = []
    for _ in range(50):
        n = randint(1,100)
        r = randint(2,9)
        if random.random() < 0.5:
            qs.append(make_q(f"Is {n*7} divisible by 7?", f"क्या {n*7}, 7 से विभाज्य है?", "Yes", ["No", "Only if n is even", "Cannot determine"], f"{n*7} ÷ 7 = {n}, exactly divisible.", f"{n*7} ÷ 7 = {n}, पूर्णतः विभाज्य।", "easy"))
        else:
            u = (n**3)%10
            qs.append(make_q(f"Unit digit of {n}² × {n}?", f"{n}² × {n} का इकाई अंक?", str(u), [str((u+1)%10), str((u+5)%10), str((u+3)%10)], f"{n}²={n**2}(unit {str(n**2)[-1]}), ×{n}={n**3}(unit {u}).", f"{n}²={n**2}(इकाई {str(n**2)[-1]}), ×{n}={n**3}(इकाई {u})।", "easy"))
    return qs

# Map and run
GENS = {
    "ntpc/mathematics/number-system.json": gen_number_system,
    "ntpc/mathematics/percentage.json": gen_percentage,
    "ntpc/mathematics/profit-loss.json": gen_profit_loss,
    "ntpc/mathematics/time-work.json": gen_time_work,
    "ntpc/mathematics/time-speed-distance.json": gen_tsd,
    "ntpc/mathematics/simple-compound-interest.json": gen_si_ci,
    "ntpc/mathematics/average.json": gen_average,
    "ntpc/mathematics/ratio-proportion.json": gen_ratio,
    "ntpc/mathematics/mensuration.json": gen_mensuration,
    "ntpc/mathematics/algebra.json": gen_algebra,
}

def append_to_file(filepath, new_questions):
    filepath = BASE / filepath
    existing = json.loads(filepath.read_text(encoding='utf-8')) if filepath.exists() else []
    max_id = max((int(q['id'].split('-')[-1]) for q in existing), default=0)
    prefix = existing[0]['id'].rsplit('-',1)[0] if existing else "q"
    for i, q in enumerate(new_questions):
        q['id'] = f"{prefix}-{max_id+i+1:04d}"
    existing.extend(new_questions)
    filepath.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding='utf-8')
    return len(new_questions)

random.seed(42)
total = 0
for path, gen_fn in GENS.items():
    try:
        qs = gen_fn()
        added = append_to_file(path, qs)
        total += added
        print(f"  {path}: +{added}")
    except Exception as e:
        print(f"  {path}: ERROR - {e}")
        import traceback; traceback.print_exc()

print(f"\nTotal: {total}")
