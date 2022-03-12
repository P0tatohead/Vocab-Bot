import wikipedia
from PyDictionary import PyDictionary as pyDict


done = True


def getWiki(command, lines):
    
    try:
        
        wiki = wikipedia.summary(command, lines)
        return (wiki)
    except:
        
        return 0

def getDict(word):
    
    try:
        
        defintion = pyDict.meaning(word)
        return definition
    except:
        
        return 0

def writeToFile(output):
    
    with open("definitions.txt", "a", encoding = "utf-8") as textFile:
        
        print (output)
        print (" ")
        textFile.write(str(output))
        textFile.write("\n")
        textFile.write(" ")
        textFile.write("\n")

def getDef(search):
    
        lines = search.count(" ")
        if (lines <= 2):   
            lines = 2
                
        definition = getDict(search)
        if (definition == 0):    
            definition = getWiki(search, lines)

        writeToFile(definition)

def getVocab():

    with open("vocab.txt", "r") as vocab:

        terms = vocab.readlines()
        print (terms)
        return terms

def giveDefs():

    vocab = getVocab()

    for terms in vocab:
        getDef(terms)

giveDefs()
