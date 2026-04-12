class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        s = s.replace(' ', '')
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

        print(s)