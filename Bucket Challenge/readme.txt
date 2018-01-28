----bucket_challenge.py----

--Command Line Arguments--
For passing command-line arguments, requires the array argument to be a string, so that, if one wanted to pass in the argument [1, 2, 3] for the bucket sizes and 2 for the target size, one would have to use:

    python bucket_challenge.py "[1, 2, 3]" 2

--Additional Notes--
Note that the implementation for this question uses a recursive method which, although conditionals were placed to avoid such a possibility, could lead to a stack overflow (or python's integrated recursion limit) for very large values. I have tested it on some very large values but to do so on all is clearly impossible. Hopefully this is never issue.

Function runs on python 2.7
