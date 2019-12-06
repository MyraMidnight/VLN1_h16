# InputHandler in UI layer
Currently the incomplete methods in the `InputHandler` class will return dummy data in same format as you would expect to get from it, so there should be no issue by calling on them.

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