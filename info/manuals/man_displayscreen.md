# DisplayScreen in UI layer
This class provides methods to display data on the screen, 
the basic feature takes a list of dictionaries and prints it out in a table.

> Plan to have options to format the lists in specific ways, but that feature is lower in priority.

## `cutString()`
> This method doesn't actually print anything, but returns a string that has been trimmed to fit within certain width.
```python

```

## `printList()`
### Parameters
* `data`, REQUIRED, takes a list of dictionaries (such as the raw data from IOAPI)
* `rowLimit`, OPTIONAL, takes integer, limits the number of rows/dictionaries that printed
* `colWidth`, OPTIONAL, takes integer, customizes the width of the columns

```python
data = IOAPI().opener("SomeDataFile.csv") #returns list of dictionaries

#this would simply print the full list with default colWidth
DisplayScreen().printList(data)

#this would print 5 rows, each column width = 10
DisplayScreen().printList(data, 5, 10)

#this would bypass the rowLimit and just set the colWidth
DisplayScreen().printList(data, colWidth = 10)
```

## `printListFormat()`
This method behaves like the `printList()`
> This method will allow the caller to specify how they wish the list to be printed according to predefined format templates that describe how wide each column should be and which columns should be printed.
>
### Parameters
* `data`, REQUIRED
* `template`, OPTIONAL (but if you skip this, might as well use `printList()` instead)
* `rowLimit`, OPTIONAL, integer, limits the number of rows printed
### Templates
* `crew` (all employees)
* `pilots`
* `cabincrew`
* `flights`
* `destinations`
* `planes`
* `voyages` (this might get it's own method, it will be complex enough)

```python
data = IOAPI().opener("SomeDataFile.csv") #returns list of dictionaries

#this would simply print the full list with default colWidth
DisplayScreen().printListFormat(data)

#this prints the full list according to the 'crew' template
DisplayScreen().printListFormat(data, "crew")

#this includes the template and rowLimit
DisplayScreen().printListFormat(data, "crew", 5)
```
### Addjusting the `printListFormat()` 
* `self.stringLimits` just dictates how wide each column should be if printed
* `self.printTemplate` decides what stringLimit type to use, and what columns to print