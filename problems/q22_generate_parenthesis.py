def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """

    strings = []

    def recursion(string, new, balance):

        print(string)
        if new == 0 and balance == 0:
            strings.append(string)
            return

        if new > 0:
            recursion(string + '(', new - 1, balance + 1)
        if balance > 0:
            recursion(string + ')', new, balance - 1)
    
    recursion('', n, 0)
    return strings



# --- Things needed for this infrastructure to run ----
modifier = ''
signature = 'def generateParenthesis(self, n):'
test_cases = None
input_string = """
3
"""    