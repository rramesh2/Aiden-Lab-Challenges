"""
bucket_challenge.py

Santiago Garcia Acosta
01/27/2018
Challenge 1A for Aiden Lab
"""

import sys
import ast

# In the case of the need for more recursive calls
sys.setrecursionlimit(4000)

def bucket_challenge(bucket_sizes, target_value):
    """
    Determines whether the given buckets can be filled to make the desired target
    value, with repetition of the buckets being allowed.

    Parameters: bucket_sizes, array with numerical values for the sizes of each
    bucket; target_value, the desired overall amount of liquid to be attained with
    use of the buckets.

    Output: True if the buckets can be used to reach the target value; False otherwise.
    """

    if [bucket for bucket in bucket_sizes if target_value % bucket == 0]:
        # Base case for if target value is a multiple of any bucket

        return True

    elif target_value < 0:

        return False

    else:
        # Recursive case for if target_value > bucket_sizes for all buckets

        for bucket in bucket_sizes:
            # Recursion through subtraction of target_value by bucket size

            return bool(bucket_challenge(bucket_sizes, target_value - bucket))


print bucket_challenge(ast.literal_eval(sys.argv[1]), ast.literal_eval(sys.argv[2]))
