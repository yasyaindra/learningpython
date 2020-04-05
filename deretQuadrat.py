#Cara1
numbers = [1,2,3,4,5]
squares = []
for n  in numbers:
	squares.append(n**2)
print(squares)

#Cara2
numbers = [1,2,3,4,5]
squares = [n**2 for n in numbers]
print(squares)