import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def pile_plan(lengthCm, widthCm, heightCm):
    if not (lengthCm > 0) or not (widthCm > 0) or not (heightCm > 0):
        return {"error": "the pile dimensions must be positive"}
    liters = round1(lengthCm * widthCm * heightCm / 3 / 1000)
    if liters < 500: verdict = "a weekend pile"
    elif liters <= 2000: verdict = "a truckload pile"
    else: verdict = "a fleet pile"
    return {"liters": liters, "verdict": verdict}

def trip_plan(pileLiters, barrowLiters):
    if not (pileLiters > 0) or not (barrowLiters > 0):
        return {"error": "the pile and the barrow must be positive"}
    trips = math.ceil(pileLiters / barrowLiters)
    last_load = round1(pileLiters - (trips - 1) * barrowLiters)
    if trips == 1: verdict = "one trip"
    elif trips <= 6: verdict = "a short haul"
    else: verdict = "a long haul"
    return {"trips": trips, "lastLoad": last_load, "verdict": verdict}

def load_plan(barrowLiters, densityKgPerL):
    if not (barrowLiters > 0) or not (densityKgPerL > 0):
        return {"error": "the barrow and the density must be positive"}
    kg = round1(barrowLiters * densityKgPerL)
    if kg < 25: verdict = "a light load"
    elif kg <= 60: verdict = "a working load"
    else: verdict = "a heavy load"
    return {"kg": kg, "verdict": verdict}

def render_pile(r, lengthCm, widthCm, heightCm):
    return ("A pile " + fmt(lengthCm) + " cm by " + fmt(widthCm) + " cm by " + fmt(heightCm)
            + " cm holds " + fmt(r["liters"]) + " liters by the labeled cone rule - " + r["verdict"] + ".")

def render_trip(r, pileLiters, barrowLiters):
    return ("A pile of " + fmt(pileLiters) + " liters in a labeled " + fmt(barrowLiters) + " liter barrow takes "
            + plural(r["trips"], "trip") + ", the last one carrying " + fmt(r["lastLoad"]) + " liters - " + r["verdict"] + ".")

def render_load(r, barrowLiters, densityKgPerL):
    return ("A labeled " + fmt(barrowLiters) + " liter barrow at " + fmt(densityKgPerL) + " kg a liter carries "
            + fmt(r["kg"]) + " kg - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[200,150,80],[120,100,60],[200,0,80],[0,150,80],[200,150,0],[300,200,100],[310,200,100],[100,100,50],[150,120,90],[180.5,140,70]]:
    add("pilePlan", pile_plan, render_pile, a)
for a in [[800,90],[240,90],[90,90],[0,90],[800,0],[540,90],[550,90],[1000,120],[50,90],[95.5,90]]:
    add("tripPlan", trip_plan, render_trip, a)
for a in [[90,1.2],[90,0.4],[0,1.2],[90,0],[60,0.4],[65,0.4],[90,1.6],[80,0.75],[81,0.75],[50,0.49]]:
    add("loadPlan", load_plan, render_load, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
