'''Datetime
Tanggal dalam Python bukan tipe data sendiri, tetapi kita dapat mengimpor 
modul bernama datetimeuntuk bekerja dengan tanggal sebagai objek tanggal.'''

#Impor modul datetime dan tampilkan tanggal saat ini:
import datetime

x = datetime.datetime.now()
print(x)

'''Tanggal Output
Ketika kita menjalankan kode dari contoh di atas hasilnya adalah:
2020-08-04 11:44:26.414345
Tanggal berisi tahun, bulan, hari, jam, menit, detik, dan mikrodetik.

The datetimemodul memiliki banyak metode untuk kembali informasi tentang obyek date.

Berikut adalah beberapa contoh, Anda akan belajar lebih banyak 
tentang mereka nanti di bab ini:'''

#Kembalikan tahun dan nama hari kerja:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

'''Membuat Objek Tanggal
Untuk membuat tanggal, kita bisa menggunakan datetime()
kelas (konstruktor) dari datetimemodul.

The datetime()kelas membutuhkan tiga parameter untuk membuat tanggal: 
tahun, bulan, hari.'''
#Buat objek tanggal:
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

'''The datetime()kelas juga mengambil parameter untuk waktu dan zona waktu 
(jam, menit, detik, mikrodetik, tzone), tetapi mereka adalah opsional, 
dan memiliki nilai default 0, ( Nonezona waktu).'''

'''Metode strftime ()
The datetimeobjek memiliki metode untuk memformat objek tanggal ke string dibaca.

Metode ini dipanggil strftime(), dan mengambil satu parameter format,, 
untuk menentukan format string yang dikembalikan:'''
#Tampilkan nama bulan:
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))