def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    best = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[i][j] == '1':

                #print((i,j))

                done = False
                c = 2
                while not done:
                    
                    okay = True

                    if i + c >= len(matrix) or j + c >= len(matrix[0]):
                        break

                    for k in range(c):
                        if matrix[i + c - 1][j + k] != '1':
                            okay = False

                    if not okay:
                        break
                    
                    for k in range(c):
                        if matrix[i + k][j + c - 1] != '1':
                            okay = False
                    
                    if not okay:
                        break
                    
                    c += 1
                    
                    #print(i+c)
                    #print(j+c)

                c = c - 1
                best = max(best, c)
    
    return best



signature = 'def maximalSquare(self, matrix):'
input_string = """[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
"""  
