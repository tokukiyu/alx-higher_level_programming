# 0x0C. Python - Almost a circle
> This project contains some tasks for reviewing everything learned previously in **Python**.

![Pep8 style](https://img.shields.io/badge/PEP8-style%20guide-green?style=round-square)

## Learning Objectives
* What is Unit testing and how to implement it in a large project
* Serialization/Deserialization
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function

## Resources
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Tasks To Complete

+ [x] 0\. If it's not tested it doesn't work <br/>_**[tests/](tests/)**_ contains unit tests for all the files, classes and methods and all Python files are PEP 8 or pycodestyle (version 2.x) validated. <br/> **[0-main.sh](0-main.sh)** an example to run which shows the expected output.
+ [x] 1\. Base class <br/>_**[models/](models/)**_ contains a file ([\_\_init\_\_.py](models/__init__.py)) that makes the folder become a package. <br/> _**[1-main.py](1-main.py)**_ an example to run which shows expected output. <br/> _**[models/base.py](models/base.py)**_ contains a class `Base` that will be the “base” of all other classes in this project:
  + Private class attribute `__nb_objects = 0`.
  + Class constructor: `def __init__(self, id=None):`. The public instance attribute `id` is assigned with this argument's value if the argument's value is not `None`, otherwise `__nb_objects` is incremented and `__nb_objects`'s new value is assigned to the public instance attribute `id`.
+ [x] 2\. First Rectangle <br/>_**[2-main.py](2-main.py)**_ an example to run which shows the expected output
  + Class [Rectangle](models/rectangle.py) inherits from [Base](models/base.py)
  + Private instance attributes, each with its own public getter and setter:
      + __width -> width
      + __height -> height
      + __x -> x
      + __y -> y
  + Class constructor: `def __init__(self, width, height, x=0, y=0, id=None)`:
      + Call the super class with `id` - this super call with use the logic of the `__init__` of the `Base` class
      + Assign each argument `width`, `height`, `x` and `y` to the right attribute
+ [x] 3\. Validate attributes <br/>_**[3-main.py](3-main.py)**_ an example to run which shows the expected output <br/> Update the class [Rectangle](models/rectangle.py) by adding validation of all setter methods and instantiation (`id` excluded).
  + If the input is not an integer, raise the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
  + If `width` or `height` is under or equals `0`, raise the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
  + If `x` or `y` is under `0`, raise the `ValueError` exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`
+ [x] 4\. Area first <br/>_**[4-main.py](4-main.py)**_ an example to run which shows the expected output <br/> Update the class [Rectangle](models/rectangle.py) by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.
+ [x] 5\. Display #0 <br/>_**[5-main.py](5-main.py)**_ an example to run which shows the expected output <br/> Update the class [Rectangle](models/rectangle.py) by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#`. There's no need to handle `x` and `y` here.
+ [x] 6\. \_\_str\_\_ <br/>_**[6-main.py](6-main.py)**_ an example to run which shows the expected output <br/> Update the class [Rectangle](models/rectangle.py) by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`.
+ [x] 7\. Display #1 <br/>_**[7-main.py](7-main.py)**_ an example to run which shows the expected output <br/> Update the class [Rectangle](models/rectangle.py) by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`.
+ [x] 8\. Update #0 <br/>_**[8-main.py](8-main.py)**_ an example to run which shows the expected output <br/> Update the class [Rectangle](models/rectangle.py) by adding the public method `def update(self, *args):` that assigns an argument to each attribute. `args[0] -> id`, `args[1] -> width`, `args[2] -> height`, `args[3] -> x`, and `args[4] -> y`.
+ [x] 9\. Update #1 <br/>_**[9-main.py](9-main.py)**_ an example to run which shows the expected output <br/> Update the class [Rectangle](models/rectangle.py) by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes:
  + `**kwargs` must be skipped if `*args` exists and is not empty.
  + Each key in this dictionary (`**kwargs`) represents an attribute to the instance.
+ [x] 10\. And now, the Square! <br/>_**[10-main.py](10-main.py)**_ an example to run which shows the expected output <br/>_**[models/square.py](models/square.py)**_ contains a class `Square` that inherits from [Rectangle](models/rectangle.py):
  + Public instance attributes: `first_name`, `last_name`, and `age`.
  + Class constructor: `def __init__(self, size, x=0, y=0, id=None):`. Calls the super class with `id`, `x`, `y`, `width`, and `height`.
  + The overloading `__str__` method should return `[Square] (<id>) <x>/<y> - <size>` - in this case, `width` or `height`.
+ [x] 11\. Square size <br/>_**[11-main.py](11-main.py)**_ an example to run which shows the expected output <br/> Update the class [Square](models/square.py) by adding the public getter and setter `size`:
  + The setter should assign (in this order) the `width` and the `height` - with the same value.
  + The setter should have the same value validation as the `Rectangle` for `width` and `height` - No need to change the exception error message (It should be the one from `width`).
+ [x] 12\. Square update <br/>_**[12-main.py](12-main.py)**_ an example to run which shows the expected output <br/> Update the class [Square](models/square.py) by adding the public method `def update(self, *args, **kwargs):` that assigns attributes:
  + `*args` is the list of arguments. `args[0] -> id`, `args[1] -> size`, `args[2] -> x`, and `args[3] -> y`.
  + `**kwargs` must be skipped if `*args` exists and is not empty.
  + Each key in this dictionary (`**kwargs`) represents an attribute to the instance.
+ [x] 13\. Rectangle instance to dictionary representation <br/>_**[13-main.py](13-main.py)**_ an example to run which shows the expected output <br/> Update the class [Rectangle](models/rectangle.py) by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle`. This dictionary must contain `id`, `width`, `height`, `x`, and `y`.
+ [x] 14\. Square instance to dictionary representation <br/>_**[14-main.py](14-main.py)**_ an example to run which shows the expected output <br/> Update the class [Square](models/square.py) by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`. This dictionary must contain `id`, `size`, `x`, and `y`.
+ [x] 15\. Dictionary to JSON string <br/>_**[15-main.py](15-main.py)**_ an example to run which shows the expected output <br/> Update the class [Base](models/base.py) by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`:
  + `list_dictionaries` is a list of dictionaries.
  + If `list_dictionaries` is `None` or empty, return the string: `"[]"`.
+ [x] 16\. JSON string to file <br/>_**[16-main.py](16-main.py)**_ an example to run which shows the expected output <br/> Update the class [Base](models/base.py) by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file:
  + `list_objs` is a list of instances who inherit from `Base` - example: list of `Rectangle`.
  + If `list_objs` is `None`, save an empty list.
  + The filename must be: `<Class name>.json` - example: `Rectangle.json`.
  + You must use the static method `to_json_string`.
  + You must overwrite the file if it already exists.
+ [x] 17\. JSON string to dictionary <br/>_**[17-main.py](17-main.py)**_ an example to run which shows the expected output <br/> Update the class [Base](models/base.py) by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`:
  + `json_string` is a string representing a list of dictionaries.
  + If `json_string` is `None` or empty, return an empty list.
+ [x] 18\. Dictionary to Instance <br/>_**[18-main.py](18-main.py)**_ an example to run which shows the expected output <br/> Update the class [Base](models/base.py) by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set:
  + You must use the method `def update(self, *args, **kwargs)`.
  + `**dictionary` must be used as `**kwargs` of the method `update`.
  + You are not allowed to use `eval`.
+ [x] 19\. File to Instance <br/>_**[19-main.py](19-main.py)**_ an example to run which shows the expected output <br/> Update the class [Base](models/base.py) by adding the class method `def load_from_file(cls):` that returns a list of instances:
  + The filename must be: `<Class name>.json` - example: `Rectangle.json`.
  + If the file doesn’t exist, return an empty list.
  + The type of these instances depends on `cls` (current class using this method).
  + You must use the previously implemented `from_json_string` and `create` methods.
+ [x] 20\. JSON ok, but CSV? <br/>_**[20-main.py](20-main.py)**_ an example to run which shows the expected output <br/> Update the class [Base](models/base.py) by adding the class methods `def save_to_file_csv(cls, list_objs):` and `def load_from_file_csv(cls):` that serializes and deserializes in CSV:
  + The filename must be: `<Class name>.csv` - example: `Rectangle.csv`.
  + Has the same behavior as the JSON serialization/deserialization
  + Format of the CSV:
    + Rectangle: `<id>,<width>,<height>,<x>,<y>`.
    + Square: `<id>,<size>,<x>,<y>`.
+ [x] 21\. Let's draw it <br/>_**[21-main.py](21-main.py)**_ an example to run which shows the expected output <br/> Update the class [Base](models/base.py) by adding the static method `def draw(list_rectangles, list_squares):` that opens a window and draws all the `Rectangles` and `Squares`:
  + You must use the [Turtle graphics module](https://docs.python.org/3.0/library/turtle.html).
  + To install it: `sudo apt-get install python3-tk`
  + To make the GUI available outside your vagrant machine, add this line in your Vagrantfile: `config.ssh.forward_x11 = true`
  + No constraints for color, shape etc… be creative!
  + Uncommented line in `/etc/ssh/ssh_config` that said `# ForwardX11 no` and change `no` to `yes`.
  + Then added line `config.ssh.forward_agent = true` to my Vagrantfile in addition to `config.ssh.forward_x11 = true`.
  + Halted my vm with `vagrant halt` and started it back up with `vagrant up --provision` then `vagrant ssh`
  + If you get an error that looks like `/usr/bin/xauth: timeout in locking authority file /home/vagrant/.Xauthority`, then enter `rm .Xauthority` (you may have to `sudo`).
  + Logout and restart the vm with `vagrant up --provision`
  + Test with `xeyes`. If Xquartz is installed on the Mac OS it should open in an Xquartz window.
