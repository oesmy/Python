'''Iterator
Iterator adalah objek yang berisi jumlah nilai yang dapat dihitung.
Iterator adalah objek yang dapat diulangi, artinya Anda dapat melintasi semua nilai.

Secara teknis, dalam Python, sebuah iterator adalah objek yang mengimplementasikan 
protokol iterator, yang terdiri dari metode __iter__() dan __next__().
'''
'''Iterator vs Iterable
Daftar, tupel, kamus, dan set adalah semua objek yang dapat diubah. 
Ini adalah wadah yang dapat Anda gunakan untuk mendapatkan iterator.

Semua objek ini memiliki iter()metode yang digunakan untuk mendapatkan iterator:
'''
#Kembalikan iterator dari tuple, dan cetak setiap nilai:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

'''Bahkan string adalah objek yang dapat diubah, dan dapat mengembalikan iterator:'''

#String juga merupakan objek yang dapat diubah, yang berisi urutan karakter:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

'''Looping Melalui Iterator
Kita juga bisa menggunakan forloop untuk beralih melalui objek yang dapat diulang:'''
#Iterasi nilai-nilai tuple:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#Iterasi karakter string:
mystr = "banana"

for x in mystr:
  print(x)

'''The forLoop benar-benar menciptakan sebuah objek iterator dan mengeksekusi ()
 metode berikutnya untuk setiap loop.'''

'''Buat Iterator
Untuk membuat objek / kelas sebagai iterator Anda harus mengimplementasikan 
metode __iter__()dan __next__()objek Anda.

Seperti yang telah Anda pelajari di bab Python Classes / Objects , 
semua kelas memiliki fungsi yang disebut __init__(), 
yang memungkinkan Anda untuk melakukan inisialisasi ketika objek sedang dibuat.

The __iter__()Metode bertindak serupa, Anda dapat melakukan operasi 
(menginisialisasi dll), tetapi harus selalu kembali objek iterator sendiri.

The __next__()Metode ini juga memungkinkan Anda untuk melakukan operasi, 
dan harus kembali item berikutnya dalam urutan.'''

'''Contoh
Buat iterator yang mengembalikan angka, dimulai dengan 1, 
dan setiap urutan akan bertambah satu (mengembalikan 1,2,3,4,5 dll.):'''
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

'''StopIteration
Contoh di atas akan berlanjut selamanya jika Anda memiliki cukup banyak pernyataan()
berikutnya, atau jika itu digunakan dalam satu forlingkaran.

Untuk mencegah iterasi berjalan selamanya, kita bisa menggunakan StopIteration
pernyataan itu.

Dalam __next__()metode ini, kita dapat menambahkan kondisi terminating 
untuk meningkatkan kesalahan jika iterasi dilakukan beberapa kali:'''
#Contoh: Hentikan setelah 20 iterasi
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

  