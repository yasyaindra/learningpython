def printinfo(fixedarg, *args):
	print('Output: fixedarg {}'.format(fixedarg))
	for a in args:
		print('argumen posisi {}'.format(a))

printinfo(10)
printinfo(70,60,50,30,20,10)

def printing(*args, **kwargs):
	for a in args:
		print('Argumen ke {}'.format(a))
	for key, value in kwargs.items():
		print('argument kata kunci {}:{}'.format(key,value))

printing(1,2,3)
printing(j=3,k=4,l=9)
printing(3,2,12,o=9,p=7,u=2)
printing(*(4,5),**{'k':9,'s':6,'w':0})
print('+++++++++++++++++++++++++++++++++++')
sum =  lambda a, b : a+b;
print('Nilai dari sum adalah ',sum(4,6) )
print('')
print('')
total = 0
def sum(arg1, arg2):
	total = arg1 + arg2
	print('hasil dalam fungsi adalah {}'.format(total))

sum(10,8)
print('total di luar fungsi {}'.format(total))
