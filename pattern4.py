#Question 4: Increasing Number Triangle

n = 5
for i in range(1,n+1):  # iterates through the rows  from 1 to 5
    for j in range(1,i+1): # iterates through the columns of each row
        print(j,end=" ")  # prints the column number
    print()          # prints a new line after each row