#!/usr/bin/python

""" 
Here we use definitions a.k.a defined functions
to do our health calculations
Definitions have to be defined above the first place 
you use them.
"""

def takeDamage(health):
    # Even though the argument is named health it could be 'x'
    # as long as we replace all the health variables in this definition
    # with x. It only matters what we return in the end.
    damage = input("Enter damage: ")
    damage = int(damage)

    health = health - damage

    return health

def takeHeals(health):
    heals = input("Enter heals: ")
    heals = int(heals)

    health += heals

    return health


## Here is where we started before
health = input("Enter the fighters starting health: ")

health = int(health)


# now that we are using defined functions our loop looks
# much cleaner
while True : 
    
    print ""
    print ""

    print "Your health is currently: " + str(health)


    # Give our function the current health
    # Let takeDamage do the work, 
    # and we get our new health value back!
    health = takeDamage(health)

    if (health <= 0):
        print "You dead fool!"
        break

    health = takeHeals(health)


