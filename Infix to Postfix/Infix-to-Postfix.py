class poshte:
    def __init__(self):
        self.b = []

    def count(self):

        return len(self.b)

    def is_empty(self):
        if len(self.b) == 0:
            return True
        else:
            return False

    def set(self, a):
        self.b = a

    def push(self, v):
        self.b.append(v)

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

        # self.i=0
        while len(self.b) != 0:
            del self.b[0]




if __name__ == "__main__":

    # print("please enter your sentence")
    # a=str(input("please enter your sentence:"))
    o = poshte()
    a = str(input("please enter your sentence:"))
    i = 0
    j = ""
    sen = ""

    while i < len(a):
        k = o.top()

        if a[i] != '+' and a[i] != '-' and a[i] != '*' and a[i] != '/' and a[i] != '(' and a[i] != ')':
            sen = sen + a[i]

        elif a[i] == '(':
            o.push(a[i])

        elif a[i] == ')':
            j = o.pop()

            while j != '(':
                sen = sen + j

                j = o.pop()
        elif a[i] == '-' or a[i] == '+' or a[i] == '*' or a[i] == '/':

            if o.count() == 0:

                o.push(a[i])


            elif  a[i] == '-':
                while True:
                    if o.top()=='-' or o.top()=="+"or o.top()=="*"or o.top()=="*":
                        sen = sen + o.pop()

                    else:break


                o.push(a[i])



            elif a[i] == '+':
                while True:
                    if o.top() == '-' or o.top() == "+"or o.top()=="*"or o.top()=="*":
                        sen = sen + o.pop()

                    else:
                        break

                o.push(a[i])




            elif a[i] == '*':
                while True:
                    if o.top() == '*' or o.top() == "/":
                        sen = sen + o.pop()

                    else:
                        break

                o.push(a[i])

            elif a[i] == '/':
                while True:
                    if o.top() == '*' or o.top() == "/":
                        sen = sen + o.pop()

                    else:break

                o.push(a[i])


            else:
                o.push(a[i])

        i = i + 1

    while o.count() != 0:
        sen = sen + o.pop()

    print(sen)