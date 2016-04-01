"""
Anjali Shah and Roni Kobrosly
4/1/2016

https://leetcode.com/problems/basic-calculator/
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        Remove all whitespaces from the expression string.
        
        Build an expression stack. Push operands into the stack until you encounter an operator.
        Upon encountering an operator, pull the last operand and perform the operation (based on the nature of
        the operator) with the next operand in the expression string.
        
        Special cases:
        
        1. Parentheses: When '(' is encountered, push all expression operators and operands onto the stack
        until the ')' is ecountered. This forms a mini-expression for which the steps outlined above should be 
        repeated.
        
        """
