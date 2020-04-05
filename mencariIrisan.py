list_a = [1,2,3,4,5]
list_b = [3,4,5,6]
hasil_irisan = []
for a in list_a:
	for b in list_b:
		if a == b:
			hasil_irisan.append(a)
print(hasil_irisan)