class GuessResult:
    def __init__(self, hits, blows):
        self._hits = hits
        self._blows = blows

    def GetHits(self):
        return self._hits

    def GetBlows(self):
        return self._blows
