

def findCircleNum(self, M):
    """
    :type M: List[List[int]]
    :rtype: int
    """

    circle_count = 0
    visited = [False for i in range(len(M))]


    for i in range(len(M)):

        if visited[i] == False:
            circle_count += 1

        queue = [i]

        while len(queue) > 0:

            cur = queue[0]
            queue = queue[1:]

            if visited[cur]:
                continue

            visited[cur] = True

            for j in range(len(M)):
                if M[cur][j] == 1:
                    queue.append(j)

    return circle_count

        

signature = 'def findCircleNum(self, M)'
input_string = """[[1,1,0],[1,1,0],[0,0,1]]
151
"""