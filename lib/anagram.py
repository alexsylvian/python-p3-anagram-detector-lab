class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        return [anagram for anagram in words if self.is_anagram(anagram)]

    def is_anagram(self, candidate):
        return sorted(self.word.lower()) == sorted(candidate.lower())
