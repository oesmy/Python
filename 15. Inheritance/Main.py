'''Inheritance/Warisan
memungkinkan kita untuk mendefinisikan kelas yang mewarisi semua metode 
dan properti dari kelas lain.

Kelas induk adalah kelas yang diwarisi dari, juga disebut kelas dasar.
Kelas anak adalah kelas yang mewarisi dari kelas lain, juga disebut kelas turunan.
'''

'''Buat Kelas Induk
Setiap kelas bisa menjadi kelas induk, jadi sintaksnya sama dengan membuat kelas lain:'''
#Buat kelas bernama Person, dengan firstnamedan lastnameproperti, dan printnamemetode:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

'''Buat Kelas Anak
Untuk membuat kelas yang mewarisi fungsi dari kelas lain, 
kirim kelas induk sebagai parameter saat membuat kelas anak:'''
#Buat kelas bernama Student, yang akan mewarisi properti dan metode dari Personkelas:
class Student(Person):
      pass

'''Catatan
Gunakan pass kata kunci saat Anda tidak ingin menambahkan properti atau 
metode lain ke dalam kelas.

Sekarang kelas Siswa memiliki properti dan metode yang sama dengan kelas Person.'''

#Gunakan Studentkelas untuk membuat objek, dan kemudian jalankan printnamemetode:
x = Student("Mike", "Olsen")
x.printname()

'''Tambahkan Fungsi __init __ ()
Sejauh ini kami telah membuat kelas anak yang mewarisi properti dan metode dari induknya.

Kami ingin menambahkan __init__()fungsi ke kelas anak (bukan passkata kunci).'''

'''Catatan
__init__()fungsi disebut secara otomatis setiap kali kelas sedang digunakan 
untuk membuat objek baru.'''

#Tambahkan __init__()fungsi ke Studentkelas:
class Student(Person):
      def __init__(self, fname, lname):
    #add properties etc.

'''
Saat Anda menambahkan __init__()fungsi, kelas anak tidak akan lagi
mewarisi fungsi orangtua __init__().
'''

'''Catatan: 
The anak __init__() fungsi menimpa warisan dari orang tua __init__()fungsi.

Untuk menjaga warisan fungsi induk __init__() , 
tambahkan panggilan ke fungsi induk __init__():'''
#Contoh
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

'''Sekarang kami telah berhasil menambahkan fungsi __init __ (), 
dan mempertahankan warisan dari kelas induk, dan kami siap untuk menambahkan 
fungsionalitas dalam __init__()fungsi tersebut.'''

'''Gunakan Fungsi super ()
Python juga memiliki super()fungsi yang akan membuat 
kelas anak mewarisi semua metode dan properti dari induknya:'''
#Contoh
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

'''Dengan menggunakan super()fungsi ini, Anda tidak harus menggunakan nama elemen induk,
itu akan secara otomatis mewarisi metode dan properti dari induknya.'''

#Tambahkan properti yang dipanggil graduationyearke Studentkelas:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

'''Dalam contoh di bawah ini, tahun 2019harus berupa variabel,
 dan diteruskan ke Studentkelas saat membuat objek siswa. 
 Untuk melakukannya, tambahkan parameter lain dalam fungsi __init __ ():'''

#Tambahkan yearparameter, dan lulus tahun yang benar saat membuat objek:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

#Tambahkan metode yang dipanggil welcomeke Studentkelas:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

'''Jika Anda menambahkan metode di kelas anak dengan nama yang sama dengan fungsi 
di kelas induk, warisan metode induk akan ditimpa.'''
