'''
Variable adalah tempat menyimpan data,
Tipe data adalah jenis data yang tersimpan dalam variable,
Variable bersifat mutable, artinya nilai bisa berubah-ubah
'''
''' Aturan Penulisan
- Nama variabel harus dimulai dengan huruf atau karakter garis bawah
    ex : _nama, nama_variable
- Nama variabel tidak dapat dimulai dengan angka
- Nama variabel hanya dapat berisi karakter alfanumerik dan garis bawah (Az, 0-9, dan _)
    ex : nama2, __nilai, b2
- karakter bersifat case sensitif 
    ex : nama dan Nama adalah variable yang berbeda
- tidak boleh mengandung kata kunci, yang sudah digunakan python
    ex : if, while, for, etc
'''
# Contoh penulisan variable
variable_ku = "ini isi variable"
variable2 = 10

print (variable2)
print (variable_ku)
print ('--------------')

# Menulis beberapa variable dalam satu baris
a, b, c = "Usmoyo", 'harif', "Munandar"
print(a)
print(b)
print(c)

# Atau nilai yang sama di variable yang berbeda
d = e = f = "Usmoyo Harif Munandar"

# Menggabungkan teks dan variable, dengan +
a = 'Usmoyo'
print("nama saya " + a)

# Menggabungkan variable
b = 'Usmoyo'
c = "harif"
print(b + c)

# VARIABLE GLOBAL
'''
- Variabel yang dibuat di luar fungsi
  (seperti dalam semua contoh di atas) dikenal sebagai variabel global
- Variabel global dapat digunakan oleh semua orang, baik di dalam fungsi maupun di luar
'''
# Buat variabel di luar fungsi, dan gunakan di dalam fungsi
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

"""
Jika Anda membuat variabel dengan nama yang sama di dalam suatu fungsi, 
variabel ini akan menjadi lokal, dan hanya dapat digunakan di dalam fungsi. 
Variabel global dengan nama yang sama akan tetap seperti itu, global dan dengan nilai asli.
"""
# Buat variabel di dalam suatu fungsi, dengan nama yang sama dengan variabel global
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Jika Anda menggunakan globalkata kunci, variabel milik lingkup global:
def myfunc():  
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)