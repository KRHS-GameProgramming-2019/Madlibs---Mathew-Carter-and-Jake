from Getters import*

def Story2(debug = False):
    if debug: print("Story2 Function")
    
    print("/n")
    animalName1 = getWord("Enter a cat's name: ", debug)
    toyName1 = getWord("Enter a name of a toy: ", debug)
    speciesName1 = getWord("Enter a kind of species: ", debug)
    personName1 = getWord("Enter a name of a person: ", debug)
    jobName1 = getWord("Enter in a specific job: ", debug)
    townName1 = getWord("Enter a name of a town: ", debug)
    stateName1 = getWord("Enter a name of a state: ", debug)
    activityName1 = getWord("Enter in an activity: ", debug)
    activityName2 = getWord("Enter in a second activity: ", debug)
    activityName3 = getWord("Enter in a third activity: ", debug)

    out = "/n"
    out += "There was a cat named, " + animalName1
    out += "He is playing a fun toy. The toy that he is playing with is a, " + toyName1
    out += "He is part of a known life species, " + speciesName1
    out += "A person takes care of, " + animalName1 + "in their own household."
    out += "The person is, " + personName1

    out += personName1 + "is a good, well kinded person."
    out += "He is a, " + jobName1 + ", working in his homwtown of, " + townName1
    out += "The town is in the state of, " + stateName1
    out += "He lives alone in a one story house all to himself and with his cat, " + animalName1
    out += "During his days off, he does various activities throughout his day, such as, " + activityName1 + "," activityName2 ", and, " + activityName3
    