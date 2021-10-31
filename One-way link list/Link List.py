import sys

from pip._vendor.requests.utils import select_proxy


class node:
    def __init__(self,data=None,next=None):
        self.data=data;
        self.next=next;




    def __str__(self):
        return str(self.data)






class list:
    def __init__(self):
        self.header = node("Empty")
        self.pointer=node(None)
        self.pointer.next=self.header






    def insert(self,item):
        #if self.header.next==None:


        self.d=node(item)
        self.p=self.pointer.next
        if self.p.next==None:
            self.p.next=self.d
        else:
            self.d.next=self.p.next
            self.p.next=self.d

        self.pointer.next=self.d

    def insertbef(self,item):
        self.pointer.next=self.findbef()
        self.insert(item)


    def insertatfirst(self):
        self.p=node()

        if self.pointer.next!=self.header:
           self.p=self.pointer.next
        #if self.p!=None:
           self.o=self.p.data
           self.remove()
           self.pointer.next=self.header.next
           self.insertbef(self.o)
        #print(self.p.next)





    def poin(self):
        self.p=self.pointer
        print(self.p.next)



    def poin1(self):
        self.p=self.pointer
        return self.p.next

    def printlist(self):
        self.sen=""

        if self.header.next==None:
            print("Empty")
        else:
         self.d=self.header.next
         while self.d:
           self.sen=self.sen+str(self.d)
           self.sen=self.sen+" "
           self.d = self.d.next
         print(self.sen)



    def findprevious (self):
        self.current = self.header
        while (self.current.next != None and self.current.next !=self.pointer.next):
            self.current = self.current.next

        self.cur = node()
        self.cur = self.current
        if self.cur.data!=None:self.pointer.next=self.cur
        #print(self.pointer.next)





    def findafter(self):
        self.current = self.header
        while (self.current.next != None and self.current.next != self.pointer.next):
            self.current = self.current.next

        self.cur = node()
        if self.current.next==None:
            self.pointer.next=self.header
        else :
            self.cur = self.current.next
            if self.cur.next != None: self.pointer.next = self.cur.next


       # print(self.pointer.next)

    def head(self):
        print(self.header.next)


    def remove(self):
        self.re=self.findbef()
        self.w=self.pointer.next
        if self.re.data==None and self.w.next==None:
            self.re.next=self.w.next
            #print("hello")
            #self.findafter()
            self.pointer.next=self.header
            #self.pointer.next=self.header

        else:
          if self.w!=self.header:
           self.findaf()
          if self.w!=None:self.re.next = self.w.next
        #if self.w.next==None:self.re.next=self.w.next

    def findbef(self):
        self.current = self.header
        while (self.current.next != None and self.current.next != self.pointer.next):
            self.current = self.current.next

        self.cur = node()
        self.cur = self.current
        # print(self.cur.data)
        #if self.cur.data != None: self.pointer.next = self.cur
        return self.cur



    def findaf(self):
        self.current = self.header
        while (self.current.next != None and self.current.next != self.pointer.next):
            self.current = self.current.next

        self.cur = node()
        if self.current.next==None :self.pointer.next = self.header.next
        else:

          if self.current.next.next == None:
            self.pointer.next = self.header.next
          else:
            self.cur = self.current.next
            if self.cur.next != None:
                self.pointer.next = self.cur.next







if __name__ == '__main__':

    obj=list()
    while True:
        a = str(input())
        if a[0]==";":
            break
        if a[0]=="+":obj.insert(a[1:len(a)])
        if a[0]=="-":obj.remove()
        if a[0]=="*":obj.insertatfirst()
        if a[0]=="?":obj.printlist()
        if a[0]=="@":obj.insertbef(a[1:len(a)])
        if a[0]=="^":obj.poin()
        if a[0]==">":obj.findafter()
        if a[0]=="<":obj.findprevious()
        if a[0]=="!":obj.head()




