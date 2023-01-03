class SmartRandomizer():
    def __init__(self, randomizerList):
        self.randomizerList = randomizerList  # List[tuple(randomFunc, min, max)]
        self.lastResults = []

    def getRandom(self):
        if not len(self.lastResults):
            self.lastResults = [randFunc(bottom, top) for randFunc, bottom, top in self.randomizerList]
        else:
            self.lastResults = [
                randFunc(max(bottom, result - (top - bottom) // 20), min(top, result + (top - bottom) // 20))
                if randFunc.__name__ == "randint" else
                randFunc(max(bottom, result - (top - bottom) / 20), min(top, result + (top - bottom) / 20))
                for result, (randFunc, bottom, top) in zip(self.lastResults, self.randomizerList)]

        return self.lastResults
