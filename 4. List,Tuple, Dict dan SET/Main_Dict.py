'''Dictionary
Kamus adalah kumpulan yang tidak berurutan, dapat diubah, dan diindeks. 
Dalam kamus Python ditulis dengan kurung keriting, 
dan mereka memiliki kunci dan nilai.
'''
#Buat dan cetak kamus:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Anda dapat mengakses item kamus dengan merujuk nama kuncinya, di dalam tanda kurung:
#Dapatkan nilai kunci "model":
x = thisdict["model"]
#Atau
x = thisdict.get("model")

#Ubah "tahun" menjadi 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#Anda dapat mengulang-ulang kamus dengan menggunakan for lingkaran.
#Cetak semua nama kunci dalam kamus, satu per satu:
for x in thisdict:
  print(x)

#Cetak semua nilai dalam kamus, satu per satu:
for x in thisdict:
  print(thisdict[x])

#Anda juga dapat menggunakan values()metode ini untuk mengembalikan nilai kamus:
for x in thisdict.values():
  print(x)

#Ulangi kedua kunci dan nilai , dengan menggunakan items()metode:
for x, y in thisdict.items():
  print(x, y)

#Periksa apakah "model" ada di kamus:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Cetak jumlah item dalam kamus:
print(len(thisdict))

#Menambah Item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#The pop()Metode menghilangkan item dengan nama kunci yang ditentukan:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem()Metode menghilangkan item dimasukkan 
# terakhir (dalam versi sebelum 3.7, item acak dihapus sebagai gantinya):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#Kata delkunci menghapus item dengan nama kunci yang ditentukan:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#The clear()Metode mengosongkan kamus:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Buat salinan kamus dengan copy()metode:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Buat salinan kamus dengan dict() fungsi:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Buat kamus yang berisi tiga kamus (kamus bersarang):
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Buat tiga kamus, lalu buat satu kamus yang akan berisi tiga kamus lainnya:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#menggunakan konstruktor dict () untuk membuat kamus baru:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

