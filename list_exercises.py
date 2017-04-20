numbers = [-1, 0, 1, 2, 3, 4, 5]

#Sum of Numbers
total = sum(numbers)
print total

#Largest Number
largest = max(numbers)
print largest

#Smallest Number
smallest = min(numbers)
print smallest

#Even Numbers
for i in numbers:
	if (i % 2 == 0):
		print i

#Positive Numbers
for j in numbers:
	if (j > 0):
		print j

#Positive Numbers II
pos_num_only = []
for k in numbers:
	if (k > 0):
		pos_num_only.append(k)
print pos_num_only

#Multiply a List
new_list = []
for m in numbers:
	new_list.append(m * 5)
print new_list

#Matrix Addition
matrix1 = [[1, 2],
	[3, 4]]
matrix2 = [[1, 1],
	[1, 1]]
combo_matrix = [[0, 0],
	[0, 0]]
for x in range(len(matrix1)):
	for y in range(len(matrix2)):
		combo_matrix[x][y] = matrix1[x][y] + matrix2[x][y]
print combo_matrix

#Matrix Addition II

#De-dup
letters = ["a", "b", "c", "b", "d"]
letters_no_duplicates = []
for t in letters:
	if t not in letters_no_duplicates:
		letters_no_duplicates.append(t)
print letters_no_duplicates

#Matrix Multiplication
matrix1 = [[1, 2],
	[3, 4]]
matrix2 = [[1, 1],
	[1, 1]]
combo_matrix = [[0, 0],
	[0, 0]]
for x in range(len(matrix1)):
	for y in range(len(matrix2)):
		combo_matrix[x][y] = matrix1[x][y] * matrix2[x][y]
print combo_matrix
