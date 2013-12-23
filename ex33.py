def build_list(upper_bound, step = 1):
    i = 0
    numbers = []
    while i < upper_bound:
        print "At the top i is %d" % i
        numbers.append(i)

        i += step
        print "Numbers now: %r" % numbers
        print "At the bottom i is %d" % i

    return numbers

upper_bound = int(raw_input("What's the upper bound of the list you want to build? "))
step = int(raw_input("And step? "))
numbers = build_list(upper_bound, step)

print "The numbers:"

for num in numbers:
    print num
