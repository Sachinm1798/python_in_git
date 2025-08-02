print("This is the program to print multiplication table\n")
i = int(input("Enter the Number to Find Multiplication table : "))
j = int(input("\nEnter the limit to which you need to find:"))
x = 1
for x in range(1,j+1):
        print(x*i,end = '\t')
