# 0x08. Python - More Classes and Objects

![Pep8 style](https://img.shields.io/badge/PEP8-style%20guide-green?style=round-square)
![Betty style](https://img.shields.io/badge/betty-style%20guide-purple?style=round-square)

## Tasks To Complete

+ [x] 0\. Simple rectangle <br/>_**[0-rectangle.py](0-rectangle.py)**_  contains an empty class `Rectangle` that defines a rectangle.
+ [x] 1\. Real definition of a rectangle <br/>_**[1-rectangle.py](1-rectangle.py)**_  contains a class `Rectangle` that defines a rectangle by: (based on [`0-rectangle.py`](0-rectangle.py)).
  + Private instance attribute: `width`.
     + Property `def width(self):` to retrieve it.
     + Property setter `def width(self, value):` to set it (`width` must be an integer and greater than or equal to 0).
  + Private instance attribute: `height`.
     + Property `def height(self):` to retrieve it.
     + Property setter `def height(self, value):` to set it (`height` must be an integer and greater than or equal to 0).
  + Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`.
+ [x] 2\. Area and Perimeter <br/>_**[2-rectangle.py](2-rectangle.py)**_  contains a class `Rectangle` that defines a rectangle by: (based on [`1-rectangle.py`](1-rectangle.py)).
  + Private instance attribute: `width`.
     + Property `def width(self):` to retrieve it.
     + Property setter `def width(self, value):` to set it (`width` must be an integer and greater than or equal to 0).
  + Private instance attribute: `height`.
     + Property `def height(self):` to retrieve it.
     + Property setter `def height(self, value):` to set it (`height` must be an integer and greater than or equal to 0).
  + Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`.
  + Public instance method: `def area(self):` that returns the rectangle area.
  + Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
+ [x] 3\. String representation <br/>_**[3-rectangle.py](3-rectangle.py)**_  contains a class `Rectangle` that defines a rectangle by: (based on [`2-rectangle.py`](2-rectangle.py)).
  + Private instance attribute: `width`.
     + Property `def width(self):` to retrieve it.
     + Property setter `def width(self, value):` to set it (`width` must be an integer and greater than or equal to 0).
  + Private instance attribute: `height`.
     + Property `def height(self):` to retrieve it.
     + Property setter `def height(self, value):` to set it (`height` must be an integer and greater than or equal to 0).
  + Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`.
  + Public instance method: `def area(self):` that returns the rectangle area.
  + Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  + `print()` and `str()` should print the rectangle with the character `#`. (if `width` or `height` is equal to 0, return an empty string).
+ [x] 4\. Eval is magic <br/>_**[4-rectangle.py](4-rectangle.py)**_  contains a class `Rectangle` that defines a rectangle by: (based on [`3-rectangle.py`](3-rectangle.py)).
  + Private instance attribute: `width`.
     + Property `def width(self):` to retrieve it.
     + Property setter `def width(self, value):` to set it (`width` must be an integer and greater than or equal to 0).
  + Private instance attribute: `height`.
     + Property `def height(self):` to retrieve it.
     + Property setter `def height(self, value):` to set it (`height` must be an integer and greater than or equal to 0).
  + Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`.
  + Public instance method: `def area(self):` that returns the rectangle area.
  + Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  + `print()` and `str()` should print the rectangle with the character `#`. (if `width` or `height` is equal to 0, return an empty string).
  + `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
+ [x] 5\. Detect instance deletion <br/>_**[5-rectangle.py](5-rectangle.py)**_  contains a class `Rectangle` that defines a rectangle by: (based on [`4-rectangle.py`](4-rectangle.py)).
  + Private instance attribute: `width`.
     + Property `def width(self):` to retrieve it.
     + Property setter `def width(self, value):` to set it (`width` must be an integer and greater than or equal to 0).
  + Private instance attribute: `height`.
     + Property `def height(self):` to retrieve it.
     + Property setter `def height(self, value):` to set it (`height` must be an integer and greater than or equal to 0).
  + Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`.
  + Public instance method: `def area(self):` that returns the rectangle area.
  + Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  + `print()` and `str()` should print the rectangle with the character `#`. (if `width` or `height` is equal to 0, return an empty string).
  + `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
  + Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted.
+ [x] 6\. How many instances <br/>_**[6-rectangle.py](6-rectangle.py)**_  contains a class `Rectangle` that defines a rectangle by: (based on [`5-rectangle.py`](5-rectangle.py)).
  + Private instance attribute: `width`.
     + Property `def width(self):` to retrieve it.
     + Property setter `def width(self, value):` to set it (`width` must be an integer and greater than or equal to 0).
  + Private instance attribute: `height`.
     + Property `def height(self):` to retrieve it.
     + Property setter `def height(self, value):` to set it (`height` must be an integer and greater than or equal to 0).
  + Public class attribute `number_of_instances` that is initialized to `0`, incremented by 1 during each new instance instantiation, and decremented by 1 during each instance deletion.
  + Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`.
  + Public instance method: `def area(self):` that returns the rectangle area.
  + Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  + `print()` and `str()` should print the rectangle with the character `#`. (if `width` or `height` is equal to 0, return an empty string).
  + `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
  + Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted.
+ [x] 7\. Change representation <br/>_**[7-rectangle.py](7-rectangle.py)**_  contains a class `Rectangle` that defines a rectangle by: (based on [`6-rectangle.py`](6-rectangle.py)).
  + Private instance attribute: `width`.
     + Property `def width(self):` to retrieve it.
     + Property setter `def width(self, value):` to set it (`width` must be an integer and greater than or equal to 0).
  + Private instance attribute: `height`.
     + Property `def height(self):` to retrieve it.
     + Property setter `def height(self, value):` to set it (`height` must be an integer and greater than or equal to 0).
  + Public class attribute `number_of_instances` that is initialized to `0`, incremented by 1 during each new instance instantiation, and decremented by 1 during each instance deletion.
  + Public class attribute `print_symbol` that is initialized to `#`, used as symbol for string representation and can be any type.
  + Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`.
  + Public instance method: `def area(self):` that returns the rectangle area.
  + Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  + `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`. (if `width` or `height` is equal to 0, return an empty string).
  + `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
  + Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted.
+ [x] 8\. Compare rectangles <br/>_**[8-rectangle.py](8-rectangle.py)**_  contains a class `Rectangle` that defines a rectangle by: (based on [`7-rectangle.py`](7-rectangle.py)).
  + Private instance attribute: `width`.
     + Property `def width(self):` to retrieve it.
     + Property setter `def width(self, value):` to set it (`width` must be an integer and greater than or equal to 0).
  + Private instance attribute: `height`.
     + Property `def height(self):` to retrieve it.
     + Property setter `def height(self, value):` to set it (`height` must be an integer and greater than or equal to 0).
  + Public class attribute `number_of_instances` that is initialized to `0`, incremented by 1 during each new instance instantiation, and decremented by 1 during each instance deletion.
  + Public class attribute `print_symbol` that is initialized to `#`, used as symbol for string representation and can be any type.
  + Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`.
  + Public instance method: `def area(self):` that returns the rectangle area.
  + Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  + `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`. (if `width` or `height` is equal to 0, return an empty string).
  + `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
  + Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted.
  + Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area. Returns `rect_1` if both have the same area value.
+ [x] 9\. A square is a rectangle <br/>_**[9-rectangle.py](9-rectangle.py)**_  contains a class `Rectangle` that defines a rectangle by: (based on [`8-rectangle.py`](8-rectangle.py)).
  + Private instance attribute: `width`.
     + Property `def width(self):` to retrieve it.
     + Property setter `def width(self, value):` to set it (`width` must be an integer and greater than or equal to 0).
  + Private instance attribute: `height`.
     + Property `def height(self):` to retrieve it.
     + Property setter `def height(self, value):` to set it (`height` must be an integer and greater than or equal to 0).
  + Public class attribute `number_of_instances` that is initialized to `0`, incremented by 1 during each new instance instantiation, and decremented by 1 during each instance deletion.
  + Public class attribute `print_symbol` that is initialized to `#`, used as symbol for string representation and can be any type.
  + Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`.
  + Public instance method: `def area(self):` that returns the rectangle area.
  + Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  + `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`. (if `width` or `height` is equal to 0, return an empty string).
  + `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
  + Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted.
  + Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area. Returns `rect_1` if both have the same area value.
  + Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`.
+ [x] 10\. N queens <br/>_**[101-nqueens.py](101-nqueens.py)**_ contains a program that solves the N queens problem.
  + The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.
       + Usage: `./101-nqueens.py N`
            + If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
       + where N must be an integer greater or equal to `4`
            + If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
            + If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
       + The program should print every possible solution to the problem
            + One solution per line
            + Format: see example
            + You don’t have to print the solutions in a specific order
       + You are only allowed to import the `sys` module
  + Info: [Queen, Backtracking](https://en.wikipedia.org/wiki/Backtracking)
