def repeat_me(

        func):

    def wrapper(arg, count):
        for x in range(0, count):
            func(arg)
            print('')

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
