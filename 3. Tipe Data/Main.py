# Casting adalah merubah tipe data ke tipe data lain
'''Tipe Data Internal
Dalam pemrograman, tipe data adalah konsep penting.
Variabel dapat menyimpan data dari tipe yang berbeda, 
dan tipe yang berbeda dapat melakukan hal yang berbeda.
Tipe data di python :
- Jenis teks:	str
- Jenis Numerik:	int, float, complex
- Jenis Urutan:	list, tuple, range
- Jenis pemetaan:	dict
- Setel Jenis:	set, frozenset
- Jenis Boolean:	bool
- Jenis Biner:	bytes, bytearray, memoryview
'''

# Melihat tipe data, dengan type()
x = 5
print(type(x))

# Mengatur Tipe data
# Dalam Python, tipe data diatur saat Anda menetapkan nilai ke variabel:
x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview

# Mengatur tipe data spesifik
# Jika Anda ingin menentukan tipe data, Anda dapat menggunakan fungsi konstruktor berikut:
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview

