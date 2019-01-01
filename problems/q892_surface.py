def surfaceArea(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    def adjust(existing, new):
        if new > existing:
            return -existing * 2
        else:
            return -new * 2

    if len(grid) == 0:
        return 0

    # padding
    grid.insert(0, [0 for i in range(len(grid[0]))])
    grid.append([0 for i in range(len(grid[0]))])
    for g in grid:
        g.insert(0, 0)
        g.append(0)
        print(g)

    total = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):

            cur = grid[i][j]
            temp = 0
            if cur > 0:
                temp += 4 * cur
                temp += 2
                temp += adjust(cur, grid[i-1][j])
                temp += adjust(cur, grid[i][j-1])
            
            total += temp
            print(total)
    return total                
    


modifier = ''
signature = 'def surfaceArea(self, grid):'
test_cases = None
input_string = """[[1,2],[3,4]]
[[1,1,1],[1,0,1],[1,1,1]]
"""    