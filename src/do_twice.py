def do_twice(func):
    def wrap_func():
        func()
        func()
    return wrap_func