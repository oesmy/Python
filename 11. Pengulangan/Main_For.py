'''For Loop
Dengan for loop kita dapat mengeksekusi seperangkat pernyataan, 
satu kali untuk setiap item dalam daftar, tuple, set dll.
'''

#Cetak setiap buah dalam daftar buah:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

'''
The for loop tidak memerlukan variabel pengindeksan untuk mengatur terlebih dahulu.
Bahkan string adalah objek yang dapat diubah, mereka mengandung serangkaian karakter:
'''
#Lingkarilah huruf-huruf dalam kata "pisang":
for x in "banana":
  print(x)

#Keluar dari loop kapan x"pisang":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Keluar dari loop ketika x"pisang", tetapi kali ini istirahat datang sebelum cetak:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

'''
pernyataan continue, kita dapat menghentikan iterasi loop saat ini, 
dan melanjutkan dengan yang berikutnya:
'''
#Jangan cetak pisang:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

'''Fungsi Range()
Untuk mengulang satu set kode beberapa kali, kita dapat menggunakan fungsi range (),
Fungsi range () mengembalikan urutan angka, mulai dari 0 secara default, 
dan bertambah dengan 1 (secara default), dan berakhir pada angka yang ditentukan.
'''
#Menggunakan fungsi rentang ():
for x in range(6):
  print(x)
#Perhatikan bahwa rentang (6) bukan nilai 0 hingga 6, tetapi nilai 0 hingga 5.

'''
Fungsi rentang () default ke 0 sebagai nilai awal, namun dimungkinkan untuk 
menentukan nilai awal dengan menambahkan parameter: rentang (2, 6) , 
yang berarti nilai dari 2 hingga 6 (tetapi tidak termasuk 6):
'''
#Menggunakan parameter awal:
for x in range(2, 6):
      print(x)
    
'''
Fungsi rentang () secara default untuk menambah urutan dengan 1, 
namun dimungkinkan untuk menentukan nilai kenaikan dengan menambahkan parameter ketiga: 
rentang (2, 30, 3 ) :
'''
#Tambahkan urutan dengan 3 (standarnya adalah 1):
for x in range(2, 30, 3):
  print(x)

'''
Kata elsekunci dalam forloop menentukan blok kode yang akan dieksekusi ketika loop selesai:
'''
#Cetak semua angka dari 0 hingga 5, dan cetak pesan saat loop telah berakhir:
for x in range(6):
      print(x)
else:
  print("Finally finished!")

'''
Loop bersarang
Loop bersarang adalah loop di dalam loop.

"Loop dalam" akan dieksekusi satu kali untuk setiap iterasi "loop luar":
'''
#Cetak setiap kata sifat untuk setiap buah:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

'''
forloop tidak boleh kosong, tetapi jika Anda karena alasan tertentu memiliki 
forloop tanpa konten, masukkan passpernyataan untuk menghindari kesalahan.
'''
#Contoh
for x in [0, 1, 2]:
  pass