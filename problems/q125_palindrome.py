def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    import re
    s = re.sub(r'[^a-zA-Z0-9]', '',s).lower()
    #s = s.replace(' ','')
    print(s)
    mid = int((len(s) + 1) / 2)

    for i in range(mid):
        back = len(s) - i - 1
        if s[back] != s[i]:
            return False
    
    return True



input_string=\
"""
"A man, a plan, a dsfsdanal: Panama"
"""