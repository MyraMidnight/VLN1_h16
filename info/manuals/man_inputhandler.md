# InputHandler in UI layer
The InputHandler does just that, handles the user input and makes sure that it follows specified format rules, but __it does not handle varifying it against any existing data__, that needs to done by the caller.

### Basics shared traits
All the input methods will have optional parameter `inputQuestion` that lets you customise what is printed before the user is promted for input. 

There will also be a optional `exitKey` (will be `q` by default) that is the trigger __for exiting the input loop and returns `False`__. This feature might not work properly at the moment, but it will be a proper feature. 

## Methods 
Some of the unfinished methods will just return dummy data so the caller can actually work with something. You should be able to call on any of these methods even if they have not been fully defined since they will return dummy data that can be worked with.

* `numOptions()` : menu/list index from input
* `numSetLength()` : string of numbers of set length
* `ssn()` : social security num
* `dateTime()` : get date and time from input
* `dateOnly()`: get only the date
* `textSetLength` : string of letters of set length
* `names()` : get names (only alphanumeric or spaces)
* `flightId()`: flight ID format

### Numbered list options (`numOptions`)
This method just checks if the user inputs a integer within a set range, this is essentially for handling selecting from lists where the user is provided with a list of choices as a numbered list and needs to input a number to select it.

* It only requires one parameter, `numOfChoices`, which just tells the method how many options are presented to the user
* The optional parameters are `inputQuestion` and `exitKey`
* `inputQuestion` is the string that is printed before input

```python
InputHandler().numChoices(numOfChoices: int, inputQuestion : str)
```
```python
#input range 1-4
InputHandler().numChoices(4) 

#input range 1-6, with custom string
InputHandler().numChoices(6, "What do you want?") 
```

### Date and time inputs 
#### `dateTime()`, `dateOnly()`
These return a datetime string in isoformat, `2019-11-06T10:39:00` (`YYYY-MM-DDTHH:MM:SS`). 

* `dateTime()` promts both dateOnly() and timeOnly() to compile the datetime
* `dateOnly()`

#### `timeOnly()`
This method will return a time string (`HH:MM:SS`)

### `textSetLength()` 
You tell it how long you want the string to be, and will prompt the user until it writes input of correct length.
```python
InputHandler().textSetLength(6)
```

### `numSetLength()` and `ssn()`
works the same as `textSetLength()` but only allows the input to be numbers
```python
InputHandler().numSetLength(6) #returns a string of lenght 6
```
`ssn()` prompts `numSetLength(10)` and then might have some extra varification ontop of that (such as checking if first half is a valid date, since it is the birthday of the person) 
