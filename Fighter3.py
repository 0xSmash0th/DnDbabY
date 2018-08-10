#!/usr/bin/python

""" 
Here we are using a class, a perfect analogy for D&D. 
A class is a generic template of a charater like an 
empty character sheet.
It becomes a object when you fill out the 
sheet and make a character, or what we call an object.
Like defined functions, it must be placed before the code
it is used in.
"""
# Tell python what a generic Fighter is
class Fighter:
    # the initialization function is what you 
    # use to fill out your character sheet
    # The key word self makes the class work on the attributes 
    # of one particular object
    def __init__(self, health):
        # now when you initialize the object and give
        # it some health the health will be asigned to
        # this one object or character
        self.health = health

    # We are now giving the fighter thing he can do
    # Like take damage or heals
    # When you define a function for a class they are
    # called methods. So the fighter class has
    # a takeDamage method and a takeHeals method

    # Notice that we dont have the return 
    # on these methods
    # that is because the health value is kept
    # inside the object, that is, health is an
    # attribute of the object
    def takeDamage(self):
        damage = input("Enter damage: ")
        damage = int(damage)
        self.health -= damage

    def takeHeals(self):
        heals = input("Enter heals: ")
        heals = int(heals)
        self.health += heals


## Here is where we started before
health = input("Enter the fighters starting health: ")

health = int(health)

# Initialize the fighter, lets call him smashkins
# Challenge: Can we make a second fighter using this
# same templet? Say smashkels? Can we put them in the
# loop together?

smashkins = Fighter(health)

# now that we are using a fighter class our loop looks
# super clean!
while True : 
    
    print ""
    print ""

    # Access smashkins health attribute
    print "Your health is currently: " + str(smashkins.health)

    # Let smashkins takeDamage ability a.k.a method 
    # do the work
    smashkins.takeDamage()

    if (smashkins.health <= 0):
        print "You dead fool!"
        break

    
    smashkins.takeHeals()


