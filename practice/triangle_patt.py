#right angled triangle pattern in python
rows= int(input("enter the row size for pattern"))
for i in range (1,rows+1): #outer loop for rows
	for j in range(1,i+1): #inner loop for colums
		print("*",end=" ") #print *
	print()