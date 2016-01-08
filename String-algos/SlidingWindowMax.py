##max of the sliding window
from BaseClass import Node

class LL:
    def __init__(self):
        self.back = None
        self.front = None
    def push_back(self,value):
        newnode = Node(value)
        temp = self.back
        newnode.next = temp
        if self.back == None:
            self.front = newnode
            self.back = newnode
        else:
            self.back.prev = newnode
            self.back = newnode

    def pop_back(self):
        if self.back!=None:
            temp = self.back.value
            self.back = self.back.next
            if self.back == None:
                self.front=None
            return temp
    def pop_front(self):
        if self.front!=None:
            temp = self.front.value
            self.front = self.front.next
            if self.front == None:
                self.back = None
            return temp

Q = LL()
a = map(int,raw_input().split())
k = int(raw_input())
b = []
for i in range(k):
    while Q.front != None and Q.back != None and a[i]>=a[Q.back.value]:
        print Q.pop_back()
    Q.push_back(i)

for i in range(k,len(a)):
    b.append(a[Q.front.value])
    while Q.front != None and Q.back != None and a[i]>=a[Q.back.value]:
        print Q.pop_back()
    
    while Q.front != None and Q.back != None and Q.front.value<=i-w:
        print Q.pop_front()
    Q.push_back(i)
b.append(a[Q.front.value])
print b

            
