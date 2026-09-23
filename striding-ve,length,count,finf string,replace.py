Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#stridng
a="python course"
a[6:2:1]
''
#negative
a[-1:-8:-2]
'ero '
a[-2:-12:-3]
'sont'
a[-4:-13:-4]
'uny'
#lenght()
a="sahiti"
len9a0
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    len9a0
NameError: name 'len9a0' is not defined
len(a)
6
b="python"
len(b)
6
c="123456789"
len(c)
9
d=""
len(d)
0
#count()
a="twinkle twinkle little star"
a.count("twinkle)
        
SyntaxError: unterminated string literal (detected at line 1)
>>> a.count("twinkle")
...         
2
>>> b.count("t")
...         
1
>>> c.count("l")
...         
0
>>> a.count("")
...         
28
>>> #find a string
...         
>>> a="python"
...         
>>> a[3]
...         
'h'
>>> a.find("h")
...         
3
>>> b="hello"
...         
>>> b.find("l")
...         
2
>>> b[2:4]
...         
'll'
>>> a[2:4]
...         
'th'
>>> #replace()
...         
>>> a="wait until you succeed"
...         
>>> a.replace("wait","work")
...         
'work until you succeed'
>>> b="python ml"
...         
>>> b.replace("ml","ai")
...         
'python ai'
