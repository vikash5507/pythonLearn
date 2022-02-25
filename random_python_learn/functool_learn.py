from ast import operator
from functools import cached_property, partial, reduce, singledispatchmethod, wraps, singledispatch
from math import prod

"""

About Functool - module is for higher-order functions: functions that act on or return other functions. 
In general, any callable object can be treated as a function for the purposes of this module.

"""


class FunctoolLearn:
    """
        Source - https://docs.python.org/3/library/functools.html

        Tutorial - https://www.youtube.com/watch?v=Jztj_yuFTlk&ab_channel=IndianPythonista
    """

    def __init__(self, name, grades) -> None:
        self.name = name
        self.grades = grades

    # cache_property
    @cached_property
    def findGradeSum(self):
        print("calculating grade sum")
        return sum(self.grades)


# partial function

# def partial(func, /, *args, **keywords):
#     def newfunc(*fargs, **fkeywords):
#         print("new function invoked")
#         newkeywords = {**keywords, **fkeywords}
#         return func(*args, *fargs, **newkeywords)

#     print("new function invoked auto get called")
#     newfunc.func = func
#     newfunc.args = args
#     newfunc.keywords = keywords
#     return newfunc


def add(a, b, c, d):
    return a+b+c+d


def generic_operator(*args, operation):
    # print(args, *args)
    if operation == 'add_all':
        return sum(*args)
    elif operation == 'product_all':
        return prod(*args)
    else:
        return args

# wraps


def mylogger_decorator(func):

    def wrapper(*args, **kargs):
        print(f"Running {func.__name__}")
        return func(*args, **kargs)

    return wrapper


@mylogger_decorator
def add_list(*args):
    return sum(*args)


def mylogger_decorator_with_wraps(func):

    @wraps(func)
    def wrapper(*args, **kargs):
        print(" ---- ")
        print(*args, **kargs)
        print(f"Running {func.__name__}")
        return func(*args, **kargs)

    return wrapper


@mylogger_decorator_with_wraps
def add_list_with_wraps(*args):
    return sum(*args)

# singledispatch


@singledispatch
def append_one(obj):
    return f"{type(obj)} is Unsupported, append_one supports only these types: {append_one.registry.keys()}"


@append_one.register
def _(obj: list):
    return obj + [1]


@append_one.register
def _(obj: int):
    return obj + 1


@append_one.register
def _(obj: str):
    return obj + str(1)

# singledispatchmethod


class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError(
            f"Cannot negate {type(arg)}")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg


if __name__ == '__main__':
    # reduce
    print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))

    # cache_property
    learn = FunctoolLearn('rio', [80, 78, 96, 89])
    print(learn.findGradeSum)

    print(learn.findGradeSum)  # return cached value

    # partial
    add_hundred_extra = partial(add, d=100)

    print(add_hundred_extra(1, 2, 3))

    sum_all_method = partial(generic_operator, operation="add_all")

    print(sum_all_method([1, 2, 3, 4, 5]))

    product_all_method = partial(generic_operator, operation="product_all")

    print(product_all_method([1, 2, 3, 4, 5]))

    # wraps

    add_list([1, 2, 3, 4, 5])  # just invoke a method with custom decorator

    # Note -> it is returing wrapper (not the add_list because of decorator) -> To RESOLVE this use functool wraps
    print(add_list.__name__)

    add_list_with_wraps([1, 2, 3, 4, 5])
    print(add_list_with_wraps.__name__)  # resolved with use of wraps(func)

    # singledispatch test
    print(append_one([1, 2, 3]))
    print(append_one(3))
    print(append_one("abcd"))
    print(append_one({1, 2, 3}))

    # singledispatchmethod test
    negator = Negator()
    print(negator.neg(3))
    print(negator.neg(True))
    print(negator.neg("abcd"))
