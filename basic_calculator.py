class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
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
        s.replace(" ","")
        
        # Initialize expression stack
        exprstack = []
        
        # Read the string from leftmost character to the rightmost
        for ch in range(len(s)):
            if ch == '(':
                continue
            else if isinstance(ch, int):
                exprstack.append(ch)
            else if 
