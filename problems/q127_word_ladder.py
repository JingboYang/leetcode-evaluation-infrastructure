def ladderLength(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """

    iterables = [set() for i in range(len(wordList[0]))]

    for i in range(len(iterables)):
        for w in wordList:
            iterables[i].add(w[i])
    
    visited = {}
    for w in wordList:
        visited[w] = False
    visited[beginWord] = False

    queue = [(beginWord, 0)]
    while len(queue) > 0:
        cur, lvl = queue[0]
        queue.pop(0)
        #print('Visiting ' + cur)
        if cur == endWord:
            return lvl
        
        if visited[cur] == False:
            visited[cur] = True

            for p in range(len(iterables)):
                for i in iterables[p]:
                    nw = cur[:p] + i + cur[p+1:]
                    if nw in visited:
                        queue.append((nw, lvl+1))
        





modifier = ''
signature = 'def ladderLength(self, beginWord, endWord, wordList):'
input_string = """"hit"
"cog"
["hot","dot","dog","lot","log","cog"]
"""