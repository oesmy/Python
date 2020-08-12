'''
Kondisi Python dan pernyataan If
Kondisi ini dapat digunakan dalam beberapa cara, paling umum di "jika pernyataan" dan loop.

Pernyataan "jika" ditulis dengan menggunakan kata kunci if .
'''
#Pernyataan If
a = 33
b = 200
if b > a:
  print("b is greater than a")

'''
Dalam contoh ini kita menggunakan dua variabel, a dan b , yang digunakan sebagai 
bagian dari pernyataan if untuk menguji apakah b lebih besar dari a . 
Karena a adalah 33 , dan b adalah 200 , kita tahu bahwa 200 lebih besar dari 33,
dan jadi kita mencetak ke layar bahwa "b lebih besar dari a".
'''

'''Elif
Kata kunci elif adalah cara python mengatakan "jika kondisi sebelumnya tidak benar, 
maka coba kondisi ini".
'''

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

'''
Dalam contoh ini a sama dengan b , jadi kondisi pertama tidak benar, 
tetapi kondisi elif benar, jadi kami mencetak ke layar bahwa "a dan b sama".
'''

#Kata kunci elif menangkap apa pun yang tidak tertangkap oleh kondisi sebelumnya.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

'''
Dalam contoh ini a lebih besar dari b , jadi kondisi pertama tidak benar, 
juga kondisi elif tidak benar, jadi kami pergi ke kondisi lain dan mencetak 
ke layar bahwa "a lebih besar dari b".
'''
#Anda juga dapat memiliki else tanpa elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Satu baris jika pernyataan:
if a > b: print("a is greater than b")

#Satu baris jika ada pernyataan:
a = 2
b = 330
print("A") if a > b else print("B")

#Satu baris jika lain pernyataan, dengan 3 syarat:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

'''AND
Kata kunci dan adalah operator logis, dan digunakan 
untuk menggabungkan pernyataan bersyarat:
'''
#Tes jika alebih besar dari b, DAN jika c lebih besar dari a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

'''OR
Kata orkunci adalah operator logis, 
dan digunakan untuk menggabungkan pernyataan bersyarat:
'''
#Tes jika alebih besar dari b, ATAU jika a lebih besar dari c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

'''If Bersarang
Anda dapat memiliki ifpernyataan di dalam if pernyataan, 
ini disebut pernyataan bersarang if.
'''
#Contoh
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

'''
if pernyataan tidak boleh kosong, tetapi jika Anda karena suatu alasan 
memiliki if pernyataan tanpa konten, masukkan PASS pernyataan itu untuk
menghindari kesalahan.
'''
#Contoh
a = 33
b = 200

if b > a:
  pass

