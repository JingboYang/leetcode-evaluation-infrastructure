def longestIncreasingPath(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """

    directions = [(0,1),(1,0),(-1,0),(0,-1)]

    def check(coord, d):

        r = coord[0] + d[0]
        c = coord[1] + d[1]

        if r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix):
            return r, c
        
        return False

    def less(c1, c2):
        return coord[c1[0]][c1[1]] < coord[c2[0]][c2[1]]
    

    longest = [[None for j in range(len(matrix[0]))] for i in range(len(matrix))]

    def traverse(cur):
        
        if longest[cur[0]][cur[1]] is not None:
            return False
    

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            traverse((i, j))
    
    best = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            best = max(best, longest[i][j])

    return best
    

# --- Things needed for this infrastructure to run ----
modifier = ''
signature = 'def longestIncreasingPath(self, matrix):'
test_cases = None
input_string = """[[9,9,4],[6,6,8],[2,1,1]]
"""  