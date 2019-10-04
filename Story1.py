from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function")

    print("\n")
    Name1 = getWord("Enter a name: ", debug)
    sport1 = getWord("Enter a Sport: ", debug)
    Noun1 = getWord("Enter a Noun: ") 
    Noun2 = getWord("Enter another Noun: ")
    ad1 = getWord("Enter an Adjective: ")
    out = "\n"
    out += "One day me and my friend, " + Name1
    out += " were out playing " + sport1
    out +=" then we saw a " + Noun1
    out +=" it was very " + ad1
    out +=" then my favorite " + Noun2 + "walked out"
    return out

print(Story1())
