import wikipedia
from PyDictionary import PyDictionary as pyDict


done = True

#The getWiki() function uses the wikipedia library to get the definition of the string input
#Later in the getDef() function, the number of spaces in the term gets the number of lines form the summary (i know i'm so smart §(*￣▽￣*)§)
def getWiki(command, lines):
    
    try:
        
        wiki = wikipedia.summary(command, lines)
        return (wiki)
    except:
        
        return 0

#The getDict function uses the PyDictionary libtary to get the definition of the string input
def getDict(word):
    
    try:
        
        definition = pyDict.meaning(word)
        return definition
    except:
        
        return 0

#Pretty simple, just uses the open(function) and prints the inputed string into the defintions.txt file
def writeToFile(output):
    
    with open("definitions.txt", "a", encoding = "utf-8") as textFile:
        
        print (output)
        print (" ")
        textFile.write(str(output))
        textFile.write("\n")
        textFile.write(" ")
        textFile.write("\n")

#The getDef() functions takes a string input and outputs the defintion
def getDef(search):
    
        lines = search.count(" ")
        if (lines <= 2):   
            lines = 2
                
        definition = getDict(search)
        if (definition == 0):    
            definition = getWiki(search, lines)

        writeToFile(definition)

#Using the open() functions, the getVocab() function downloads all the vocab into a list and outputs it
def getVocab():

    with open("vocab.txt", "r") as vocab:

        terms = vocab.readlines()
        print (terms)
        return terms

#final function that get the list from getVocab and inputs into the getDef() functions
def giveDefs():

    vocab = getVocab()

    for terms in vocab:
        getDef(terms)

giveDefs()
