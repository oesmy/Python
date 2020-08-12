'''Try Except
The tryblok memungkinkan Anda menguji blok kode kesalahan.
The exceptblok memungkinkan Anda menangani kesalahan.
The finallyblok memungkinkan Anda mengeksekusi kode, 
terlepas dari hasil coba-dan kecuali blok.'''

'''Penanganan Exception
Ketika kesalahan terjadi, atau pengecualian seperti yang kita sebut, 
Python biasanya akan berhenti dan menghasilkan pesan kesalahan.

Pengecualian ini dapat ditangani dengan menggunakan trypernyataan:'''

#The tryblock akan menghasilkan pengecualian, karena xtidak didefinisikan:
try:
  print(x)
except:
  print("An exception occurred")

'''Karena blok coba memunculkan kesalahan, blok kecuali akan dieksekusi.
Tanpa blok try, program akan macet dan menimbulkan kesalahan:'''

'''Banyak Pengecualian
Anda dapat mendefinisikan sebanyak mungkin blok pengecualian, 
misalnya jika Anda ingin menjalankan blok kode khusus untuk jenis kesalahan khusus:'''

'''Cetak satu pesan jika blok percobaan 
menimbulkan a NameErrordan lainnya untuk kesalahan lainnya:'''
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

'''Else
Anda dapat menggunakan elsekata kunci untuk menentukan blok kode yang akan dieksekusi
jika tidak ada kesalahan yang muncul:'''
#Dalam contoh ini, tryblok tidak menghasilkan kesalahan apa pun:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

'''Finally
AThe finally blok, bila ditentukan, akan dieksekusi terlepas 
jika blok try menimbulkan kesalahan atau tidak.'''
#Contoh
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
#Ini berguna untuk menutup objek dan membersihkan sumber daya:

#Cobalah untuk membuka dan menulis ke file yang tidak dapat ditulisi:
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
#Program dapat melanjutkan, tanpa membiarkan objek file terbuka.

'''Raise an exception
Sebagai pengembang Python, Anda dapat memilih untuk melemparkan pengecualian 
jika suatu kondisi terjadi.

Untuk melempar (atau menaikkan) pengecualian, gunakan raisekata kunci.'''
#Angkat kesalahan dan hentikan program jika x lebih rendah dari 0:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

'''Kata raise kunci digunakan untuk memunculkan pengecualian.

Anda dapat menentukan jenis kesalahan apa yang ingin diangkat, 
dan teks yang akan dicetak kepada pengguna.'''
#Naikkan TypeError jika x bukan bilangan bulat:
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
