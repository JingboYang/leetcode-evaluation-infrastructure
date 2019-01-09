def largestIsland(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    R = len(grid)
    C = len(grid[0])

    visited  = [[False for i in range(C)] for j in range(R)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    marker = 'X'

    def traverse(pos, label):
        
        queue = [pos]
        counter = 0
        while len(queue) > 0:
            cr, cc = queue.pop(0)

            if not visited[cr][cc]:
                
                visited[cr][cc] = True
                counter += 1
                grid[cr][cc] = marker

                for d in dirs:
                    nr = cr + d[0]
                    nc = cc + d[1]

                    if nr >= 0 and nc >= 0 and nr < R and nc < C:
                        if grid[nr][nc] == 1:
                            queue.append((nr, nc))


        mark(counter, label)


    def mark(size, label):
        for i in range(R):
            for j in range(C):
                if grid[i][j] == marker:
                    grid[i][j] = (size, label)


    def flip_and_check():

        best = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:

                    seen = set()
                    added = 1
                    for d in dirs:   
                        nr = i + d[0]
                        nc = j + d[1]

                        if nr >= 0 and nc >= 0 and nr < R and nc < C:
                            if grid[nr][nc] != 0 and grid[nr][nc][1] not in seen:
                                added += grid[nr][nc][0]
                                seen.add(grid[nr][nc][1])
                    best = max(best, added)
                else:
                    best = max(best, grid[i][j][0])
        
        return best

    label = 1
    for i in range(R):
        for j in range(C):
            if not visited[i][j] and grid[i][j] == 1:
                traverse((i, j), label)
                label += 1

    for r in grid:
        print(r)

    return flip_and_check()


modifier = ''
signature = 'def largestIsland(self, grid):'
test_cases = None
input_string = """[[1,0],[0,1]]
[[1, 1], [1, 1]]
[[1, 1], [1, 0]]
"""    