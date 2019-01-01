def findLadders(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """

    wordList = set(wordList)
    parent_dict = {beginWord: None}
    visited = set()
    
    visited.add((None, beginWord))
    ladder_queue = [beginWord]
    while len(ladder_queue) > 0:

        cur = ladder_queue[0]
        ladder_queue.pop(0)

        if cur == endWord:
            continue

        for i in range(len(cur)):
            for l in [chr(v) for v in range(ord('a'), ord('z') + 1)]:
                constructed = cur[:i] + l + cur[i + 1:]
                if constructed != cur:
                    if constructed in wordList:
                        
                        if constructed in parent_dict:
                            parent_dict[constructed].append(cur)
                        else:
                            parent_dict[constructed] = [cur]

                        visited_lookup = (cur, constructed)
                        if visited_lookup not in visited:
                            ladder_queue.append(constructed)
                            visited.add(visited_lookup)

        print('Visiting {}'.format(cur))

    global results
    results = [[]]
    def build_path(cur, previous):
        previous.append(cur)
        if parent_dict[cur] == None:
            if cur == beginWord:
                results.append(previous.reverse())
            return

        for p in parent_dict[cur]:
            build_path(p, previous.copy())
    
    build_path(endWord, [])

    return results



signature = 'def findLadders(self, beginWord, endWord, wordList):'
input_string = """"hit"
"cog"
["hot","dot","dog","lot","log","cog"]
"""