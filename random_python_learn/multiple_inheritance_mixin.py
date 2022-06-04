"""
    Understand Multiple inheritance and Mixin - https://www.thedigitalcatonline.com/blog/2020/03/27/mixin-classes-in-python/
"""


class Ancestor:
    def rewind(self):
        print("Ancestor: rewind")


class Parent1(Ancestor):
    def open(self):
        print("Parent1: open")


class Parent2(Ancestor):
    def open(self):
        print("Parent2: open")

    def close(self):
        print("Parent2: close")

    def flush(self):
        print("Parent2: flush")


class Child(Parent1, Parent2):
    def flush(self):
        print("Child: flush")


if __name__ == '__main__':
    # python's method resolution order to avoid DIAMOND PROBLEM in M.I
    print(Child.__mro__)
    c = Child()
    c.rewind()
    c.open()
    c.close()
    c.flush()
