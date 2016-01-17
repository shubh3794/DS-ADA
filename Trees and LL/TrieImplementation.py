##TRIE IMPLEMENTATION IN PYTHON:
class TrieNode:
    def __init__(self):
        self.value=None
        self.pointers = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        self.insert_rec(word,self.root)
        return self.root

    def insert_rec(self,word,node):
        if word[:1] not in node.pointers:
            newnode = TrieNode()
            newnode.value = word[:1]
            node.pointers[word[:1]]=newnode
            return self.insert_rec(word,self.root)
        else:
            if len(word[1:])==0:
                node.pointers['end']=1
                return
            else:
                nextNode = node.pointers[word[:1]]
                return self.insert_rec(word[1:],nextNode)
    
