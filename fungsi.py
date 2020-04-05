hello = 'hello dunia!'
def tampilkan_halo(hello):
	print(hello)
	return
tampilkan_halo(hello)

def sum(a,b):
	total = a+b
	return total
total = sum(78,2)
print('hasilnya adalah ', format(total))

def kuadrat(x):
	return x*x

x = 2
k = kuadrat(x)
print('hasil kuadrat dari {} adalah {}'.format(x,k))

def changename(mylist):
	mylist = [1,2,3,4,5]
	print('Nilai di dalam fungsi {}'.format(mylist))

mylist = [10,20,30]
changename(mylist)
print('Nilai di luar fungsi {}'.format(mylist))

def printinfo(name, age):
	print('Name : ',name)
	print('Age : ',age)

printinfo(name='Indra',age=19)