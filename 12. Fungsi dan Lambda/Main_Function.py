'''Funtion
Fungsi adalah blok kode yang hanya berjalan ketika dipanggil.
Anda dapat mengirimkan data, yang dikenal sebagai parameter, ke suatu fungsi.
Suatu fungsi dapat mengembalikan data sebagai hasilnya.
'''
#Dalam Python fungsi didefinisikan menggunakan kata kunci def :
def my_function():
      print("Hello from a function")

'''
Untuk memanggil suatu fungsi, gunakan nama fungsi yang diikuti oleh tanda kurung:
'''
#Contoh
def my_function():
      print("Hello from a function")

my_function()

'''Arguments
Informasi dapat diteruskan ke fungsi sebagai argumen.
Argumen ditentukan setelah nama fungsi, di dalam tanda kurung. 
Anda dapat menambahkan argumen sebanyak yang Anda inginkan,
cukup pisahkan dengan koma.

Contoh berikut memiliki fungsi dengan satu argumen (fname). 
Ketika fungsi dipanggil, kami memberikan nama depan, 
yang digunakan di dalam fungsi untuk mencetak nama lengkap:
'''
#Contoh
def my_function(fname):
      print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

'''Argumen sering disingkat menjadi ARGS dalam dokumentasi Python.'''

'''Parameter atau Argumen?
Parameter istilah dan argumen dapat digunakan untuk hal yang sama: 
informasi yang diteruskan ke fungsi.Parameter istilah dan argumen
dapat digunakan untuk hal yang sama: informasi yang diteruskan ke fungsi.
'''
'''Dari perspektif fungsi:
Parameter adalah variabel yang tercantum di dalam tanda kurung dalam definisi fungsi.
Argumen adalah nilai yang dikirim ke fungsi saat dipanggil.
'''

'''Jumlah Argument
Secara default, suatu fungsi harus dipanggil dengan jumlah argumen yang benar. Berarti bahwa jika fungsi Anda mengharapkan 2 argumen, Anda harus memanggil fungsi dengan 2 argumen, tidak lebih, dan tidak kurang.
'''
#Fungsi ini mengharapkan 2 argumen, dan mendapat 2 argumen:
def my_function(fname, lname):
      print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Jika Anda mencoba memanggil fungsi dengan 1 atau 3 argumen, 
#Anda akan mendapatkan kesalahan:
def my_function(fname, lname):
      print(fname + " " + lname)

my_function("Emil")

'''
Jika Anda tidak tahu berapa banyak argumen yang akan diteruskan ke fungsi Anda, 
tambahkan *sebelum nama parameter dalam definisi fungsi.
Dengan cara ini fungsi akan menerima tuple argumen, dan dapat mengakses item sesuai:
'''
#Jika jumlah argumen tidak diketahui, tambahkan *sebelum nama parameter:
def my_function(*kids):
      print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

'''Argumen sewenang-wenang sering disingkat menjadi * args dalam dokumentasi Python.'''

'''Keyword Arguments
Anda juga dapat mengirim argumen dengan sintaks kunci = nilai .
Dengan cara ini urutan argumen tidak menjadi masalah.
'''
#Contoh
def my_function(child3, child2, child1):
      print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

'''Frasa Keyword Argumen sering disingkat menjadi kwargs dalam dokumentasi Python.'''

'''
Jika Anda tidak tahu berapa banyak argumen kata kunci yang akan diteruskan 
ke fungsi Anda, tambahkan dua tanda bintang: **sebelum nama parameter 
dalam definisi fungsi.
Dengan cara ini fungsi akan menerima kamus argumen, dan dapat mengakses item-item
yang sesuai:
'''
#Jika jumlah argumen kata kunci tidak diketahui, tambahkan ganda **sebelum nama parameter:
def my_function(**kid):
      print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

'''Argumen Kword Sewenang-wenang sering disingkat menjadi ** kwargs dalam dokumentasi Python.'''

'''
Contoh berikut menunjukkan cara menggunakan nilai parameter default.
Jika kita memanggil fungsi tanpa argumen, itu menggunakan nilai default:
'''
#Contoh
def my_function(country = "Norway"):
      print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

'''Passing a List as an Argument
Anda dapat mengirim tipe data argumen apa pun ke suatu fungsi
(string, angka, daftar, kamus, dll.), Dan itu akan diperlakukan 
sebagai tipe data yang sama di dalam fungsi.

Misalnya, jika Anda mengirim Daftar sebagai argumen, 
itu masih akan menjadi Daftar ketika mencapai fungsi:
'''
#Contoh
def my_function(food):
    for x in food:
print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

'''Return Value
Untuk membiarkan suatu fungsi mengembalikan nilai, gunakan return pernyataan:
'''
#Nilai pengembalian
def my_function(x):
      return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

'''
functiondefinisi tidak boleh kosong, tetapi jika Anda karena suatu alasan 
memiliki function definisi tanpa konten, masukkan PASS pernyataan untuk 
menghindari kesalahan.
'''
#Contoh
def myfunction():
  pass

