from .word import Word

from .word_tokenizer import word_tokenizer, spans

def add_tags(sentence):
    sentence_length=len(sentence.tokens)
    for i in range(sentence_length):
        word=sentence.get(i)
        word.index=sentence.indexes[i]
        sentence.words[i]=word
    determine_space(sentence)
    return sentence


def sorting_hat(inp, proper_tokenization=False):
    if isinstance(inp, str):
        sent=Sentence(inp, proper_tokenization)
        sent.type="str"
    elif isinstance(inp, list) and len(inp)>0 and isinstance(inp[0], dict):
        sent=Sentence(" ".join([x["text"] for x in inp]))
        sent.type="dict"
        if len(inp) > 1 and all("endTime" in x and x["endTime"] != None and "startTime" in x and x["startTime"] != None for x in inp):
            sent.pauseValues = dict([(i, inp[i + 1]["startTime"] - inp[i]["endTime"]) for i in range(len(inp) - 1)])
            sent.pause=True
    elif isinstance(inp, list) and all([isinstance(x, str) for x in inp]):
        sent=Sentence(" ".join(inp))
        sent.type="list"
    else:
        raise TypeError("This type of input is not supported.")
    return sent

def determine_space(sent):
    if sent.type=="str":
        S=spans(sent.text, sent.tokens)
        for i in range(1, len(sent.words)):
            sent.get(i).spaceBefore=not (S[i][1][0]==S[i-1][1][1])

class Sentence:
    def __init__(self, text=None, proper_tokenization=False):
        self.text=text
        self.type=None
        self.tokens=word_tokenizer(self.text, include_last_dot=False) if proper_tokenization else self.text.split()
        self.tags = None
        self.pause=False
        self.pauseValues=None
        self.indexes=[str(i) for i in range(len(self.tokens))]
        self.words=[Word(x) for x in self.tokens]
        self.status=None
        
    def len(self):
        return len(self.tokens)

    def tag(self):
        add_tags(self)

    def get(self, i):
        if i >= len(self.tokens) or i < 0:
            return None  # to avoid out of range errors
        return self.words[i]
    
    def remove_word(self, index):
        if isinstance(index, int): del self.words[index]
        if isinstance(index, list):
            for i in index:
                del self.words[index[0]]

    def merge(self, indexes):
        main=indexes[0]
        for i in indexes[1:]:
            self.get(main).text+=" "+self.get(i).text
            self.get(main).index+="+"+self.get(i).index
            self.get(main).endTime=self.get(i).endTime

    def glue_back(self):
        final=""
        for word in self.words:
            if (not word.spaceBefore) or (word.spaceBefore and word.spaceBefore==False):
                final+=word.final
            else:
                final+=" "+word.final
        return final
