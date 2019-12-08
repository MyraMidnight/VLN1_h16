# `DateUtil` from UI layer
`DateUtil` will parse a datetime string (isoformat) into parts.

## Creating the DateUtil object
```python
from modules.ui_layer.DateUtil import DateUtil

datetime = "2019-11-06T10:39:00" #datetime.date().isoformat()

#create the parsedDate object
parsedDate = DateUtil(datetime)

#then call on any attribute you need
parsedDate.day #returns only the day
```

## Accessable attributes 
> These are not methods, so you do not run them. These attributes only exist if you initiate the DateUtil with a datetime string, or run the `parse(datetime)` method.
* `date`: returns only date part `YYYY-MM-DD`
* `time`: returns only time part `HH:MM:SS`
* `day`
* `month`
* `year`
* `hour`
* `minute`
* `second`

## Methods
> You can actually use the the DateUtil without initiating it with a datetime string, then it will not generate the list of attributes, but still allows you to use the methods.

All these methods __require a datetime string of isoformat__. You can u
se the individual parsers to get a specific part of the datetime string.
* `parse(datetime)`, creates all the previously listed attributes.

* `date_parse(datetime)`
* `time_parse(datetime)`
* `day_parse(datetime)`
* `month_parse(datetime)`, 
> __unique features of month_parse()__ are optional parameter `name` to get the month name.
> Just give it a non-empty string to enable, it does not care what you write
* `year_parse(datetime)`
* `hour_parse(datetime)`
* `minute_parse(datetime)`
* `second_parse(datetime)`
