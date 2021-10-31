class HEAP():
    def __init__(self):

        self.heap = [0]
        self.length = 0

    def newsort(self, arr):
        n = len(arr)

        for i in range(n, -1, -1):
            self.newcahnge(arr, n, i)

        self.heap = self.heap + arr

    def newcahnge(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.newcahnge(arr, n, largest)

    def insert(self, item):
        self.heap.append(item)
        self.change(len(self.heap) - 1)

    def rem(self):
        if len(self.heap) > 2:
            self.swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.change1(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = "Empty"
        return max

    def swap(self, i, j):
        self.temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = self.temp

    def heapsort(self):
        self.w = []

        while True:
            if len(self.heap) == 1:
                break
            self.w.append(self.rem())

        return self.w

    def change(self, item):
        parent = item // 2
        if item <= 1:
            return
        elif self.heap[item] > self.heap[parent]:
            self.swap(item, parent)
            self.change(parent)

    def change1(self, item):
        left = item * 2
        right = item * 2 + 1
        largest = item
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != item:
            self.swap(item, largest)
            self.change1(largest)

    def pri(self):

        p = 1
        pp = 1
        k = 1
        se = ""
        if len(self.heap) == 1:
            print("Empty")
        else:
            while True:
                if k == len(self.heap):
                    break

                while p <= pp and k < len(self.heap):
                    se = se + str(self.heap[k]) + " "
                    k = k + 1
                    p = p + 1

                print(se)
                se = ""
                p = 1
                pp = pp * 2

    def printinline(self):
        p = 1
        pp = 0
        left = p * 2
        right = p * 2 + 1
        stri = ""

        if len(self.heap) == 0:
            print("Empty")
        else:
            if (len(self.heap) % 2) == 0:

                print(self.heap[p])
                while p < len(self.heap) // 2:
                    if len(self.heap) > left:
                        stri = str(self.heap[left]) + " "
                    if len(self.heap) > right:
                        stri += str(self.heap[right])
                    print(stri)
                    p = p + 1
                    left = p * 2
                    right = p * 2 + 1
                    stri = ""



            else:
                print(self.heap[p])
                while p <= len(self.heap) // 2:
                    if len(self.heap) > left:
                        stri = str(self.heap[left]) + " "
                    if len(self.heap) > right:
                        stri += str(self.heap[right])
                    print(stri)
                    p = p + 1
                    left = p * 2
                    right = p * 2 + 1
                    stri = ""

    def toin(self, index):
        co = 0
        r = 1
        if index == 1:
            return 0
        for i in range(1, len(self.heap)):
            co += 1
            r += i * 2
            if index <= r:
                return co

    def tarsim(self, k):
        if len(self.heap) == 1:
            print('Empty')
        # elif len(self.list) == 2:
        #   print(self.list[1])
        else:
            left = k * 2
            right = k * 2 + 1
            if len(self.heap) > right:
                self.tarsim(right)
            dep = self.toin(k)
            for i in range(dep):
                print('', end='\t')
            if len(self.heap) > k * 2 + 1 and len(self.heap) > k * 2:
                print(str(self.heap[k]) + '<')
            elif len(self.heap) > k * 2:
                print(str(self.heap[k]) + '\\')
            else:
                print(self.heap[k])
            if len(self.heap) > left:
                self.tarsim(left)
if __name__ == '__main__':

    p = HEAP()
    q = [1, 2, 3]
    e = []
    while True:
        a = str(input())
        q = []
        qq = []
        senten = ""
        kk = 0
        k = 1
        if a[0] == ";":
            break
        if a[0] == "+": p.insert(int(a[1:len(a)]))
        if a[0] == "-": print(p.rem())
        if a[0] == "?": p.pri()
        if a[0] == "=": p.tarsim(1)
        if a[0] == "*":
            qq = p.heapsort()
            kk = len(qq) - 1
            if len(qq) == 0:
                print("Empty")
            else:
                while kk >= 0:
                    senten = senten + str(qq[kk]) + " "
                    kk -= 1

                print(senten)

        if a[0] == "[":
            s = []
            p = HEAP()
            a = str(input())
            while a != "]":
                s.append(int(a))
                a = str(input())
            p.newsort(s)

        # print( s[0:len(s)])
        if a[0] == "!":
            p = HEAP()


