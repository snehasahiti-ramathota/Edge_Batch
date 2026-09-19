Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#indexing
a=vizag
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a=vizag
NameError: name 'vizag' is not defined
a="vizag"
a[1]
'i'
a[2]
'z'
a[3]
'a'
a4[4]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a4[4]
NameError: name 'a4' is not defined. Did you mean: 'a'?
a[4]
'g'
a="I am in class"
a[3]+a[4]
'm '
a[1]
' '
a[2]
'a'
a="i am in class"
a[3]+a[4]
'm '
a[2]
'a'
a[1]
' '
a[0]
'i'
a[2]+a[3]
'am'
a[8]+a[9]+a[10]+a[11]
'clas'
a[1]+a[4]+a[7]
'   '
a="I am learning python full stack"
a[2]+a[3]
'am'
a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
a[20]+a[21]+a[22]
' fu'
a[21]+a[22]+a[23]+a[24]
'full'
#negative
a=sahiti ramathota
SyntaxError: invalid syntax
>>> a"sahiti ramathota"
SyntaxError: invalid syntax
>>> a="sahiti ramathota"
>>> a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]+a[-7]+a[-8]+a[-9]
'atohtamar'
>>>  a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
...  
SyntaxError: unexpected indent
>>> a[-1]
'a'
>>> a[-2]
't'
>>> a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-6]+a[-4]a[-3]+a[-2]+a[-1]
SyntaxError: invalid syntax
>>> a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-6]+a[-4]+a[-3]+a[-2]+a[-1]
'ramatahota'
>>> a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]a[-3]+a[-2]+a[-1]
SyntaxError: invalid syntax
>>> a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'ramathota'
>>> a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]
'atohta'
>>> a[-11]+a[-12]+a[-13]+a[-14]+a[-15]+a[-16]
'itihas'
>>> a[-16]+a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'sahiti'
>>> #slicing
>>> a="anits"
>>> a[0:5]
'anits'
>>> a[0:3]
'ani'
>>> a="I am learning python full stack"
>>> a[0:13]
'I am learning'
>>> a[-16:-1]
'ython full stac'
>>> a[-17:0]
''
>>> a[-15:-1]
'thon full stac'
>>> 
>>> a[-17:-1]
'python full stac'
>>> a[-1]
'k'
