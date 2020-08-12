'''
Tuple adalah jenis data lain yang mirip list,
perbedaannya indeks tidak bisa diubah (immutable),
List bersifat mutable, sedangkan tuple bersifat immutable.
Sekali tuple dibuat, maka isinya tidak bisa dimodifikasi lagi.

Tuple di deklarasikan dengan tanda ()
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Access tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative Index
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Rentang Index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Rentang Index Negative
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

'''Ubah Nilai Tuple
Setelah tuple dibuat, Anda tidak dapat mengubah nilainya. Tuples tidak dapat diubah,
atau tidak dapat diubah sebagaimana disebut juga.

Tapi ada solusinya. Anda dapat mengubah tuple menjadi daftar, mengubah daftar,
dan mengubah daftar kembali menjadi tuple.
'''
#Ubah tuple menjadi daftar untuk dapat mengubahnya:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Anda dapat mengulang item tuple dengan menggunakan forloop.
#Iterasi item-itemnya dan cetak nilainya:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Untuk menentukan apakah ada item tertentu dalam tupel, gunakan inkata kunci:
#Periksa apakah "apel" ada di tuple:
thistuple = ("apple", "banana", "cherry") 
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Cetak jumlah item dalam tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Setelah tuple dibuat, Anda tidak dapat menambahkan item ke dalamnya. Tuple tidak bisa diubah .
#Anda tidak dapat menambahkan item ke tuple:
thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)

#Buat Tuple Dengan Satu Item, Untuk membuat tuple dengan hanya satu item,
#Anda harus menambahkan koma setelah item, jika tidak, Python tidak akan mengenalinya sebagai tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuples tidak dapat diubah , sehingga Anda tidak dapat menghapus item dari itu,tetapi Anda dapat menghapus tuple sepenuhnya:
#Kata delkunci dapat menghapus tuple sepenuhnya:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Bergabunglah dengan dua tuple:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Dimungkinkan juga untuk menggunakan konstruktor tuple () untuk membuat tuple.
#Menggunakan metode tuple () untuk membuat tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

'''Metode Tuple
Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''