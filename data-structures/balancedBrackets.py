# python3

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def GetPosition(self):
        return self.position;

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True

        return False


class Stack:
    def __init__(self):
        self.storage = []

    def pop(self):
        return self.storage.pop()

    def push(self, element):
        self.storage.append(element)

    def empty(self):
        return len(self.storage) == 0


def isBalanced(text):
    BracketsStack = Stack()
    problemBracket = False

    for i, next in enumerate(text):
        current_text_position = i + 1;

        if next == '(' or next == '[' or next == '{':
            BracketsStack.push(Bracket(next, current_text_position))

        if next == ')' or next == ']' or next == '}':
            if not BracketsStack.empty():
                prevBracket = BracketsStack.pop();

                if not prevBracket.Match(next):
                    problemBracket = current_text_position
                    break
            else:
                problemBracket = current_text_position

    if problemBracket != False:
        return problemBracket
    elif not BracketsStack.empty():
        return BracketsStack.pop().GetPosition()
    else:
        return "Success"


if __name__ == "__main__":
    text = sys.stdin.read()

    print(isBalanced(text))