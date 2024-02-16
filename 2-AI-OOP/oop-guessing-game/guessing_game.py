class GuessingGame:

    def __init__(self, answer):
        self.answer = answer
        self.guess_num = 0

    def guess(self, user_guess):
        self.guess_num = user_guess
        if user_guess > self.answer:
            return "high"
        elif user_guess < self.answer:
            return "low"
        elif user_guess == self.answer:
            return "correct"

    def solved(self):
        if self.answer == self.guess_num:
            return True
        else:
            return False

        

# game = GuessingGame(10)
# print(game.guess(20))
# print(game.solved())
# print(game.guess(5))
# print(game.solved())
# print(game.guess(10))
# print(game.solved())


import random

# class GuessingGame:

#     def __init__(self, answer):
#         self.answer = answer
#         self.guess_num = "This was your first guess"
#         # self.last_result = 
    
#     def your_last_guess(self):
#         return "Your last guess was" + self.guess_num

#     def guess(self):
#         user_guess = input("Enter your guess: ")
#         user_guess = int(user_guess)
#         if(1<=user_guess<=100):
#             self.guess_num = user_guess
#             if user_guess > self.answer:
#                 print(your_last_guess())
#                 print(f"Your guess of {user_guess} was too high.")
#             elif user_guess < self.answer:
#                 print(your_last_guess())
#                 print(f"Your guess of {user_guess} was too low.")
#             elif user_guess == self.answer:
#                 print(your_last_guess())
#                 print(f"Your guess of {user_guess} is correct!!!!")


    
# game = GuessingGame(random.randint(1,100))
# game.guess()


####### READ ME PART TW0#########################


class GuessingGame:

    def __init__(self, answer):
        self.answer = answer
        self.guess_num = 0

    def guess(self, user_guess):
        self.guess_num = user_guess
        if user_guess > self.answer:
            return "high"
        elif user_guess < self.answer:
            return "low"
        elif user_guess == self.answer:
            return "correct"

    def solved(self):
        if self.answer == self.guess_num:
            return True
        else:
            return False
        
game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = int(input("Enter your guess: "))
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")