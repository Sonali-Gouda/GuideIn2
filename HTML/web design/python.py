a=input()
b=input()
mul=add=sub=""
t1=t2=t3=0
for i in range(len(a)):
    t1=int(a[i]+b[i])
    t2=abs(int(a[i]-b[i]))
    t3=int(a[i]*b[i])
    print(t1,t2,t3)