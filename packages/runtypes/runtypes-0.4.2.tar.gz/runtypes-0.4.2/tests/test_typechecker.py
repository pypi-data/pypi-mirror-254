from runtypes import typechecker


def test_creation():
    # Just create a simple typechecker
    @typechecker
    def MyType(value):
        return value


def test_conversion():
    # Create new typechecker that converts strings to int
    @typechecker
    def IntThatCanBeString(value):
        return int(value)

    # Make sure the type-checker works
    assert IntThatCanBeString("10") == 10, "Failed to execute typechecker logic"

    # Make sure the type-checker works with isinstance
    assert isinstance("10", IntThatCanBeString), "Failed to type-check using isinstance"

    # Make sure the type-checker fails when given something that cannot be converted to int
    assert not isinstance(object(), IntThatCanBeString), "Type-checker accepts to many things"


def test_arguments():

    @typechecker
    def StringThatMustContain(value, must_contain=None):
        # Make sure value is a string
        if not isinstance(value, str):
            raise TypeError("Not a string")

        # If must contain exists, check it
        if must_contain:
            if must_contain not in value:
                raise TypeError("%r not in value" % must_contain)

        # Return the value
        return value

    # Make sure simple typechecker works
    assert isinstance("Hello World", StringThatMustContain), "String check failed"

    # Make sure advanced typechecker works
    assert isinstance("Hello World", StringThatMustContain["World"]), "Must-contain check failed"

    # Make sure no false positives
    assert not isinstance("Hello World", StringThatMustContain["runtypes"]), "Must-contain check failed"


def test_representation():

    @typechecker
    def MyType(value, *args):
        return value

    # Make sure empty representation is ok
    assert repr(MyType) == "MyType"

    # Make sure arguments representation is ok
    assert repr(MyType[None]) == "MyType[None]"
    assert repr(MyType[None, 10]) == "MyType[None, 10]"
