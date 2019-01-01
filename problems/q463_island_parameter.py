grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]


if len(grid) == 0:
    
    #return 0
    pass

sides = [(-1, 0), (1,0), (0, 1), (0, -1)]

total = 0
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == 1:
            
            counter = 0
            for s in sides:
                nr = r + s[0]
                nc = c + s[1]
                
                if nr >= 0 and nc >= 0 and nr <= len(grid) and nc <= len(grid[0]):
                    print(nr)
                    print(nc)
                    if grid[nr][nc] == 0:
                        counter += 1
                else:
                    counter += 1
            
            total += counter

print(total)