# 0x0B. Python - Input/Output

![Pep8 style](https://img.shields.io/badge/PEP8-style%20guide-green?style=round-square)

## Learning Objectives

* Why Python programming is awesome
* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the `with` statement
* What is `JSON`
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure

## Resources
* [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
* [Dive Into Python 3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf) (until “11.4 Binary Files” (included))
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) (ch. 8 p 180-183 and ch. 14 p 326-333)
* [All about py-file I/O](https://techvidvan.com/tutorials/python-file-read-write/)

## Tasks To Complete

+ [x] 0\. Read file <br/>_**[0-read_file.py](0-read_file.py)**_ contains a function that reads a text file (`UTF8`) and prints it to stdout.
   + Prototype: `def read_file(filename="")`:
   + You must use the `with` statement
   + You don’t need to manage `file permission` or `file doesn't exist` exceptions.
+ [x] 1\. Write to a file <br/>_**[1-write_file.py](1-write_file.py)**_ contains a function that writes a string to a text file (`UTF8`) and returns the number of characters written.
   + Prototype: `def write_file(filename="", text="")`:
   + You must use the `with` statement
   + You don’t need to manage file permission exceptions.
   + Your function should create the file if doesn’t exist.
   + Your function should overwrite the content of the file if it already exists.
+ [x] 2\. Append to a file <br/>_**[2-append_write.py](2-append_write.py)**_ contains a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added.
   + Prototype: `def append_write(filename="", text="")`:
   + If the file doesn’t exist, it should be created
   + You must use the `with` statement
   + You don’t need to manage `file permission` or `file doesn't exist` exceptions.
+ [x] 3\. To JSON string <br/>_**[3-to_json_string.py](3-to_json_string.py)**_ contains a function that returns the JSON representation of an object (string).
   + Prototype: `def to_json_string(my_obj)`:
+ [x] 4\. From JSON string to Object <br/>_**[4-from_json_string.py](4-from_json_string.py)**_ contains a function that returns an object (Python data structure) represented by a JSON string.
   + Prototype: `def from_json_string(my_str)`:
+ [x] 5\. Save Object to a file <br/>_**[5-save_to_json_file.py](5-save_to_json_file.py)**_ contains a function that writes an Object to a text file, using a JSON representation.
   + Prototype: `def save_to_json_file(my_obj, filename)`:
   + You must use the `with` statement
   + You don’t need to manage exceptions if the object can’t be serialized.
   + You don’t need to manage file permission exceptions.
+ [x] 6\. Create object from a JSON file <br/>_**[6-load_from_json_file.py](6-load_from_json_file.py)**_ contains a function that creates an Object from a “JSON file”.
   + Prototype: `def load_from_json_file(filename)`:
   + You must use the `with` statement
   + You don’t need to manage exceptions if the JSON string doesn’t represent an object.
   + You don’t need to manage file permissions / exceptions.
+ [ ] 7\. Load, add, save <br/>_**[7-add_item.py](7-add_item.py)**_ contains a script that adds all arguments to a Python list, and then save them to a file named `add_item.json`.
   + You must use your function `save_to_json_file` from [5-save_to_json_file.py](5-save_to_json_file.py)
   + You must use your function `load_from_json_file` from [6-load_from_json_file.py](6-load_from_json_file.py)
+ [x] 8\. Class to JSON <br/>_**[8-class_to_json.py](8-class_to_json.py)**_ contains a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.
   + Prototype: `def class_to_json(obj)`:
   + `obj` is an instance of a Class
   + All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
+ [x] 9\. Student to JSON <br/>_**[9-student.py](9-student.py)**_ contains a class `Student` that defines a student by:
  + Public instance attributes: `first_name`, `last_name`, and `age`.
  + Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`.
  + Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as [8-class_to_json.py](8-class_to_json.py)).
+ [x] 10\. Student to JSON with filter <br/>_**[10-student.py](10-student.py)**_ contains a class `Student` that defines a student by: (based on [9-student.py](9-student.py)).
  + Public instance attributes: `first_name`, `last_name`, and `age`.
  + Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`.
  + Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as [8-class_to_json.py](8-class_to_json.py)).
    + If `attrs` is a list of strings, only attribute names contained in this list must be retrieved, otherwise all attributes must be retrieved.
+ [x] 11\. Student to disk and reload <br/>_**[11-student.py](11-student.py)**_ contains a class `Student` that defines a student by: (based on [10-student.py](10-student.py)).
  + Public instance attributes: `first_name`, `last_name`, and `age`.
  + Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`.
  + Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as [8-class_to_json.py](8-class_to_json.py)). If `attrs` is a list of strings, only attribute names contained in this list must be retrieved, otherwise all attributes must be retrieved.
  + Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance. `json` is a dictionary whose key-value pairs correspond to the public attribute names and values of the `Student` instance.
+ [x] 12\. Pascal's Triangle <br/>_**[12-pascal_triangle.py](12-pascal_triangle.py)**_ contains a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`.
+ [x] 13\. Search and update <br/>_**[100-append_after.py](100-append_after.py)**_ contains a function that inserts a line of text to a file, after each line containing a specific string.
+ [x] 14\. Log parsing <br/>_**[101-stats.py](101-stats.py)**_ contains a script that reads `stdin` line by line and computes metrics:.
  + Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`.
  + Each 10 lines and after a keyboard interruption (`CTRL + C`), prints those statistics since the beginning according to the following requirements:
    + Total file size: `File size: <total size>`. Where `<total size>` is the sum of all previous `<file size>`.
    + Number of lines by status code. Possible status codes are `200`, `301`, `400`, `401`, `403`, `404`, `405`, and `500`. Format: `<status code>: <number>`. Where `<number>` is the number of times a status code has appeared. The status codes should be printed in ascending order.
