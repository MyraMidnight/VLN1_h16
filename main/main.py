# Here we will create the main program
# ------------------------  Import classes  ------------------ 
from modules.ui_layer.MenuHandler import MenuHandler

import os
# print(os.name)
os.system('mode con: cols=300 lines=50')  # works on M$ Windows
os.system("printf '\e[8;50;300t'")        # works on MacOS
# pause = input("Press any key to continue...")


# ------------------------  Main program  -------------------- 
def main():
  """The core program"""
  #print the main menu
  MenuHandler().displayMenu()

# ------------------------  Run program  --------------------- 
main()