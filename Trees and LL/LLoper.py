import sys
from BaseClass import Node
from random import randint

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertBeg(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        if self.head.next == None:
            self.tail = self.head
        return self.head

    def insertEnd(self,data):
        temp = Node(data)
        temp.next = None
        self.tail.next = temp
        self.tail = temp
        return self.tail

    def insertAtPos(self,data,pos):
        temp = Node(data)
        count = 1
        curr = self.head
        while count < pos-1:
            curr = curr.next
            count += 1
        storeNext=curr.next
        curr.next = temp
        temp.next = storeNext

    def delete(self):
        if self.head.next == None:
            self.tail = None
        self.head = self.head.next
        return self.head

    def printLL(self):
        curr = self.head
        while curr !=None:
            print curr
            curr = curr.next

    ##This does not reverses the linked list, this just prints the reverse list
    def reversePrint(self,x):
        if x == None:
            return
        self.reversePrint(x.next)
        print x
        

    ##This actually reverses linked list physically
    def reverseLLInPlace(self,x,end):
        if x == None:
            return
        if x.next==None:
            self.head=x
        temp = x.next
        x.next = end
        end = x
        self.reverseLLInPlace(temp,x)

    ##function reverse LL in pair of k, for example 1-2-3-4-5-6 becomes
    ##3-2-1-6-5-4
    def reverseK(self,x,count,k,end):
        if count>k or x==None:
            return end
        if count <=k:
            temp = x.next
            x.next = end
            end = x
            return self.reverseK(temp,count+1,k,end)
        

    def revK(self,k):
        curr = self.head
        cnt = 0
        previ = None
        while curr != None:    
            temp = curr
            count = 0
            
            while curr!=None and count != k:
                count += 1
                curr = curr.next
            m = self.reverseK(temp,1,k,curr)

            if temp.value == self.head.value:
                self.head=m
                previ = m
            else:
                previ.next = m
                previ = m
            cnt = 0
            if previ != None:
                while cnt < k-1 and previ!=None:
                    previ = previ.next
                    cnt += 1

a = LinkedList()
b = LinkedList()
for i in range(1,8):
    a.insertBeg(i)
a.reverseLLInPlace(a.head,None)
a.revK(3)
a.printLL()
print "\nholalala"
for i in range(3,9,1):
    b.insertBeg(i)
a.reverseLLInPlace(a.head,None)
b.reverseLLInPlace(b.head,None)
result = LinkedList()

##http://www.geeksforgeeks.org/sum-of-two-linked-lists/
def addtwoLL(a,b,result,carry):
    if a==None or b==None:
        if a==None and b != None:
            sumi=b.value+carry
            res = sumi%10
            carry = sumi/10
            result.insertBeg(res)
            return addtwoLL(None,b.next,result,carry)
            
        if b==None and a != None:
            sumi=a.value+carry
            res = sumi%10
            carry = sumi/10
            result.insertBeg(res)
            return addtwoLL(a.next,None,result,carry)

        if a==None and b==None and carry>9:
            res = carry%10
            carry = carry/10
            result.insertBeg(res)
            addtwoLL(None,None,result,carry)
        if a==None and b==None and carry<=9:
            result.insertBeg(carry)
            return result
    else:
        sumi = a.value+b.value+carry
        res = sumi%10
        carry = sumi/10
        result.insertBeg(res)
        return addtwoLL(a.next,b.next,result,carry)
    
x = addtwoLL(a.head,b.head,result,0)    
x.printLL()

##LL to test merge sort functions
sortLL = LinkedList()
sortLL.insertBeg(5)
sortLL.insertBeg(9)
sortLL.insertBeg(6)
sortLL.insertBeg(8)
sortLL.insertBeg(5)
def findMid(x):
    if x==None:
        return
    if x.next==None:
        return x
    slow = x
    fast = x
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

def mergeSortLL(x):
    if x.next==None:
        return x
    mid = findMid(x)
    temp = mid.next
    mid.next = None
    a = mergeSortLL(x)
    b = mergeSortLL(temp)
    return merge(a,b)
    
def merge(head,mid):
    if head == None:
        return mid
    if mid == None:
        return head
    curr = Node()
    temp = curr
    while head!=None and mid!= None:
        if head.value<=mid.value:
            temp.next = head
            head = head.next
        else:
            temp.next=mid
            mid=mid.next

        temp= temp.next
    if head==None and mid != None:
        temp.next = mid
    else:
        temp.next = head
    return curr.next    
        


s= mergeSortLL(sortLL.head)
print s.next
print "\n yayaya \n"
while s != None:
    print s
    s = s.next
