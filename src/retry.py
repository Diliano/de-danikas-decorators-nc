def retry(num):

    def outer_wrapper(func):
        count = 0
        def inner_wrapper():
            nonlocal count
            while count < num:
                try:
                    return func()
                except Exception:
                    count += 1
            print("FAILURE")
        return inner_wrapper
    
    return outer_wrapper