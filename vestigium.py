# rows
# loop through values and increment by one if any duplicates
# row1: [x,y,z] - list, dictionary not necessary

# columns
# iterate over all rows at position [x]
# column1: [row1[0], row2[0]] - get value at same time as row values

# trace
# iterate over the rows at position [x] and incrementing each time

# each is a 1-dim array
# 2-d array will be constant because of the indices
matrix = [[1,2,3,4],[2,1,4,3]]
# row2 column one is at 
matrix[1][0]

row1 = [1,2,3,4]
row2 = [2,1,4,3]
row3=  [3,4,1,2]
row4=  [4,3,2,1]

# input of 4 test case
# matrix = [[],[],[],[]]
matrix = []
row_duplicates = 0


for row in matrix:
    # checks here b/c purpose is to check duplicates in the row
    checks = []
    # column check
    
    # row check
    for i in row:
        checks.append(row[i]) 
        if row[i] in checks:
            row_duplicates += 1
            # rows with duplicates, not duplicates per row
            break

print(f'Case #{x}: {k} {r} {c}')




