d = {'ratarata': '10.0'}
try:
    print('rata rata : {}'.format(d['rata_rata']))
except KeyError:
    print('kunci tidak ditemukan')
except ValueError:
    print('value tidak sesuai')
try:
    print('rata rata : {}'.format(d['ratarata']/3))
except KeyError:
    print('kunci tidak ditemukan')
except (ValueError, TypeError):
    print('value tidak sesuai')

d = {'ratarata': '10.0'}
if 'total' not in d:
	raise KeyError('harus memiliki total')
