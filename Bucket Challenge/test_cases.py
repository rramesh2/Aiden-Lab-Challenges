"""
Test cases for bucket_challenge.py

Santiago Garcia Acosta
01/28/2018
Aiden Lab Challenge 1A
"""

import bucket_challenge

# Should return True as 5 + 7 = 12
print bucket_challenge.bucket_challenge([5, 7], 12)

# Should return True as 5 = 5
print bucket_challenge.bucket_challenge([5, 7], 5)

# Should return True as 5 + 7 + 7 + 7 + 7 = 33
print bucket_challenge.bucket_challenge([5, 7], 33)

# Should return False as not possible
print bucket_challenge.bucket_challenge([5, 7], 9)

# Should return True as 2 + 17 = 19
print bucket_challenge.bucket_challenge([2, 9, 17], 19)

# Should return False as negative
print bucket_challenge.bucket_challenge([5, 7], -12)

# Should return True as 0 is always possible
print bucket_challenge.bucket_challenge([5,7], 0)

# Should return True as (400000000 * 5) + (3 * 7) = 2000000021
print bucket_challenge.bucket_challenge([5, 7], 2000000021)
