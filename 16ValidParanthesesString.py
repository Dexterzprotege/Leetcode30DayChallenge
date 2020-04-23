'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        right = len(s)-1
        openCount, closedCount = 0, 0
        for i in range(0, right+1):
            if (s[i] == '*' or s[i] == '(') :
                openCount += 1
            else:
                openCount -= 1
            if (s[right - i] == '*' or s[right - i] == ')'):
                closedCount += 1
            else:
                closedCount -= 1
            if (openCount < 0 or closedCount < 0) :
                return False
        return True
            
