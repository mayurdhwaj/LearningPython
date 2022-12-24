a=input()#if input is integer  typecast integer into string str()
x=str(a)
c=x[::-1]
if x==c:
    print(a,'is palindrome')
else:
    print('not a palindrome')