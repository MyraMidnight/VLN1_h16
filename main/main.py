# Here we will create the main program
# ------------------------  Import classes  ------------------ 
from modules.ui_layer.MenuHandler import MenuHandler

import platform 
print(platform.system())

import os
# print(os.name)
try:
  os.system('mode con: cols=200 lines=45')  # works on M$ Windows
except:
  os.system("printf '\e[8;50;250t'")        # works on MacOS
# pause = input("Press any key to continue...")


# ------------------------  Main program  -------------------- 

logo_str = """
                 |     |
                 | ___ |
              ----/___\----
  x--------------(  .  )--------------x
     x|x   |   |  \___/  |   |   x|x
      x    x   |___| |___|   x    x  
    _   __        _   __   ___     _      
   / | / /____ _ / | / /  /   |   (_)_____
  /  |/ // __ `//  |/ /  / /| |  / // ___/
 / /|  // /_/ // /|  /  / ___ | / // /    
/_/ |_/ \__,_//_/ |_/  /_/  |_|/_//_/  
"""

def main():
  """The core program"""
  #print the main menu
  MenuHandler(logo=logo_str).displayMenu()

# ------------------------  Run program  --------------------- 
main()