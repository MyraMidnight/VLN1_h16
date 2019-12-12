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
def main():
  """The core program"""
  #print the main menu
  MenuHandler().displayMenu()

# ------------------------  Run program  --------------------- 
main()