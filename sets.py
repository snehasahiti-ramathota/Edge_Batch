Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#set{}
a={2,3,4,5,6,7,8}
b={5,6,8,7}
a.issubset(b)
False
b.issubset(a)
True
a={3,4,5,6,7,8}
b={6,7,8}
a.issuperset(b)
True
b.issuperset(a)
False
#union()
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#intersection()
a={3,4,5,6,7,8}
b={6,7,8,9,10,11}
a.intersection(b)
{8, 6, 7}
#add()
c={5,6,7,8,9}
c.add(10)
c
{5, 6, 7, 8, 9, 10}
a={10,11,12,13,14,15}
b={13,14,15,16,17,18}
a.diffreence(b)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.diffreence(b)
AttributeError: 'set' object has no attribute 'diffreence'. Did you mean: 'difference'?
a.difference(b)
{10, 11, 12}
b.difference(a)
{16, 17, 18}
#update()
a={10,20,30,40,50}
b={30,40,50,60,70}
a.update(b)
a
{70, 40, 10, 50, 20, 60, 30}
b.update(a)
b
{70, 40, 10, 50, 20, 60, 30}
#symmetric_difference
a={2,3,4,5,6,7}
b={4,5,6,7,8,9,}
a.symmetric_difference(b)
{2, 3, 8, 9}
#difference_update
a={3,4,5,6,7,8}
b={7,8,9,10,11}
a.difference_update(b)
a
{3, 4, 5, 6}
b.difference_update(a)
b
{7, 8, 9, 10, 11}
#intersection_update()
a={3,4,5,6,7,8,8}
b={6,7,8,9,10,11}
a.intersection_update(b)
a
{8, 6, 7}
b.intersection_update(a)
b
{8, 6, 7}
#symmetric_update()
a={3,4,5,6,7}
b={6,7,8,9,10}
a.symmetric_difference(b)
{3, 4, 5, 8, 9, 10}
b.symmetric_difference(a)
{3, 4, 5, 8, 9, 10}
#sets{}
a={3,5.6,"sahiti,8+8j,True,False}
   
SyntaxError: unterminated string literal (detected at line 1)
a={3,5.6,"sahiti",8+8j,True,False}
   
print(a)
   
{False, True, (8+8j), 3, 'sahiti', 5.6}
type(a)
   
<class 'set'>
b={2,3,4,5,6,7}
   
print(b)
   
{2, 3, 4, 5, 6, 7}

a={7,8,9,10,11}
   
a.copy()
   
{7, 8, 9, 10, 11}
b=a.copy()
   
>>> b
...    
{7, 8, 9, 10, 11}
>>> a.pop()
...    
7
>>> a
...    
{8, 9, 10, 11}
>>> a.pop(9)
...    
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.pop(9)
TypeError: set.pop() takes no arguments (1 given)
>>> a.remove(9)
...    
>>> a
...    
{8, 10, 11}
>>> a={5,6,7,8}
...    
>>> a.discard(7)
...    
>>> a
...    
{8, 5, 6}
>>> a.clear()
...    
>>> a
...    
set()
>>> b=set()
...    
>>> b.add(30)
...    
>>> b
...    
{30}
>>> a={2,3,4,5,6}
...    
>>> b={7,8,9,10,11}
...    
>>> a.isdisjoint(b)
...    
True
