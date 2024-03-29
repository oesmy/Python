'''
Python adalah bahasa pemrograman berorientasi objek.
Hampir semua yang ada di Python adalah objek, dengan properti dan metodenya.
Kelas seperti konstruktor objek, atau "cetak biru" untuk membuat objek.
'''

'''Buat Kelas
Untuk membuat kelas, gunakan kata kunci class:
'''
#Buat kelas bernama MyClass, dengan properti bernama x:
class MyClass:
  x = 5

'''Buat Obyek
Sekarang kita bisa menggunakan kelas bernama MyClass untuk membuat objek:
'''
#Buat objek bernama p1, dan cetak nilai x:
p1 = MyClass()
print(p1.x)

'''Fungsi __init __ ()
Contoh di atas adalah kelas dan objek dalam bentuknya yang paling sederhana, 
dan tidak terlalu berguna dalam aplikasi kehidupan nyata.

Untuk memahami makna kelas, kita harus memahami fungsi __init __ () bawaan.

Semua kelas memiliki fungsi yang disebut __init __ (), 
yang selalu dieksekusi ketika kelas sedang dimulai.

Gunakan fungsi __init __ () untuk menetapkan nilai ke properti objek, 
atau operasi lain yang perlu dilakukan ketika objek sedang dibuat:
'''
#Buat kelas bernama Person, gunakan fungsi __init __ () untuk menetapkan nilai untuk nama dan usia:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

'''Catatan
__init__()fungsi disebut secara otomatis setiap kali kelas sedang digunakan untuk 
membuat objek baru.'''

'''Metode Objek
Objek juga bisa berisi metode. Metode dalam objek adalah fungsi yang dimiliki objek.
Mari kita membuat metode di kelas Person:
'''
#Masukkan fungsi yang mencetak ucapan, dan jalankan pada objek p1:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

'''Catatan
The selfparameter adalah referensi ke contoh saat ini kelas, 
dan digunakan untuk variabel akses dalam kelas.'''

'''Parameter diri
The selfparameter adalah referensi ke contoh saat ini kelas, 
dan digunakan untuk variabel akses yang dimiliki kelas.

Itu tidak harus dinamai self, Anda bisa menyebutnya apa pun yang Anda suka, 
tetapi itu harus menjadi parameter pertama dari setiap fungsi di kelas:
'''
#Gunakan kata-kata mysillyobject dan abc sebagai ganti self :
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

'''Ubah Properti Objek
Anda dapat memodifikasi properti pada objek seperti ini:'''
#Atur usia p1 hingga 40:
p1.age = 40

'''Hapus Properties Object
Anda dapat menghapus properti pada objek dengan menggunakan delkata kunci:'''
#Hapus properti umur dari objek p1:
del p1.age
'''Hapus Objek
Anda dapat menghapus objek dengan menggunakan delkata kunci:'''
#Hapus objek p1:
del p1

'''
class definisi tidak boleh kosong, tetapi jika Anda karena suatu alasan 
memiliki classdefinisi tanpa konten, masukkan PASS pernyataan 
untuk menghindari kesalahan.
'''
#Contoh
class Person:
  pass