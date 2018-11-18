import functools

#decorators use a function but modifies it so that the function becomes something else


def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator")
        func()
        print("After the decorator")
    #This line is v.imp. Here the modified function is returned. So we pass in another function defined below, this calls it
    #and adds extra things to it
    return function_that_runs_func

#This function gets replaced by function_that_runs_func
@my_decorator
def my_function():
    print("I'm the function!")


#my_function()

## Advanced

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func():
            print("In the decorator")
            if number == 56:
                print('Not running the function!')
            else:
                func()
            print("After the decorator")
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(56)
def my_function_too():
    print('I am the function!')

my_function_too()
