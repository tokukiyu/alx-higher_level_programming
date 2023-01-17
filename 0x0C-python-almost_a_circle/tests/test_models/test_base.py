#!/usr/bin/python3
"""A unit test module for the polygon models.
"""
import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests the Base class and its methods.
    """

    @staticmethod
    def remove_files():
        """Removes the serialized polygon object files
        from the current working directory.
        """
        if os.path.isfile('Base.json'):
            os.unlink('Base.json')
        if os.path.isfile('Rectangle.json'):
            os.unlink('Rectangle.json')
        if os.path.isfile('Square.json'):
            os.unlink('Square.json')
        if os.path.isfile('Base.csv'):
            os.unlink('Base.csv')
        if os.path.isfile('Rectangle.csv'):
            os.unlink('Rectangle.csv')
        if os.path.isfile('Square.csv'):
            os.unlink('Square.csv')

    @staticmethod
    def read_text_file(file_name):
        """Reads the contents of a given file.

        Args:
            file_name (str): The name of the file to read.

        Returns:
            str: The contents of the file if it exists.
        """
        lines = []
        if os.path.isfile(file_name):
            with open(file_name, mode='r') as file:
                for line in file.readlines():
                    lines.append(line)
        return ''.join(lines)

    def test_init(self):
        """Tests the initialization of the Base class.
        """
        id_init = Base().id
        self.assertEqual(id_init + 1, Base().id)
        self.assertEqual('0x10', Base('0x10').id)
        self.assertListEqual([1, 5], Base([1, 5]).id)
        self.assertIsNotNone(Base(None).id)
        self.assertNotEqual(None, Base(None).id)
        self.assertEqual(False, Base(False).id)
        self.assertEqual(True, Base(True).id)
        self.assertEqual(0, Base(0).id)
        self.assertEqual(-10, Base(-10).id)
        self.assertEqual(10, Base(10).id)
        self.assertFalse('nb_objects' in dir(Base))
        self.assertFalse('__nb_objects' in dir(Base))
        # with self.assertRaises(AttributeError):
        #     polygon.__nb_objects += 1
        # with self.assertRaises(AttributeError):
        #     polygon.nb_objects += 1
        with self.assertRaises(TypeError):
            polygon = Base(1, 2)
        with self.assertRaises(OverflowError):
            polygon = Base(int(float('inf')))

    def test_to_json_string(self):
        """Tests the to_json_string method of the Base class.
        """
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{}]), '[{}]')
        self.assertEqual(Base.to_json_string([{'x': 6}]), '[{"x": 6}]')
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_from_json_string(self):
        """Tests the from_json_string static method of the Base class.
        """
        self.assertEqual(Base.from_json_string('null'), None)
        self.assertEqual(Rectangle.from_json_string('34'), 34)
        self.assertEqual(Square.from_json_string('"foo_bar"'), 'foo_bar')
        self.assertEqual(Square.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Square.from_json_string('   '), [])
        self.assertEqual(Rectangle.from_json_string('   \n \t '), [])
        self.assertEqual(
            Base.from_json_string('[-4, 1, 2, 5]'),
            [-4, 1, 2, 5]
        )
        self.assertEqual(
            Rectangle.from_json_string(
                '[{"y": 8, "id": 89, "width": 10, "x": 4, "height": 4}]'
            ),
            [{'id': 89, 'width': 10, 'height': 4, 'x': 4, 'y': 8}]
        )
        self.assertEqual(
            Square.from_json_string(
                '[{"id": 98, "x": 15, "size": 30, "y": 10}]'
            ),
            [{'id': 98, 'size': 30, 'x': 15, 'y': 10}]
        )
        with self.assertRaises(TypeError):
            polygon_list = Base.from_json_string('[{"id": 45, "x": 3', '34')
        with self.assertRaises(TypeError):
            polygon_list = Base.from_json_string('[{"id": 45, "x": 3', None)

    def test_create(self):
        """Tests the create method of the Base class.
        """
        self.assertIsNone(Base.create(**{'id': '89'}))
        self.assertIsNone(Base.create())
        self.assertIsNotNone(Rectangle.create())
        self.assertIsNotNone(Square.create())
        self.assertDictEqual(Rectangle.create(**{
            'id': 89, 'width': 3, 'height': 5,
            'x': 8, 'y': 16
            }).to_dictionary(),
            {'id': 89, 'width': 3, 'height': 5, 'x': 8, 'y': 16}
        )
        self.assertFalse('foo' in dir(Rectangle.create(**{
            'id': None, 'width': 3, 'height': 5,
            'x': 8, 'y': 16, 'foo': 23
        })))
        self.assertDictEqual(Square.create(**{
            'id': 89, 'width': 3, 'height': 5,
            'size': 15, 'x': 8, 'y': 16
            }).to_dictionary(),
            {'id': 89, 'size': 15, 'x': 8, 'y': 16}
        )
        self.assertDictEqual(Square.create(**{
            'id': None, 'width': 13, 'height': 25,
            'x': 8, 'y': 16, 'foo': 34
            }).to_dictionary(), {
            'id': None, 'size': 1,
            'x': 8, 'y': 16,
        })
        self.assertFalse('foo' in dir(Square.create(**{
            'id': None, 'width': 13, 'height': 25,
            'x': 8, 'y': 16, 'foo': 34
        })))
        with self.assertRaises(TypeError):
            Base.create(None)
        with self.assertRaises(TypeError):
            Square.create({'id': 1, 'size': 5})

    def test_update(self):
        """Tests the update function in the Base class.
        """
        polygon = Square(5)
        # region valid arguments
        polygon.update(1)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 5)
        polygon.update(1, 7)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        polygon.update(1, 7, 5)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        polygon.update(1, 7, 5, 2)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, 15)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion
        # region *args with **kwargs
        polygon = Square(5)
        polygon.update(1, size=12)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 5)
        polygon.update(1, size=[12, ])
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 5)
        polygon.update(1, 7, size=12)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        polygon.update(1, 7, size={12, })
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        polygon.update(1, 7, 5, size=12, x=17)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        polygon.update(1, 7, 5, size=12, x='17')
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        polygon.update(1, 7, 5, 2, size=12, x=17, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, size=12, x=17, y=1.8)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, size=12, x=17, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, size=12, x=17, y='18')
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, 15, size=12, x=17, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, 15, size=12, x=17, y=(18, 54))
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None, size=12, x=17, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None, size=None, x={'f': 17}, y=None)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None, size='12', x=1.7, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None, size='12', x=1.7, y=18, bee=12)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion
        # region **kwargs and no *args
        polygon = Square(5)
        id_init = polygon.id
        polygon.update(id='35')
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 5)
        # id has no get/set function
        polygon.update(id=None)
        self.assertEqual(polygon.id, None)
        self.assertEqual(polygon.size, 5)
        polygon.update(size=7, id='35')
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        polygon.update(x=5, size=7, id='35')
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        polygon.update(x=5, size=7, id='35', y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion
        # region update should only update supported attributes
        polygon.update(x=5, size=7, id='35', y=2, foo=63)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        with self.assertRaises(AttributeError):
            print(polygon.foo == 63)
        polygon.update(x=5, width=425, id='35', y=2, foo=63)
        self.assertFalse(polygon.size == 425)
        self.assertFalse(polygon.width == 425)
        self.assertFalse(polygon.height == 425)
        # endregion
        # region update does not recognize width and height
        polygon.update(x=5, size=7, width=35, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, width='35', y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, width=None, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, width=True, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, height=35, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, height='35', y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, height=None, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, height=True, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion
        # region update allows validations to be performed
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size='7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size=b'7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size=True, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size=False, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size=None, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x='7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x=b'7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x=True, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x=False, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x=None, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y='7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y=b'7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y=True, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y=False, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y=None, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(size=0, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(size=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(x=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(y=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        # endregion

    def test_save_to_file(self):
        """Tests the save_to_file function of the Base class.
        """
        # region Base
        TestBase.remove_files()
        Base.save_to_file(None)
        self.assertEqual(TestBase.read_text_file('Base.json'), '[]')
        self.assertFalse(os.path.isfile('Rectangle.json'))
        self.assertFalse(os.path.isfile('Square.json'))
        TestBase.remove_files()
        Base.save_to_file([])
        self.assertEqual(TestBase.read_text_file('Base.json'), '[]')
        self.assertFalse(os.path.isfile('Square.json'))
        self.assertFalse(os.path.isfile('Rectangle.json'))
        with self.assertRaises(AttributeError):
            TestBase.remove_files()
            Base.save_to_file([Base(3), Base(10)])
        TestBase.remove_files()
        Base.save_to_file([Square(3, 0, 0, 1), Square(10, 9, 7, 8)])
        self.assertEqual(TestBase.read_text_file('Base.json'), '[]')
        self.assertFalse(os.path.isfile('Square.json'))
        self.assertFalse(os.path.isfile('Rectangle.json'))
        polygons = [Rectangle(5, 13, 0, 0, 1), Rectangle(10, 2, 9, 7, 8)]
        TestBase.remove_files()
        Base.save_to_file(polygons)
        self.assertEqual(TestBase.read_text_file('Base.json'), '[]')
        self.assertFalse(os.path.isfile('Square.json'))
        self.assertFalse(os.path.isfile('Rectangle.json'))
        polygons = [Square(3, 0, 0, 1), Rectangle(10, 3, 9, 7, 8), Base(2)]
        with self.assertRaises(AttributeError):
            TestBase.remove_files()
            Base.save_to_file(polygons)
        with self.assertRaises(TypeError):
            Base.save_to_file(polygons, polygons)
        with self.assertRaises(TypeError):
            Base.save_to_file()
        # endregion
        # region Rectangle
        polygons = None
        TestBase.remove_files()
        Rectangle.save_to_file(polygons)
        self.assertEqual(TestBase.read_text_file('Rectangle.json'), '[]')
        polygons = []
        TestBase.remove_files()
        Rectangle.save_to_file(polygons)
        self.assertEqual(TestBase.read_text_file('Rectangle.json'), '[]')
        polygons = [Rectangle(3, 5, 0, 0, 1), Rectangle(10, 4, 9, 7, 8)]
        TestBase.remove_files()
        Rectangle.save_to_file(polygons)
        contents = TestBase.read_text_file('Rectangle.json')
        self.assertIn('"id": 1', contents)
        self.assertIn('"width": 3', contents)
        self.assertIn('"height": 5', contents)
        self.assertIn('"x": 0', contents)
        self.assertIn('"y": 0', contents)
        self.assertIn('"id": 8', contents)
        self.assertIn('"width": 10', contents)
        self.assertIn('"height": 4', contents)
        self.assertIn('"x": 9', contents)
        self.assertIn('"y": 7', contents)
        polygons = [Rectangle(3, 5, 0, 0, 1), Base(34), Square(10, 9, 7, 8)]
        TestBase.remove_files()
        Rectangle.save_to_file(polygons)
        contents = TestBase.read_text_file('Rectangle.json')
        self.assertIn('"id": 1', contents)
        self.assertIn('"width": 3', contents)
        self.assertIn('"height": 5', contents)
        self.assertIn('"x": 0', contents)
        self.assertIn('"y": 0', contents)
        self.assertNotIn('"id": 34', contents)
        self.assertNotIn('"id": 8', contents)
        self.assertNotIn('"size": 10', contents)
        self.assertNotIn('"width": 10', contents)
        self.assertNotIn('"height": 10', contents)
        self.assertNotIn('"x": 9', contents)
        self.assertNotIn('"y": 7', contents)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(polygons, polygons)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        # endregion
        # region Square
        polygons = None
        TestBase.remove_files()
        Square.save_to_file(polygons)
        self.assertEqual(TestBase.read_text_file('Square.json'), '[]')
        polygons = []
        TestBase.remove_files()
        Square.save_to_file(polygons)
        self.assertEqual(TestBase.read_text_file('Square.json'), '[]')
        polygons = [Square(3, 0, 0, 1), Square(10, 9, 7, 8)]
        TestBase.remove_files()
        Square.save_to_file(polygons)
        contents = TestBase.read_text_file('Square.json')
        self.assertIn('"id": 1', contents)
        self.assertIn('"size": 3', contents)
        self.assertNotIn('"width": 3', contents)
        self.assertNotIn('"height": 3', contents)
        self.assertIn('"x": 0', contents)
        self.assertIn('"y": 0', contents)
        self.assertIn('"id": 8', contents)
        self.assertIn('"size": 10', contents)
        self.assertNotIn('"width": 10', contents)
        self.assertNotIn('"height": 10', contents)
        self.assertIn('"x": 9', contents)
        self.assertIn('"y": 7', contents)
        polygons = [Square(3, 0, 0, 1), Rectangle(10, 5, 9, 7, 8), Base(11)]
        TestBase.remove_files()
        Square.save_to_file(polygons)
        contents = TestBase.read_text_file('Square.json')
        self.assertIn('"id": 1', contents)
        self.assertIn('"size": 3', contents)
        self.assertNotIn('"width": 3', contents)
        self.assertNotIn('"height": 3', contents)
        self.assertIn('"x": 0', contents)
        self.assertIn('"y": 0', contents)
        self.assertNotIn('"id": 8', contents)
        self.assertNotIn('"size": 10', contents)
        self.assertNotIn('"size": 5', contents)
        self.assertNotIn('"width": 10', contents)
        self.assertNotIn('"height": 5', contents)
        self.assertNotIn('"x": 9', contents)
        self.assertNotIn('"y": 7', contents)
        self.assertNotIn('"id": 11', contents)
        with self.assertRaises(TypeError):
            Square.save_to_file(polygons, polygons)
        with self.assertRaises(TypeError):
            Square.save_to_file()
        # endregion
        TestBase.remove_files()

    def test_load_from_file(self):
        """Tests the load_from_file class method.
        """
        # region Base
        TestBase.remove_files()
        polygons = Base.load_from_file()
        self.assertTrue(len(polygons) == 0)
        polygons_list = [Base(3), Base(10)]
        with self.assertRaises(AttributeError):
            Base.save_to_file(polygons_list)
        with self.assertRaises(TypeError):
            polygons = Base.load_from_file(None)
        with self.assertRaises(TypeError):
            polygons = Base.load_from_file(True)
        with self.assertRaises(TypeError):
            polygons = Base.load_from_file('Base.json')
        # endregion
        # region Rectangle
        TestBase.remove_files()
        polygons = Rectangle.load_from_file()
        self.assertTrue(len(polygons) == 0)
        polygons_list = [Rectangle(3, 17, 0, 0, 1), Rectangle(10, 5, 9, 7, 8)]
        Rectangle.save_to_file(polygons_list)
        polygons = Rectangle.load_from_file()
        self.assertTrue(len(polygons) == len(polygons_list))
        self.assertTrue(
            polygons[0].to_dictionary() == polygons_list[0].to_dictionary() or
            polygons[0].to_dictionary() == polygons_list[1].to_dictionary()
        )
        self.assertTrue(
            polygons[1].to_dictionary() == polygons_list[0].to_dictionary() or
            polygons[1].to_dictionary() == polygons_list[1].to_dictionary()
        )
        with self.assertRaises(TypeError):
            polygons = Rectangle.load_from_file(None)
        with self.assertRaises(TypeError):
            polygons = Rectangle.load_from_file(True)
        with self.assertRaises(TypeError):
            polygons = Rectangle.load_from_file('Rectangle.json')
        # endregion
        # region Square
        TestBase.remove_files()
        polygons = Square.load_from_file()
        self.assertTrue(len(polygons) == 0)
        polygons_list = [Square(3, 0, 0, 1), Square(10, 9, 7, 8)]
        Square.save_to_file(polygons_list)
        polygons = Square.load_from_file()
        self.assertTrue(len(polygons) == len(polygons_list))
        self.assertTrue(
            polygons[0].to_dictionary() == polygons_list[0].to_dictionary() or
            polygons[0].to_dictionary() == polygons_list[1].to_dictionary()
        )
        self.assertTrue(
            polygons[1].to_dictionary() == polygons_list[0].to_dictionary() or
            polygons[1].to_dictionary() == polygons_list[1].to_dictionary()
        )
        with self.assertRaises(TypeError):
            polygons = Square.load_from_file(None)
        with self.assertRaises(TypeError):
            polygons = Square.load_from_file(True)
        with self.assertRaises(TypeError):
            polygons = Square.load_from_file('Square.json')
        # endregion
        TestBase.remove_files()
class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

if __name__ == "__main__":
    unittest.main()
