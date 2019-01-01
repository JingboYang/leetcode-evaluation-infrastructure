
def lala(str):
    splits = str.split()
            
    for s in splits:
        
        sign = 1
        s = s.strip()
        if len(s) > 0:
            if s[0] == '-':
                sign = -1
        
            if s.isnumeric():
                return int(s) * sign


print(' -42')