class Solution:
    def removeStars(self, s: str) -> str:
        myStack = []
        for char in s:
            if char == '*':
                if myStack:
                    myStack.pop()
            else:
                myStack.append(char)
        return ''.join(myStack)
