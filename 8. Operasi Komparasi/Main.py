# Setiap hasil komparasi adalah boolean

'''
    Operasinya : > , < , >= , <= , !=, is, is not
'''
a = 4
b = 7
c = 4

# Operator >
print("======OPERATOR >")

hasil = a > b
print (hasil)

hasil = b > a
print (hasil)

# Operator <
print("======OPERATOR <")

hasil = a < b
print (hasil)

hasil = b < a
print (hasil)

# Operator >=
print("======OPERATOR >=")

hasil = a <= b
print (hasil)

hasil = b <= a
print (hasil)

hasil = a >= c
print(hasil)

# Operator <=
print("======OPERATOR <=")

hasil = a <= b
print (hasil)

hasil = b <= a
print (hasil)

hasil = c <= a
print(hasil)

# Operator ==
print("======OPERATOR ==")

hasil = a == b
print (hasil)

hasil = a == c
print (hasil)

# Operator !=
print("======OPERATOR !=")

hasil = a != b
print (hasil)

hasil = a != c
print (hasil)

# Operator is dan is not

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

'''
returns True because x is not the same object as y,
even if they have the same content
'''

print(x != y)

''' 
to demonstrate the difference betweeen "is not" and "!=": 
this comparison returns False because x is equal to y
'''

print("=====Operator Is not")
print(x is not z)

# returns False because z is the same object as x

print(x is not y)

'''
returns True because x is not the same object as y,
even if they have the same content
'''

print(x != y)

'''
to demonstrate the difference betweeen "is not" and "!=": 
this comparison returns False because x is equal to y
'''
