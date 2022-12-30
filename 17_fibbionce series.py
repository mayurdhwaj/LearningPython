a=0
b=1
c=int(input())
def feb(c):
    global a
    global b
    for i in range(2,c):#0,1,1,
        x=a+b
        a=b
        b=x
        print(x)
print(a)
print(b)
feb(c) 