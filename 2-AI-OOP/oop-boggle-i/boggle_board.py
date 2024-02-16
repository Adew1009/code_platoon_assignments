"""
1. create a 4x4 board
2. "shake" method that fills each space in the board with a
    random capital letter A-Z. this will require import random
    - shake should be a for or a for each type loop
3. 
"""
import random
import string

class BoggleBoard:
  #create a board that is 4 spaces x 4 spaces
  def __init__(self):
   self.blank_row = [
     [" _ ", " _ ", " _ ", " _ "],
     [" _ ", " _ ", " _ ", " _ "],
     [" _ ", " _ ", " _ ", " _ "],
     [" _ ", " _ ", " _ ", " _ "]
   ]
   for row in self.blank_row:
      print("".join(row))

   
  def shake(self):
    rand0=random.choice("AAEEGN") 
    rand1=random.choice("ELRTTY")
    rand2 = random.choice('AOOTTW')
    rand3 = random.choice('ABBJOO')
    rand4 = random.choice('EHRTVW')
    rand5 = random.choice('CIMOTU')
    rand6 = random.choice('DISTTY')
    rand7 = random.choice('EIOSST')
    rand8 = random.choice('DELRVY')
    rand9=  random.choice('ACHOPS')
    rand10 = random.choice('HIMNQU')
    rand11 = random.choice('EEINSU')
    rand12 = random.choice('EEGHNW')
    rand13 = random.choice('AFFKPS')
    rand14 = random.choice('HLNNRZ')
    rand15 = random.choice('DEILRX')
    

    random_string = f"{rand0}{rand1}{rand2}{rand3}{rand4}{rand5}{rand6}{rand7}{rand8}{rand9}{rand10}{rand11}{rand12}{rand13}{rand14}{rand15}"
    for row in range(4):
      for character in range(4):
       letter = random.choice(random_string)
      #  self.blank_row[row][character] = random.choice(string.ascii_uppercase)
       if letter != "Q":
            self.blank_row[row][character] = letter + "  "
       else:
            self.blank_row[row][character] = "Qu "
            # self.blank_row[row][character+1] = (self.blank_row[row][character+1]).strip( )
            
          # (self.blank_row[row][character+1]) = (self.blank_row[row][character+1]) + " "
     
    for row in self.blank_row:
      printed_board = ("".join(row))
      print(printed_board)




james = BoggleBoard()




#Add terminal function