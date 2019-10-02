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
      while not goodInput:
      
        goodInput =False
        if isSwear(word,debug):
            goodInput= False
            print ("Don't use language like that")
     `  else goodInput = True
                        ] 
def getSport(prompt,debug = False
    while not goodInput:
        word = input(prompt)
         sports = ["soccer",
              "football",
              "hockey",
              "wrestling",
              "rugby",
              "chess",
              "esports",
              "ultimate",
        goodInput = False
        if isSwear(word, debug):    
            goodInput = False
            print ("Don't use language like that")
        elif not in sports
            goodInput = False
            print("I don't know that one") 
        else goodInput= True
    return word
    
def getNoun(promt,debug):
    word=input()
    properNoun = ["Matt",
                  "Chris",
                  "Jake"
                            ]
    while not goodInput:
        goodInput =False
        if isSwear(word,debug):
            goodInput= False
            print ("Don't use language like that")
        elif in properNoun:
            goodInput = False\
            print ("that is a proper noun")
    return word
            
            
def isSwear(word, debug = False):    
    if debug: print("isSwear Function")
    if word.lower() in swearList:
        return True
    else:
        return False


swearList = ["crap",
             "piss",
             "shit",
             "fuck",
             "pussy"
             
]
