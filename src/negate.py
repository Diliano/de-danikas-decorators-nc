def negate(func):
    def wrap_func():
        return not func()
    return wrap_func