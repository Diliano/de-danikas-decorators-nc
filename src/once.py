def once(func):
    count = 0
    def wrap_func():
        nonlocal count
        if count == 0:
            count += 1
            return func()
    return wrap_func