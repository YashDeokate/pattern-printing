#Question 9: Diamond pattern

# Upper half
for i in range(1, 6): #iterate till 5
    for j in range(1, 6-i):    #printing spaces
        print("  ", end="")     #printing spaces to align the diamond pattern to the center
    for k in range(1, 2*i):  #printing stars in the upper half of the diamond pattern
        print("* ", end="")
    print()

# Lower half
for i in range(4, 0, -1):  #iterate  till 4
    for j in range(1, 6-i): #printing spaces
        print("  ", end="") #printing spaces to align the diamond pattern to the center
    for k in range(1, 2*i):  #printing stars in the lower half of the diamond patterngit 
        print("* ", end="")
    print()