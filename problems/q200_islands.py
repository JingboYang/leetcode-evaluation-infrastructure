def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    num_rows = len(grid)
    num_cols = len(grid[0])


    visited = [[False for j in range(num_cols)] for i in range(num_rows) ]
    directions = [(1,0),(0,1),(0,-1),(-1,0)]

    def BFS(start):

        queue = [start]
        
        while len(queue) > 0:
            cur = queue[0]
            queue = queue[1:]
            
            if visited[cur[0]][cur[1]]:
                continue
            else:
                visited[cur[0]][cur[1]] = True

            for d in directions:
                nr = cur[0] + d[0]
                nc = cur[1] + d[1]

                if nr < num_rows and nr >= 0 and nc >= 0 and nc < num_cols:
                    if grid[nr][nc] == '1':
                            queue.append((nr, nc))


    island_count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and visited[i][j] == False:
                island_count += 1
                BFS((i,j))


    return island_count



signature = 'def numIslands(self, grid)'
input_string = """[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
"""  
