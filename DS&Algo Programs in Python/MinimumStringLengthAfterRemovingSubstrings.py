class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for alpha in s:
            if alpha == "B" and len(stack) >= 1:
                if stack[-1] == "A":
                    stack.pop()
                else:
                    stack.append(alpha)

            elif alpha == "D" and len(stack) >= 1:
                if stack[-1] == "C":
                    stack.pop()
                else:
                    stack.append(alpha)
            else:
                stack.append(alpha)
        return len(stack)
            
            
