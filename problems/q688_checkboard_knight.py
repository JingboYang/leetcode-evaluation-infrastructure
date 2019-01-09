def v1():
    positions = []
    visited = set()
    
    def recursion(pos, k):
        
        print(pos, k)

        if k == K:
            positions.append(pos)
            return
        
        if pos in visited:
            return
        visited.add((pos, k))

        for m in moves:
            nr = m[0] + pos[0]
            nc = m[1] + pos[1]

            if nr >= 0 and nr < N and nc >= 0 and nc < N:
                recursion((nr, nc), k + 1)

    recursion((r,c), 0)



def knightProbability(self, N, K, r, c):
    """
    :type N: int
    :type K: int
    :type r: int
    :type c: int
    :rtype: float
    """
        
    moves = [(1,2),(-1,2),(-1,-2),(1,-2),(2,1),(-2,-1),(2,-1),(-2,1)]

    DP0 = [[1 for i in range(N)] for j in range(N)]

    for k in range(K):
        DP1 = [[0 for i in range(N)] for j in range(N)]

        for i in range(N):
            for j in range(N):
                for m in moves:
                    nr = m[0] + i
                    nc = m[1] + j

                    if nr >= 0 and nr < N and nc >= 0 and nc < N:
                        DP1[i][j] += DP0[nr][nc]
        
        DP0 = DP1

    prob = DP0[r][c] / 8 ** K
    #print(positions)

    for d in DP0:
        print(d)

    return prob



signature = 'def knightProbability(self, N, K, r, c):'
test_cases = [0]
input_string = """3
2
0
0
3
3
0
0
8
30
6
4
"""