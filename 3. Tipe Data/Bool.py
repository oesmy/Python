"""
Nilai Booleans,
Dalam pemrograman Anda sering perlu tahu apakah sebuah ekspresi Trueatau False.

Saat Anda membandingkan dua nilai, ekspresi dievaluasi dan Python mengembalikan jawaban Boolean:
"""
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Cetak pesan berdasarkan apakah kondisinya Trueatau False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

'''
Mengevaluasi Nilai dan Variabel,
The bool()fungsi memungkinkan Anda untuk mengevaluasi nilai apapun,
dan memberikan Trueatau False imbalan,
'''
#Mengevaluasi string dan angka:
print(bool("Hello"))
print(bool(15))

#Evaluasi dua variabel:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

'''
Kebanyakan Nilai Benar,
Hampir semua nilai dievaluasi Truejika memiliki semacam konten.
Setiap string True, kecuali string kosong.

Angka berapa pun True, kecuali 0.
Daftar, tuple, set, dan kamus apa pun True, kecuali yang kosong.
'''
#Berikut ini akan mengembalikan True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

"""
Beberapa Nilai Salah,
Bahkan, tidak ada banyak nilai-nilai yang mengevaluasi ke False,
kecuali nilai kosong, seperti (), [], {}, "", jumlah 0, dan nilai None.
Dan tentu saja nilainya Falsedievaluasi False.
"""
#Berikut ini akan mengembalikan False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
'''
Satu lagi nilai, atau objek dalam hal ini, dievaluasi ke False,
dan itu adalah jika Anda memiliki objek yang dibuat dari kelas
dengan __len__fungsi yang mengembalikan 0atau False:
'''
class myclass():
      def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#Fungsi dapat Mengembalikan Boolean
#Anda dapat membuat fungsi yang mengembalikan Nilai Boolean:
def myFunction() :
      return True

print(myFunction())

#Anda dapat mengeksekusi kode berdasarkan jawaban Boolean dari suatu fungsi:
#Cetak "YA!" jika fungsi mengembalikan True, jika tidak, cetak "TIDAK!":
def myFunction() :
      return True

if myFunction():
  print("YES!")
else:
  print("NO!")
'''
Python juga memiliki banyak fungsi bawaan yang mengembalikan nilai boolean,
seperti isinstance() fungsi, yang dapat digunakan untuk menentukan
apakah suatu objek memiliki tipe data tertentu:
'''
#Periksa apakah suatu objek bilangan bulat atau tidak:
x = 200
print(isinstance(x, int))
