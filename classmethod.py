class Kalkulator:
	def f(self):
		return 'hello world'

	@staticmethod
	def tambah_angka(angka1, angka2):
		return '{}+{}={}'.format(angka1,angka2,angka1+angka2)

class Kalkulator2:
	def f(self):
		return 'hello world'

	@classmethod
	def kali_angka(cls, angk1, angk2):
		return '{}x{}={}'.format(angk1,angk2,angk1*angk2)

print(Kalkulator.tambah_angka(89,2))
print(Kalkulator2.kali_angka(89,2))