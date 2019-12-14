# Here we will create the main program
# ------------------------  Import classes  ------------------ 
from modules.ui_layer.MenuHandler import MenuHandler

import platform 

import os
if platform.system() == "Windows":
    os.system('mode con: cols=200 lines=45')  # works on M$ Windows
elif platform.system() == "Darwin":
    os.system("printf '\e[8;50;250t'")        # works on MacOS
else:
    print("Could resize screen, assumed reason: you are not using a mac or windows")
# pause = input("Press any key to continue...")


# ------------------------  Main program  -------------------- 
def main():
  """The core program"""
  #print the main menus
  MenuHandler().displayLogo()
  MenuHandler().displayMenu()

# ------------------------  Run program  --------------------- 
main()