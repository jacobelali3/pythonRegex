import re
from os import system


def begin():
    
    answer = input("1. Match First and Last Word\n2. Find number of matches in all phrases\n3. add phrase to phrases\n4. Show all phrases\n5. Quit\n")
    
    if answer == "1":
        user.matchWord()
        begin()
    elif answer == "2":
        user.numberOfMatches()
        begin()
    elif answer == "3":
        user.addSentences()
        begin()
    elif answer == "4":
        user.showSentences()
        begin()
    elif answer == "5":
        return
    else:
        print("Please enter a valid number\n")
        return

   



class nameSearch:
    def __init__(self, word, sentences = []):
       self.word = word
       self.sentences = sentences
       self.sentences = ["I work at Income Energy", "I love my job", "I feel like im out of energy"]
       

    #Create an object to add sentences
    def addSentences(self):
            self.sentences.append(input("Enter a sentence\n"))
      

    #Create an object to match sentences
    def matchWord(self):
        newWord = self.word
        newMatchWord = "^" + newWord + ".*" + newWord + "$"
        for sentence in self.sentences:
            
         if re.search(newMatchWord, sentence):
             print("Word matches!\n")
         else:
    
             print("Words don't match\n")
    
    #Create object to count number of matches
    def numberOfMatches(self):
    
        numberOfMatches = 0
        for currentSentence in self.sentences:
            numberOfMatches += len(re.findall( self.word, currentSentence))
            
        print("Your exact string has matched: " + str(numberOfMatches) + " times\n")
    
    #Create object to show all sentences
    def showSentences(self):
        print(self.sentences)

#initialize the user and their phrase
userWord = input("Enter your phrase:\n")
userSentence =[]
user = nameSearch(userWord,userSentence)  
begin()        

        


        



        
            
        










    
  