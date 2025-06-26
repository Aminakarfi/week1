import random

from Dog import Dog as dog

class PetDog(dog):
        def __init__(self, name, age, weight, trained=True):
            super().__init__(name, age, weight)
            self.trained = trained

        def train(self):
            print(self.bark())
            self.trained = True
        
        def play(self,*args):
            names = [self.name] + [dog.name for dog in args]
            print(f"{', '.join(names)}")

        def do_a_trick(self):
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            
            if self.trained:
                trick = random.choice(tricks)
                print(f"{self.name} {trick}")
            else:
                print(f"{self.name} is not trained yet!")



dog1 = PetDog("Max", 3, 10)
dog2 = PetDog("Luna", 2, 7)
dog3 = PetDog("Rocky", 4, 12)

dog1.train()
dog1.play(dog2, dog3)
dog1.do_a_trick()
