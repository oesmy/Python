'''
Bilangan Python
Ada tiga jenis numerik dalam Python:
- int
- float
- complex
'''

#Variabel tipe numerik dibuat saat Anda menetapkan nilai padanya:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#Untuk memverifikasi jenis objek apa pun di Python, gunakan type()fungsi:
print(type(x))
print(type(y))
print(type(z))

# Int, adalah bilangan bulat, positif atau negatif, tanpa desimal
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float, adalah angka, positif atau negatif, yang mengandung satu atau lebih desimal.
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
#Float juga bisa berupa angka ilmiah dengan "e" untuk menunjukkan kekuatan 10.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Kompleks, ditulis dengan "j" sebagai bagian imajiner:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Konversi tipe data (casting), Konversi dari satu jenis ke yang lain:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#Anda tidak dapat mengubah bilangan kompleks menjadi tipe angka lain.

'''Angka acak, 
Python tidak memiliki random()fungsi untuk membuat angka acak,
tetapi Python memiliki modul bawaan randomyang dapat digunakan untuk membuat angka acak:
'''
#Impor modul acak, dan tampilkan angka acak antara 1 dan 9:
import random

print(random.randrange(1, 10))