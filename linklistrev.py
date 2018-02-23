class Node(object):
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))

def rev(link):
    pre=link
    cur=link.next
    pre.next=None
    while cur:
        tmp=cur.next
        cur.next=pre
        pre=cur
        cur=tmp
    return pre

def rev2(link):
    if not link or not link.next:
        return link
    first=link
    rest=link.next
    newhead=rev2(rest)
    first.next.next=first
    first.next=None
    return newhead

    

def rev3(head,k):
    pre=head
    cur=head.next
    pre.next=None
    end=pre
    while cur and k-1>0:
        tmp=cur.next
        cur.next=pre
        pre=cur
        cur=tmp
        k=k-1
    end.next=cur
    return pre
def printlist(test):
    while test:
        print("%s->"%test.data)
        test=test.next
test=rev3(link,10)
printlist(test)

def rev_str(string,start,end):
    if not string:
        return
    while start<end:
        string[start],string[end]=string[end],string[start]
        start+=1
        end-=1
    return
    

l=list("abcdefghi")
print(l[-3:]+l[0:-3])
def revstr(string,k):
    l=len(string)
    if l<k:
        rev_str(string,0,l-1)
        return string
    else:
        rev_str(string,0,l-k-1)
        print(string)
        rev_str(string,l-k,l-1)
        print(string)
        rev_str(string,0,l-1)
        print(string)
        return string
print(revstr(l,3))
print(l)

def rev_word(string):
    return " ".join(string.split(' ')[::-1])
print(rev_word("I am a student."))


