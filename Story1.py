from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function")

    print("\n")
    Name1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a Sport: ", debug)
    Noun1 = getWord("Enter a Noun: ") 
    Noun2 = getWord("Enter another Noun: ")
    ad1 = getWord("Enter an Adjective: ")
    Verb1 = getWord("Enter a Verb: ")
    Food1 = Food("Enter a food: ")

    out = "\n"
    out += "One day me and my friend, " + Name1
    out += " were out playing " + sport1
    out +=" then we saw a " + Noun1
    out +=" it was very " + ad1
    out +=" then my favorite " + Noun2 + "walked out"
    out +=" it began to " + Verb1 + " " 
=======
    Food1 = getFood("Enter a food: ")
    out = "\n"
    out += "One day me and my friend, " + Name1
    out += " were out playing " + sport1
    out +=" then we saw a " + Noun1 + ","
    out +=" it was very " + ad1 + "."
    out +=" then my favorite " + Noun2 + " walked out"
    out +=" it began to " + Verb1 + " " 
    out +="then we ate some " + Food1
>>>>>>> origin/master
    return out

