'''Format string ()
The format()Metode memungkinkan Anda untuk format yang dipilih bagian dari string.

Terkadang ada bagian teks yang tidak Anda kendalikan, mungkin berasal dari basis data, 
atau input pengguna?

Untuk mengontrol nilai-nilai tersebut, tambahkan placeholder (kurung keriting {})
dalam teks, dan jalankan nilai melalui format()metode:'''

#Tambahkan placeholder tempat Anda ingin menampilkan harga:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

'''Anda dapat menambahkan parameter di dalam 
kurung keriting untuk menentukan cara mengkonversi nilai:'''
#Format harga yang akan ditampilkan sebagai angka dengan dua desimal:
txt = "The price is {:.2f} dollars"

'''Berbagai Nilai
Jika Anda ingin menggunakan lebih banyak nilai, 
tambahkan saja nilai lebih ke metode format ():'''
print(txt.format(price, itemno, count))

#Dan tambahkan lebih banyak penampung:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

'''Angka indeks
Anda dapat menggunakan nomor indeks (angka di dalam kurung keriting {0})
untuk memastikan nilai ditempatkan di placeholder yang benar:'''
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#Juga, jika Anda ingin merujuk ke nilai yang sama lebih dari sekali, gunakan nomor indeks:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

'''Indeks Bernama
Anda juga dapat menggunakan indeks bernama dengan memasukkan nama 
di dalam kurung keriting {carname}, tetapi kemudian Anda harus menggunakan 
nama saat Anda melewati nilai parameter txt.format(carname = "Ford"):'''
#Contoh
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))