# `Voyage` in model classes
This is a _model class_ that lives outside of the layers (ui, data and logic) which can be passed between layers as a data object.

#### Examples of usage:
Just create a instance of the model class, and then pass it directly between classes. This allows the data layer to call on methods in the model classes that would handle processing the data into usable layout to be saved on file.
* Passing a `new employee` to the _data layer_
* Passing updated data to the _data layer_

## Creating a new instance of `Voyage`
The `voyage` can be initialized with existing flight data, just give it a list containing the connected flights (could give it full data list, but it only processes the first two flights).
```python
from modules.models.Voyage import Voyage

flights = [{"raw data of outgoing flight"}, {"raw data of incoming flight"}]

#initialize the Voyage with the flight data
newVoyage = Voyage(flights)

print(newVoyage) #will print the voyage info
```

## Methods
`Voyage` contains alot of methods, but most of them are just for internal use. Here is a list of methods that you are most likely to use.
* `setVoyage(flights)` will overwrite the voyage with provided flightdata, this is automatically run if you initialize the voyage with flightdata.
* `createVoyage()` will prompt the user for the data to create a new Voyage
* `getFlights()` will return a list of the associated flights.
* `updateCrew(crew)` will update the voyage crew

## `updateCrew()`
> Will take a dictionary with roles as keys and value is employee info