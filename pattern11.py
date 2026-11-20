#Question 11: Hollow Right-Angled Triangle

n=5
for i in range(1, n+1): #iterate till 5
    for j in range(1, i+1): #iterate till the current row number
        if j==1 or j==i or i==n: #current position is on the border of the triangle
            print("*", end=" ") #printing stars on the border of the triangle
        else:
            print(" ", end=" ") #printing spaces inside the triangle
    print() 