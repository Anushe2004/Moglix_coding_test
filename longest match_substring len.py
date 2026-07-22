def find_longest_match(s):
    if s == "":
        return 0
    n = len(s)
    max_len = 0
    op = 0
    close = 0
    for i in range(n):
        char = s[i]
        if char == '(':
            op += 1
        elif char == ')':
            close += 1
            
        if op == close:
            max_len = max(max_len, 2 * close)
        elif close > op:
            op = 0
            close = 0
            
    op = 0
    close = 0
    for i in range(n - 1, -1, -1):
        char = s[i]
        if char == '(':
            op += 1
        elif char == ')':
            close += 1
        if op == close:
            max_len = max(max_len, 2 * op)
        elif op > close:
            op = 0
            close = 0
    return max_len

s = "(()"
print(find_longest_match(s))

