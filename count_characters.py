'''
<Name>, <Grade> <Course>
Frequency Analysis

This program reads a text file from a path given on the command line and counts
the letters and numbers in the text file. Letters are converted to upper
case. Then, it prints a histogram in reverse order of frequency with each
line containing frequency, character, and percentage of occurence.
'''

import sys
import os

# check for the correct usage (having one text file path argument)
if len(sys.argv) != 2:
    print("usage: py count_characters.py <text file>", file=sys.stderr)
    sys.exit(1)

# initialze fname to the file name passed in as first argument
fname = sys.argv[1]

# check that the file exists
if not os.path.isfile(fname):
    print(f"no such file: {fname}", file=sys.stderr)
    sys.exit(1)

# open the text file and process it
with open(fname) as fh:
    # REPLACE THE FOLLOWING LINES WITH YOUR OWN CODE
    # This reads the first 1K bytes from the file.
    txt = fh.read(1000)
    print(txt)