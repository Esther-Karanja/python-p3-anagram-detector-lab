# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, my_list):
        value =[item for item in my_list]
        if len(self.word) != len(value):
            return []
        else:
            if sorted(self.word) == sorted(value):
                if value == 1:
                    return value
                pass

        
        