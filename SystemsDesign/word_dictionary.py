class WordDictionary:

    def __init__(self):
        self.words = {} # map[len(word)]set(words...)

    def addWord(self, word: str) -> None:
        l = len(word)
        if not l in self.words:
            self.words[l] = set() # make sure there's a set in place before adding
        self.words[l].add(word) # you can do this regardless because it doesn't make a diff

    def search(self, word: str) -> bool:
        m = len(word)
        if m not in self.words: return False

        for w in self.words[m]:
            i = 0
            while i < m and (w[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True
        return False


    '''
    Testing
    wd = WordDictionary()
    wd.addWord("cat")
    wd.addWord("hat")
    wd.addWord("bat")

    wd.addWord("doll")
    wd.addWord("matt")
    wd.addWord("crow")

    print(wd.words)

    print(wd.search("..t")) # should return true
    print(wd.search("d..")) # should return true

    print(wd.search("..o.")) # should return true

    # print(wd.search("...est")) # should return true

    # print(wd.search("notadded")) # should return false

    '''
