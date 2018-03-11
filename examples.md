All the examples are using dates, so let's import the date class.
>>> from datetime import date

We define a function
>>> def previous_business_day():
...     day = date.today() - timedelta(days=1)
...     if day.weekday == 6:
...         day = day - timedelta(days=1)
...     if day.weekday == 5:
...         day = day - timedelta(days=1)
...     return day
