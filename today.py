def use_today(f):
    def f_using_today(*args, day=None, **kwargs):
        if day is None:
            day = date.today()
        return f(*args, day, **kwargs)
    return f_using_today
