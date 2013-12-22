# You can use 'pydoc raw_input' to get documentation from the command line.
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")
address = raw_input("Where do you live? ")

print "So, you are %s old, %s tall, %s heavy, and you live in %s." % (
        age, height, weight, address)
