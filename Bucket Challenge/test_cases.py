"""
Test cases for bucket_challenge.py

Santiago Garcia Acosta
01/28/2018
Aiden Lab Challenge 1A
"""

import pytest
from bucket_challenge import bucket_challenge

def test1():
    # 5 + 7 = 12
    assert bucket_challenge([5, 7], 12)

def test2():
    # 5 = 5
    assert bucket_challenge([5, 7], 5)

def test3():
# 5 + 7 + 7 + 7 + 7 = 33
    assert bucket_challenge([5, 7], 33)

def test4():
# not possible
    assert not bucket_challenge([5, 7], 9)

def test5():
# 2 + 17 = 19
    assert bucket_challenge([2, 9, 17], 19)

def test6():
# negative
    assert not bucket_challenge([5, 7], -12)

def test7():
# 0 is always possible
    assert bucket_challenge([5, 7], 0)

def test8():
# (400000000 * 5) + (3 * 7) = 2000000021
    assert bucket_challenge([5, 7], 2000000021)

pytest.main()
