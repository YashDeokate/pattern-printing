#Question 10: Hollow Square

n=5
for i in range(n): #iterate till 5
    for j in range(n): #iterate till 5
        if i==0 or i==n-1 or j==0 or j==n-1: #e current position is on the border of the square
            print("*", end=" ") #printing stars on the border of the square
        else:
            print(" ", end=" ") #printing spaces inside the square
    print()  