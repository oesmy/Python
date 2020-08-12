"""
List adalah tipe data yang berisi item yang berurutan.
Seperti type data string, tiap item (anggota) list memiliki
indeks sesuai urutannya, indeks mulai dari 0 bukan 1.

namalist[indeks]
"""

thislist = ["apple", "banana", "cherry"]

print(thislist)

print(thislist[1])

print(thislist[-1])

#slicing pengaksesan terhadap sejumlah item dari indeks ke indeks.

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist2[2:5])

print(thislist2[:4])

print(thislist[2:])

print(thislist[-4:-1])

#Merubah indeks (muttable)
thislist[1] = "blackcurrant"
print(thislist)

#Mengulang daftar dengan for
for x in thislist:
      print(x)

#Periksa isi daftar
if "apple" in thislist:
      print("Yes, 'apple' is in the fruits list")

#Periksa panjang list
print(len(thislist))

#Tambahkan item dengan append()
thislist.append("orange")
print(thislist)

#Untuk menambahkan item pada indeks yang ditentukan, gunakan metode insert () :
thislist.insert(1, "orange")
print(thislist)

#Hapus indeks dengan remove()
thislist.remove("banana")
print(thislist)

#The pop()Metode menghilangkan indeks tertentu, 
# (atau item terakhir jika indeks tidak ditentukan):
thislist.pop()
print(thislist)

#Kata delkunci menghapus indeks yang ditentukan:
del thislist[0]
print(thislist)

#Kata delkunci juga dapat menghapus daftar sepenuhnya:
del thislist

#The clear()Metode mengosongkan daftar:
thislist.clear()
print(thislist)

#Buat salinan daftar dengan copy()metode:
mylist = thislist.copy()
print(mylist)

#Cara lain untuk membuat salinan adalah dengan menggunakan metode bawaan list().
mylist = list(thislist)
print(mylist)

#Bergabung dengan dua daftar:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Tambahkan list2 ke list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Gunakan extend()metode untuk menambahkan list2 di akhir list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Menggunakan list()konstruktor untuk membuat Daftar:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)