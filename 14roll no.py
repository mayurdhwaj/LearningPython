a=int(input('enter the roll no:'))
rollno = [1,2,3,4,5,6,7,8]
def is_present(a):
    if a in rollno:
        print(a,'roll no is present')
    else:
        print('absent')
is_present(a)