def balanced_brackets(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    opening = set('([{')
    closing = set(')]}')
    
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
    
    return len(stack) == 0
