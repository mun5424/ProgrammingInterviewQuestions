def operate(op, second, first):
    if op == '+':
        return first + second
    if op == '-':
        return first - second
    if op == '*':
        return first * second
    if op == '/':
        return first / second

def precedence(current_op, op_from_stack):
    if op_from_stack == '(' or op_from_stack == ')':
        return False
    if (current_op == '*' or current_op == '/') and (op_from_stack == '+' or op_from_stack == '-'):
        return False
    return True


def basicCalculator(s):
    nums = [] 
    ops = [] 
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            num = ord(c) - ord('0')
            while i+1 < len(s) and s[i+1].isdigit():
                num = num * 10 + ord(s[i+1])-ord('0')
                i +=1
            nums.append(num)
        elif c == ')':
            while ops and ops[-1] != '(':
                nums.append(operate(ops.pop(), nums.pop(), nums.pop()))
            ops.pop()
        elif c == '(':
            ops.append(c)
        elif c in '+-*/':
            while ops and precedence(c, ops[-1]):
                nums.append(operate(ops.pop(), nums.pop(), nums.pop()))
            ops.append(c) 
    
    while ops: 
        nums.append(operate(ops.pop(), nums.pop(), nums.pop()))

    return nums.pop() 



