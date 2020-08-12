# Operasi Aritmatika
''' Ada enam jenis operator pemrograman 
    - Operator Aritmatika
    - Operator Perbandingan
    - Operator Penugasan
    - Operator Logika
    - Operator Bitwise
    - Operator Ternary 
Operator aritmatika :
Operator	Name	   Example	T
+	      Addition   	x + y	
-	    Subtraction	    x - y	
*	  Multiplication	x * y	
/	     Division	    x / y	
%	     Modulus	    x % y	
**	  Exponentiation	x ** y	
//	  Floor division	x // y

'''

# Penjumlahan dan Pengurangan
a = 5
b = 6

hasil_1 = a + b
print(a, "+", b, "= ", hasil_1)

hasil_2 = b - a
print(b, "-", a, "= ", hasil_2)

print("---------------------")

# Perkalian dan Pembagian
x = 10
y = 5

nilai_1 = x * y
print(x, "*", y, "= ", nilai_1)

nilai_2 = x / y
print(x, "/", y, "= ", nilai_2)

print("---------------------")

# Exponen, Modulus dan Floor Division
x = 10
y = 5

nilai_1 = x ** y
print(x, "**", y, "= ", nilai_1)

nilai_2 = x % y
print(x, "%", y, "= ", nilai_2)

nilai_2 = x // y
print(x, "//", y, "= ", nilai_2)

# Prioritas Operasi
x = 10
y = 5
z = 2

nilai_1 = x ** y * z - y + x / z % y // z
print(x,"**",y,"*",z,"-",y,"+",x,"/",z,"%",y,"//",z , "= ", nilai_1)

'''
    Urutan Eksekusi Operasi : 1. ()
                              2. Exponen **
                              3. Perkalian dkk * / % //
                              4. Penjumlahan dan pengurangan + -
'''
