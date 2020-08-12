'''SET
Satu set adalah koleksi yang tidak terurut dan tidak terindeks. 
Dalam set Python ditulis dengan kurung keriting.
'''

#Buat Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Catatan:  
#Set tidak berurutan,sehingga Anda tidak dapat memastikan urutan item yang akan muncul.

'''Akses Item
Anda tidak dapat mengakses item dalam set dengan merujuk pada indeks,
 karena set tidak terurut item tidak memiliki indeks.

Tapi Anda bisa mengulang item yang diatur menggunakan for loop, 
 atau bertanya apakah nilai yang ditentukan hadir dalam set, 
 dengan menggunakan in kata kunci.
'''

#Ulangi set, dan cetak nilainya:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Periksa apakah "pisang" ada di set:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

'''Ubah Item
Setelah set dibuat, Anda tidak dapat mengubah itemnya, 
 tetapi Anda dapat menambahkan item baru.

Untuk menambahkan satu item ke set, gunakan add() metode ini.
Untuk menambahkan lebih dari satu item ke set, gunakan update() metode ini.
'''

#Tambahkan item ke set, menggunakan add() metode ini:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Tambahkan beberapa item ke set, menggunakan update() metode ini:
thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

#Dapatkan jumlah item dalam satu set:
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Untuk menghapus item dalam set, gunakan remove(), atau discard()metode.
#Hapus "pisang" dengan menggunakan remove() metode:
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#Hapus "pisang" dengan menggunakan discard() metode:
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

'''
Anda juga dapat menggunakan pop()metode, untuk menghapus item, 
tetapi metode ini akan menghapus item terakhir . 
Ingat bahwa set tidak berurutan, sehingga Anda tidak akan tahu item apa yang akan dihapus.

Nilai pengembalian pop()metode ini adalah item yang dihapus.
'''

#Hapus item terakhir dengan menggunakan pop() metode ini:
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#The clear() Metode mengosongkan set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#Kata delkunci akan menghapus set sepenuhnya:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

'''Menggabungkan SET
Ada beberapa cara untuk bergabung dengan dua set atau lebih dalam Python.

Anda dapat menggunakan union()metode yang mengembalikan set baru yang berisi 
semua item dari kedua set, atau update()metode yang memasukkan semua item 
dari satu set ke yang lain:
'''
#The union()method mengembalikan satu set baru dengan semua item dari kedua set:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#The update()Metode memasukkan item dalam set2 ke set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

'''
Ada metode lain yang menggabungkan dua set dan membuat HANYA duplikat, 
atau TIDAK PERNAH duplikat, periksa daftar lengkap metode set di bagian bawah 
halaman ini.
'''
#Menggunakan konstruktor set () untuk membuat set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)