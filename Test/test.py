class Test:
    def a(self):
        return

    def b(self):
        return

    def c(self):
        return


all_func = [x for x in dir(Test) if not x.startswith('__')]

print(all_func)