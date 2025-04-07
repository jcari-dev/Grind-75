class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for character in s:

            if stack == []:
                most_recent = character
            else:
                most_recent = stack[-1]

            if most_recent == "{" and character == "}":
                stack.pop()
            elif most_recent == "(" and character == ")":
                stack.pop()
            elif most_recent == "[" and character == "]":
                stack.pop()
            else:
                stack.append(character)
        
        return stack == []
