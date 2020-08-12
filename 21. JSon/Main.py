'''JSON
JSON adalah sintaks untuk menyimpan dan bertukar data.
JSON adalah teks, ditulis dengan notasi objek JavaScript.

JSON dengan Python
Python memiliki paket bawaan yang disebut json, yang dapat digunakan
untuk bekerja dengan data JSON.'''

#Impor modul json:
import json

'''Parse JSON - Konversi dari JSON ke Python
Jika Anda memiliki string JSON, 
Anda dapat menguraikannya dengan menggunakan json.loads()metode ini.'''

#Konversi dari JSON ke Python:
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

'''Konversi dari Python ke JSON
Jika Anda memiliki objek Python, Anda bisa mengubahnya menjadi 
string JSON dengan menggunakan json.dumps()metode ini.'''
#Konversi dari Python ke JSON:
import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

#Konversikan objek Python menjadi string JSON, dan cetak nilainya:
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Konversi objek Python yang berisi semua tipe data hukum:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

'''Format hasilnya
Contoh di atas mencetak string JSON, tetapi tidak mudah dibaca, 
tanpa lekukan dan jeda baris.

The json.dumps()metode memiliki parameter untuk membuatnya lebih mudah 
untuk membaca hasilnya:'''

#Gunakan indentparameter untuk menentukan jumlah indentasi:
json.dumps(x, indent=4)

'''Anda juga dapat mendefinisikan pemisah, nilai default adalah (",", ":"), 
yang berarti menggunakan koma dan spasi untuk memisahkan setiap objek, 
dan titik dua dan ruang untuk memisahkan kunci dari nilai:'''

#Gunakan separatorsparameter untuk mengubah pemisah default:
json.dumps(x, indent=4, separators=(". ", " = "))

'''Pesan hasilnya
The json.dumps()metode memiliki parameter untuk memesan kunci dalam hasil:'''
#Gunakan sort_keysparameter untuk menentukan apakah hasilnya harus diurutkan atau tidak:
json.dumps(x, indent=4, sort_keys=True)