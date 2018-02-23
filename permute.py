def permute(chs):
    
    def allRange(a,l,r,res):
        if l==r:
            b=a[:]
            res.append(b)
        else:
            for i in range(l,r):
                a[l],a[i]=a[i],a[l]
                allRange(a,l+1,r,res)
                a[l],a[i]=a[i],a[l]
    result=[]
    allRange(chs,0,len(chs),result)
    return result

print(permute(list("abcd")))
