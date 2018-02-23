
def stringContain(s1,s2):
    d={}
    for i in range(len(s1)):
        d[s1[i]]=i
    sign=0
    for j in range(len(s2)):
        if s2[j] not in d:
            sign+=1
    if sign!=0:
        return False
    else:
        return True

print(stringContain("abc","acad"))

def brostring(s1,s2):
    l1=len(s1)
    l2=len(s2)
    if l1!=l2:
        return False
    d={}
    sign=0
    sum=0
    for i in range(l1):
        if s1[i] in d:
            d[s1[i]]+=1
        else:
            d[s1[i]]=1
    for i in range(l2):
        if s2[i] in d:
            d[s2[i]]-=1
        else:
            sign+=1
    for i in d.keys():
        sum=sum+d[i]
    if sum!=0 or sign!=0:
        return False
    else:
        return True
print(brostring("abc","bac2"))
            
