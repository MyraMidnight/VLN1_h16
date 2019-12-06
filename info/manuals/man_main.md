## Importing classes and methods
`import` is used for using classes/methods that are not accessable by default or located in different files. 

## Importing inbuilt modules
importing a python module that is already included, yet not enabled by default.
```python
import math 
```
## Importing from a file
importing from a different file, then you need to specify from where you are getting the class/methods. You do not need to specify the file extention since it expects it to be python code.
* If a file contains a single class, then it is not uncommon for the file name to be identical to the class name that it contains. Not nessisery but very handy at a glance.

```python
#all imports start looking same directory as your code/file.
from some_file import SomeClass

#you can have to look for files located in sub directories
from some_folder.some_file import SecondClass
from folder.folder.file import ThirdClass
```


You might have noticed in some places the use of `sys` when importing classes, this is because there came up some issues with importing from sibling directories or basically any directory that isn't located in same directory as your current file/code

```python
#using 'sys' to essentially add '../' infront of any file imports in this case.
import sys
sys.path.insert(1, '../') 
#and then the import below
from some_file import SomeClass
``` 
## Other manuals
* [MenuHandler (UI layer)](man_menuhandler.md)
* [InputHandler (UI layer)](man_inputhandler.md)
* [DisplayScreen (UI layer)](man_displayscreen.md)