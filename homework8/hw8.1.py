#Homework 8.1
#Oct. 27, 2020

class Animal:
    def __init__(self, type):
        self.type = type
        self.statement = "I will give you 3 hints, guess what animal I am!!"
        self.end = False

############################################################################################
    def elephantHints(self):
        while self.end != True:
            print("Hint 1: I have exceptional memory")
            self.end = self.guessCheck(type)
            if self.end != True:
                print("\nNope, try again!\n"  \
                    "Hint 2: I am the largest land-living mammal in the world")
                self.end = self.guessCheck(type)

                if self.end != True:
                    print("\nNot quite, try again!\n"  \
                        "Hint 3: I drink water from a trunk")
                    self.guessCheck(type)
                else:
                    print("So close! The answer is: elephant")
                    self.end = True
                    continue
            else:
                continue

############################################################################################
    def tigerHints(self):
        while self.end != True:
            print("Hint 1: I am the biggest cat")
            self.end = self.guessCheck(type)
            if self.end != True:
                print("\nNope, try again!\n"  \
                    "Hint 2: I come in black and white or orange and black")
                self.end = self.guessCheck(type)

                if self.end != True:
                    print("\nNot quite, try again!\n"  \
                        "Hint 3: My stripes can be seen on my skin")
                    self.guessCheck(type)
                else:
                    print("Sorry, no more hints! The answer is: tiger")
                    self.end = True
                    continue
            else:
                continue

###############################################################################################
    def batHints(self):
        while self.end != True:
            print("Hint 1: I use echo-location")
            self.end = self.guessCheck(type)
            if self.end != True:
                print("\nNope, try again!\n"  \
                    "Hint 2: I can fly")
                self.end = self.guessCheck(type)

                if self.end != True:
                    print("\nNot quite, try again!\n"  \
                        "Hint 3: I see very well in the dark")
                    self.guessCheck(type)
                else:
                    print("That was your last hint. The answer is: bat")
                    self.end = True
                    continue
            else:
                continue

################################################################################################
    def guess_who(self):
        print(self.statement)
        if self.type == "elephant":
            self.elephantHints()
        elif type == "tiger":
            self.tigerHints()
        elif type == "bat":
            self.batHints()

 ###############################################################################################   
    def guessCheck(self, type):
        guess = input("Who am I?:   ")
        if self.type == "elephant" and guess == "elephant":
            print("Yes!! I'm an elephant!")
            return True
        elif self.type == "tiger" and guess == "tiger":
            print("You got it, I'm a tiger!!")
            return True
        else:
            print("Alright!! I'm a bat!")
            return True

   
#################################################################################################
def main(): 
    #object creations
    e = Animal("elephant")
    t = Animal("tiger")
    b = Animal("bat")

    e.guess_who()
    t.guess_who()
    b.guess_who()

#################################################################################################
main()