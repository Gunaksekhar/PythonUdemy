def new_func(original_func):

    def wrap_func():
        print("Execute the function, before the original function")

        original_func

        print("Excute the function, after the original function")

    return wrap_func()


def func_needs_decorator():
    print("I want to be decorated!!")

dec_funct = new_func(func_needs_decorator())
print(dec_funct())

@new_func
def func_needs_decorator():
    print("I want to be decorated!!")

func_needs_decorator()




