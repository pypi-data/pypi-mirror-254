
class Psuedonym(str):
    """ A string that is equal to a bunch of other strings """
    def __new__(cls, official:str, *psuedonyms:str, caseSensitive=False):
        obj = str.__new__(cls, official)
        obj.name = official
        obj._psuedonyms = psuedonyms
        obj.caseSensitive = caseSensitive
        return obj

    def __eq__(self, other):
        return other == self.name or any([other == i or ((other.lower() == i.lower()) if not self.caseSensitive else False) for i in self._psuedonyms])
