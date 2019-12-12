>__Do NOT try to add formatting through the data__ by adding `spaces`, `tabs` or anything to the data for formatting purposes because it might end up causing problems when we finalize the layout with the `PrintHandler`.
>
>If the layout is driving you up the wall, then take a look at what `PrintHandler` is doing to process the strings before handing them to the `DisplayScreen` for printing.
>
>The frame itself and anything between sections is handled by the `DisplayScreen` in ui layer.

# DisplayScreen in UI layer
This is the class that you import to print anything for the user to see, since the `User Interface (UI)` should be kept seperate from the rest of the program to make it simpler to swap out interfaces.
```python
from modules.ui_layer.DisplayScreen import DisplayScreen
```

## Pre-formatted print methods
* These are frameless by default
#### Parameters for preFormatted print methods
This includes the `printList()`, `printOptions()` and `printText()`. 
1. `data` is required, expects a list
1. `header` is optional, but should be used. Takes a string.
1. `frame` is optional, takes bool value `True` or `False` (default: `False`)

>All arguments should work in that order, but you can always call the parameter by name when passing the arguments to avoid any issues connected to the order of things, `header="Custom header"` or `frame=True`

### Printing lists with `printList(data)`
The only thing you need to give the method is the raw data, and the method will handle detecting what type of data file you were giving it by comparing the column keys with keys in the stored dataTypes. 

> If it does not recognize the dataType, then it will simply create one for you based on the keys in the given data (so no worries, it just won't have custom column widths or titles)
```python
from modules.data_layer.IOAPI import IOAPI
rawData = IOAPI().opener("DataFile.csv")

#printing full list
DisplayScreen().printList(rawData)

# printing just the first 10 rows, by trimming the given data
DisplayScreen().printList(rawData[:10])
```

* There will be a feature that will skip printing columns if they all appear to be empty (waste of space) if we  have time to implement it. This removes the need to specify templates and makes the programming simpler. 

### Enumerated lists with `printOptions(data)`
The only difference between this method and `printList()` is that it adds numbers infront of the table rows to make index selection easier for the user. Use this when asking the user to pick from a given list.

```python
from modules.data_layer.IOAPI import IOAPI
rawData = IOAPI().opener("DataFile.csv")

#printing full list
DisplayScreen().printOptions(rawData)
```

### Printing text with `printText(data)`

```python
from modules.data_layer.IOAPI import IOAPI
textData = ["line1", "line2", "line3"]

#printing full list
DisplayScreen().printText(textData)
```
## Creating custom screens with `printCustom(sectionData)`
All the pre-formatted print methods are created by using sections, and this method let you create your own custom formatted printer using the same tools.

### Compile the sections
These are the available `section` types and what kind of data each section expects. 
* Each section type can be used more than once
* The order of sections will decide the order they print in.
* By default your custom screen will be framed, which can be disabled optionally with `frame=False` parameter.

```python
sectionData = [
    {"header": [""]}, #list of strings
    {"text": [""]}, #list of strings
    {"shortcuts": [""]}, #list of strings
    {"list": [{}]}, #list of dictionaries
    {"options": [{}]} #list of dictionaries
]
```
### Tables (`list` and `options`) 
* __Data format__: list of dictionaries, just like how it comes raw from the data layer file opener.
1. `list` prints tables of data, including title/header row and dividers
1. `options` it is basically `list` with added enumeration

### Text sections (`header`, `text` and `shortcuts`)
* __Data format__: list of strings
1. `header` prints the data as a header
1. `text` will treat each string as a paragraph
1. `shortcuts` will print a horizontal list of shortcuts, so keep the strings short. 

