'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

'''

def isValid(s) -> bool:
    # input s = "()"
    check = {'{':'}', '[':']', '(':')'}
    stack = []

    for c in s:                     # c = )
        if c in check:
            stack.append(check[c])      # stack = ['(']
        else:
            if len(stack) == 0:
                return False

            tmp = stack.pop()
            if c != tmp:
                return False
    return len(stack) == 0

input = ["()","()[]{}", "(]", "]","[", ""]
expect = [True, True, False, False, False, True]

for i in range(len(input)):
    print(f'Test # {i+1}: Expected {expect[i]} ---> Output {isValid(input[i])}')


