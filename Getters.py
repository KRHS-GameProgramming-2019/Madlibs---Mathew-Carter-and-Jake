def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")

    goodInput = False
    
    while not goodInput:
        option = input("please select an option: ")
        option = option.lower()
        
        if {option == "q" or 
            option == "quit" or
            option == "x" or 
            option == "exit"}:
                option = "q"
                goodInput = True
                
        elif {option == "1" or 
            option == "one" or
            option == "story 1" or 
            option == "story1"}:
                option = "1"
                goodInput = True
        
        else:
            print("Please make a valid choice")
            
    return option

def getWord(prompt, debug = False):
    if debug: print("getWord Function")

    goodInput = False
    

                            
    names = ["Matt",
             "Jake",
             "Chris"
                        ] 
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):    
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in sports:
            goodInput = False
            print ("Sorry, I don't know that one.")
        elif not in names:
             print ("they are not in this class")
        
            
    return word

def getSport(prompt, debug = False):
    if debug: print("getSport Function")

    goodInput = False
    sports = ["soccer",
              "football",
              "hockey",
              "wrestling",
              "rugby",
              "chess",
              "esports",
              "ultimate",
                            ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):    
            goodInput = False
            print ("Don't use language like that")
            
    return word
def isSwear(word, debug = False):    
    if debug: print("isSwear Function")
    if word.lower() in swearList:
        return True
    else:
        return False


swearList = ["crap",
             "piss,"
             "ass",
             "bitch",
             "fuck",
             "whore",
             "hoe",
             "slut",
             "fucker",
             "shit",
             "nig",
             "nigger",
             "nigga",
             "cunt",
             "retard",
             "degenerate",
             "bitchass",
             "retard",
             "hore",
             "downie",
             "dick",
             "cock",
             "blackie",
             "vagina",
             "sex",
             
        
]
