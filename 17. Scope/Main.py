'''Scope Python
Variabel hanya tersedia dari dalam wilayah yang dibuatnya.Ini disebut ruang lingkup.'''

'''Lingkup Lokal
Variabel yang dibuat di dalam fungsi milik lingkup lokal dari fungsi itu, 
dan hanya bisa digunakan di dalam fungsi itu.'''

#Variabel yang dibuat di dalam suatu fungsi tersedia di dalam fungsi itu:
def myfunc():
  x = 300
  print(x)

myfunc()

'''Function Inside Function
Seperti dijelaskan dalam contoh di atas, variabel xtidak tersedia di luar fungsi, 
tetapi tersedia untuk fungsi apa pun di dalam fungsi:'''
#Variabel lokal dapat diakses dari fungsi di dalam fungsi:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

'''Lingkup Global
Variabel yang dibuat dalam tubuh utama kode Python adalah variabel global 
dan termasuk dalam lingkup global.

Variabel global tersedia dari dalam lingkup apa pun, global dan lokal.'''

#Variabel yang dibuat di luar fungsi adalah global dan dapat digunakan oleh siapa saja:
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

'''Variabel Penamaan
Jika Anda beroperasi dengan nama variabel yang sama di dalam dan di luar fungsi, 
Python akan memperlakukan mereka sebagai dua variabel terpisah, 
satu tersedia di lingkup global (di luar fungsi) dan satu tersedia 
di lingkup lokal (di dalam fungsi):'''

#Fungsi akan mencetak lokal x, dan kemudian kode akan mencetak global x:
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

'''Kata Kunci Global
Jika Anda perlu membuat variabel global, tetapi terjebak dalam lingkup lokal, 
Anda dapat menggunakan globalkata kunci.

Kata globalkunci membuat variabel global.'''
#Jika Anda menggunakan globalkata kunci, variabel milik lingkup global:
def myfunc():
  global x
  x = 300

myfunc()

print(x)

'''Juga, gunakan globalkata kunci jika Anda ingin membuat perubahan
ke variabel global di dalam suatu fungsi.'''
'''Contoh
Untuk mengubah nilai variabel global di dalam suatu fungsi,
lihat variabel dengan menggunakan globalkata kunci:'''

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)



