print("THIS IS THE PROGRAM TO FIND THE LEAP YEAR\n\n")
m = int(input("Enter the year : \n"))
if m%100 == 0:
    print(str(m),"is a Leap Year")
elif m%4 == 0:
    print(str(m),"is a Leap Year")
else:
    print(str(m),"is not  a leap year")
