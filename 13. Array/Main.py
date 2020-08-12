'''
Python tidak memiliki dukungan bawaan untuk Array, 
tetapi LIST Python dapat digunakan sebagai gantinya.

Halaman ini menunjukkan kepada Anda bagaimana menggunakan LISTS sebagai ARRAYS,
namun, untuk bekerja dengan array dengan Python Anda harus mengimpor perpustakaan, 
seperti library NumPy .

'''
#Buat larik yang berisi nama mobil:
cars = ["Ford", "Volvo", "BMW"]

'''Apa itu Array?
Array adalah variabel khusus,
yang dapat menampung lebih dari satu nilai pada suatu waktu.

Jika Anda memiliki daftar item (daftar nama mobil, misalnya), 
menyimpan mobil dalam variabel tunggal dapat terlihat seperti ini:
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

Namun, bagaimana jika Anda ingin melewati mobil dan menemukan yang spesifik? 
Dan bagaimana jika Anda tidak memiliki 3 mobil, tetapi 300?

Solusinya adalah sebuah array!
Array dapat menampung banyak nilai dengan satu nama, 
dan Anda dapat mengakses nilai dengan merujuk ke nomor indeks.
'''
#Dapatkan nilai dari item array pertama:
x = cars[0]

#Ubah nilai item array pertama:
cars[0] = "Toyota"

#Gunakan len()metode untuk mengembalikan panjang array (jumlah elemen dalam array).
x = len(cars)

'''Array Loop
Anda bisa menggunakan for inloop untuk mengulang semua elemen dari array.
'''
#Cetak setiap item dalam carsarray:
for x in cars:
  print(x)

#Tambahkan satu elemen lagi ke cars array, menggunakan append():
cars.append("Honda")

#Hapus elemen kedua cars array:
cars.pop(1)
#Anda juga dapat menggunakan remove() :
cars.remove("Volvo")

'''Metode daftar remove()hanya menghilangkan kemunculan pertama dari nilai yang ditentukan.'''
