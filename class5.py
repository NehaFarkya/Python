Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> names=['neha','jatin',]
>>> names_dict={i:names[i]for i in range(len(names))}
>>> names_dict
{0: 'neha', 1: 'jatin'}
>>> enumerate(names)
<enumerate object at 0x02333B48>
>>> list(enumerate(names))
[(0, 'neha'), (1, 'jatin')]
>>> name_dict={i:j for i,j in enumerate(names)}
>>> names_dict
{0: 'neha', 1: 'jatin'}
>>> name_dict={i:j for i,j in enumerate(names)}
>>> age=[35,25]
>>> names
['neha', 'jatin']
>>> age
[35, 25]
>>> 
>>> names_ages={names[i]:age[i] for i in range(len(names))}
>>> names_ages
{'neha': 35, 'jatin': 25}
>>> zip(names,age)
[('neha', 35), ('jatin', 25)]
>>> names_ages={i:j] for i,j in zip(names))}
SyntaxError: invalid syntax
>>> names_ages={i:j for i,j in zip(names)}

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    names_ages={i:j for i,j in zip(names)}
  File "<pyshell#16>", line 1, in <dictcomp>
    names_ages={i:j for i,j in zip(names)}
ValueError: need more than 1 value to unpack
>>> names_ages={i:j for i,j in zip(names,ages)}

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    names_ages={i:j for i,j in zip(names,ages)}
NameError: name 'ages' is not defined
>>> names_ages={i:j for i,j in zip(names,age)}
>>> names_age

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    names_age
NameError: name 'names_age' is not defined
>>> names_ages
{'neha': 35, 'jatin': 25}
>>> 
