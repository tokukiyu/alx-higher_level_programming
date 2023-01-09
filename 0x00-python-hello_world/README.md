# 0x00. Python - Hello, World

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

## Resources
* [The Python tutorial](https://docs.python.org/3/tutorial/index.html)
* [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
* [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
* [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
* [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
* [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Tasks To Complete

+ [x] 0\. Run Python file<br/>_**[0-run](0-run)**_ contains a Shell script that runs a Python script that is saved in the environment variable `PYFILE`.
+ [x] 1\. Run inline<br/>_**[1-run_inline](1-run_inline)**_ contains a Shell script that runs Python code that is saved in the environment variable `PYCODE`.
+ [x] 2\. Hello, print<br/>_**[2-print.py](2-print.py)**_ contains a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
+ [x] 3\. Print integer<br/>_**[3-print_number.py](3-print_number.py)**_ contains a Python script that will print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.
+ [x] 4\. Print float<br/>_**[4-print_float.py](4-print_float.py)**_ contains a Python script that will print the float stored in the variable `number` with a precision of 2 digits.
+ [x] 5\. Print string<br/>_**[5-print_string.py](5-print_string.py)**_ contains a Python script that will print 3 times a string stored in the variable `str`, followed by its first 9 characters.
+ [x] 6\. Play with strings<br/>_**[6-concat.py](6-concat.py)**_ contains a Python script that will print `Welcome to Holberton School!`.
+ [x] 7\. Copy - Cut - Paste<br/>_**[7-edges.py](7-edges.py)**_ contains a Python script that will extract parts of a `word` variable.
+ [x] 8\. Create a new sentence<br/>_**[8-concat_edges.py](8-concat_edges.py)**_ contains a Python script that will print `object-oriented programming with Python`, followed by a new line.
+ [x] 9\. Easter Egg<br/>_**[9-easter_egg.py](9-easter_egg.py)**_ contains a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
+ [x] 10\. Linked list cycle<br/>_**[10-check_cycle.c](10-check_cycle.c)**_ contains a function in C that checks if a singly linked list has a cycle in it.
+ [x] 11\. Hello, write<br/>_**[100-write.py](100-write.py)**_ contains a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
+ [x] 12\. Compile<br/>_**[101-compile](101-compile)**_ contains a Shell script that compiles a Python script file in the environment variable `PYFILE`.
+ [x] 13\. ByteCode -> Python #1<br/>_**[102-magic_calculation.py](102-magic_calculation.py)**_ contains a Python script that defines the function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:<br/>
  ```c
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
	```
