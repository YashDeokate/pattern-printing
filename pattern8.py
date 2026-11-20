#Question 8: Inverted Star Pyramid

n=5
for i in range(n,0,-1): #iterate from 5 to 1
    for j in range(1,n+1-i): # printing spaces before the stars in the inverted pyramid and the number of spaces will be equal to the row number
        print(" ", end=" ") #here we are printing spaces to align the inverted pyramid to the center
    for k in range(1,2*i): #in k loop we are printing the stars in the inverted pyramid and the number of stars will be equal to 2*row number-1
        print("*", end=" ")  # printing the stars in the inverted pyramid
    print()  