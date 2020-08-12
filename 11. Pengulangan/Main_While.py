'''While Loop
Dengan loop sementara, 
kita dapat menjalankan serangkaian pernyataan selama suatu kondisi benar.
'''

#Cetak saya selama saya kurang dari 6:
i = 1
while i < 6:
  print(i)
  i += 1
#ingatlah untuk menambah i, atau jika tidak, pengulangan akan berlanjut selamanya.
'''
The sedangkan lingkaran membutuhkan variabel yang relevan untuk siap, 
dalam contoh ini kita perlu mendefinisikan variabel pengindeksan, i , 
yang kita set ke 1.
'''

'''
Dengan pernyataan break kita dapat menghentikan loop bahkan jika 
kondisi sementara benar:
'''
#Keluar dari loop saat saya berusia 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

'''
Dengan pernyataan continues, kita dapat menghentikan iterasi saat ini, 
dan melanjutkan dengan yang berikutnya:
'''
#Lanjutkan ke iterasi berikutnya jika saya berusia 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

'''
Dengan pernyataan else kita dapat menjalankan satu blok kode sekali 
ketika kondisinya tidak lagi benar:
'''
#Cetak pesan setelah kondisinya salah:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

