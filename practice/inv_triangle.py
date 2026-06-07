 #Inverted Right-Angled Triangle in Python
rows=int(input("enter the number of rows"))
for i in range(rows,0,-1): #outer loop with rev
	for j in range(1,i+1): #inner loop for colums
		print("*",end=" ")	
	print()	
