
# Question 12: Butterfly Pattern

for i in range(1, 6): #iterate till 5

    for j in range(1, i+1): #printing stars in the left wing 
        print("*", end=" ")

    # Middle spaces
    for j in range(1, 2*(5-i)+1): #printing spaces in the middle oF pattern
        print(" ", end=" ")

    # Right wing
    for j in range(1, i+1): #Printing stars in the right wing
        print("*", end=" ")

    print()

# Lower half
for i in range(4, 0, -1): #iterate from 4 to 1

    
    for j in range(1, i+1): #printing stars in the left wing
        print("*", end=" ")

    for j in range(1, 2*(5-i)+1): #printing spaces in the middle of pattern
        print(" ", end=" ")

  
    for j in range(1, i+1): #printing stars in the right wing
        print("*", end=" ")

    print()
