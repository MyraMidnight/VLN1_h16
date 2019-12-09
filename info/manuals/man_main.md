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
#basic example
from folder.subfolder.someModuleFile import someModule

from modules.logic_layer.someModule import SecondClass
from modules.ui_layer.someModule import ThirdClass
```

The special (or confusing) part about importing from other files is the fact that all paths not relative to the file location, but are instead relative to the location of the main file that runs the program (in our case `main.py`).

## Other manuals
* [MenuHandler (UI layer)](man_menuhandler.md) 
* [InputHandler (UI layer)](man_inputhandler.md) varifies input
* [DisplayScreen (UI layer)](man_displayscreen.md) displaying lists
* [DateUtil (UI layer)](man_dateutil.md) for parsing datetime strings