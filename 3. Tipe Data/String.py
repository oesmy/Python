"""
String Literal
String literal dalam python dikelilingi oleh tanda kutip tunggal, atau tanda kutip ganda.
'halo' sama dengan "halo" .
"""
#Anda dapat menampilkan string literal dengan print()fungsi:
print("Hello")
print('Hello')

#Tetapkan String ke Variabel
a = "Hello"
print(a)

#String Multiline
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

'''
String adalah Array, Seperti banyak bahasa pemrograman populer lainnya,
string dalam Python adalah array byte yang mewakili karakter unicode.

Namun, Python tidak memiliki tipe data karakter, 
satu karakter hanyalah sebuah string dengan panjang 1.
'''
#Dapatkan karakter di posisi 1 (ingat bahwa karakter pertama memiliki posisi 0):
a = "Hello, World!"
print(a[1])

'''Slicing (Mengiris), 
Tentukan indeks awal dan indeks akhir,
dipisahkan oleh titik dua, untuk mengembalikan bagian dari string.
'''
#Dapatkan karakter dari posisi 2 ke posisi 5 (tidak termasuk):
b = "Hello, World!"
print(b[2:5])

#Pengindeksan Negatif,Dapatkan karakter dari posisi 5 ke posisi 1 (tidak termasuk), 
#mulai penghitungan dari akhir string:
b = "Hello, World!"
print(b[-5:-2])

#Untuk mendapatkan panjang string, gunakan len()fungsinya.
a = "Hello, World!"
print(len(a))

"""Metode String
Python memiliki seperangkat metode bawaan yang dapat Anda gunakan pada string.
"""
#The strip()Metode menghapus setiap spasi dari awal atau akhir:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#The lower()Metode mengembalikan string dalam huruf kecil:
a = "Hello, World!"
print(a.lower())

#The upper()Metode mengembalikan string dalam huruf besar:
a = "Hello, World!"
print(a.upper())

#The replace()Metode menggantikan string dengan string lain:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split()Metode membagi string menjadi substring jika menemukan kasus separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

'''Periksa String
Untuk memeriksa apakah ada frasa atau karakter tertentu dalam sebuah string,
kita dapat menggunakan kata kunci inatau not in.
'''
#Periksa apakah frasa "ain" ada dalam teks berikut:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

#Periksa apakah frasa "ain" TIDAK ada dalam teks berikut:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)

'''Penggabungan string
Untuk menggabungkan, atau menggabungkan, dua string Anda dapat menggunakan operator +.
'''
#Gabungkan variabel adengan variabel bmenjadi variabel c:
a = "Hello"
b = "World"
c = a + b
print(c)

#Untuk menambahkan spasi di antara mereka, tambahkan " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

'''Format string
Seperti yang kita pelajari di bab Python Variables,
kita tidak bisa menggabungkan string dan angka.

Tetapi kita dapat menggabungkan string dan angka dengan menggunakan format()metode ini!
The format()metode mengambil argumen berlalu, format mereka,
dan tempat-tempat mereka dalam string mana placeholder {}adalah:
'''
#Gunakan format()metode untuk memasukkan angka ke dalam string:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Format () metode mengambil 
#jumlah argumen yang tidak terbatas, dan ditempatkan ke masing-masing placeholder:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Anda dapat menggunakan nomor indeks {0}
#untuk memastikan argumen ditempatkan di placeholder yang benar:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

'''Escape Karakter
Untuk menyisipkan karakter yang ilegal dalam string, gunakan karakter escape.
Karakter melarikan diri adalah garis miring terbalik \diikuti oleh karakter yang ingin Anda masukkan.

Karakter melarikan diri 
memungkinkan Anda untuk menggunakan tanda kutip ganda ketika Anda biasanya tidak diizinkan:
'''
txt = "We are the so-called \"Vikings\" from the north."

'''
Karakter pelarian lain yang digunakan dalam Python:
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''

'''
Metode String :
Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''
