def removeKdigits(k, num):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    
    num =[int(n) for n in num]
    
    for i in range(k):
        
        first = -1
        removed = False
        for j in range(0, len(num)):
            if num[j] >= first:
                first = num[j]
                continue
            else:
                num.pop(j - 1)
                removed = True
                break
        
        if not removed:
            num.pop(-1)   
        
    if len(num) == 0:
        return "0"
    num =[str(n) for n in num]
    result = str(int(''.join(num)))
    
    return result

r = removeKdigits(1, "112")
print(r)