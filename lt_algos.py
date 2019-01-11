class TrieNode():

    def __init__(self):
        import collections
        self.children = collections.defaultdict(TrieNode)
        self.ends_here = False
        self.val = None                 # Note this is optional
        self.level = 0                  # This only helps printing
    
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        string = '---' * self.level + str(self.val)
        if self.ends_here:
            string += '|\n'
        else:
            string += '\n'
        for w in self.children:
            string += str(self.children[w])
        return string


class Trie():

    def __init__(self):
        self.root = TrieNode()

    def insert(self, item):

        cur = self.root
        for i, w in enumerate(item):
            cur = cur.children[w]
            cur.val = w
            cur.level = i + 1
        cur.ends_here = True
    
    def search(self, item):

        cur = self.root
        for i, w in enumerate(item):
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.ends_here
    
    def partial_search(self, item):

        cur = self.root
        for i, w in enumerate(item):
            if w not in cur.children:
                return (False, False)
            cur = cur.children[w]
        return (True, cur.ends_here)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.root)


if __name__ == '__main__':
    trie = Trie()
    trie.insert('hello')
    trie.insert('heck')
    trie.insert('apple')
    trie.insert('application')

    print(trie.root)

    print(trie.partial_search('a'))