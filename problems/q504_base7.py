def convertToBase7(self, num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return '0'

    vals = []
    minus = False
    if num < 0:
        minus = True

    num = abs(num)
    while num > 0:
        num, r = divmod(num, 7)
        vals.insert(0, str(r))

    if not minus:
        return ''.join(vals)
    else:
        return '-' + ''.join(vals)

# --- Things needed for this infrastructure to run ----
modifier = ''
signature = 'def convertToBase7(self, num):'
test_cases = None
input_string = """100
-200
"""  