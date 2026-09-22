Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #slicing
>>> a="vizag is known as city of destiny"
>>> a[-6:0]
''
>>> a[-6:]
'estiny'
>>> a[-7:]
'destiny'
>>> a[-15:-12]
'cit'
>>> a[-15:-11]
'city'
>>> a[-19:-23]
''
>>> a[-23:-19]
'nown'
>>> a[-24:-19]
'known'
>>> a[-33:-29]
'viza'
>>> a=data
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a=data
NameError: name 'data' is not defined
>>> a="data"
>>> a[::]
'data'
>>> a[::1]
'data'
>>> a="data science"
>>> a[::1]
'data science'
>>> a[::3]
'dacn'
>>> a="machine learning"
>>> a[::2]
'mcielann'
>>> 'mcielann'
'mcielann'
>>> a[::4]
'miln'
>>> a[5:9]
'ne l'
a[6:]
'e learning'
a[:11]
'machine lea'
a[::8]
'ml'
a"colud computing"
SyntaxError: invalid syntax
a="cloud computing"
a[1:8:2]
'lu o'
a[2:12:4]
'ocu'
a[1:14:5]
'lct'
a[2:12]
'oud comput'
a[1:14:5]
'lct'
a[1:13:3]
'ldou'
a[3:9:4]
'uo'
