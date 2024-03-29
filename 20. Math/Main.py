'''Python memiliki seperangkat fungsi matematika bawaan,
termasuk modul matematika yang luas, yang memungkinkan Anda untuk melakukan tugas
matematika pada angka.'''

'''Fungsi Matematika bawaan
Fungsi min()dan max()dapat digunakan untuk menemukan nilai terendah 
atau tertinggi dalam iterable:'''
#Contoh
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

'''abs()mengembalikan fungsi (positif) nilai absolut dari jumlah yang ditentukan:'''
#Contoh
x = abs(-7.25)

print(x)

'''The fungsi mengembalikan nilai x dengan kekuatan y (x y ).pow(x, y)'''
#Kembalikan nilai 4 ke kekuatan 3 (sama dengan 4 * 4 * 4):
x = pow(4, 3)

print(x)

'''Modul Matematika
Python juga memiliki modul built-in yang disebut math, 
yang memperpanjang daftar fungsi matematika.

Untuk menggunakannya, Anda harus mengimpor mathmodul:'''

import math

'''Ketika Anda telah mengimpor mathmodul, Anda dapat mulai menggunakan 
metode dan konstanta dari modul.

The math.sqrt()Metode misalnya, mengembalikan akar kuadrat dari angka:'''
import math
x = math.sqrt(64)
print(x)

'''The math.ceil()Metode putaran sejumlah atas untuk bilangan bulat terdekat, 
dan math.floor() metode putaran sejumlah bawah ke integer terdekat, 
dan kembali hasilnya:'''
#Contoh
import math

x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1

'''The math.pikonstan, mengembalikan nilai PI (3.14 ...):'''

#Contoh
import math

x = math.pi
print(x)

