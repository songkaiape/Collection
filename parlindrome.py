class Node(object):
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

def parlindrome(s):
    if not s :
        return False
    l=len(s)
    if l==1:
        return True
    left,right=0,0
    if l%2==0:
        left=l//2-1
        right=l//2
    else:
        left=l//2-1-1
        right=l//2+1-1
    while left>=0 and right<=l-1:
        if s[left]!=s[right]:
            return False
        left-=1
        right+=1
    return True

#print(parlindrome("abccbva"))
        
def rev_link(head):
    pre=head
    if not head.next:
        return head
    cur=head.next
    pre.next=None
    while cur:
        tmp=cur.next
        cur.next=pre
        pre=cur
        cur=tmp
    return pre
            
def printlist(test):
    while test:
        print("%s->"%test.data)
        test=test.next
def link_parlindrome(head):
    pre=fast=slow=head
    mid=head
    while fast:
        if fast.next==None:
            mid=slow.next
            break
        elif fast.next!=None and fast.next.next==None:
            mid=slow.next
            print(slow.data)
            print("Not even")
            break
        fast=fast.next.next
        slow=slow.next
    newhead=p=rev_link(mid)
    printlist(p)
    while newhead:
        if pre.data!=newhead.data:
            return False
        newhead=newhead.next
        pre=pre.next
    return True

link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(5, Node(4, Node(3, Node(2,Node(1))))))))))
print(link_parlindrome(link))
printlist(link)
                                                            

def stackParlindrome(stack):
    if not stack:
        return False
    if len(stack)==1:
        return True
    sign=False
    l=len(stack)
    if l%2==1:
        sign=True
    else:
        sign=False
    t=[]
    for i in range(l//2):
        t.append(stack.pop())
    if sign:
        stack.pop()
    for i in range(len(t)):
        if t[i]!=stack[i]:
            return False
    return True

print(stackParlindrome([1,2,3,4,3,2,1]))


def maxParlindrome(s):
    if not s:
        return
    l=len(s)
    start=maxlen=0
    for i in range(l):
        low,high=i-1,i
        while low>=0 and high<l and s[low]==s[high]:
            low-=1
            high+=1
        if high-low-1>maxlen:
            maxlen=high-low-1
            start=low+1
        low,high=i-1,i+1
        while low>=0 and high<l and s[low]==s[high]:
            low-=1
            high+=1
        if high-low-1>maxlen:
            maxlen=high-low-1
            start=low+1
    return s[start:maxlen+start]

print(maxParlindrome("dsdasdasdassssaaaddadaa"))
    
