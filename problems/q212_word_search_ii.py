from lt_algos import *


def findWords(self, board, words):
    """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    """
    R = len(board)
    C = len(board[0])
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    visited = [[False for i in range(C)] for j in range(R)]

    completed = []
    def recursion(cur, prev_letters):
        print(cur)
        if cur[0] < 0 or cur[0] >= R or cur[1] < 0 or cur[1] >= C:
            print('x')
            return
        elif visited[cur[0]][cur[1]] == True:
            print('y')
            return

        visited[cur[0]][cur[1]] = True
        letters = prev_letters + board[cur[0]][cur[1]]
        print(letters)
        temp = trie.partial_search(letters)
        print(temp)
        for v in visited:
            print(v)
        if temp[0]:
            if temp[1]:
                completed.append(letters)
        else:
            visited[cur[0]][cur[1]] = False
            return

        for d in directions:
            recursion((cur[0]+d[0], cur[1]+d[1]), letters)
        visited[cur[0]][cur[1]] = False
        print('end of {}'.format(board[cur[0]][cur[1]]))
        for v in visited:
            print(v)

    trie = Trie()
    for w in words:
        trie.insert(w)
    
    print(trie)
    
    for i in range(R):
        for j in range(C):
            recursion((i, j), '')


    return completed



modifier = ''
signature = 'def findWords(self, board, words):'
test_cases = None
input_string = """[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
["oath","pea","eat","rain"]
[["a","b"],["c","d"]]
["acdb"]
"""    

