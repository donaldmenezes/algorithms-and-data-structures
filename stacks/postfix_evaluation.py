import Stack # as prviously defined 

def do_math(op, op1, op2):
    """
    assumes op is the operator, +, *, /, - and op1 and op2 are numbers.
    evaluates op1 and op2 as per the op
    
    >>> do_math(+, 1, 0)
    1
    """
    
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2
        
        
def postfix_eval(postfix_expr):
    """ 
    Assumes that the postfix_expr has numeric characters - '0123456789', and operators are +, -, /, *;
    evaluates the expression and returns the result
    
    >>>456*+
    34
    """
    
    #creating a stack to store operands
    operand_stack = Stack()
    token_list = postfix_expr.split()
    
    for token in token_list:
        if token in '0123456789':
            #pushing the operand to the stack
            operand_stack.push(int(token))
        else:
            #ejecting the last two operands of the stack when an operator is detected
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            #evaluating the two operands with the operator token
            result = do_math(token, operand_1, operand_2)
            #pushing the result back to the stack for further evaluation of the postfix expression
            operand_stack.push(result)
            
    return operand_stack.pop()
    

print(postfix_eval('7 8 + 3 2 + /'))
