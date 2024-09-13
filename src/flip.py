def flip(func):
    def wrap_func(*args):
        return func(*args[::-1])
    return wrap_func