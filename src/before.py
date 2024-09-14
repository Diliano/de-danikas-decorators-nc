def before(num):
    def outer_wrapper(func):
        count = 0
        def inner_wrapper():
            nonlocal count
            if count < (num - 1):
                count += 1
                return func()
        return inner_wrapper
    return outer_wrapper