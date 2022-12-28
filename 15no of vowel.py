a =input('enter the word:')
vowel =['a','e','i','o','u']
def count(a):
    count1=0
    count2=0
    for i in a:
        if i in vowel:
            count1+=1
        else:
            count2+=1
    print('no of vowel:',count1)
    print('no of constant:',count2)
count(a)
