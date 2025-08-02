print("The program to print numbers")
x = int(input("Enter the number to which you have to print : "))
if x == 0:
    print("Enter a number greater than zero")
elif x < 0 :
    print("Enter a positive number")
else:
    print ("The numbers are")
    i = 1
    while  i <= x:
        print(i)
        i = i+1
print ("Loop finished")


