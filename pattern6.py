#Question 6: Right-Aligned Triangle
n=5
for i in range(1,n+1): #here we are iterating through the rows of the triangle
    
    for j in range(1,n+1-i): # printing spaces before the stars in the triangle and the number of spaces will be equal to the row number
        print(" ", end=" ") #here we are printing spaces to align the triangle to the right
    for k in range(1,i+1): #in k loop we are printing the stars in the triangle and the number of stars will be equal to the row number
        print("*", end=" ")  # printing the stars in the triangle
    print()  # printing a new line after each row of the triangle