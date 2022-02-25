
class Base():
    pass


class GrandParent(Base):
    pass


class GrandMaternalParent(Base):
    pass


class Parent(GrandParent):
    pass


class Children(Parent):
    pass


class GrandChildren(Children):
    pass


def list_all_sublcasses(cls):
    return set(cls.__subclasses__()).union(
        [s for sub in cls.__subclasses__() for s in list_all_sublcasses(sub)]
    )


def list_subclasses(cls):
    print(cls.__subclasses__())


if __name__ == '__main__':
    # list_subclasses(Base)
    print(__name__)
    print(list_all_sublcasses(Base))
