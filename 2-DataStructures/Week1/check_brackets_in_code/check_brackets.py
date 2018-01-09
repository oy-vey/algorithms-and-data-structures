# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    head = -1
    opening_brackets_stack = []
    result = True
    for i, symb in enumerate(text):
        if symb == '(' or symb == '[' or symb == '{':
            opening_brackets_stack.append(symb)
            head += 1
            b = Bracket(opening_brackets_stack[head], i)
            pass

        if symb == ')' or symb == ']' or symb == '}':
            if head == -1:
                result = False
                print(i + 1)
                break
            else:
                b = Bracket(opening_brackets_stack[head], i)
            if not b.Match(symb):
                print(i + 1)
                result = False
                break

            opening_brackets_stack.pop()
            head -= 1
            pass

    if head == -1:
        print('Success')
    elif result:
        print(b.position + 1)
