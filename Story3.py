from Getters import *

def Story3(debug = False):
    if debug: print("you are in debug")
    
    
    print("\n")
    Noun1 = getWord("Enter a noun: ")
    Name1 = getWord("Enter a name: ")
    Verb1 = getWord("Enter a verb: ")
    Food1 = Food("Enter a Food: ")
    Noun2 = getWord("Enter a noun: ")
    Sport1 = getSport("Enter a sport: ")
    Place1 = getWord("Enter a place: ")
    Person1 = getWord("Enter a name: ")
    adj1 = getWord("Enter an adjective: ")
    out = "/n"
    out += "One day me and my dog," +Name1
    out += " went " +Verb1 + "ing" 
    out += " then we found a " + Noun1
    out += "on the doorway of the " +  Place1 + "."
    out += " Then me and my dog ate some " +Food1
    out += " I was given a " +Noun2 + " by "  + Person1 + " while they were playing " + Sport1 
    out += " that was a " +adj1 + " day."
