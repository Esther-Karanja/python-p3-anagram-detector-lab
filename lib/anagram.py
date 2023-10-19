# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, my_list):
        for value in my_list:
            if sorted(self.word) == sorted(value):
             return [value]
        else:
            return []
        

        
        