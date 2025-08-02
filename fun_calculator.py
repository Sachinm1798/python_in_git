def sum(a,b):
     x = a+b
     print("The sum of given numbers is : ",x)
def mul(a,b):
    x = a*b
    print("The muliplication of given numbers is : ",x)
def diff(a,b):
    x = a-b
    print("The subtraction of given numbers is : ",x)
def div(a,b):
    x = a/b
    print("The division of given numbers is : ",x)
input("The Simple calculator using functions\n")
k,l = input("Enter the two numbers seperated by commas : ").split(',')
i=input("Enter the Keyword to perforrm calculation\n""A:Addition M:Multiplication D:Division S:Subtraction")
a = int(k)
b = int(l)
if i == "A":
    sum(a,b)
elif i == "M":
    mul(a,b)
elif i == "D":
    div(a,b)
elif i == "S":
    diff(a,b)
else:
    print("Give a valid input")
















