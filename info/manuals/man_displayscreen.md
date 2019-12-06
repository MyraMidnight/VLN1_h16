# DisplayScreen in UI layer
This class provides methods to display data on the screen, 
the basic feature takes a list of dictionaries and prints it out in a table.

> Plan to have options to format the lists in specific ways, but that feature is lower in priority.

## `printList()`
### Parameters
* `data`, REQUIRED, takes a list of dictionaries (such as the raw data from IOAPI)
* `rowLimit`, OPTIONAL, takes integer, limits the number of rows/dictionaries that printed
* `colWidth`, OPTIONAL, takes integer, customizes the width of the columns