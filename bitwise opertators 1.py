Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#bitwise opertators
#&,|,~,^,<<,>>
a=3
b=5
>>> a&b
1
>>> b in (3)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b in (3)
TypeError: argument of type 'int' is not iterable
>>> b in (3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b in (3)
TypeError: argument of type 'int' is not iterable
>>> bin(5)
'0b101'
>>> a&b
1
>>> bin(4)
'0b100'
>>> a&b
1
>>> a=5
>>> b=7
>>> a&b
5
>>> a=6
>>> b=8
>>> a|b
14
>>> a=5
>>> b=7
>>> a|b
7
>>> 07
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> a=3
>>> ~a
-4
>>> b=-20
>>> ~b
19
>>> a=18
>>> ~a
-19
>>> a=-234567
>>> ~a
234566
