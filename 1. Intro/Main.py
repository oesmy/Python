"""
Python adalah bahasa pemrograman tingkat tinggi berorientasi object,
merupakan bahasa interpreter yang artinya kode python dieksekusi baris perbaris.

Diciptakan oleh Guido Van Rossum
"""

"""
Kata Kunci yang sudah digunakan python dan tidak bisa digunakan,
True,	def,	if,	raise
False,	del,	import,	return
None,	elif,	in,	try
and,	else,	is,	while
as,	except,	lambda,	with
assert,	finally,	nonlocal,	yield
break,	for,	not	
class,	from,	or	
continue,	global,	pass
"""

"""
Aturan Penulisan :
1. Bisa terdiri dari kobinasi huruf (a-z), angka (0-9), dan underscore (_)
ex : namaKaryawan, Bilangan_2, dan Nama_Lengkap
2. Tidak bisa diawali oleh angka
ex : 1Nama, yang bisa adalah Nama1
3. Karakter spesial tidak bisa digunakan
ex : !, @, % , $, dsb
4. Bersifat case sensitif, huruf besar/kecil berpengaruh
ex : nilai dengan Nilai itu berbeda
5. Untuk penulisan variable bisa camelCase atau underscore
ex : namaLengkap atau nama_Lengkap
"""

"""
Statement (Pernyataan) :
Misal, a = 10 
selain itu ada penugasan if, for dsb

Statement Multibaris :
Di python akhir dari statement adalah karakter baris baru (newline),
dapat dibuat lebih dari 1 baris dengan tanda backslash (\).
ex : a = panjang1 + panjang2 \
    panjang3 + \
    panjang4
Statement didalam tanda [],{}, dan () tidak memerlukan tanda \
ex : nama_bulan['januari', 'februari', 'maret',
    'april', 'mei', 'juni']

Baris dan Indentasi :
Python tidak menggunakan tanda {} untuk menandai blok/grup kode.
Tapi menggunakan tanda (spasi), jumlah (spasi) dalam kode blok harus sama.
ex : if nilai <= 5 :
        print("Nilai merah")
        print("Tidak Lulus)
    else :
        print("Nilai Biru")
        print("Lulus")
#Bila dalam blok indentasi tidak sama, maka akan error
"""