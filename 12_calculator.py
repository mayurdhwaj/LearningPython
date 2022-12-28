a =  int(input('enter 1st number :'))
b= int(input('enter 2nd number:'))
c=input('enter the operation')
def calculator(a,b,c):
    if c=='+':
        x=a+b
        print(x)
    elif c=='-':
        x=a-b
        print(x)
    elif c=='*':
        x=a*b
        print(x)
    elif c=='/':
        x=a/b
        print(x)
    elif c=='%':
        x=a%b
        print(x)
    else:
        print('enter the correct operation')

#calculator(5,3,'+')
calculator(a,b,c)
