'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
x=int(input("Enter number="))
s=0;
r=x;
while r>0:
    d=r%10
    s=s+d**3
    r=r//10
if s==x:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
