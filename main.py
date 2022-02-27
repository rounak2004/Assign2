import random
from Wordle175 import ScrabbleDict

dict_1= ScrabbleDict(5,"scrabble5.txt")

class Wordle175main:
    
    def hidden_word(self):
        hidden_word = random.choice(dict_1.dict.values()) #taking a random word
        return hidden_word
    
    def main_game(self,hidden_word):
        number_of_tries = 0
        Orange = []
        Green = []
        Red = []
        list=[]
        word_list=[]
        while True and number_of_tries>7:
            attempt = ("Attempt"+str(number_of_tries)+": Please enter a 5 five-letter word:")
            if len(attempt)>5:
                print(attempt.upper()+"is too Short")
                
            elif len(attempt)<5:
                print(attempt.upper()+"is too Long")
                
            elif hidden_word !=attempt.upper():
                print(attempt.upper()+"is not a Recognized word")
                
            else:
                number_of_tries=number_of_tries+1
                for i in attempt:
                    j=1
                    if i in hidden_word:
                        Orange.append(i.upper())
                        Orange.sort()
                    elif i == hidden_word[list]:
                        if letter in Green:
                            Green.append(i.upper()+str(j))
                        Green.append(i.upper())
                        Green.sort()
                        list=list+1
                    else:
                        Red.append(i.upper())
                        Red.sort()
                        
            game_round = attempt.upper() + "Green = " + "{" + ",".join(Green)+ "}" + "-" + "Orange = " "{"+ ",".join(OrangeDict)+ "}" + "-" + "Red" + "{" + ",".join(RedDict)+ "}"
            word_list.append(string)
            for i in word_list:
                print(i)
                if number_of_tries == 7 and attempt != hidden_word:
                    print("Sorry you lost. The word is" + str(hidden_word))
                elif attempt == hidden_word:
                    print("Found in " + str(number_of_tries-1) + " attempts. Well Done. The Word is " + str(hidden_word))
                    return False
                word_list.append(attempt)
                        
                        
                        
                        
                        
                            
                    
                    
            
        
    