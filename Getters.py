def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")

    goodInput = False
    
    while not goodInput:
        option = input("please select an option: ")
        option = option.lower()
        goodInput=False
        if(option == "q" or 
            option == "quit" or
            option == "x" or 
            option == "exit"):
                option = "q"
                goodInput = True
                
        elif (option == "1" or 
            option == "one" or
            option == "story 1" or 
            option == "story1"):
                option = "1"
                goodInput = True
        
        else:
            print("Please make a valid choice")
            
    return option

def getWord(prompt, debug = False):
    if debug: print("getWord Function")
    word = input(prompt)
    goodInput = False
    
    while not goodInput:
        goodInput =False
        if isSwear(word,debug):
            goodInput= False
            print ("Don't use language like that")
            exit()
        else: 
            goodInput= True
    return word

def getSport(prompt,debug = False):
    
    sports= ["soccer",
            "football",
            "hockey",
            "wrestling",
            "rugby",
            "chess",
            "esports",
            "ultimate",
                            ]
    goodInput=False
    while not goodInput:
        word = input(prompt)
        goodInput = False
        if isSwear(word, debug):    
            goodInput = False
            print ("Don't use language like that")
            exit()
        elif word.lower() not in sports:
            goodInput = False
            print ("Sorry, I don't know that one.")
        else:
            goodInput = True
            
    return word
    
def getFood (prompt,debug):
    word = input(prompt)
    goodInput = False
    Food= ["bacon",
           "pizza",
           "pasta",
           "burgers",
           "eggs"
                        ]
    while not goodInput:
        if isSwear(word,debug):
            goodInput= False
            print ("Don't use language like that")
            exit()
        elif word=="Food":
            print("you have succeeded in mooing")
            goodInput=True
        elif word.lower() not in Food:
            print("I have not heard of that before")
            goodInput=True
            
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
             "motherfucker",
             "pussy",
             "s'wit",
             "n'wah"
             
        
]
