from datetime import date


def use_today(f):
    def f_using_today(day=None, *args, **kwargs):
        if day is None:
            day = date.today()
        return f(*args, day, **kwargs)
    return f_using_today
