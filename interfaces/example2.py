import random

class LottoGenerator:
    def __init__(self, maxi):
        self.maxi = maxi
        self.current_number = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_number <= self.maxi:
            self.current_number +=1
            return random.randint(1,25)
        else:
            raise StopIteration
        
lotto_generator = LottoGenerator(10)
for number in lotto_generator:
    print(number)