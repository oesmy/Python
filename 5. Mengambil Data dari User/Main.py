'''input user
Python memungkinkan input pengguna.
Itu berarti kami dapat meminta input dari pengguna.

Metode ini sedikit berbeda dalam Python 3.6 dari Python 2.7.
Python 3.6 menggunakan input()metode ini.
Python 2.7 menggunakan raw_input()metode ini.

Contoh berikut menanyakan nama pengguna, dan ketika Anda memasukkan nama pengguna, 
itu akan dicetak di layar:'''
#Python 3.6
username = input("Enter username:")
print("Username is: " + username)
#Python 2.7
username = raw_input("Enter username:")
print("Username is: " + username)

'''
Python berhenti mengeksekusi ketika datang ke input()fungsi, 
dan berlanjut ketika pengguna telah memberikan beberapa input.'''