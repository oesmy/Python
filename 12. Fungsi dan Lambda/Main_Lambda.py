'''Lambda
Fungsi lambda adalah fungsi anonim kecil.
Fungsi lambda dapat mengambil sejumlah argumen,
tetapi hanya dapat memiliki satu ekspresi.
'''
'''lambda arguments : expression
Ekspresi dieksekusi dan hasilnya dikembalikan:
'''

'''
Fungsi lambda yang menambahkan 10 ke angka yang diteruskan sebagai argumen, 
dan mencetak hasilnya:
'''
#Contoh
x = lambda a : a + 10
print(x(5))

#Fungsi Lambda dapat mengambil sejumlah argumen:
#Fungsi lambda yang mengalikan argumen a dengan argumen b dan mencetak hasilnya:
x = lambda a, b : a * b
print(x(5, 6))

#Fungsi lambda yang merangkum argumen a, b, dan c dan mencetak hasilnya:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

'''Mengapa Menggunakan Fungsi Lambda?
Kekuatan lambda lebih baik ditampilkan ketika Anda 
menggunakannya sebagai fungsi anonim di dalam fungsi lain.

Katakanlah Anda memiliki definisi fungsi yang mengambil satu argumen, 
dan argumen itu akan dikalikan dengan angka yang tidak dikenal:
'''
def myfunc(n):
  return lambda a : a * n

#Gunakan definisi fungsi itu untuk membuat fungsi yang selalu menggandakan nomor yang Anda kirim:
def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#gunakan definisi fungsi yang sama untuk membuat fungsi yang selalu tiga kali lipat dari jumlah yang Anda kirim:
def myfunc(n):
      return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

#gunakan definisi fungsi yang sama untuk membuat kedua fungsi, dalam program yang sama:
def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

'''Gunakan fungsi lambda ketika fungsi anonim diperlukan untuk waktu yang singkat.'''
 