"""
https://www.thedigitalcatonline.com/blog/2014/09/01/python-3-oop-part-5-metaclasses/
"""


class MyType(type):
    pass


class MySpecialClass(metaclass=MyType):
    pass


msp = MySpecialClass()
print(type(msp))
print(type(MySpecialClass))
print(type(MyType))
print(MyType.__class__, MyType.__base__, type.__bases__)
