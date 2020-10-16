from array import *
class Stack():
    def _init_(self):
        self.items = array('i',[4,3,2,4072])

    def end(self, item):
        self.items.append(item)
        print(item)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        if self.items:
            return len(self.items)
        else:
            return None

    def display(self):
        for i in self.items:
            print(i)

    def start(self, i):
        self.items.insert(0, i)

    def search(self, a):
        l = self.items
        for i in l:
            if i == a:
                print("found Value : ", a)
                break
        else:
            print("not found")

    def traverse(self):
        a = []
        l = self.items
        for i in l:
            a.append(i)
        print(a)

    def shoting_element(self):
        
        nums=self.items
        def sort(nums):
            for i in range(len(nums) - 1, 0, -1):
                for j in range(i):
                    if nums[j] > nums[j + 1]:
                        temp = nums[j]
                        nums[j] = nums[j + 1]
                        nums[j + 1] = temp

        sort(nums)
        print(nums)
    def reverse(self):
        l=self.items
        print(l[::-1])

class merge1(Stack):
 
    def _init_(self):
        Stack._init_(self)
        self.items1 = array('i',[4,3,2,1,6])

    def merge(self):
        l = self.items
        l1=self.items1
        a=(l+l1)
        print(a)

s = Stack()

s.end(5)
s.end(6)
s.end(7)
s.start(-1)
s.start(-2)
print("search the specific value : ")
s.search(-2)

print("Display the values one by one :")
s.display()
print("peek (End  Value) :", s.peek())
print("treverse the values : ")
s.traverse()


print("Shotting the values : ")
s.shoting_element()

print("Reversing  the values : ")
s.reverse()

s1=merge1()
print("merge")
s1.merge()