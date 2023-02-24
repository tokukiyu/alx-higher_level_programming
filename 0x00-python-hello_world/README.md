# 0x00. Python - Hello, World

![Pep8 style](https://img.shields.io/badge/PEP8-style%20guide-green?style=round-square)
![Betty style](https://img.shields.io/badge/betty-style%20guide-purple?style=round-square)

## Learning Objectives
* Why Python programming is awesome
* Who created Python
* Who is Guido van Rossum
* Where does the name ‘Python’ come from
* What is the Zen of Python
* How to use the Python interpreter
* How to print text and variables using `print`
* How to use strings
* What are indexing and slicing in Python
* What is the official Python coding style and how to check your code with `pycodestyle`
* How `Pycodestyle` is the new [standard of Python style code](https://github.com/PyCQA/pycodestyle/issues/466)

## Resources
* [The Python tutorial](https://docs.python.org/3/tutorial/index.html) (only the first three chapters below)
* [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
* [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
* [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) (Read up until “3.1.2. Strings” included)
* [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
* [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Tasks To Complete

+ [x] 0\. Run Python file<br/>_**[0-run](0-run)**_ contains a Shell script that runs a Python script that is saved in the environment variable `PYFILE`.<br/>__Example__:
```c
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
```
+ [x] 1\. Run inline<br/>_**[1-run_inline](1-run_inline)**_ contains a Shell script that runs Python code that is saved in the environment variable `PYCODE`.<br/>__Example__:
```c
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 
```
+ [x] 2\. Hello, print<br/>_**[2-print.py](2-print.py)**_ contains a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.<br/>__Example__:
```c
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```
+ [x] 3\. Print integer<br/>_**[3-print_number.py](3-print_number.py)**_ contains a Python script that will print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.<br/>__Example__:
```c
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```
+ [x] 4\. Print float<br/>_**[4-print_float.py](4-print_float.py)**_ contains a Python script that will print the float stored in the variable `number` with a precision of 2 digits.<br/>__Example__:
```c
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
```
+ [x] 5\. Print string<br/>_**[5-print_string.py](5-print_string.py)**_ contains a Python script that will print 3 times a string stored in the variable `str`, followed by its first 9 characters.<br/>__Example__:
```c
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$ 
```
+ [x] 6\. Play with strings<br/>_**[6-concat.py](6-concat.py)**_ contains a Python script that will print `Welcome to Holberton School!`.<br/>__Example__:
```c
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 
```
+ [x] 7\. Copy - Cut - Paste<br/>_**[7-edges.py](7-edges.py)**_ contains a Python script that will extract parts of a `word` variable.<br/>__Example__:
```c
guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$ 
```
+ [x] 8\. Create a new sentence<br/>_**[8-concat_edges.py](8-concat_edges.py)**_ contains a Python script that will print `object-oriented programming with Python`, followed by a new line.<br/>__Example__:
```c
guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$ 
```
+ [x] 9\. Easter Egg<br/>_**[9-easter_egg.py](9-easter_egg.py)**_ contains a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.<br/>__Example__:
```c
guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/0x00$
```
+ [x] 10\. Linked list cycle<br/>_**[10-check_cycle.c](10-check_cycle.c)**_ contains a function in C that checks if a singly linked list has a cycle in it.<br/>__Example__:
```c
carrie@ubuntu:~/0x00$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
carrie@ubuntu:~/0x00$$ ./cycle 
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
carrie@ubuntu:~/0x00$
```
+ [x] 11\. Hello, write<br/>_**[100-write.py](100-write.py)**_ contains a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.<br/>__Example__:
```c
guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2> q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ 
```
+ [x] 12\. Compile<br/>_**[101-compile](101-compile)**_ contains a Shell script that compiles a Python script file in the environment variable `PYFILE`.<br/>__Example__:
```c
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./101-compile
Compiling main.py ...
guillaume@ubuntu:~/py/0x00$ ls
101-compile  main.py  main.pyc
guillaume@ubuntu:~/py/0x00$ cat main.pyc | zgrep -c "Best School"
1
guillaume@ubuntu:~/py/0x00$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
guillaume@ubuntu:~/py/0x00$ 
```
+ [x] 13\. ByteCode -> Python #1<br/>_**[102-magic_calculation.py](102-magic_calculation.py)**_ contains a Python script that defines the function `def magic_calculation(a, b):` that does exactly the same as the following [Python bytecode](https://docs.python.org/3.4/library/dis.html):<br/>
  ```c
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
	```
	__Example__:
	```c
	bekalue@BEKALU-PC:~/c/0x00$ export CFILE=main.c
	bekalue@BEKALU-PC:~/c/0x00$ ./0-preprocessor 
	bekalue@BEKALU-PC:~/c/0x00$ tail c
	```
