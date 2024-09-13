def convert_type(type):

    def outer_wrapper(func):
        def inner_wrapper():
            return type(func())
        return inner_wrapper
    
    return outer_wrapper
