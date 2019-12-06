# InputHandler in UI layer
Currently the incomplete methods in the `InputHandler` class will return dummy data in same format as you would expect to get from it, so there should be no issue by calling on them.

This only handles basic varification and returns the value when it meets the requirements, then the caller needs to handle further varification if it needs to be compared to existing data (such as employee exists)

### Methods (ready)
Some of the unfinished methods will just return dummy data so the caller can actually work with something.

* `numOptions()` : menu/list index from input
* `numSetLength()` : string of numbers of set length
* `ssn()` : social security num
* `dateTime()` : get date and time from input
* `dateOnly()`: get only the date
* `textSetLength` : string of letters of set length
* `names()` : get names (only alphanumeric or spaces)
* `flightId()`: flight ID format

## Numbered list options (`numOptions`)
This method just checks if the user inputs a integer within a set range, this is essentially for handling selecting from lists where the user is provided with a list of choices as a numbered list and needs to input a number to select it.

* It only requires one parameter, `numOfChoices`, which just tells the method how many options are presented to the user
* The optional parameters are `inputQuestion` and `exitKey`
* `inputQuestion` is the string that is printed before input

```python
InputHandler().numChoices(numOfChoices: int, inputQuestion : str)
```
#### example of use
```python
#input range 1-4
InputHandler().numChoices(4) 

#input range 1-6, with custom string
InputHandler().numChoices(6, "What do you want?") 
```