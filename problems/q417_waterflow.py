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

        if r < 0:
            return (True, r, c, (True, True, False))
        elif r >= m:
            return (True, r, c, (True, False, True))
        elif c < 0:
            return (True, r, c, (True, True, False))
        elif c >= n:
            return (True, r, c, (True, False, True))
        else:
            can_ceach = matrix[cur[0]][cur[1]] >= matrix[r][c]
            return (can_ceach, r, c, reach[r][c])
    
    reach = [[[False, False, False] for j in range(len(matrix[0]))]  for i in range(len(matrix))]
    for i in range(len(matrix)):
        reach[i][0][1] = True
        reach[i][-1][2] = True
    for i in range(len(matrix[0])):
        reach[0][i][1] = True
        reach[-1][i][2] = True
    
    #for r in reach:
    #    print(r)

    def dfs_search(cur):
        global reach

        cur_r, cur_c = cur
        #print('Processing {}'.format(cur))
        reach[cur_r][cur_c][0] = True

        reach_p = reach[cur_r][cur_c][1]
        reach_a = reach[cur_r][cur_c][2]
        for d in directions:
            can_ceach, r, c, status = check_valid(cur, d, matrix, reach)
            if can_ceach:
                if status[0] == False:
                    #print('{} is visiting ({},{})'.format(cur, r, c))
                    reach_returned = dfs_search((r, c))
                    reach_p |= reach_returned[0]
                    reach_a |= reach_returned[1]
                    reach[cur_r][cur_c][1] = reach_p
                    reach[cur_r][cur_c][2] = reach_a
                    #print('{} just visited ({},{}), got {}'.format(cur, r, c, reach_returned))
                else:
                    reach_p |= status[1]
                    reach_a |= status[2]
                    reach[cur_r][cur_c][1] = reach_p
                    reach[cur_r][cur_c][2] = reach_a
                    #print('{} just checked ({},{}), got {}'.format(cur, r, c, status))
            else:
                #print('{} cannot reach ({},{})'.format(cur, r, c))
                pass

        return (reach_p, reach_a)


    for r in range(len(matrix)):
        for c in range(len(matrix[0])):

            if reach[r][c][0] == False:
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
input_string = """[[4,8,5,8,0,2,19,18,1,7,13,9,13,16,6,15,15,12,18,5,8,11,6,17,5,11],[17,16,9,19,12,6,13,19,0,6,7,9,7,13,9,18,5,15,16,8,18,9,6,0,11,14],[11,5,13,3,12,19,5,15,2,15,9,16,6,12,8,0,19,19,11,0,16,8,15,15,1,12],[15,16,16,19,14,1,2,11,14,8,16,13,2,0,3,8,1,5,4,15,12,5,13,3,5,3]]
"""