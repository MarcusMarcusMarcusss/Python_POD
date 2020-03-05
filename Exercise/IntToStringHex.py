#Given a non-negative integer n, convert the integer to hexadecimal and return the result as a string. 
#Hexadecimal is a base 16 representation of a number, where the digits are 0123456789ABCDEF. 
#Do not use any builtin base conversion functions like hex.


def to_hex(n):
  return "%X" % int(n)

print(to_hex(123))
# 7B
