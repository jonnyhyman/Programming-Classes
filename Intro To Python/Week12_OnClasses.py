

"""
    ON: Classes / "Classifications" (but don't call them that)

    Classes are groups of similar things. For example, fruits...
"""

class Fruit:

    seeds = True
    sweet = True
    sour  = None  # not yet known (some fruits are, some fruits arent!)
    hard  = None
    soft  = None

    def __init__(self, sour = None, soft = None):
        # this runs when we run " apple = Fruit(...) "

        if soft:
            self.hard = False



# Lets create.... An apple!!
apple = Fruit(sour = True, soft = False)

print('Apples have seeds:', apple.seeds)
print('Apples are sour  :', apple.sour)
print('Apples are hard  :', apple.hard)

apple.sour = False  # we can change internal things from the outside too!

print('Apples are sour:', apple.sour)

# -------- This is great and all, but there are so many kinds of fruit!
# How could we possibly describe them all?
# ... How about this:

# Apples are a KIND of fruit!
class Apple(Fruit):  # (Fruit) here says that Apple INHERITS from Fruit!

    def __init__(self):

        # This SUPER command is magical...
        # It runs the __init__ function of the PARENT class (the inherited one)
        super().__init__(sour = True, hard = True)
        # Notice how that is a lot like calling Fruit(sour=True, hard=True)
        # .. That's because IT IS THE SAME THING WOAH

    def __str__(self):
        # This magical "dunder" function allows you to CUSTOM PRINT

        if self.hard:
            softness = 'hard'

        else:
            softness = 'soft'

        if self.sour:
            sourness = 'sour'
        else:
            sourness = 'not that sour'

        return "Apple which is " + softness + ' and ' + sourness

""" -------------------------- CHALLENGE TIME! -------------------------- """

""" Write a vegetable class, or some other class of your choosing that is
    slightly more interesting than fruits and vegetables... :) """
