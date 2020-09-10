class TrieTree():
    def __init__(self):
        self.d ={}


    def insert(self,word:str):
        t = self.d
        for c in word:
            if c not in self.d:
                t[c]={}
            t=t[c]
        t["end"] = True


    def search(self,word:str):
        t =self.d
        for c in word:
            if c not in t:
                return False
            t = t[c]
            print(t)
        return "end" in t

    def startswith(self,word:str):
        t= self.d 
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return True


    def delete(self,word:str):
        t=self.d
        stack =[] 
        for c in word:
            if c not in t:
                return  
            stack.append(t)
            t =t[c]

        for c in word[::-1]:
            if c not in t:
                return 
            del t[c]


    def info(self):
        print(self.d)

trie= TrieTree()
trie.insert("apple")
# trie.insert("appbl")
trie.insert("boo")
trie.info()
print (trie.search("a"))

