#!/usr/bin/python

# Prompt the user to enter the amount of health the fighter has
health = input("Enter the fighters starting health: ")

# Change the type of the variable from a string to an integer
health = int(health)


# Start a while loop to simulate turns. Break out
# of the loop when the fighter reaches 0 health
while True : # True means we would loop forever, unless we break
    
    # print a few newlines just to be pretty
    print ""
    print ""

    # to print health you need to change the type back
    # to a string. health is only a string for this one
    # line since we arent using the = as we did with 
    # health = int(health)
    print "Your health is currently: " + str(health)

    # Prompt user for damage done to fighter, and cast it to an integer 
    # Challenge: How can this process be done in one line?
    damage = input("Enter damage: ")
    damage = int(damage)

    # subtract the damage from health
    # python shorthand for this is health -= damage
    health = health - damage


    # Did the damage kill the fighter?
    # if health is less than or equal to 0 break the loop
    if (health <= 0):
        print "You dead fool!"
        break

    # Challenge: How could we use an "if" statement to print when the fighter 
    # was enraged because he was below 20 health points?

    # Prompt the user for healing done to fighter, and cast it to an integer
    heals = input("Enter heals: ")
    heals = int(heals)

    # add the amount healed to health
    # using the shorthand that means health = health + heals
    health += heals

