passord = input("Enter a password: ")
uppercase = False
lowercase = False
number=False
specialchar = False
char=('@','#','$','%','&','*')
if len(passord)>=8:
    for i in passord:
        if (i.isupper()):
            uppercase=True
        elif (i.islower()):
            lowercase=True
        elif (i.isdigit()):
            number=True
        elif i in char:
            specialchar=True
    if(uppercase and lowercase and number and specialchar):
        print("Valid Password")
    else:
        print("Not a valid password")
else:
    print("Password must be atleast 8 char long")