
def findCheapestPrice(n, flights, src, dst, K):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type K: int
    :rtype: int
    """

    import heapq

    edge_table = {}
    for f in flights:
        if f[0] in edge_table:
            edge_table[f[0]].append((f[1], f[2]))
        else:
            edge_table[f[0]] = [(f[1], f[2])]

    E = K + 1

    cost_map = {(src, 0): 0}
    queue = [(0, src, 0)]
    while len(queue) > 0:

        cur = heapq.heappop(queue)
        cur_cost, cur_node, cur_edge = cur
        cur_tuple = (cur_node, cur_edge)

        if cur_edge > E:
            continue
        elif cur_edge == E and cur_node != dst:
            continue
        elif cur_node == dst:
            continue 

        for flight in edge_table[cur_node]:
            next_E = cur_edge + 1
            next_tuple = (flight[0], next_E)
            next_cost = cur_cost + flight[1]
            next_queue = (next_cost, flight[0], next_E)

            if next_tuple in cost_map:
                if cost_map[next_tuple] <= next_cost:
                    pass
                else:
                    cost_map[next_tuple] = next_cost
                    heapq.heappush(queue, next_queue)
            else:
                cost_map[next_tuple] = next_cost
                heapq.heappush(queue, next_queue)

        #print(queue)

    #print(cost_map)
    results = []
    for i in range(1, E + 1):
        t = (dst, i)
        #print(t)
        if t in cost_map:
            #print(cost_map[t])
            results.append(cost_map[t])
    return min(results)


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 1

n = 5
flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
src = 2
dst = 1
K = 1


result = findCheapestPrice(n, flights, src, dst, K)
print(result)


        