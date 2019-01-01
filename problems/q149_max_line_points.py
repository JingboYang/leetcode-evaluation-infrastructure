def maxPoints(self, points):

    class Point:
        def __init__(self, a=0, b=0):
            self.x = a
            self.y = b
        def __str__(self):
            return '({}, {})'.format(self.x, self.y)
        def __repr__(self):
            return '({}, {})'.format(self.x, self.y)

    points = [Point(p[0], p[1]) for p in points]

    import math

    def on_line(p1, p2, pt):

        if p1.x == p2.x:
            return p1.x == pt.x
        elif p1.y == p2.y:
            return p1.y == pt.y
        else:
            r1 = (p2.y - p1.y)/(p2.x - p1.x)
            ty = r1 * (pt.x - p1.x) + p1.y

            return ty == pt.y
    
    def line_compute(p1, p2):
        if p1.x == p2.x:
            return (p1.x, None)
        elif p1.y == p2.y:
            return (None, p1.y)
        elif p1.x == 0 and p1.y == 0:
            if p2.x < 0 and p2.y < 0:
                g = math.gcd(-p2.x, -p2.y)
                return (0, -p2.x / g, -p2.y / g)
            else:
                g = math.gcd(p2.x, p2.y)
                return (0, p2.x / g, p2.y / g)
        elif p2.x == 0 and p2.y == 0:
            if p1.x < 0 and p1.y < 0:
                g = math.gcd(-p1.x, -p1.y)
                return (0, -p1.x / g, -p1.y / g)
            else:
                g = math.gcd(p1.x, p1.y)
                return (0, p1.x / g, p1.y / g)
        else:
            #print(p1)
            #print(p2)
            a = (p2.y - p1.y)/(p2.x - p1.x)
            b = p1.y - a * p1.x
            #print((a,b))
            
            return (round(-b/a, 10), round(b, 10))

    if len(points) == 1:
        return 1

    lines = {}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            l = line_compute(points[i], points[j])
        
            if l in lines:
                lines[l].add(points[i])
                lines[l].add(points[j])
            else:
                lines[l] = set([points[i], points[j]])

    longest = 0
    for l in lines:
        longest = max(longest, len(lines[l]))
        print(l)
        print(lines[l])

    return longest


signature = 'def maxPoints(self, points):'
input_string = """[[0,0],[-1,-1],[2,2]]
"""