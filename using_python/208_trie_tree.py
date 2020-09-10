class TrieTree():
    def __init__():
        self.d ={}


    def insert(word:str):
        t = self.d
        for c in word:
            if c not in self.d:
                t[c]={}
            t=t[c]
        t["end"] = True


    def search(word:str):
        t =self.d
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return "end" in t

    def startswith(word:str):
        t= self.d 
        for c in word：
            if c not in t:
                return False
            t = t[c]
        return True
    


