def sumOfDistancesInTree(self, N, edges):

    import copy

    if N == 0 :
        return []

    out_edge = {}
    
    for e in edges:
        if e[0] in out_edge:
            out_edge[e[0]].append(e[1])
        else:
            out_edge[e[0]] = [e[1]]

        if e[1] in out_edge:
            out_edge[e[1]].append(e[0])
        else:
            out_edge[e[1]] = [e[0]]


    global edge_matrix
    edge_matrix = [[0 for i in range(N)] for j in range(N)]
    visited = set()

    head = 0

    def dfs(cur, prevs):
        
        if cur in visited:
            return {}

        visited.add(cur)
        for p in prevs:
            p[1] += 1
            edge_matrix[p[0]][cur] = p[1]
            edge_matrix[cur][p[0]] = p[1]

        prevs.append([cur, 0])
        
        if cur in out_edge:
            peer = []
            for o in out_edge[cur]:
                if o in visited:
                    continue
                print('Visiting {} from {} with peer {}'.format(o, cur, peer))
                d = copy.deepcopy(prevs)
                d.extend(peer)
                below = dfs(o, d)
                print('Things below {} are {} with peer {}'.format(o, below, peer))
                peer.extend(below)

            if len(peer) == 0:
                print('{} is leaf'.format(cur))
                #return {cur:1}

            for p in peer:
                p[1] += 1

            peer.append([cur, 1])

            return peer
            
        

    dfs(head, [])

    results = []
    for edge in edge_matrix:
        print(edge)
        results.append(sum(edge))
    
    return results


signature = 'def sumOfDistancesInTree(self, N, edges):'
input_string = """6
[[0,1],[0,2],[2,3],[2,4],[2,5]]
"""