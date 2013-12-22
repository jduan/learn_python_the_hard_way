name = 'Zed A. Shaw'
age = 35
height = 74
height_centimeters = height * 2.54
weight = 180
weight_kilos = weight * 0.9 / 2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %0.2f centimeters tall." % height_centimeters
print "He's %d pounds heavy." % weight
print "He's %0.2f kilos heavy." % weight_kilos
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
        age, height, weight, age + height + weight)
