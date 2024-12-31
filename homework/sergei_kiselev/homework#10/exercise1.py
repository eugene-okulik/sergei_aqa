def finish_me(func):

    def wrapper(anything):
        func(anything)
        print('')
        print('finished')
    return wrapper


@finish_me
def example(text):
    print(text)

example('print me')