
# MenuHandler in UI Layer

## Printing a menu (`displayMenu` method)
* The `displayMenu` handles both printing the desired menu, as well as prompting the user for input to select available options.

* By default it prints the __main menu__ if no parameter is set.

* All available menu options are kept in the `self.menuOptions`
* The `self.menuLayout` dictionary contains the menu names and list of options that will be available which are just references to the keys in `self.menuOptions`

```python
# prints the 'main menu' 
MenuHandler().displayMenu()

# prints specified menues
MenuHandler().displayMenu("main")
```
> ### Where to add the menus?
> When the program is returning back to the menu after performing something, such as creating/updating/getting data.
>
> For example, if we would run 'createEmployee', then when it finishes running and gets ready to return, then it would print the specific menu that should appear at that point, in this case "create" submenu would be printed.


## The `self.menuOptions` 
Any option that the user should be able to access through the menu need to be in the `menuOptions` dictionary before it can be displayed.

* if a menu option is supposed to access a submenu, then the `function` should contain a string that references the name used for the submenu in `self.menuLayout`
* else the function should contain a function/method without calling it, meaning not adding the parethesis at the end `()`
* Sub menus are seperated by dots, the previous numbers indicate the parent.
```python
self.menuOptions = {
    #basemenu
    "1": {
        "title": "Create new data",
        "function": "create" 
    },
    #submenu of 1
    "1.1" : {
        "title": "New Employee",
        "function": LLAPI().createEmployee
    },
    ...
}
```

## The `self.menuLayout`
It is basically a list of references for the `self.menuOptions`

```python
self.menuLayout = {
    "main": ["1", "2", "3"],
    "create": ["1.1", "1.2", "1.3", "1.4"],
    "get": ["2.1", "2.2", "2.3", "2.4"],
    "update": ["3.1", "3.2", "3.3"]
}
```
