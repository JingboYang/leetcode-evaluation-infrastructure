matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False] * len(matrix[0]) for i in range(len(matrix))]

def change_direction(row, col, d):
    fr = row - directions[d][0]
    fc = col - directions[d][1]
    
    d = (d + 1) % 4
    
    row = fr+ directions[d][0]
    col = fc + directions[d][1]

    return row, col, d


row = 0
col = 0
d = 0
counter = 0
results = []
while counter < len(matrix) * len(matrix[0]):
    if visited[row][col] is False:
        
        results.append(matrix[row][col])
        visited[row][col] = True
        counter += 1
        
        print(matrix[row][col])
    
        row = row + directions[d][0]
        col = col + directions[d][1]
        
        if row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[0]):
            pass
        else:
            row, col, d = change_direction(row, col, d)    
            
    else:
        row, col, d = change_direction(row, col, d)