class Solution(object):
    
"""
        Remove all the whitespaces from the expression string.
        
        Build an expression stack. Push operands into the stack until you encounter an operator.
        Upon encountering an operator, push the last operand and perform the operation based on the nature of
        the operator with the next operand in the expression string.
        
        Special cases:
        
        1. Parentheses: When '(' is encountered, push all expression operators and operands onto the stack
        until the ')' is ecountered. This forms a mini-expression for which the steps outlined above should be 
        repeated.  
"""

    # Remove whitespace characters from string 
    s = "".join(s.split())

    # Initialize expression stack
    expression = list(s)

    def calculate(self, expression):
        
        # Find complete parenthesis and then recursively call "calculate function" until you
        # only have a complete math expression to evaluate

        paren_start = 0
        paren_end = 0
        index = -1
        for ch in range(len(expression)):
            index += 1
            if ch == '(':
                paren_start = index
                continue
            if ch == ')':
                paren_end = index

        # Isolate characters contained with parenthesis
        sub_list = expression[(paren_start + 1):paren_end]

        # This is where the recursion would happen. 
        calculate(sub_list)







