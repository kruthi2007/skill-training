"""a={10,2,3,5j,False,'hi',(1,2)}
print(a)"""
'''a={'a':[10,20,30],'b':40}
print(a['a'][1])
'''
'''a='Hello'
print(a[2:4])
print(a[-3:-2+1])'''
'''a="good morning"
print(a[-5:-2+1:1])'''
'''a='Hello'
print(a[3:0:-1])
print(a[-2:-5:-1])
print(a[-1:-5-1:-1])
print(a[::-1])'''
'''a='Good Morning'

'odM'
print(a[1:5+1:2])

'Mng'
print(a[5::3])
print(a[-7::3])'''

'''a='Good Morning'

'nr '
print(a[-2:-8-1:-3])
print(len(a[10:4-1:-3]))'''

'''a=input("enter:")
print(type(a))'''

'''a=float(input("enter:"))
print(type(a))'''

'''a=eval(input("enter:"))
print(a,type(a))
'''
'''a=int(input("enter:"))

if a%2==0:
    print('even')
else:
    print('odd')'''

'''l=eval(input("enter:")) 
if len(l)==5:
    print('yes')
else:
    print('no')'''

'''print(ord('a'))
print(ord('A'))
print(chr(97))
 # This will return the Unicode code point for the character 'char'''
'''ch=input("enter:")'''

'''if "A"<=ch<="Z":
    print("uppercase")
elif "a"<=ch<="z":
    print("lowercase")
else:
    print("not a alpha")'''


'''un=input("enter:")
if un=='kruthi':
    print('correct username')

    pw=input("enter:")
    if pw=='kruthi123':
        print('successfully login')
    else:
        print('invalid password')
else:
    print('invalid username')'''

'''i=1
while i<=100:
    print(i)
    i=i+1 '''

#number of even numbers between 1 to 50
'''i=1
while i<=50:
    if i%2==0:
        print(i)
    i=i+1'''

#reverse of a number
'''n=int(input("enter num:"))
rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
print(rev)'''

'''for i in range(1,101):
    print(i)'''

'''for i in range(1,51):
    if i%2==0:
        print(i,"even")'''

'''l=[10,20,30]
for i in l:
    print(i)'''

'''s=input("enter:")
out=""
for i in s:
    if "A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif "a"<=i<="z":
        out+=chr(ord(i)-32)
    else:
        out+=i
print(out)'''

#using for loop to reverse a number
s=int(input("enter num:"))
rev=''
'''for i in str(s):
    rev=i+rev
print(rev)'''

'''for i in range(1,6):
    for j in range(1,6):
        print('*',end="")
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('*',end="")
        print(' ',end="")
    print()'''

for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('1',end="")
        print('@',end="")
    print()
    



