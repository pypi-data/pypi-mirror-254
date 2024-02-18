class Word:
    def __init__(self, word=""):
        self.text = word
        self.denormalized = word
        self.final = self.denormalized
        self.startTime=None
        self.endTime=None
        self.type = None
        self.subtype=None
        self.microtype=None
        self.index=None
        self.spaceBefore=None