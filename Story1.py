from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function")

    print("\n")
    friendName1 = getName("Enter a name: ", debug)
    sport1 = getSport("Enter a Sport: ", debug)
    Noun1 = getNoun("Enter a Noun") 
    out = "\n"
    out += "One day me and my friend, " + Name1
    out += " were out playing " + sport1
    out +="then we saw a " + Noun1
    out +=" it was very " + ad1

    return out
