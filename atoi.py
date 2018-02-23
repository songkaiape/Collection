import sys
def atoi(s):
    if not s:
        return
    s=s.lstrip()
    l=len(s)
    i=0
    sum=0
    sign=1
    if s[0]=='+'or s[0]=='-':
        if s[0]=="+":
            sign=1
        else:
            sign=-1
        i+=1
        
    while i<l and s[i].isdigit() :
        c=int(s[i])
        if (sign>0 and (sum>sys.maxsize//10 or (sum==sys.maxsize//10 and c>sys.maxsize%10))):
            sum=sys.maxsize
            break
        elif (sign<0 and (sum>sys.maxsize//10 or (sum==sys.maxsize//10 and c>sys.maxsize%10))):
            sum=sys.maxsize
            break
        sum=sum*10+int(s[i])
        i+=1
    return sum if sign==1 else sum*-1
    
print(atoi("8888888888888888888"))
