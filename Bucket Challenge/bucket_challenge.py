"""
bucket_challenge.py

Santiago Garcia Acosta
01/27/2018
Challenge 1A for Aiden Lab
"""

import sys
import ast

def bucket_challenge(bucket_sizes, target_value):
    """
    Determines whether the given buckets can be filled to make the desired target
    value, with repetition of the buckets being allow.

    Parameters: bucket_sizes, array with numerical values for the sizes of each
    bucket; target_value, the desired overall amount of liquid to be attained with
    use of the buckets.

    Output: True if the buckets can be used to reach the target value; False otherwise.
    """


print bucket_challenge(ast.literal_eval(sys.argv[1]), ast.literal_eval(sys.argv[2]))