class ScrabbleDict:
    
    def __init__(self, size, filename):
        
        self.dict = {}
        file= open(filename,'r')
        for i in file:
            keys_dict = i.replace("\n","")
            if len(keys_dict) == size:
                self.dict[keys_dict] = keys_dict
                
    def check(self,word):
        
        if word in self.dict.values():
            return True
        else:
            return False
        
    def getSize(self):
        
        return (len(self.dict.values()))
    
    def getWords(self,letter):
        
        sorted_list = []
        for i in self.dict.values():
            if letter in i[0]:
                sorted_list.append(i)
        sorted_list.sort()
        return sorted_list
    
    def getWordSize(self):
        for k in self.dict.values():
            return len(k)
        
if __name__ =="__main__":
    Test_Scrabble= ScrabbleDict(5,"scrabble5.txt")
    print(Test_Scrabble.check("zymes"))
    print(Test_Scrabble.getSize())
    print(Test_Scrabble.getWords("z"))
    print(Test_Scrabble.getWordSize())