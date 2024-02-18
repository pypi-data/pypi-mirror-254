from .denormalizer_helpers import is_fraction, isordinal, slicer, is_mixed_case, allowed_suffixes, meseci, generic_time, additional_words


def classify_sent(sent):
    for i in range(len(sent.words)):
        if sent.get(i).type=="num":
            classify_number(i, sent)

def classify_number(i, sent):
    if sent.get(i).subtype=="ordinal":
        classify_ordinal(i, sent)
    elif sent.get(i).subtype=="decimal":
        classify_decimal(i, sent)
    elif sent.get(i).denormalized.isnumeric() and not is_fraction(sent.get(i).denormalized):
        classify_normal_number(i, sent)


def classify_ordinal(i, sent):
    #time
    if i<len(sent.words)-1 and sent.get(i+1).denormalized in generic_time:
        sent.get(i).microtype="time"

    #tru ordinal
    elif i<len(sent.words)-1 and sent.get(i+1).denormalized in additional_words:
        sent.get(i).microtype="tru_ordinal"
    
    #date
    elif i<len(sent.words)-1 and not "+" in sent.get(i).index and 0<int(sent.get(i).denormalized.replace(".", ""))<32 and sent.get(i+1).denormalized in meseci:
        sent.get(i).microtype="date"
    
    elif i<len(sent.words)-1 and not "+" in sent.get(i).index and 0<int(sent.get(i).denormalized.replace(".", ""))<32 and any(sent.get(i).text.endswith(suf) for suf in allowed_suffixes) \
        and sent.get(i+1).subtype=="ordinal" and 0<int(sent.get(i+1).denormalized.replace(".", ""))<13 \
        and sent.get(i+1).text.endswith([suf for suf in allowed_suffixes if sent.get(i).text.endswith(suf)][0]):
        sent.get(i).microtype="date"
        sent.get(i+1).microtype="date"

def classify_decimal(i, sent):
    if i<len(sent.words)-1 and sent.get(i+1).type in ["unit", "symbol"]:
        sent.get(i).microtype="measure"

def classify_normal_number(i, sent):
    if i<len(sent.words)-1 and sent.get(i+1).type in ["unit", "symbol"]:
        sent.get(i).microtype="measure"
    elif i>0 and sent.get(i-1).type in ["symbol"]:
        sent.get(i).microtype="measure"
    elif [x for x in slicer([x.denormalized for x in sent.words], i, 1) if (x.isupper() or is_mixed_case(x))]:
        sent.get(i).microtype="part"
    elif i > 0 and (sent.get(i-1).denormalized.lower() in ["ulica", "ulici", "ulico", "ulice", "cesta", "cesti", "cesto", "ceste"] \
        or (sent.get(i-1).denormalized.istitle() and any(sent.get(i-1).denormalized.endswith(suf) for suf in ["ova", "ovi", "ovo", "ove"]))):
        sent.get(i).microtype="address"
        

def inheriter(sent):
    for i in range(len(sent.words)):
        if sent.get(i).type=="num" and [index for index in slicer([ind for ind in range(len(sent.words))], i, ctype="R") if sent.get(index).microtype]:
            maybies=[index for index in slicer([ind for ind in range(len(sent.words))], i) if sent.get(index).microtype]
            for m in maybies:
                if sent.get(m).subtype==sent.get(i).subtype:
                    sent.get(i).microtype=sent.get(m).microtype
                    break
    