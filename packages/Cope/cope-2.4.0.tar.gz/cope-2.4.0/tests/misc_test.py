from os.path import join, dirname; import sys; sys.path.append(join(dirname( __file__ ), '..'))
from Cope.misc import *
from Cope.experimental import insert_newlines
import pytest
from unittest.mock import patch, call
import tempfile
import os

# ChatGPT wrote most of these for me

def test_available():
    # def available(*args, null=None, fail_if_none:bool=True) -> list:
    assert available(7, None, 8, 9, None) == [7, 8, 9]
    assert available(-1, 2, 3, -1, 4, -1, null=-1) == [2, 3, 4]
    assert available(1, 2, 3, null=0) == [1, 2, 3]
    assert available('a', 'b', 'c', null='') == ['a', 'b', 'c']
    assert available(10, 20, 30, null=None) == [10, 20, 30]
    assert available(1, 0, 3, null=0) == [1, 3]

def test_only1():
    assert only1(1, null=0) == True
    assert only1('a', 'b', null='') == False
    assert only1(10, 20, 30, null=None) == False
    assert only1(1, 0, 3, null=0) == False
    assert only1(42, null=None) == True

def test_interpret_percentage():
    assert interpret_percentage(0.5) == 0.5
    assert interpret_percentage(75) == 0.75
    assert interpret_percentage(1.25) == 0.0125
    assert interpret_percentage(0.1) == 0.1
    assert interpret_percentage(150) == 1.5

def test_randbool():
    assert randbool() in [True, False]
    assert randbool() in [True, False]
    assert randbool() in [True, False]

def test_close_enough():
    assert close_enough(5, 5, 0) == True
    assert close_enough(10, 8, 2) == True
    assert close_enough(3, 7, 2) == False
    assert close_enough(0, 0, 0) == True
    assert close_enough(1.5, 1.7, 0.3) == True

def test_furthest():
    assert furthest(5, [1, 3, 8, 12, 6]) == 12
    assert furthest(0, [-2, 5, 10, -8, 3]) == 10
    assert furthest(7, [7, 9, 3, 2, 11]) == 2
    assert furthest(3, [2, 4, 6, 8, 10], index=True) == 4
    # assert furthest_index(-5, [-10, -7, -3, -12, -1], index=True) == 2

def test_closest():
    assert closest(5, [1, 3, 8, 12, 6]) == 6
    assert closest(0, [-2, 5, 10, -8, 3]) == -2
    assert closest(7, [7, 9, 3, 2, 11]) == 7
    assert closest(3, [2, 4, 6, 8, 10], index=True) == 0
    assert closest(-5, [-10, -7, -3, -12, -1], index=True) == 1

def test_isPowerOf2():
    assert isPowerOf2(1) == True
    assert isPowerOf2(2) == True
    assert isPowerOf2(8) == True
    assert isPowerOf2(16) == True
    assert isPowerOf2(10) == False
    assert isPowerOf2(0) == False

def test_between():
    assert between(5, 3, 7) == True
    assert between(10, 5, 15) == True
    assert between(3, 1, 5, left_open=True) == True
    assert between(20, 10, 30, right_open=True) == True
    assert between(5, 5, 10) == False
    assert between(5, 5, 10, left_open=True) == True
    assert between(15, 10, 20, left_open=True) == True
    assert between(25, 20, 30, right_open=True) == True
    assert between(30, 20, 30, right_open=True) == True
    assert between(30, 20, 30, right_open=False) == False

def test_insert_str():
    assert insert_str("hello", 2, "123") == "he123lo"
    assert insert_str("python", 0, "java") == "javaython"
    assert insert_str("abc", 3, "XYZ") == "abcXYZ"
    assert insert_str("world", 5, "123") == "world123"
    assert insert_str("", 0, "test") == "test"

def test_constrain():
    assert constrain(5, 0, 10) == 5
    assert constrain(15, 0, 10) == 10
    assert constrain(-5, 0, 10) == 0
    assert constrain(8, 2, 6) == 6
    assert constrain(3, 1, 5) == 3

def test_translate():
    assert translate(5, 0, 10, 20, 40) == 30
    # assert translate(15, 10, 20, 0, 100) == 75
    assert translate(-5, -10, 0, 0, 50) == 25
    # assert translate(8, 2, 6, 0, 10) == 5
    assert translate(3, 1, 5, 10, 20) == 15

def test_frange():
    result = list(frange(1.5, 5.5, 1.0))
    assert result == [1.5, 2.5, 3.5, 4.5]

    result = list(frange(0.1, 0.5, 0.1, accuracy=10))
    assert result == [0.1, 0.2, 0.3, 0.4]

    result = list(frange(2.0, 3.0, 0.2, accuracy=100))
    assert result == [2.0, 2.2, 2.4, 2.6, 2.8]

    result = list(frange(-1.0, 1.0, 0.5, accuracy=1000))
    assert result == [-1.0, -0.5, 0.0, 0.5]

    result = list(frange(0.0, 1.0, 0.1, accuracy=10000))
    assert result == [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    result = list(frange(2.5, 3.5))
    assert result == [2.5,]

# This has been moved to expiremental
def test_insert_newlines():
    return
    input_string = "This is a long string that needs to be split into lines."
    max_line_length = 10
    expected_output = "This is a\nlong\nstring\nthat needs\nto be\nsplit into\nlines."
    output = insert_newlines(input_string, max_line_length)
    assert max(output.splitlines(), key=len) <= max_line_length
    assert output == expected_output

    input_string = "Shorter string."
    max_line_length = 20
    expected_output = "Shorter string."
    output = insert_newlines(input_string, max_line_length)
    assert max(output.splitlines(), key=len) <= max_line_length
    assert output == expected_output

    input_string = "Another example with a really long word: pneumonoultramicroscopicsilicovolcanoconiosis."
    max_line_length = 25
    expected_output = "Another example with\na really long word:\npneumonoultramicroscopi\ncsilicovolcanoconiosis."
    output = insert_newlines(input_string, max_line_length)
    assert max(output.splitlines(), key=len) <= max_line_length
    assert output == expected_output

    input_string = "SingleWord"
    max_line_length = 10
    expected_output = "SingleWord"
    output = insert_newlines(input_string, max_line_length)
    assert max(output.splitlines(), key=len) <= max_line_length
    assert output == expected_output

def test_confirm(monkeypatch):
    # Test case where the user enters 'yes'
    with patch('builtins.input', return_value='yes'):
        assert confirm(prompt='Continue?') == True

    # Test case where the user enters 'no'
    with patch('builtins.input', return_value='no'):
        assert confirm(prompt='Continue?', quit=False, quit_msg='Exiting...') == False

    # Test case where the user enters an invalid input, and return_if_invalid is set to True
    with patch('builtins.input', side_effect=['invalid', 'yes']):
        assert confirm(prompt='Continue?', return_if_invalid=True) == None

    # TODO
    # Test case where the user enters an invalid input, and return_if_invalid is set to False
    # with patch('builtins.input', side_effect=['invalid', 'no']):
    #     with pytest.raises(SystemExit):
    #         confirm(prompt='Continue?', quit=True)

    # Test case where include_YN is set to False
    with patch('builtins.input', return_value='yes'):
        assert confirm(prompt='Continue?', include_YN=False) == True

def test_cat_file():
    # Create a temporary file with content
    content = "This is a test file."
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write(content)

    # Test reading the content of the temporary file
    assert cat_file(temp_file.name) == content

    # Clean up the temporary file
    os.remove(temp_file.name)

def test_umpteenth():
    assert umpteenth(1) == '1st'
    assert umpteenth(2) == '2nd'
    assert umpteenth(3) == '3rd'
    assert umpteenth(4) == '4th'
    assert umpteenth(10) == '10th'
    assert umpteenth(11) == '11th'
    assert umpteenth(12) == '12th'
    assert umpteenth(13) == '13th'
    assert umpteenth(21) == '21st'
    assert umpteenth(22) == '22nd'
    assert umpteenth(23) == '23rd'
    assert umpteenth(24) == '24th'
    assert umpteenth(100) == '100th'
    assert umpteenth(101) == '101st'
    assert umpteenth(112) == '112th'
    assert umpteenth(123) == '123rd'

def test_grade():
    assert grade(50) == 'F'
    assert grade(.63) == 'D'
    assert grade(68) == 'D+'
    # assert grade(70) == 'D+'
    assert grade(75) == 'C'
    assert grade(.78) == 'C+'
    # assert grade(80) == 'C+'
    assert grade(85) == 'B'
    # assert grade(.88) == 'B'
    assert grade(.89) == 'B+'
    # assert grade(92) == 'A-'
    assert grade(99) == 'A'

def test_isiterable():
    assert isiterable([1, 2, 3])
    assert isiterable((1, 2, 3))
    assert isiterable("hello")
    assert isiterable(range(5))
    assert isiterable((x for x in range(5)))
    assert isiterable(iter([1, 2, 3]))
    assert isiterable({'a': 1, 'b': 2})

    assert not isiterable(42)
    assert not isiterable(3.14)
    assert not isiterable(True)
    assert not isiterable(None)

    # Test with include_str set to False
    assert isiterable("hello", include_str=True)
    assert not isiterable("hello", include_str=False)

    # Test with a custom class that implements __iter__
    class CustomIterable:
        def __iter__(self):
            return iter([1, 2, 3])

    assert isiterable(CustomIterable())

def test_ensure_iterable():
    assert ensure_iterable([1, 2, 3]) == [1, 2, 3]
    assert ensure_iterable((1, 2, 3), cast=list) == [1, 2, 3]
    assert ensure_iterable(42, cast=list) == [42]
    assert ensure_iterable("hello") == ["hello", ]
    assert ensure_iterable({"a": 1, "b": 2}, ensure_cast_type=False) == {"a": 1, "b": 2}
    assert ensure_iterable({"a": 1, "b": 2}, ensure_cast_type=True) == ['a', 'b']

    assert ensure_iterable("world", cast=set, ensure_cast_type=False) == {"world"}
    assert ensure_iterable([1, 2, 3], cast=set, ensure_cast_type=True) == {1, 2, 3}
    assert ensure_iterable([1, 2, 3], cast=set, ensure_cast_type=False) == [1, 2, 3]
    assert ensure_iterable(42, cast=set, ensure_cast_type=False) == {42}
    assert ensure_iterable({42}, cast=set, ensure_cast_type=False) == {42}
    assert ensure_iterable({42}, cast=set, ensure_cast_type=True) == {42}
    assert ensure_iterable({"x": 10, "y": 20}, cast=dict, ensure_cast_type=False) == {"x": 10, "y": 20}

def test_ensure_not_iterable():
    assert ensure_not_iterable([1, 2, 3]) == [1, 2, 3]
    assert ensure_not_iterable((1, 2, 3)) == (1, 2, 3)
    assert ensure_not_iterable(42) == 42
    assert ensure_not_iterable("hello") == "hello"
    assert ensure_not_iterable({"a": 1, "b": 2}) == {"a": 1, "b": 2}

    # Test with a generator
    gen = (x for x in range(3))
    assert ensure_not_iterable(gen) == [0, 1, 2]

    # Test with a generator that doesn't self-terminate (avoid passing such generators)
    # infinite_gen = (x for x in itertools.count(3))
    # with pytest.raises(RuntimeError, match="Generator did not self-terminate"):
    #     ensure_not_iterable(infinite_gen)

def test_cp(monkeypatch, capsys):
    from sympy import S

    # TODO Check proper rounding and sigfigs

    with patch('clipboard.copy') as mock_copy:
        # Mocking clipboard.copy function

        # Assume _ has some value in your notebook
        monkeypatch.setitem(__builtins__, '_', 42)

        # Test copying from the variable _
        cp()
        assert mock_copy.call_args == call('42')

        # Test copying a specific value
        cp(3.14159)
        assert mock_copy.call_args == call('3.142')  # Assuming rnd is 3

        # Test copying a string
        cp('Hello, World!')
        assert mock_copy.call_args == call('Hello, World!')

        # TODO
        # Test copying a Sympy expression
        # with patch('sympy.latex') as mock_latex:
            # cp(S('x**2'))
            # assert mock_latex.call_args == call(S('x**2'))
            # assert mock_copy.call_args == call(mock_latex.return_value)

    # TODO
    # Check if the correct print statements are displayed
    # with patch('clipboard.print') as mock_print:
    #     cp(show=True)
    #     captured = capsys.readouterr()
    #     assert 'stringing' in captured.out

    #     cp('test', evalf=False, show=True)
    #     captured = capsys.readouterr()
    #     assert 'latexing' in captured.out

    #     cp(2.71828, rnd=2, show=True)
    #     captured = capsys.readouterr()
    #     assert 'rounding' in captured.out

# Really not sure if you can test this automatically
def test_in_IPython():
    return
    # with patch('sys.modules', {'IPython': None}):
    #     # Mocking the absence of IPython module
    #     assert not in_IPython()

    # with patch('sys.modules', {'IPython': 'mocked_IPython_module'}):
    #     # Mocking the presence of IPython module, but IPython.get_ipython() returns None
    #     with patch('IPython.get_ipython', return_value=None):
    #         assert not in_IPython()

    #     # Mocking the presence of IPython module, and IPython.get_ipython() returns an instance
    #     with patch('IPython.get_ipython', return_value='mocked_instance'):
    #         assert in_IPython(return_instance=True) == 'mocked_instance'
    #         assert in_IPython(return_instance=False) is True

def test_flatten():
    assert flatten([[1, 2],[3, 4],[5, [6,7]], 8, 9], True) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flatten([[1, 2],[3, 4],[5, [6,7]], 8, 9], False) == [1, 2, 3, 4, 5, [6, 7], 8, 9]

def test_invert_dict():
    input_dict = {'a': 1, 'b': 2, 'c': 3}
    inverted_dict = invert_dict(input_dict)

    assert inverted_dict == {1: 'a', 2: 'b', 3: 'c'}

    # Test with repeated values, only one should be kept
    input_dict = {'a': 1, 'b': 2, 'c': 1}
    inverted_dict = invert_dict(input_dict)

    assert inverted_dict == {1: 'c', 2: 'b'}

    # Test with an empty dictionary
    empty_dict = {}
    inverted_empty_dict = invert_dict(empty_dict)

    assert inverted_empty_dict == {}

    # Test with non-hashable values
    input_dict = {'a': [1, 2], 'b': (3, 4), 'c': {'x': 5}}
    with pytest.raises(TypeError):
        invert_dict(input_dict)
