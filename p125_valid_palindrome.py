'''
Usuage: python3 p125_valid_palindrome.py

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''
def valid_val(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    elif ord('0') <= ord(c) <= ord('9'):
        return True

    else:
        return False
def isPalindrome(s):
    l, r = 0, len(s)-1

    while l < r:
        if not valid_val(s[l].lower()):
            l +=1
        elif not valid_val(s[r].lower()):
            r -=1
        else:
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
    return True


# Test #0
s = "Amma"
print(f'0st: Expect True ---> Actual: {isPalindrome(s)}')

# Test #1
s = "A man, a plan, a canal: Panama"
print(f'1st: Expect True ---> Actual: {isPalindrome(s)}')

# Test #2
s = "race a car"
print(f'1st: Expect False ---> Actual: {isPalindrome(s)}')

# Test #3
s = " "
print(f'1st: Expect True ---> Actual: {isPalindrome(s)}')



