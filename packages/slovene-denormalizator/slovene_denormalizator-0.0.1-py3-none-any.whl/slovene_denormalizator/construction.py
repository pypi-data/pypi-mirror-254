from .denormalizer_helpers import *

#Nrs
def de_number_bigPlus(sent):
    Nrs = [x for x in nrvelike_skl.keys() if is_sublist(x.split(), [x.denormalized.lower() for x in sent.words])]
    if Nrs:
        for num in nrvelike_skl.keys():
            if is_sublist(num.split(), [x.denormalized.lower() for x in sent.words]):
                indices = where_sublist(num.split(), [x.denormalized.lower() for x in sent.words])
                for indexes in indices:
                    res = nrvelike_skl[num]
                    wrd=sent.get(indexes[0])
                    sent.merge(indexes)
                    wrd.denormalized=res
                    wrd.type="num"
                    sent.remove_word(indexes[1:])
 
def de_number_big(sent):
    Nrs = [x for x in nrvelike.keys() if is_sublist(x.split(), [x.denormalized.lower() for x in sent.words])]
    if Nrs:
        for num in Nrs:
            if is_sublist(num.split(), [x.denormalized.lower() for x in sent.words]):
                indices = where_sublist(num.split(), [x.denormalized.lower() for x in sent.words])
                for indexes in indices:
                    res = nrvelike[num]
                    wrd=sent.get(indexes[0])
                    wrd=sent.get(indexes[0])
                    sent.merge(indexes)
                    wrd.denormalized=res
                    wrd.type="num"
                    sent.remove_word(indexes[1:])

def de_number_one(sent):
    for i in range(len(sent.words)):
        wrd=sent.get(i)
        if wrd.denormalized.lower() in nr100_skl.keys():
            if len([x for x in slicer([x.denormalized.lower() for x in sent.words], i, context=3, ctype="R") if x in meseci+generic_time]) != 0 and nr100_skl[wrd.denormalized.lower()] not in ["1", "2", "3", "4"]:
                wrd.denormalized=pika(nr100_skl[wrd.denormalized.lower()])
                wrd.type="num"
                wrd.subtype="ordinal"
            else:
                wrd.denormalized=nr100_skl[wrd.denormalized.lower()]
                wrd.type="num"
        elif wrd.denormalized.lower() in nrvrst.keys():
            wrd.denormalized=nrvrst[wrd.denormalized.lower()]
            wrd.type="num"
            wrd.subtype="ordinal"
        elif wrd.denormalized.lower() in nr100.keys():
            wrd.denormalized=nr100[wrd.denormalized.lower()]
            wrd.type="num"

# devetnajststo
def de_number_specialyears(sent):
    if any(t.endswith("ststo") for t in sent.tokens):
        i = 0
        while i < (len(sent.words)):
            if i < len(sent.words) - 1 and sent.get(i).denormalized.lower() in stst.keys() and sent.get(i+1).denormalized.lower() in nr100.keys():
                wrd=sent.get(i)
                nextw = sent.get(i+1).denormalized.lower()
                repl = str(int(stst[wrd.denormalized.lower()]) + int(nr100[nextw]))
                wrd.denormalized=repl
                sent.merge([i, i+1])
                wrd.type="year"
                sent.remove_word(i+1)
            i += 1

def basic_denumberer(sent):
    de_number_specialyears(sent)
    de_number_bigPlus(sent)
    de_number_big(sent)
    de_number_one(sent)

def sum_deco_oridnals(sent):
    i=0
    while i<len(sent.words):
        wrd=sent.get(i)     
        tok=wrd.denormalized
        if i<len(sent.words)-1 and tok.isnumeric() and not is_fraction(tok) and isordinal(sent.get(i+1).denormalized) and len(tok)>2 and all(chars=="0" for chars in tok[len(sent.get(i+1).denormalized):]):
            if i>0 and sent.get(i-1).denormalized.isnumeric() and not is_fraction(sent.get(i-1).denormalized) and 1000>int(sent.get(i-1).denormalized)>1:
                res=pika(str(int(sent.get(i-1).denormalized)*int(tok)+int(sent.get(i+1).denormalized[:-1])))
                sent.get(i-1).type="num"
                sent.get(i-1).denormalized=res
                sent.merge([i-1, i, i+1])
                sent.remove_word([i, i+1])
            else:
                res=pika(str(int(tok)+int(sent.get(i+1).denormalized[:-1])))
                wrd.type="num"
                wrd.denormalized=res
                wrd.index="+".join([wrd.index, sent.get(i+1).index])
                sent.remove_word(i+1)
        i+=1

#leta 20 20, 2 3
def sum_deco_years(sent):
    i=0
    while i<len(sent.words):
        wrd=sent.get(i)
        tok=wrd.denormalized
        if 0<i<len(sent.words)-1 and ((tok=="2" and next(i, [x.denormalized for x in sent.words]).isnumeric() and 0<int(next(i, [x.denormalized for x in sent.words]))<50) or (tok=="20" and next(i, [x.denormalized for x in sent.words])=="20")) and (next(i, [x.denormalized for x in sent.words], -1) in ["leta", "leto", "letu", "letom"]+meseci or (i>1 and contains_date(sent.words[i-2:i]))):
            res="20"+nička(next(i, sent.tokens))
            wrd.denormalized=res
            wrd.type="col_year"
            sent.merge([i, i+1])
            sent.remove_word(i+1)
        i+=1

def construct_hours(sent):
    i=0
    while i < (len(sent.words)):
        wrd=sent.get(i)
        if i < len(sent.words) - 1 and (isnum(sent.get(i).denormalized) and 0 <= int(sent.get(i).denormalized.replace(".", "")) <= 24) \
            and (isnum(sent.get(i+1).denormalized) and not isordinal(sent.get(i+1).denormalized) and 0 <= int(sent.get(i+1).denormalized) < 60) \
            and \
                (([x for x in slicer([x.denormalized for x in sent.words], i, context=2, ctype="L") if x.lower() in ["ob", "do", "od", "danes", "jutri"]] ) \
                    or \
                    (([x for x in slicer([x.denormalized for x in sent.words], i, context=1, ctype="L") if x.lower() in ["okrog", "okoli"]]) \
                        and ([x for x in slicer([x.denormalized for x in sent.words], i, context=2) if x.lower() in ["zjutraj", "popoldne", "opoldne", "ponoči", "dopoldne"]]) \
                        and sent.get(i+1).denormalized in ["00", "0", "30"]) \
                    or  \
                    len([x for x in slicer([x.denormalized for x in sent.words], i, ctype="R") if x.lower() in ["včeraj", "danes", "jutri"]]) != 0):
            
            if sent.get(i+1).denormalized == "0":
                if sent.get(i+2).denormalized.isnumeric() and len(sent.get(i+2).denormalized) == 1:
                    wrd.denormalized = ("".join([pika(sent.get(i).denormalized), sent.get(i+1).denormalized + sent.get(i+2).denormalized]))
                    sent.merge([i, i+1, i+2])
                    sent.remove_word([i+1, i+2])
                    wrd.type="hour"
                    
                else:
                    wrd.denormalized = "".join([pika(wrd.denormalized), nička(sent.get(i+1).denormalized)])
                    sent.merge([i, i+1])
                    wrd.type="hour"
                    sent.remove_word(i+1)

            else:
                wrd.denormalized = "".join([pika(wrd.denormalized), nička(sent.get(i + 1).denormalized)])
                sent.merge([i, i+1])
                sent.remove_word(i+1)
                wrd.type="hour"
                
        elif i < len(sent.words) - 1 and (wrd.denormalized.lower() == "pol") and isnum(sent.get(i+1).denormalized) and (1 <= int(sent.get(i+1).denormalized.replace(".", "")) < 25) \
                and ((len([x for x in slicer([x.denormalized for x in sent.words], i, context=2, ctype="L") if x.lower() in ["ob", "do", "od", "danes", "jutri"]]) != 0 and not isnum(sent.get(i+1).denormalized)) \
                     or (len([x for x in slicer([x.denormalized for x in sent.words], i, context=1, ctype="L") if x.lower() in ["okrog", "okoli"]]) != 0 \
                         or len([x for x in slicer([x.denormalized for x in sent.words], i, ctype="R") if x.lower() in ["ura", "uro", "uri", "ure", "danes", "jutri"]]) != 0)):
            wrd.denormalized = "".join([pika(str(int(sent.get(i + 1).denormalized.replace(".", "")) - 1)), "30"])
            wrd.type="hour"
            sent.merge([i, i+1])
            sent.remove_word(i+1)
            i += 1
        elif i < len(sent.words) - 4 and isordinal(wrd.denormalized) and sent.get(i+1).denormalized.lower() == "uri" and sent.get(i+4).denormalized.lower() in ["minut", "minuta", "minuti", "minute"] and \
            sent.get(i+2).denormalized.lower() == "in" and isnum(sent.get(i + 3).denormalized):
            wrd.denormalized = "".join([pika(wrd.denormalized), nička(sent.get(i+3).denormalized)])
            wrd.type="hour"
            sent.merge([i, i+1, i+2, i+3, i+4])
            sent.remove_word([i+1, i+2, i+3, i+4])
        i += 1
    
def construct_fractions(sent):
    i = 0
    while i < (len(sent.words)):
        wrd=sent.get(i)
        tok=wrd.denormalized
        if i<len(sent.words)-1 and tok.isnumeric() and not is_fraction(tok) and sent.get(i+1).denormalized in imenovalci.keys():
            wrd.denormalized=make_fraction(tok, imenovalci[sent.get(i+1).denormalized])
            sent.merge([i, i+1])
            sent.remove_word(i+1)
            wrd.subtype="fraction"
            i+=1
        elif tok in imenovalci.keys():
            wrd.denormalized=make_fraction(1, imenovalci[tok])
            wrd.subtype="fraction"
        elif i<len(sent.words)-1 and tok.lower() in ["pol"] and (sent.get(i+1).denormalized in merskeenote or sent.get(i+1).denormalized in ["tablete", "tbl"]):
            wrd.denormalized=make_fraction(1, 2)
            wrd.subtype="fraction"
        i += 1

def construct_units(sent, include_units, include_fractions):
    if "celzija" in [x.denormalized.lower() for x in sent.words]:
        i=0
        while i<len(sent.words):
            if i>0 and sent.get(i).denormalized.lower()=="celzija" and sent.get(i-1).denormalized.lower().startswith("stopinj"):
                merskeenote.append(" ".join([sent.get(i-1).denormalized, sent.get(i).denormalized]))
                sent.get(i-1).type="unit"
                if include_units:
                    sent.get(i-1).denormalized="°C"
                    sent.merge([i-1, i])
                    sent.remove_word(i)
                i-=1
            i+=1
    for i in range(len(sent.words)):
        wrd=sent.get(i)
        tok = wrd.denormalized
        if (i > 0 and isnumber(sent.get(i-1).denormalized, True)) or (i > 1 and sent.get(i-2).type and sent.get(i-2).type in ["num", "unit"] and sent.get(i-1).denormalized.lower() == "na"):
            for enota in merske.keys():
                if tok.endswith(enota):
                    temp = ((tok).replace(enota, merske[enota]))
                    if tok != enota and temp[:-len(merske[enota])] in predpone.keys():
                        wrd.type="unit"
                        if include_units: wrd.denormalized=predpone[temp[:-len(merske[enota])]]+temp[-len(merske[enota]):]
                    elif tok==enota:
                        wrd.type="unit"
                        if include_units: wrd.denormalized=temp
    
        elif (i > 0 and sent.get(i-1).denormalized.lower() in imenovalci_risky.keys()):
            for enota in merske.keys():
                if tok.endswith(enota):
                    temp = ((tok).replace(enota, merske[enota]))
                    if tok != enota and temp[:-len(merske[enota])] in predpone.keys():
                        wrd.type="unit"
                        if include_units: wrd.denormalized=predpone[temp[:-len(merske[enota])]]+temp[-len(merske[enota]):]
                    elif tok==enota:
                        wrd.type="unit"
                        if include_units: wrd.denormalized=temp
                    if include_fractions: sent.get(i-1).denormalized = make_fraction(1, imenovalci_risky[sent.get(i-1).denormalized.lower()])
        
def number_chaos_resolver(sent):
    i = 0
    Indexes = []
    while i < len(sent.words):
        wrd=sent.get(i)
        t = wrd.denormalized
        subnr = []
        Indexes = []
        if t.isnumeric() and not is_fraction(t):
            checker=0
            while i+checker < len(sent.words) and sent.get(i+checker).denormalized.isnumeric() and not is_fraction(sent.get(i+checker).denormalized):
                subnr.append(sent.get(i+checker).denormalized)
                Indexes.append(i+checker)
                checker += 1
            if len(subnr)==1:
                pass
            else:
                el=(subnr, Indexes)
                Numbers = nr_parser(el)
                removed=0
                if not is_overlap([x[1] for x in Numbers], bool_only=True):
                    for el in Numbers:
                        sent.get(el[1][0]-removed).denormalized=str(sum_nrs(el[0]))
                        sent.merge([x-removed for x in el[1]])
                        sent.remove_word([x-removed for x in el[1][1:]])
                        removed+=len(el[1][1:])
                else:
                    for nrind in range(len(Numbers)):
                        overlap = is_overlap([Numbers[nrind][1], Numbers[nrind + 1][1]], bool_only=False) if nrind<len(Numbers)-1 else None
                        el=Numbers[nrind]  
                        if overlap:
                            I = overlap[0]
                            if (not sent.pause) or (sent.pause and sent.pauseValues[int(sent.get(I-1).index)]<=sent.pauseValues[int(sent.get(I).index)]):
                                sent.get(el[1][0]-removed).denormalized=str(sum_nrs(el[0]))
                                sent.merge([x-removed for x in el[1]])
                                sent.remove_word([x-removed for x in el[1][1:]])
                                removed+=len(el[1][1:])                           
                                Numbers[nrind + 1]=[x[1:] for x in Numbers[nrind + 1]]
                            else:
                                Numbers[nrind]=[x[:-1] for x in Numbers[nrind]]
                                el=Numbers[nrind]     
                                sent.get(el[1][0]-removed).denormalized=str(sum_nrs(el[0]))
                                sent.merge([x-removed for x in el[1]])
                                sent.remove_word([x-removed for x in el[1][1:]])
                                removed+=len(el[1][1:])                           
                                
                        else:
                            sent.get(el[1][0]-removed).denormalized=str(sum_nrs(el[0]))
                            sent.merge([x-removed for x in el[1]])
                            sent.remove_word([x-removed for x in el[1][1:]])
                            removed+=len(el[1][1:])
        i += 1

def solo_numbers(sent):
    i = 0
    while i < len(sent.words):
        wrd=sent.get(i)
        origi = i
        if i < len(sent.words) - 1 and wrd.denormalized.isnumeric() and not is_fraction(wrd.denormalized) and int(wrd.denormalized) < 10 and sent.get(i+1).denormalized.isnumeric() and not is_fraction(sent.get(i+1).denormalized) and int(sent.get(i+1).denormalized) < 10:
            res = ""
            inds = []
            while sent.get(i).denormalized.isnumeric() and not is_fraction(sent.get(i).denormalized) and int(sent.get(i).denormalized) < 10 and i < len(sent.words):
                res += sent.get(i).denormalized
                inds.append(i)
                if i < len(sent.words) - 1 and sent.get(i+1).denormalized.isnumeric() and not is_fraction(sent.get(i+1).denormalized) and int(sent.get(i+1).denormalized) < 10:
                    i += 1
                else:
                    break
            wrd.denormalized=res
            sent.merge(inds)
            sent.remove_word(inds[1:])
        i = origi+1


def decimal_creator(sent):
    if any(w in decimalke for w in [x.denormalized for x in sent.words]):
        i = 0
        while i < len(sent.words):
            wrd=sent.get(i)
            res = wrd.denormalized
            if i < len(sent.words) - 2 and wrd.denormalized.isnumeric() and not is_fraction(wrd.denormalized) and sent.get(i+1).denormalized in decimalke and sent.get(i+2).denormalized.isnumeric() and not is_fraction(sent.get(i+2).denormalized):
                res = wrd.denormalized + ','
                if sent.get(i+2).denormalized.endswith("000000"):
                    res += sent.get(i+2).denormalized[:-6]
                    wrd.denormalized=res
                    wrd.subtype="decimal"
                    sent.merge([i, i+1])
                    sent.remove_word(i+1)
                    sent.get(i+1).denormalized="milijona"
                    sent.get(i+1).type="mio"

                    sent.get(i).text += " "+sent.get(i+1).text.split()[0]
                    sent.get(i+1).text = sent.get(i+1).text.split()[1]

                    sent.get(i).index += "+"+sent.get(i+1).index.split("+")[0]
                    sent.get(i+1).index = sent.get(i+1).index.split("+")[1]
                else:
                    i+=2
                    Inds=[]
                    while i < len(sent.words) and sent.get(i).denormalized.isnumeric() and not is_fraction(sent.get(i).denormalized):
                        res += sent.get(i).denormalized
                        Inds.append(i)
                        
                        if i < len(sent.words) - 1 and sent.get(i+1).denormalized.isnumeric() and not is_fraction(sent.get(i+1).denormalized):
                            i += 1
                        else:
                            break
                        
                    wrd.denormalized=res
                    wrd.subtype="decimal"
                    sent.merge([Inds[0]-2, Inds[0]-1]+Inds)
                    sent.remove_word([Inds[0]-1]+Inds)
                    
            i += 1
        
    if any(w in decimalke for w in [x.denormalized for x in sent.words]):
        i = 0
        while i < len(sent.words):
            if i < len(sent.words) - 2 and sent.get(i).denormalized.isnumeric() and not is_fraction(sent.get(i).denormalized) and sent.get(i+1).denormalized in decimalke and "-" in sent.get(i+2).denormalized and (sent.get(i+2).denormalized.split("-")[0].isnumeric() and sent.get(i+2).denormalized.split("-")[1].isalpha()):
                sent.get(i).denormalized=",".join([sent.get(i).denormalized, sent.get(i+2).denormalized])
                sent.get(i).subtype="decimal"
                sent.merge([i, i+1, i+2])
                sent.remove_word([i+1, i+2])
            elif i < len(sent.words) - 2 and sent.get(i).denormalized.isnumeric() and not is_fraction(sent.get(i).denormalized) and sent.get(i+1).denormalized in decimalke and sent.get(i+2).denormalized.isalpha() and any(sent.get(i+2).denormalized.lower().startswith(nr) for nr in nr100):
                nr=sorted([x for x in nr100 if sent.get(i+2).denormalized.lower().startswith(x)], key=len, reverse=True)[0]
                nr_nr=nr100[nr]
                sent.get(i).denormalized=sent.get(i).denormalized + ',' + nr_nr + "-"+sent.get(i+2).denormalized[len(nr):]
                sent.get(i).subtype="decimal"
                sent.merge([i, i+1, i+2])
                sent.remove_word([i+1, i+2])
            i += 1

def slasher(sent):
    if "skozi" in [x.denormalized.lower() for x in sent.words]:
        i = 0
        while i < (len(sent.words)):
            if 0 < i < len(sent.words) - 1 and sent.get(i).denormalized.lower() == "skozi" and sent.get(i-1).denormalized.isnumeric() and not is_fraction(sent.get(i-1).denormalized) and sent.get(i+1).denormalized.isnumeric() and not is_fraction(sent.get(i+1).denormalized):
                sent.get(i-1).denormalized+="/"+sent.get(i+1).denormalized
                sent.merge([i-1, i, i+1])
                sent.remove_word([i, i+1])
            i += 1
    #na
    if "na" in [x.denormalized.lower() for x in sent.words]:
        i=0
        while i < (len([x.denormalized.lower() for x in sent.words])):
            if 0 < i < len(sent.words) - 1 and sent.get(i).denormalized.lower() == "na" and sent.get(i - 1).type in ["num", "unit"] and sent.get(i + 1).type in ["num", "unit"] and "€" not in slicer([x.denormalized for x in sent.words], i):
                sent.get(i-1).denormalized="/".join([sent.get(i-1).denormalized, sent.get(i+1).denormalized])    
                sent.merge([i-1, i, i+1])
                sent.remove_word([i, i+1])
                i-=1
            i += 1

def construct_emails(sent):
    if "afna" in [x.denormalized for x in sent.words]:
        i=0
        while i<len(sent.words):
            if sent.get(i).denormalized=="afna" and any(ch in [x.denormalized for x in sent.words[i:]] for ch in mejlingchars):
                indices = []
                for ch in mejlingchars.keys():
                    indices.extend(find_all(ch, [x.denormalized for x in sent.words[:i]]))
                if not indices:
                    indices=[i-1]
                res_prev = ""
                if indices:
                    for x in range(indices[0] - 1, i):
                        if sent.get(x).denormalized in mejlingchars:
                            res_prev += mejlingchars[sent.get(x).denormalized]
                        else:
                            res_prev += sent.get(x).denormalized
                
                if any(is_sublist(["pika", suf], [x.denormalized for x in sent.words]) for suf in mail_suffix):
                    indexes = []
                    for suf in mail_suffix:
                        if is_sublist(["pika", suf], [x.denormalized for x in sent.words[i:]]):
                            indexes.append((suf, where_sublist(["pika", suf], [x.denormalized for x in sent.words[i:]])))
                    correct_index = sorted(indexes, key=itemgetter(1))[0][1][0][1]
                    res_post = ""
                    for y in range(i + 1, i + correct_index + 1):
                        if sent.get(y).denormalized in mejlingchars:
                            res_post += mejlingchars[sent.get(y).denormalized]
                        else:
                            res_post += sent.get(y).denormalized
                    res = res_prev + "@" + res_post
                    sent.get(indices[0]-1).denormalized=res
                    sent.merge([i for i in range(indices[0]-1, i+correct_index+1)])
                    sent.remove_word([i for i in range(indices[0], i+correct_index+1)])
            i+=1

def symbol_maker(sent):
    if any(is_sublist(key.split(), [x.denormalized.lower() for x in sent.words]) for key in symbols_multiple.keys()):
        i=0
        while i<len(sent.words):
            if i<len(sent.words)-1 and " ".join([sent.get(i).denormalized, sent.get(i+1).denormalized]) in symbols_multiple.keys() and isnumber(next(i+1, [x.denormalized for x in sent.words])):
                sent.get(i).denormalized=symbols_multiple[" ".join([sent.get(i).denormalized, sent.get(i+1).denormalized])]
                sent.get(i).type="symbol"
                sent.merge([i, i+1])
                sent.remove_word(i+1)
            i+=1
    if any(key in [x.denormalized.lower() for x in sent.words] for key in symbols.keys()):
        i = 0
        while i < (len(sent.words)):
            wrd=sent.get(i)
            tok=wrd.denormalized
            if tok.lower() in symbols.keys() and any(isnumber(sent.get(i).denormalized) for i in possible_range(i - 1, i, [x.denormalized for x in sent.words])+possible_range(i + 1, i + 2, [x.denormalized for x in sent.words])):
                #1 + 2
                if 0<i<len(sent.words)-1 and isnumber(sent.get(i-1).denormalized, True) and isnumber(sent.get(i+1).denormalized, True):
                    wrd.denormalized=symbols[tok.lower()]
                    wrd.type="symbol"
                    wrd.status="done"
                #5+
                elif 0<i and isnumber(sent.get(i-1).denormalized, True):
                    sent.get(i-1).denormalized=sent.get(i-1).denormalized+symbols[tok.lower()]
                    sent.get(i-1).type="symbol"
                    sent.merge([i-1, i])
                    sent.remove_word(i)
                    i-=1
                #-5
                elif i<len(sent.words)-1 and isnumber(sent.get(i+1).denormalized, True):
                    sent.get(i).denormalized=symbols[sent.get(i).denormalized.lower()]+sent.get(i+1).denormalized
                    sent.get(i).type="symbol"
                    sent.merge([i, i+1])
                    sent.remove_word(i+1)
            i += 1

def swapped_combos(sent):
    i=0
    while i<len(sent.words):
        wrd=sent.get(i)
        tok=wrd.denormalized
        if tok.isnumeric() and next(i, [x.type for x in sent.words]) in ["unit"] and next(i, [x.denormalized for x in sent.words], 2).lower() in ["in", "pa"] and is_fraction(next(i, [x.denormalized for x in sent.words], 3)) and not next(i, [x.type for x in sent.words], 4) in ["unit"]:
            res1=str(int(tok)+(numeric(next(i, [x.denormalized for x in sent.words], 3)))).replace(".", ",")
            res2=next(i, [x.denormalized for x in sent.words])
            res=res1+" "+res2
            wrd.denormalized=res
            wrd.type="combo_unit"
            sent.merge([i, i+1, i+2, i+3])
            sent.remove_word([i+1, i+2, i+3])
        
        elif tok.isnumeric() and next(i, [x.type for x in sent.words]) in ["unit"] and next(i, [x.denormalized for x in sent.words], 2).lower() in ["in", "pa"] and next(i, [x.denormalized for x in sent.words], 3) in imenovalci_risky and not next(i, [x.type for x in sent.words], 4) in ["unit"]:
            res1=str(int(tok)+numeric(make_fraction(1, imenovalci_risky[next(i, [x.denormalized for x in sent.words], 3)]))).replace(".", ",")
            res2=next(i, [x.denormalized for x in sent.words])
            res=res1+" "+res2
            wrd.denormalized=res
            wrd.type="combo_unit"
            sent.merge([i, i+1, i+2, i+3])
            sent.remove_word([i+1, i+2, i+3])
        
        elif tok.isnumeric() and next(i, [x.denormalized for x in sent.words]) in merskeenote and next(i, [x.denormalized for x in sent.words], 2).lower() in ["in", "pa"] and next(i, [x.denormalized for x in sent.words], 3).isnumeric()  and next(i, [x.denormalized for x in sent.words], 4) in imenovalci and not next(i, [x.denormalized for x in sent.words], 5) in merskeenote:
            res1=str(int(tok)+numeric(make_fraction(next(i, [x.denormalized for x in sent.words], 3), imenovalci[next(i, [x.denormalized for x in sent.words], 4)]))).replace(".", ",")
            res2=next(i, [x.denormalized for x in sent.words])
            res=res1+" "+res2
            wrd.denormalized=res
            wrd.type="combo_unit"
            sent.merge([i, i+1, i+2, i+3, i+4])
            sent.remove_word([i+1, i+2, i+3, i+4])
        i += 1

def stylish_word_old(i, sent):
    wrd=sent.get(i)
    if not isnum(wrd.denormalized):
        # tukaj še za merske enote
        if i>0 and wrd.type=="unit" and isnumber(sent.get(i-1).denormalized, True):
            if "+" not in wrd.index:
                wrd.final=wrd.text
            else:
                wrd.final=wrd.denormalized
        elif wrd.type=="combo_unit":
            parts=parse_units(wrd.text.split()[1])
            wrd.final=" ".join([wrd.denormalized.rsplit(" ", 1)[0], parts[0]+merske_changed[merske[parts[1]]]])
        elif any(sent.get(i).denormalized in symbols.values() for i in possible_range(i-1, i, [x.denormalized for x in sent.words])+possible_range(i+1, i+2, [x.denormalized for x in sent.words])) or any(sent.get(i).denormalized in symbols_multiple.values() for i in possible_range(i-1, i, [x.denormalized for x in sent.words])+possible_range(i+1, i+2, [x.denormalized for x in sent.words])):
            sent.get(i).final=sent.get(i).denormalized
        else:
            sent.get(i).final=sent.get(i).denormalized
    elif sent.get(i).subtype=="decimal":
        wrd.final=wrd.text
    elif str(sent.get(i).denormalized)[-6:] == "000000" and str(sent.get(i).denormalized) not in ["1000000", "000000", "0000000"]:
        wrd.final=wrd.denormalized[:-6]+" "+wrd.text.split()[-1]
    elif first_zero(sent.get(i).denormalized):
        sent.get(i).final=sent.get(i).denormalized
    elif sent.get(i).denormalized.isnumeric() and not is_fraction(sent.get(i).denormalized) and int(sent.get(i).denormalized.replace(".", "")) not in [100, 1000, 1000000] and int(sent.get(i).denormalized.replace(".", "")) > 10:
        sent.get(i).final=sent.get(i).denormalized

    # ordinal tipa prvič
    elif isordinal(sent.get(i).denormalized) and int(sent.get(i).denormalized.replace(".", "")) < 11 and sent.get(i).text.endswith("ič"):
        sent.get(i).final=sent.get(i).text
        
    # ali je naslednji token mesec ali merska enota
    elif i < len(sent.words) - 1 and isnum(sent.get(i).denormalized) and (sent.get(i+1).denormalized in meseci+generic_time+additional_words or "/" in sent.get(i+1).denormalized or sent.get(i+1).denormalized in merskeenote or "°C" in slicer([x.denormalized for x in sent.words], i, 7)):
        sent.get(i).final=sent.get(i).denormalized

    # ali sosednja vsebuje datum in ali je del mixed/upper
    elif (isordinal(sent.get(i).denormalized) and not "+" in sent.get(i).index and not sent.get(i).text.endswith("ič") and contains_date(slicer(sent.words, i, include_self=True))) or (len([x for x in slicer([x.denormalized for x in sent.words], i, 1) if (x.isupper() or is_mixed_case(x))]) != 0):
        sent.get(i).final=sent.get(i).denormalized
    elif is_nr_seq(slicer([x.denormalized for x in sent.words], i, context=3, include_self=True, include_index=True)):
        sent.get(i).final=sent.get(i).denormalized
    elif i>0 and sent.get(i).denormalized in ["1000", "1000000"] and isnumber(sent.get(i-1).denormalized) and not is_fraction(sent.get(i-1).denormalized):
        sent.get(i).final=sent.get(i).text
        
    # ali so v okolici številke, ki morajo ostat številke
    # če niso
    elif (int(sent.get(i).denormalized.replace(".", "")) < 11 or int(sent.get(i).denormalized.replace(".", "")) in [100, 1000, 1000000]) \
            and not any([stays_number(x, sent) for x in possible_range(i - 2, i, sent.words) + possible_range(i + 1, i + 3, sent.words)]):
        if not "+" in wrd.index:
            wrd.final=wrd.text
    # če so
    elif (int(sent.get(i).denormalized.replace(".", "")) < 11 or int(sent.get(i).denormalized.replace(".", "")) in [100, 1000, 1000000]) \
            and any([stays_number(x, sent) for x in possible_range(i - 2, i, sent.words) + possible_range(i + 1, i + 3, sent.words)]):
        Nrs=[sent.get(x) for x in possible_range(i - 2, i, sent.words) + possible_range(i + 1, i + 3, sent.words) if stays_number(x, sent)]
        if not (all([same_type_nr(wrd.denormalized, x.denormalized) for x in Nrs]) and wrd.denormalized != "1000000" and wrd.denormalized.replace(".", "") not in ["1", "2"]):
            if not "+" in wrd.index:
                wrd.final=wrd.text
        i += 1
    else:
        sent.get(i).final=sent.get(i).denormalized

def stylish_word(i, sent):
    wrd=sent.get(i)
    if wrd.type=="num":
        if str(sent.get(i).denormalized)[-6:] == "000000" and str(sent.get(i).denormalized) not in ["1000000", "000000", "0000000"]:
            wrd.final=wrd.denormalized[:-6]+" "+wrd.text.split()[-1]
        elif stays_number(i, sent):
            wrd.final=wrd.denormalized
        else:
            wrd.final=wrd.text
    elif wrd.type=="unit":
        if i>0 and sent.get(i-1).type=="num":
            if "+" not in wrd.index:
                wrd.final=wrd.text
            else:
                wrd.final=wrd.denormalized

    elif wrd.type=="combo_unit":
        parts=parse_units(wrd.text.split()[1])
        wrd.final=" ".join([wrd.denormalized.rsplit(" ", 1)[0], parts[0]+merske_changed[merske[parts[1]]]])

    elif wrd.type=="symbol":
        wrd.final=wrd.denormalized
    
    else:
        sent.get(i).final=sent.get(i).denormalized


#*************************************************

def prettify(sent):
    i = 0
    while i < len(sent.words):
        stylish_word(i, sent)
        i += 1

def decode_multimeaning_words(sent):
    i = 0
    while i < len(sent.words):
        if sent.get(i).denormalized in ["2.", "5."]:
            stylish_word(i, sent)
        else:
            sent.get(i).final=sent.get(i).denormalized

        i += 1

def titler(sent):
    i = 0
    for i in range(len(sent.words)):
        wrd=sent.get(i)
        t = wrd.denormalized
        if i == len(sent.words)-1 and len(sent.words)!=1 and t in nazivi.keys() and sent.get(i-1).type in ["title"]:
            wrd.denormalized=nazivi[t]
            wrd.final=wrd.denormalized
            wrd.type="title"
        elif i<len(sent.words)-1 and t in nazivi.keys() and (sent.get(i+1).denormalized in nazivi.keys() or sent.get(i+1).denormalized in lastnaimena or sent.get(i+1).denormalized in podrocja or isabbr(sent.get(i+1).denormalized)):
            wrd.denormalized=nazivi[t]
            wrd.final=wrd.denormalized
            wrd.type="title"
        elif i>0 and t in nazivi.keys() and (sent.get(i-1).type=="title"):
            wrd.denormalized=nazivi[t]
            wrd.final=wrd.denormalized
            wrd.type="title"

def abbreviator(sent):
    i = 0
    if any(ab in " ".join([x.denormalized for x in sent.words]) for ab in other_abbr):
        for abbr in other_abbr:
            while is_sublist(abbr.split(), [x.denormalized for x in sent.words]):
                indices = where_sublist(abbr.split(), [x.denormalized for x in sent.words])[0]
                i=indices[0]
                sent.get(i).denormalized=other_abbr[" ".join([sent.get(x).denormalized for x in indices])]
                sent.get(i).final=sent.get(i).denormalized
                sent.get(i).type="abbr"
                sent.merge(indices)
                sent.remove_word(indices[1:])
    # tako imenovan
    if any(a in " ".join([x.denormalized.lower() for x in sent.words]) for a in TI):
        AllTI = [a for a in TI if a in " ".join([x.denormalized.lower() for x in sent.words])]
        for abbr in AllTI:
            if is_sublist(abbr.split(), [x.denormalized.lower() for x in sent.words]):
                indices = where_sublist(abbr.split(), [x.denormalized.lower() for x in sent.words])
                for indexes in indices:
                    sent.get(indexes[0]).denormalized = "t."
                    sent.get(indexes[0]).final = sent.get(indexes[0]).denormalized
                    sent.get(indexes[0]).type="abbr"
                    sent.get(indexes[1]).denormalized = "i."
                    sent.get(indexes[1]).final = sent.get(indexes[1]).denormalized
                    sent.get(indexes[1]).type="abbr"