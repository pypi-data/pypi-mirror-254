import pickle
from operator import itemgetter
from unicodedata import numeric

#FREKVENCA ZA ALNUM DICT
tf_for_alnum=10

# *********************************************
# datoteke
with open(r"data/denormalizator-nr100+.pickle", 'rb') as handle:
    nrvelike = pickle.load(handle)

with open(r"data/denormalizator-nrvelike_skl.pickle", 'rb') as handle:
    nrvelike_skl = pickle.load(handle)

with open(r"data/denormalizator-nrskupaj.pickle", 'rb') as handle:
    nrskupaj = pickle.load(handle)

with open(r"data/denormalizator-nr100.pickle", 'rb') as handle:
    nr100 = pickle.load(handle)

with open(r"data/denormalizator-nr100_skl.pickle", 'rb') as handle:
    nr100_skl = pickle.load(handle)

with open(r"data/denormalizator-nrvrst.pickle", 'rb') as handle:
    nrvrst = pickle.load(handle)

with open(r"data/lastnaimena.pickle", 'rb') as handle:
    lastnaimena = pickle.load(handle)

with open(r"data/alnum_dict.pickle", 'rb') as handle:
    alnum_dict = pickle.load(handle)

alnum_dict=dict([(x, y[0]) for x, y in alnum_dict.items() if y[1]>=tf_for_alnum])

decimalke = ["cela", "cele", "celi", "celih"]

meseci = ["januar", "januarja", "januarju", "januarjem", "februar", "februarja", "februarju", "februarjem", "marec", "marca", "marcu", "marcem",
          "aprilom", "april", "aprila", "aprilu", "maj", "maja", "maju", "majem", "junijem", "junij", "junija", "juniju", "julijem", "julij", "julija", "juliju",
          "avgustom", "avgust", "avgusta", "avgustu", "septembrom", "september", "septembra", "septembru", "oktobrom", "oktober", "oktobra", "oktobru",
          "novembrom", "november", "novembra", "novembru", "decembrom", "december", "decembra", "decembru"]

generic_time= ["ura", "uri", "uro", "ure",
            "stoletje", "stoletja", "stoletju", "stoletjem"]

additional_words=["člen", "člena", "členu", "členom", "členih", "odstavka", "odstavek", "odstavku", "odstavkom",
                    "točka", "točki", "točko", "paragraf", "paragrafa", "paragrafu", "paragrafom"]

allowed_suffixes = ["ega", "im", "em", "i"]

merske = {"meter": "m", "metra": "m", "metri": "m", "metre": "m", "metrov": "m",
          "gram": "g", "grama": "g", "grami": "g", "gramov": "g",
          "liter": "l", "litra": "l", "litri": "l", "litrov": "l",
          "tona": "t", "toni": "t", "tone": "t", "ton": "t",
          "bar": "b", "bara": "b", "bari": "b", "barov": "b",
          "newton": "N", "paskal": "Pa", "volt": "V", "watt": "W", "amper": "A",
          "sekunda": "s", "sekundi": "s", "sekunde": "s", "sekund": "s", "sekundo": "s",
          "minuta": "min", "minuti": "min", "minute": "min", "minut": "min", "minuto": "min",
          "ura": "h", "uri": "h", "ure": "h", "ur": "h", "uro": "h", "urah": "h",
          "kelvin": "K", "kelvinov": "K", "kelvini": "K", "kelvina": "K",
          "herc": "Hz", "herca": "Hz", "herce": "Hz", "hercev": "Hz", "herci": "Hz",
          "joule": "J", "farad": "F",
          "stopinja": "°", "stopinji": "°", "stopinje": "°", "stopinj": "°",
          "Celzija": "C",
          "promil": "‰", "promila": "‰", "promilov": "‰", "promili": "‰",
          "odstotek": "%", "odstotka": "%", "odstotke": "%", "odstotki": "%", "odstotkih": "%", "odstotkov": "%",
          "procent": "%", "procenta": "%", "procente": "%", "procenti": "%", "procentih": "%", "procentov": "%",
          "evro": "€", "evra": "€", "evrov": "€", "evri": "€", "evre": "€",
          "dolar": "$", "dolarja": "$", "dolarji": "$", "dolarjev": "$"}

merske_changed={"m": "metra", "g": "grama", "l": "litra", "t": "tone", "N": "newtona", "s": "sekunde", "min": "minute", "h": "ure", "K": "kelvina", "Hz": "herca", "J": "joula", "°": "stopinje", "‰": "probila", "%": "odstotka", "€": "evra", "$": "dolarja" }

merskeenote = list(merske.keys())

predpone = {'piko': 'p', 'nano': 'n', 'mikro': 'μ', 'mili': 'm', 'centi': 'c', 'deci': 'd', 'deka': 'da', 'hekto': 'h', 'kilo': 'k', 'mega': 'M', 'giga': 'G', 'tera': 'T'}

nazivi = {"doktorica": "dr.", "doktorice": "dr.", "doktorici": "dr.", "doktorico": "dr.",
          "medicine": "med.",
          "doktor": "dr.", "doktorja": "dr.", "doktorju": "dr.", "doktorjem": "dr.",
          "profesor": "prof.", "profesorja": "prof.", "profesorju": "prof.", "profesorjem": "prof.",
          "profesorica": "prof.", "profesorice": "prof.", "profesorici": "prof.", "profesorico": "prof.",
          "diplomiran": "dipl.", "diplomiranega": "dipl.", "diplomiranemu": "dipl.", "diplomiranim": "dipl.", "diplomiranem": "dipl.",
          "diplomirana": "dipl.", "diplomirane": "dipl.", "diplomirani": "dipl.", "diplomirano": "dipl.",
          "gospa": "ga.", "gospe": "ge.", "gospo": "go.",
          "gospodična": "gdč.", "gospodične": "gdč.", "gospodični": "gdč.", "gospodično": "gdč.",
          "gospod": "g.", "gospoda": "g.", "gospodu": "g.", "gospodom": "g.",
          "docent": "doc.", "docenta": "doc.", "docentu": "doc.", "docentom": "doc.", "docentka": "doc.", "docentke": "doc.", "docentki": "doc.", "docentko": "doc.",
          "specialist": "spec.", "specialista": "spec.", "specialistu": "spec.", "specialistom": "spec.",
          "specialistka": "spec.", "specialistke": "spec.", "specialistki": "spec.", "specialistko": "spec.",
          "asistent": "asist.", "asistenta": "asist.", "asistentu": "asist.",
          "asistentka": "asist.", "asistentke": "asist.", "asistentko": "asist.", "asistentki": "asist.",
          "primarij": "prim.", "primarija": "prim.", "primariju": "prim.", "primarijem": "prim.",
          "primarijka": "prim.", "primarijke": "prim.", "primarijki": "prim.", "primarijko": "prim.",
          "magister": "mag.", "magistra": "mag.", "magistru": "mag.", "magistrom": "mag.",
          "magistrica": "mag.", "magistrice": "mag.", "magistrico": "mag.", "magistrici": "mag.",
          "magistre": "mag.", "magistri": "mag.", "magistro": "mag.",
          "izredni": "izr.", "izrednega": "izr.", "izrednemu": "izr.", "izrednim": "izr.", "izrednem": "izr.", "izredna": "izr.", "izredne": "izr.", "izredno": "izr.",
          "redni": "red.", "rednega": "red.", "rednemu": "red.", "rednim": "red.", "rednem": "red.",
          "redne": "red.", "redno": "red.",
          "univerzitetni": "univ.", "univerzitetnega": "univ.", "univerzitetnemu": "univ.", "univerzitetnim": "univ.", "univerzitetnem": "univ.",
          "univerzitetna": "univ.", "univerzitetne": "univ.", "univerzitetno": "univ."}

other_abbr = {"oziroma": "oz.", "in tako dalje": "itd.", "in tako naprej": "itn.", "in podobno": "ipd."}
TI = ["tako imenovan", "tako imenovani", "tako imenovanega", "tako imenovanemu", "tako imenovanim", "tako imenovanem",
      "tako imenovanih", "tako imenovanima", "tako imenovana", "tako imenovne", "tako imenovanimi",
      "tako imenovano", "tako imenovane"]

podrocja = ["dermatologije", "gastroenterologije", "ginekologije", "nefrologije", "nevrologije", "oftalmologije", "onkologije", "ortopedije", "pulmologije", "radiologije", "geriatrije", "pediatrije"]

stst = {"devetnajststo": "1900", "osemnajststo": "1800", "sedemnajststo": "1700", "šestnajststo": "1600", "petnajststo": "1500"}

mejlingchars = {"podčrtaj": "_", "minus": "-", "pomišljaj": "-", "pika": ".", "afna": "@"}
mail_suffix = ["si", "com"]

symbols={"plus": "+", "minus": "-", "krat": "×"}
symbols_multiple={"je enako": "=", "plus minus": "±"}

imenovalci={"četrtina": "4", "četrtino": "4", "četrtine": "4", "četrtini": "4", "četrtin": "4",
            "tretjina": "3", "tretjino": "3", "tretjine": "3", "tretjini": "3", "tretjin": "3",
            "polovica": "2", "polovico": "2", "polovice": "2", "polovici": "2", "polovic": "2"}

imenovalci_risky={"četrtina": "4", "četrtino": "4", "četrtine": "4", "četrtini": "4", "četrtin": "4", "četrt": "4",
                "tretjina": "3", "tretjino": "3", "tretjine": "3", "tretjini": "3", "tretjin": "3",
                "polovica": "2", "polovico": "2", "polovice": "2", "polovici": "2", "polovic": "2", "pol": "2"}

deconstructed_fractions={(1, 4): "¼", (1, 2): "½", (3, 4): "¾", (1, 7): "⅐", (1, 9): "⅑", (1, 10): "⅒", (2, 3): "⅔", (1, 3): "⅓",
(1, 5): "⅕", (2, 5): "⅖", (3, 5): "⅗", (4, 5): "⅘", (1, 6): "⅙", (5, 6): "⅚", (1, 8): "⅛", (3, 8): "⅜", (5, 8): "⅝", (7, 8): "⅞", (0, 3): "↉"}

#NOTE: include_special_chars overweighs convert_to_decimal
def make_fraction(n1, n2, include_special_chars=True, convert_to_decimal=False):
    if include_special_chars:
        try:
            return deconstructed_fractions[(int(n1), int(n2))]
        except KeyError:
            return str(n1)+"/"+str(n2)
    if convert_to_decimal:
        return str(int(n1)/int(n2)).replace(".", ",")
    else:
        return str(n1)+"/"+str(n2)

def get_key(val, dikš):
    for key, value in dikš.items():
        if val == value:
            return key
    
def next(i, tokens, howmuch=1):
    if i+howmuch<len(tokens):
        return tokens[i+howmuch]
    else:
        return ""


def pika(t):
    if t[-1] == ".":
        return t
    else:
        return t + "."

def clean_whitespace(sent):
    return " ".join(sent.split())


def nička(t):
    if len(t) == 2:
        return t
    else:
        return "0" + t


def isordinal(tok):
    if tok[:-1].isnumeric() and tok[-1] == ".":
        return True
    else:
        return False


def is_fraction(tok):
    if tok in ["¼", "½", "¾", "⅐", "⅑", "⅒", "⅔", "⅓", "⅕", "⅖", "⅗", "⅘", "⅙", "⅚", "⅛", "⅜", "⅝", "⅞", "⅟", "↉"]:
        return True
    else:
        return False


def isnum(tok):
    if is_fraction(tok):
        return False
    elif tok.isnumeric():
        return True
    elif isordinal(tok):
        return True
    else:
        return False


def isnumber(tok, include_fracs=False):
    if tok.isnumeric() and not is_fraction(tok):
        return True
    elif "," in tok and tok.replace(",", "").isnumeric():
        return True
    elif include_fracs==True and is_fraction(tok):
        return True
    else:
        return False


def isabbr(tok):
    if tok[-1] == "." and tok[:-1].isalpha():
        return True
    else:
        return False


def is_mixed_case(tok):
    if tok.isalpha():
        if tok.islower():
            return False
        elif tok.isupper():
            return False
        elif tok.istitle():
            return False
        else:
            return True
    else:
        return False


def slicer(listsent, i, context=3, ctype="all", include_self=False, include_index=False):
    if ctype == "all":
        if len(listsent) < (context * 2):
            if include_self:
                sliced_sent = listsent[:i] + listsent[i:]
                C=len(listsent[:i])
            else:
                sliced_sent = listsent[:i] + listsent[i + 1:]
        else:
            if i < context:
                if include_self:
                    sliced_sent = listsent[:i] + listsent[i:i + context + 1]
                    C=len(listsent[:i])
                else:
                    sliced_sent = listsent[:i] + listsent[i + 1:i + context + 1]
            elif i > (len(listsent) - context):
                if include_self:
                    sliced_sent = listsent[i - context:i] + listsent[i:]
                    C=len(listsent[i - context:i])
                else:
                    sliced_sent = listsent[i - context:i] + listsent[i + 1:]
            else:
                if include_self:
                    sliced_sent = listsent[i - context:i] + listsent[i:i + context + 1]
                    C=len(listsent[i - context:i])
                else:
                    sliced_sent = listsent[i - context:i] + listsent[i + 1:i + context + 1]
    elif ctype == "R":
        if len(listsent) < (context * 2):
            if include_self:
                sliced_sent = listsent[i:]
                C=0
            else:
                sliced_sent = listsent[i + 1:]
        else:
            if i < context:
                if include_self:
                    sliced_sent = listsent[i:i + context + 1]
                    C=0
                else:
                    sliced_sent = listsent[i + 1:i + context + 1]
            elif i > (len(listsent) - context):
                if include_self:
                    sliced_sent = listsent[i:]
                    C=0
                else:
                    sliced_sent = listsent[i + 1:]
            else:
                if include_self:
                    sliced_sent = listsent[i:i + context + 1]
                    C=0
                else:
                    sliced_sent = listsent[i + 1:i + context + 1]
    elif ctype == "L":
        if len(listsent) < (context * 2):
            if include_self:
                sliced_sent = listsent[:i + 1]
                C=len(listsent[:i + 1])

            else:
                sliced_sent = listsent[:i]
        else:
            if i < context:
                if include_self:
                    sliced_sent = listsent[:i + 1]
                    C=len(sliced_sent)
                else:
                    sliced_sent = listsent[:i]
            elif i > (len(listsent) - context):
                if include_self:
                    sliced_sent = listsent[i - context:i + 1]
                    C=len(sliced_sent)
                else:
                    sliced_sent = listsent[i - context:i]
            else:
                if include_self:
                    sliced_sent = listsent[i - context:i + 1]
                    C=len(sliced_sent)
                else:
                    sliced_sent = listsent[i - context:i]
    if include_index and include_self:
        return(sliced_sent, C)
    return sliced_sent


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + 1)
        n -= 1
    return start


def find_all(t, toklist):
    return [i for i, ltr in enumerate(toklist) if ltr == t]


def contains_date(words):
    if any([x.microtype in ["date"] for x in words]): return True
    return False

def is_sublist(small, big):
    for i in range(len(big) - len(small) + 1):
        if small == big[i:i + len(small)]: return True
    return False

def where_sublist(small, big):
    results = []
    for i in range(len(big) - len(small) + 1):
        if small == big[i:i + len(small)]:
            results.append([i for i in range(i, i + len(small))])
    return results


def first_zero(t):
    if is_fraction(t):
        return False
    elif t.isnumeric():
        if str(int(t)) == t:
            return False
        else:
            return True
    elif isordinal(t):
        if str(int(t.replace(".", ""))) == t.replace(".", ""):
            return False
        else:
            return True

#sequence of numbers
def is_nr_seq(pck):
    toklist=pck[0]
    i=pck[1]
    t=toklist[i]
    if t.isnumeric() and not is_fraction(t):
        nrs = []
        while i < len(toklist) and toklist[i].isnumeric() and not is_fraction(toklist[i]):
            nrs.append(toklist[i])
            i += 1
        if len(nrs) > 2:
            return True
        i -=  1
        while i > 0 and toklist[i].isnumeric() and not is_fraction(toklist[i]):
            nrs = [toklist[i]] + nrs
            i -= 1
        if len(nrs) > 2:
            return True
        else:
            return False
    else:
        return False

#should this number stay in digits form for stylistic reasons?
def stays_number(i, sent):
    wrd=sent.get(i)
    if wrd.type=="num":
        if sent.get(i).microtype: return True
        elif "+" in wrd.index: return True
        elif sent.get(i).subtype=="decimal": return True
        elif first_zero(sent.get(i).denormalized): return True
        elif str(sent.get(i).denormalized)[-6:] == "000000" and str(sent.get(i).denormalized) not in ["1000000", "000000", "0000000"]: return True
        elif not wrd.subtype and int(sent.get(i).denormalized.replace(".", "")) not in [100, 1000, 1000000] and int(sent.get(i).denormalized.replace(".", "")) > 10: return True
        elif wrd.subtype=="ordinal" and int(sent.get(i).denormalized.replace(".", "")) < 11 and sent.get(i).text.endswith("ič"): return False
        elif not wrd.subtype=="ordinal" and "°C" in slicer([x.denormalized for x in sent.words], i, 7): return True
        elif is_nr_seq(slicer([x.denormalized for x in sent.words], i, context=3, include_self=True, include_index=True)): return True
        #1000 milijonov
        elif i>0 and sent.get(i).denormalized in ["1000", "1000000"] and sent.get(i-1).type=="num" and not is_fraction(sent.get(i-1).denormalized): return False
        elif (not wrd.subtype or wrd.subtype=="ordinal") and int(wrd.denormalized.replace(".", ""))>10 and not int(sent.get(i).denormalized.replace(".", "")) in [100, 1000, 1000000]: return True
        # ali so v okolici številke, ki morajo ostat številke
        elif (int(sent.get(i).denormalized.replace(".", "")) < 11 or int(sent.get(i).denormalized.replace(".", "")) in [100, 1000, 1000000]):
            #če je navadna številka in kakšna druga navadna številka ostane številka
            if not sent.get(i).subtype and any([stays_number(x, sent) for x in possible_range(i + 1, i + 3, sent.words) if sent.get(x).type=="num" and (not sent.get(x).subtype or sent.get(x).subtype=="decimal")]):
                return True
            #če ni navadna številka in je v bližini iste vrste številka, ki ostane številka
            elif sent.get(i).subtype and any([stays_number(x, sent) for x in possible_range(i + 1, i + 3, sent.words) if sent.get(x).type=="num" and sent.get(x).subtype==sent.get(i).subtype]):
                return True
            return False
        return False

def possible_range(n1, n2, toklist):
    return [x for x in [i for i in range(n1, n2)] if x < len(toklist) and x >= 0]


def sum_nrs(listofnumbers):
    tisočice = find_all("1000", listofnumbers)
    miljonice = find_all("1000000", listofnumbers)
    combo = tisočice + miljonice
    others = [i for i in range(len(listofnumbers) - 1) if i not in combo]
    mio = 1000000
    k = 1000
    res = 0
    mio_avalable = False
    k_available = False
    if len(miljonice) != 0:
        mio_avalable = True
    if len(tisočice) != 0:
        k_available = True

    for i in range(len(listofnumbers)):
        nr = int(listofnumbers[i])
        if (i in miljonice or i in tisočice):
            if i == 0:
                res = nr
            elif int(listofnumbers[i - 1]) == 1000000:
                res += 1000
            else:
                pass
        elif (i not in miljonice and i not in tisočice) and i + 1 in miljonice and mio_avalable == True:
            res += nr * mio
            mio_avalable = False
        elif (i not in miljonice and i not in tisočice) and i + 1 in tisočice and k_available == True:
            res += nr * k
            k_available = False
        else:
            res += nr
    return res

def parse_units(tok):
    for enota in merske.keys():
        if tok.endswith(enota):
            unit_part=enota
            if tok==unit_part:
                return ("", unit_part)
            if tok != enota:
                pref=tok[:len(unit_part)-1]
                if pref in predpone:
                    return((pref, unit_part))

def small(strnr):
    if 0 < int(strnr) < 1000: return True
    return False

def nr_parser(nrswindexes):
    nrs, inx = nrswindexes
    results = []
    if "1000000" in nrs:
        indices = find_all("1000000", nrs)
        for i in indices:
            yes = ["1000000"]
            first = i
            last = i
            add = []
            if i > 0 and small(nrs[i - 1]):
                yes = [nrs[i - 1]] + yes
                first = i - 1
            context = slicer(nrs, i, context=2, ctype="R")
            if "1000" in context:
                add = context[:context.index("1000") + 1]
                yes += add
                last = i + len(add)
            if i + len(add) < len(nrs) - 1 and small(nrs[i + len(add) + 1]):
                yes += [nrs[i + len(add) + 1]]
                last += 1
            results.append((yes, [i+inx[0] for i in range(first, last + 1)]))
    if "1000" in nrs:
        indices = find_all("1000", nrs)
        for i in indices:
            yes = ["1000"]
            first = i
            last = i
            if i > 0 and small(nrs[i - 1]):
                yes = [nrs[i - 1]] + yes
                first = i - 1
            if i < len(nrs) - 1 and small(nrs[i + 1]):
                yes += [nrs[i + 1]]
                last += 1
            if (len(results) == 0 or (len(results) > 0) and not any([is_sublist([i+inx[0] for i in range(first, last + 1)], X[1]) for X in results])):
                results.append((yes, [i+inx[0] for i in range(first, last + 1)]))
    additional = [([nrs[i]], [i+inx[0]]) for i in range(len(nrs)) if i+inx[0] not in sum([x[1] for x in results], [])]
    if len(additional) != 0:
        results.extend(additional)
    return sorted(results, key=itemgetter(1))

def is_overlap(lists, bool_only=True):
    allelem = sum(lists, [])
    if len(allelem) != len(set(allelem)):
        if bool_only:
            return True
        return [x for x in list(set(allelem)) if allelem.count(x) != 1]
    else:
        if bool_only:
            return False
        else:
            return [x for x in list(set(allelem)) if allelem.count(x) != 1]

def same_type_nr(nr1, nr2):
    if is_fraction(nr1) or is_fraction(nr2):
        return False
    elif nr1.isnumeric() and nr2.isnumeric():
        return True
    elif isordinal(nr1) and isordinal(nr2):
        return True
    else:
        return False

def dot_in_the_middle(tok, dot="."):
    if tok.count(dot)==1 and tok.index(dot)!=0 and tok.index(dot)!=len(tok)-1:
        return True
    return False