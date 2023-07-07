# Print a table of size n×n filled with numbers from 1 to n^2 in 
# a spiral pattern, starting from the top left corner and spiraling 
# in a clockwise direction.

# Explanation: You are given a positive integer n. 
# Your task is to generate a square table with n rows and n columns. 
# The table should be filled with numbers from 1 to n^2 in a spiral pattern, 
# starting from the top left corner and proceeding in a clockwise direction.


number = int(input())
a = [[0 for j in range(number)] for i in range(number)]

step = 0 
num = 0 
for i in range( len(a)):
    for j in range(step, len(a) - step):
        
        while a[i][j] == 0:
            a[i][j] = num
            num += 1
            if j == len(a) - 1 - step:
                for x in range(step + 1, len(a) - step):
                    a[x][j] = num  
                    num += 1
                    if x == len(a) - 1 - step: 
                        for y in range(len(a) - 2 - step, -1 + step, -1):
                            a[x][y] = num 
                            num += 1 
                            if y == step:
                                for z in range(len(a) - 2 - step  , 0 + step, -1):
                                    a[z][y] = num 
                                    num += 1
                                step+= 1
                              
for row in a:
    print(*row)