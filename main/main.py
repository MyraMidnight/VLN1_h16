# Here we will create the main program
# ------------------------  Import classes  ------------------ 
from modules.ui_layer.MenuHandler import MenuHandler

import os
import platform
if platform.system() == "Windows":
  os.system('mode con: cols=200 lines=45')  # works on M$ Windows
elif platform.system() == "Darwin":
  os.system("printf '\e[8;45;200t'")        # works on MacOS
# pause = input("Press any key to continue...")


# ------------------------  Main program  -------------------- 
def main():
  """The core program"""
  #print the main menu
  MenuHandler().displayMenu()

# ------------------------  Run program  --------------------- 
main()