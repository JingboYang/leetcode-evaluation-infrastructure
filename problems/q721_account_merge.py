
def lala(accounts):

    name_lookup = {}
    graph = {}
    for a in accounts:
        name = a[0]
        emails = set(a[1:])

        for e in emails:
            name_lookup[e] = name
            if e in graph:
                graph[e] |= emails
            else:
                graph[e] = emails
    #print(graph)

    
    visited = set()

    def explore(cur, l):
        
        if cur in visited:
            return

        visited.add(cur)
        s = graph[cur]
        l |= s

        for e in s:
            explore(e, l)

    
    useful = []
    for g in graph:
        thing  = set()
        explore(g, thing)

        if len(thing) > 0:
            temp = list(thing)
            temp.sort()
            useful.append(temp)
    
    #print(useful)

    result = []
    for u in useful:
        name = name_lookup[u[0]]
        r = [name]
        r.extend(u)
        result.append(r)
    
    print(result)


#input = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
input =  [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

lala(input)
