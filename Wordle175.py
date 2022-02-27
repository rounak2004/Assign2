def main():
    Test_Scrabble= ScrabbleDict(5,"scrabble5.txt")
    
    print(Test_Scrabble.check('zymes'))
    
    print(Test_Scrabble.getSize())
    
    print(Test_Scrabble.getWords('z'))
    
    print(Test_Scrabble.getWordSize())             
   
class ScrabbleDict:
    
    def __init__(self, size, filename):
        
        self.dict = {}
        file= open(filename,'r')      #initializes a dictionary using the content of the file specified by filename
        for i in file:
            keys_dict = i.replace('\n','')
            if len(keys_dict) == size:
                self.dict[keys_dict] = keys_dict
                
    def check(self,word):
        
        if word in self.dict.values():
            return True        #returns True if word is in the dictionary
        else:
            return False       #returns False if word is not in the dictionary
        
    def getSize(self):
        
        return (len(self.dict.values()))  #returns the number of words in the dictionary
    
    def getWords(self,letter):
        
        sorted_list = []
        for i in self.dict.values():
            if letter in i[0]:
                sorted_list.append(i)
        sorted_list.sort()
        return sorted_list    #returns a sorted list of words in the dictionary starting with the character letter.
    
    def getWordSize(self):
        for k in self.dict.values():
            return len(k)   #returns the length of the words stored in the dictionary. This is the value size provided when building the dictionary.

if __name__ =="__main__":
    main()
