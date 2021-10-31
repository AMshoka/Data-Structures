'''
  File:  stack.py
  Description:  Stack implementation
  Author:Amirhossein mohammadi
  Student number:9543023
'''


class Stack:
    def __init__(self):
        self.b = []



    def count(self):
        return len(self.b)

    def is_empty(self):
        if len(self.b) == 0:
            return True
        else:
            return False

    def push(self, e):
        self.b.append(e)

    def top(self):
        try:
            self.i = len(self.b) - 1
            return self.b[self.i]
        except:
            return "stack is empty"


    def pop(self):
        try:
            self.i = len(self.b) - 1
            self.j = self.b[self.i]
            del self.b[self.i]
            return self.j
        except:
            return "stack is empty"


    def clear(self):
        while len(self.b) != 0:
            del self.b[0]

if __name__ == "__main__":
    s = Stack()

    line = input()
    tmp = line.split(' ')
    command = tmp[0]
    if len(tmp) == 2:
        value = tmp[1]


    while command != 'end':

        if command == 'push':
            s.push(value)
        elif command == 'pop':
            print(s.pop())
        line = input()
        tmp = line.split(' ')
        command = tmp[0]
        if len(tmp)== 2:
            value = tmp[1]

    print(s.count())
    out = ''
    while not s.is_empty():
        out += s.pop() + ' '
    print(out)

    try:
        s.pop()
    except Exception:
        print("Stack is empty.")