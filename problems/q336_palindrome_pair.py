def palindromePairs(self, words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """

    class TrieNode:
        def __init__(self, val, end=-1):
            self.val = val
            self.end = end
            self.children = []

    
    def trie_insert(root, word, wi):
        
        index = 0
        cur = root
        done = False
        while done == False:

            if index >= len(word):
                c.end = wi
                done = True
            else:    
                found = False
                for c in cur.children:
                    if c.val == word[index]:
                        cur = c
                        index += 1
                        found = True
                        break
                
                if not found:
                    for i in range(index, len(word)):
                        temp = TrieNode(word[i])
                        cur.children.append(temp)
                        cur = temp
                    cur.end = wi
                    done = True
            

    def print_trie(root):

        print_stack = [(root, 0)]
        while len(print_stack) != 0:
            cur, level = print_stack[-1]
            print_stack.pop(-1)

            string = '  ' * level + cur.val
            if cur.end != -1:
                string += '|' + str(cur.end) + '|'
            print(string)

            for c in cur.children:
                print_stack.append((c, level + 1))


    def palindrome_search(root, word, wi):
        
        def check_palindrome(string):

            for i in range(len(string) // 2):
                if string[i] != string[len(string) - 1 - i]:
                    return False
            
            return True



        results = []
        index = 0
        cur = root
        done = False
        while not done:

            for c in cur.children:
                if c.val == word[index]:
                    cur = c
                    index += 1
                    found = True
                    if c.end != -1:
                        if check_palindrome(word[index + 1:]):
                            results.append(wi, cur.end)
                    
                    break

            # if trie has more stuff than word
            if index >= len(word):
                word[]

        pass


    root = TrieNode('_')
    for i, w in enumerate(words):
        trie_insert(root, w, i)

    print_trie(root)


    results = []
    for i, w in enumerate(words):
        temp = palindrome_search(root, reversed(w))
        results.extend(temp)

    return results


signature = 'def palindromePairs(self, words):'
input_string = """["abcd","dcba","lls","s","sssll"]
"""        