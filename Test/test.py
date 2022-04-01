def construct(fn):
    def func(*args, **kwargs):
        print(fn.__name__)
        fn(*args, **kwargs)
    return func


@construct
def years(a, b, c):
    pass


years(1, 2, 3)