def findStrobogrammatic(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    
    digits = [1,6,8,9,0]
    others = [1,9,8,6,0]
    sames = [1,8,0]
    
    m = n // 2
    #global output
    output = set()
    
    def construct(string_l, string_r):

        def check(s):
            if len(str(int(s))) == n:
                return True
            return False

        string = string_l + string_r
        if len(string) == n:
            if check(string):
                output.add(int(string))
            return
        
        if n % 2 == 1 and len(string_l) == n // 2:
            for d in sames:
                construct(string_l + str(d), string_r)
        else:
            for i in range(len(digits)):
                construct(string_l + str(digits[i]), str(others[i]) + string_r)
    
    construct('','')
    
    return list(output)



signature = 'def findStrobogrammatic(self, n):'
input_string = """3
"""  
