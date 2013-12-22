# import the argv feature from module sys
from sys import argv

# unpack argv into 2 variables
script, filename = argv

# open a file
txt = open(filename)

print "Here's your file %r:" % filename
# read file
print txt.read()

print "Type the filename again:"
# get user input
file_again = raw_input("> ")

txt_again = open(file_again).read()

print txt_again
