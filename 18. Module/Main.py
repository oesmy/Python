'''Apa itu Modul?
Anggap modul sama dengan pustaka kode.

File yang berisi serangkaian fungsi yang ingin Anda sertakan dalam aplikasi Anda.

Buat Modul
Untuk membuat modul, cukup simpan kode yang Anda inginkan 
dalam file dengan ekstensi file .py:'''
#Simpan kode ini dalam file bernama mymodule.py
def greeting(name):
  print("Hello, " + name)

'''Gunakan Modul
Sekarang kita dapat menggunakan modul yang baru saja kita buat, 
dengan menggunakan importpernyataan:'''
#Impor modul bernama mymodule, dan panggil fungsi ucapan:
import mymodule

mymodule.greeting("Jonathan")

'''Catatan: Saat menggunakan fungsi dari modul, gunakan sintaks:
module_name.function_name .'''

'''Variabel dalam Modul
Modul ini dapat berisi fungsi-fungsi, seperti yang sudah dijelaskan, 
tetapi juga variabel dari semua jenis (array, kamus, objek, dll):'''
#Simpan kode ini dalam file mymodule.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#Impor modul bernama mymodule, dan akses kamus person1:
import mymodule

a = mymodule.person1["age"]
print(a)