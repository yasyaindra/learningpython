class Kalkulator:
	def __init__(self, nilai=0):
		self.nilai = nilai
	
	def tambah_angka(self, angka1, angka2):
		self.nilai = angka1 + angka2
		if self.nilai > 9:
			print('angka {} melebihi angka maksimum'.format(self.nilai))
		return self.nilai

class KalkulatorKali(Kalkulator):
	def kali_angka(self, angka1, angka2):
		self.nilai = angka1*angka2
		return self.nilai

kk = KalkulatorKali()

print(kk.tambah_angka(32,2))
print(kk.kali_angka(3,2))