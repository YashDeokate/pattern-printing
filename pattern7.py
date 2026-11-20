#Question 7: Star Pyramid

n=5
for i in range(1,n+1): #iterate till 5
    for j in range(1,n+1-i): # printing spaces before the stars in the pyramid and the number of spaces will be equal to the row number
        print(" ", end=" ") #here we are printing spaces to align the pyramid to the center
    for k in range(1,2*i): #in k loop we are printing the stars in the pyramid and the number of stars will be equal to 2*row number-1
        print("*", end=" ")  # printing the stars in the pyramid
    print()  # printing a new line after each row of the pyramid