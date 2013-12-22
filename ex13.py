from sys import argv
import sys

length = len(argv) - 1

if length > 3:
    print "I only need 3 command line arguments"
    sys.exit()
elif length < 3:
    missing_args = 3 - length
    print "I need %d more arguments" % missing_args
    for x in range(0, missing_args):
        argv.append( raw_input())

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third
