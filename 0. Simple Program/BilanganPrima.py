#Program mengecek bilangan prima
'''
Bilangan prima adalah bilangan yang lebih besar dari 1 
yang tidak memiliki faktor pembagi lain kecuali 1 dan dirinya sendiri. 
Contohnya adalah 2, 3, 5, 7, dan seterusnya. Bilangan 6 bukanlah prima 
karena memiliki faktor lain, 2 x 3 = 6.
'''

#Meminta inputan user
num = int(input('Masukkan bilangan : '))

#Bilangan prima harus lebih dari 1
if num > 1:
    for i in range(2, num):
        if (num % 1) == 0:
            print(num, 'Bukan bilangan prima')
            print(i, 'kali', num//i, '=', num)
            break
    else:
        print(num, 'adalah bilangan prima')

#Jika bilangan kurang atau sama dengan satu
else:
    print(num, 'bukan bilangan')