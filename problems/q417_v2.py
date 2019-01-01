def pacificAtlantic(self, matrix):
    global reach

    if len(matrix) == 0:
        return []
    if len(matrix[0]) == 0:
        return []

    directions = [(0,1), (1,0), (0,-1), (-1, 0)]
    # p: 1, a: 2, both: 3, unvisited: -1

    def check_valid(cur, move, matrix, reach):
        
        m = len(matrix)
        n = len(matrix[0])
        
        r = cur[0] + move[0]
        c = cur[1] + move[1]

        if r >= 0 and r < m and c >= 0 and c < n:
            can_ceach = matrix[cur[0]][cur[1]] <= matrix[r][c]
            
            if can_ceach:
                if reach[cur[0]][cur[1]][1] - reach[r][c][1]  == 1 or reach[cur[0]][cur[1]][2] - reach[r][c][2] == 1:
                    return (True, r, c)
        
        return (False, r, c)

    
    reach = [[[False, False, False] for j in range(len(matrix[0]))]  for i in range(len(matrix))]
    for i in range(len(matrix)):
        reach[i][0][1] = True
        reach[i][-1][2] = True
    for i in range(len(matrix[0])):
        reach[0][i][1] = True
        reach[-1][i][2] = True
    

    def dfs_search(cur):
        global reach

        cur_r, cur_c = cur
        #print('Processing {}'.format(cur))
        #reach[cur_r][cur_c][0] = True

        for d in directions:
            do_update, r, c = check_valid(cur, d, matrix, reach)

            if do_update:
                print('Updating {} from {},{}'.format(cur, r, c))
                reach[r][c][1] |= reach[cur_r][cur_c][1]
                reach[r][c][2] |= reach[cur_r][cur_c][2]
                dfs_search((r,c))


    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            #if reach[r][c][0] == False:
            dfs_search((r,c))


    results = []
    for r in range(len(matrix)):
        line = ''
        for c in range(len(matrix[0])):
            if reach[r][c][1] and reach[r][c][2]:
                line += 'b '
                results.append([r,c])
            elif reach[r][c][1]:
                line += 'p '
            elif reach[r][c][2]:
                line += 'a '
            else:
                line += '  '
        print(line)

    return results


signature = 'def pacificAtlantic(self, matrix):'
input_string = """[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
"""