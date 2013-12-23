import mystuff

mystuff.apple()
print mystuff.tangerine

my = mystuff.MyStuff()
my.apple()
# instance variables are public by default
print my.tangerine

# 3 ways to get things from things
# 1. dict style
# mystuff['apples']
# 2. module style
# mystuff.apples()
# print mystuff.tangerine
# 3. class style
# thing = MyStuff()
# thing.apples()
# print thing.tangerine

happy_bday = mystuff.Song(["Happy birthday to you",
                            "I don't want to get sued",
                            "So I'll stop right there"])

bulls_on_parade = mystuff.Song(["They rally around the family",
    "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
