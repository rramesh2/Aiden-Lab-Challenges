"""
Test cases for num2wordmap.py

Santiago Garcia Acosta
02/12/2018
Aiden Lab Challenge 1B
"""

import pytest
import num2wordmap

def test1():
    # Simple test

    mapp = {1:'a'}

    assert num2wordmap.conv_num(11111, mapp) == "aaaaa"

def test2():
    # Weirder test

    mapp = {1: 'a', 11: 'b'}

    assert num2wordmap.conv_num(11111, mapp) == "bba"

def test3():
    # Even weirder test

    mapp = {1:'a', 2: 'b', 12: 'l', 11: 'q', 22: 'w'}

    assert num2wordmap.conv_num(121212121212222112121121, mapp) == "llllllwbqblqba"

def test4():
    # Test with actual mapping

    assert num2wordmap.conv_num(1, num2wordmap.mapp) + num2wordmap.conv_num(
        234567891011121314151617, num2wordmap.mapp) == 'subdermatoglyphic'

def test5():
    # Test1 backwards

    mapp = {1: 'a'}

    assert num2wordmap.conv_wrd("aaaaa", mapp) == 11111

def test6():
    # Test2 backwards

    mapp = {1: 'a', 11: 'b'}

    assert num2wordmap.conv_wrd("bba", mapp) == 11111

def test7():
    # Test3 backwards

    mapp = {1: 'a', 2: 'b', 12: 'l', 11: 'q', 22: 'w'}

    assert num2wordmap.conv_wrd("llllllwbqblqba", mapp) == 121212121212222112121121

def test8():
    # Test4 backwards

    assert num2wordmap.conv_wrd('subdermatoglyphic', num2wordmap.mapp) == 1234567891011121314151617

def test9():
    # Weird test with real mapping

    assert num2wordmap.conv_num(100101010, num2wordmap.mapp) == "o-ooo"

def test10():
    # test9 backwards
    
    assert num2wordmap.conv_wrd("o-ooo", num2wordmap.mapp) == 100101010

pytest.main()
