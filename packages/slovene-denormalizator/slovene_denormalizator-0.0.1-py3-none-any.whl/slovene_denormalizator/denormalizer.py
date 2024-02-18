from .classifier import classify_sent, inheriter
from .construction import abbreviator, basic_denumberer, construct_emails, construct_hours, construct_fractions, construct_units, decimal_creator, decode_multimeaning_words, number_chaos_resolver, slasher, solo_numbers, sum_deco_oridnals, sum_deco_years, swapped_combos, symbol_maker, titler, prettify
from .configs import configs
from .denormalizer_helpers import *
from .sentence import add_tags, sorting_hat


def denormalize(inp, custom_config="default"):
    #config: uses default for what is not specified
    config=configs["default"]
    if isinstance(custom_config, str) and custom_config!="default":
        try:
            config={**config, **configs[custom_config]}
        except KeyError:
            raise KeyError("This config does not exist yet. You can choose between **default**, **technical** or **everyday** config or make a custom config.")
    elif isinstance(custom_config, dict):
        config={**config, **custom_config}
    elif not isinstance(config, str) and not isinstance(config, dict):
        raise TypeError("This type of config is not supported. You can choose between **default**, **technical** or **everyday** config or make a custom config.")

    sent=add_tags(sorting_hat(inp, config["proper_tokenization"]))
    
    if sent.text.strip() == "":
        return {"denormalized_content": [], "denormalized_string": None}
    # menjam številke-besede v številke-številke
    if config["include_numbers"]:
        basic_denumberer(sent)

    if any(isordinal(tok) for tok in [x.denormalized for x in sent.words]):
        sum_deco_oridnals(sent)
        
    if config["col_years"] and any(tok.isnumeric() for tok in [x.denormalized for x in sent.words]):
        #leta 2 2, leta 2 25, 20 20
        sum_deco_years(sent)
    if config["include_numbers_part_token"] and config["include_numbers"]:
        # 20-odstotni
        for wrd in sent.words:
            tok = wrd.denormalized
            for št in nrskupaj.keys():
                if (wrd.denormalized.lower()).startswith(št):
                    wrd.denormalized = str(nrskupaj[št]) + "-" + tok[len(št):]
                    wrd.type="num_part_token"
                    break
    #hours
    construct_hours(sent)
    #FRACTIONS                
    if config["include_stylistic"] and config["include_fractions"] and any(k in [x.denormalized.lower() for x in sent.words] for k in imenovalci.keys()):
        construct_fractions(sent)
        
    # merske enote
    if config["include_units"]:
        construct_units(sent, config["include_units"], config["include_fractions"])
    
    if config["include_numbers"]:
        number_chaos_resolver(sent)
        
        #posamezne številke
        if config["punct_is_included"]:
            solo_numbers(sent)
        decimal_creator(sent)
            
    #skozi
    if config["include_slash"]:
        slasher(sent)
    #emails
    if config["include_email"]:
        construct_emails(sent)
    #symbols
    if config["include_symbols"]:
        symbol_maker(sent)
    
    if config["include_alnum"] and any(tok.isnumeric() for tok in [x.denormalized for x in sent.words]):
        i=0
        while i < len(sent.words):
            if i>0 and sent.get(i).denormalized.isnumeric() and (sent.get(i-1).denormalized, sent.get(i).denormalized) in alnum_dict:
                sent.get(i-1).denormalized=alnum_dict[(sent.get(i-1).denormalized, sent.get(i).denormalized)]
                sent.merge([i-1, i])
                sent.remove_word(i)
                i-=1
            i+=1
    #SPECIAL NUMBERS
    if config["merge_sep_numbers"] and any(tok.isnumeric() for tok in [x.denormalized for x in sent.words]):
        swapped_combos(sent)

    #stylistic
    classify_sent(sent)
    inheriter(sent)
    if config["include_stylistic"]:
        prettify(sent)
    if not config["include_stylistic"]:
        decode_multimeaning_words(sent)
    
    # nazivi
    if config["include_title"]:
        titler(sent)
    #ostale okrajšave
    if config["include_abbr"]:
        abbreviator(sent)

    final_string=sent.glue_back() if sent.type=="str" else None
    return {"denormalized_content": [{"text": x.final, "index": [int(x) for x in x.index.split("+")]} for x in sent.words], "denormalized_string": final_string}