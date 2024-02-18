import os

from runtypes.typechecker import typechecker


def _assert(_condition, _error):
    # Check the value and raise accordingly
    if not _condition:
        raise TypeError(_error)


def _assert_istype(_value, _type):
    # Check the instance
    _assert(type(_value) == _type, "Value is not of type {0}".format(_type.__name__))


def _assert_isinstance(_value, _type):
    # Check the instance
    _assert(isinstance(_value, _type), "Value is not an instance of {0}".format(_type))


@typechecker
def Any(value):
    return value


@typechecker
def Optional(value, optional_type=Any):
    # Return if value is none
    if value is None:
        return

    # Check the optional type
    _assert_isinstance(value, optional_type)

    # Validate further
    return value


@typechecker
def Union(value, *value_types):
    # Validate value with types
    for value_type in value_types:
        if isinstance(value, value_type):
            return value

    # Raise a value error
    raise TypeError("Value is not an instance of one of the following types: {0}".format(value_types))


@typechecker
def Literal(value, *literal_values):
    # Make sure value exists
    _assert(value in literal_values, "Value is not one of {0}".format(literal_values))

    # Return the value
    return value


@typechecker
def Text(value):
    # Make sure the value is an instance of a string
    # In Python 2, u"".__class__ returns unicode
    # In Python 3, u"".__class__ returns str
    if str == u"".__class__:
        # Python 3, check for unicode is redundant
        _assert_isinstance(value, str)
    else:
        # Python 2, check for unicode is required
        _assert_isinstance(value, (str, u"".__class__))

    # Return the value
    return value


@typechecker
def Bytes(value):
    # Make sure the value is an instance of bytes
    _assert_isinstance(value, bytes)

    # Return the value
    return value


@typechecker
def List(value, item_type=Any):
    # Make sure value is a list
    _assert_isinstance(value, list)

    # Loop over value and check items
    for item in value:
        _assert_isinstance(item, item_type)

    # Convert the list
    return value


@typechecker
def Dict(value, key_type=Any, value_type=Any):
    # Make sure value is a dictionary
    _assert_isinstance(value, dict)

    # Loop over value and check items
    for _key, _value in value.items():
        # Check the key and value types
        _assert_isinstance(_key, key_type)
        _assert_isinstance(_value, value_type)

    # Loop over keys and values and check types
    return value


@typechecker
def Tuple(value, *item_types):
    # Make sure value is a tuple
    _assert_isinstance(value, tuple)

    # If types do not exist, return
    if not item_types:
        return value

    # Make sure value is of length
    _assert(len(value) == len(item_types), "Value length does not match types")

    # Check all item types
    for item, item_type in zip(value, item_types):
        # Check the item type
        _assert_isinstance(item, item_type)

    # Loop over values in tuple and validate them
    return value


@typechecker
def Integer(value):
    # Make sure value is an int
    _assert_istype(value, int)

    # Return the value
    return value


@typechecker
def Float(value):
    # Make sure value is an float
    _assert_istype(value, float)

    # Return the value
    return value


@typechecker
def Bool(value):
    # Make sure the value is a bool
    _assert_istype(value, bool)

    # Return the value
    return value


@typechecker
def Schema(value, schema):
    # Make sure value and schema are dicts
    _assert_isinstance(value, dict)
    _assert_isinstance(schema, dict)

    # Loop over each key and value
    for _key, _value_type in schema.items():
        # Fetch the value from the dict
        _value = value.get(_key)

        # If the value type is a sub-schema
        if isinstance(_value_type, dict):
            # Update value type with sub-schema
            _value = Schema[_value_type]

        # Validate the value
        _assert_isinstance(_value, _value_type)

    # Make sure all items are valid
    return value


@typechecker
def Charset(value, chars):
    # Make sure value is a string
    _assert_isinstance(value, Text)

    # Validate charset
    for char in value:
        _assert(char in chars, "Value contains invalid characters")

    # Validation has passed
    return value


@typechecker
def Domain(value):
    # Make sure value is a string
    _assert_isinstance(value, Text)

    # Split to parts by dot
    parts = value.split(".")

    # Make sure all parts are not empty
    _assert(all(parts), "Value parts are invalid")

    # Loop over parts and validate characters
    for part in parts:
        _assert_isinstance(part.lower(), Charset["abcdefghijklmnopqrstuvwxyz0123456789-"])

    # Validation has passed
    return value


@typechecker
def Email(value):
    # Make sure value is a string
    _assert_isinstance(value, Text)

    # Split into two (exactly)
    parts = value.split("@")

    # Make sure the length is 2
    _assert(len(parts) == 2, "Value can't be split into address and domain")

    # Make sure all parts are not empty
    _assert(all(parts), "Value address and domain are empty")

    # Extract address and domain
    address, domain = parts

    # Make sure the domain is an FQDN
    _assert_isinstance(domain, Domain)

    # Make sure the address is valid
    for part in address.split("."):
        # Make sure part is not empty
        _assert(part, "Value part is empty")

        # Make sure part matches charset
        _assert_isinstance(part, Charset["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'*+-/=?^_`{|}~"])

    # Validation has passed
    return value


@typechecker
def Path(value):
    # Make sure value is a string
    _assert_isinstance(value, Text)

    # Convert the path into a normal path
    value = os.path.normpath(value)

    # Split the path by separator
    for part in value.split(os.path.sep):
        # Make sure the part is a valid path name
        _assert_isinstance(part, PathName)

    # Path is valid
    return value


@typechecker
def PathName(value):
    # Make sure value is a string
    _assert_isinstance(value, Text)

    # Convert the path into a normal path
    value = os.path.normpath(value)

    # Make sure there are not path separators in the value
    _assert(os.path.sep not in value)

    # Make sure the path does not contain invalid characters
    for char in value:
        # Check for forbidden characters
        _assert(char not in ':"*?<>|', "Value contains invalid characters")

    # Pathname is valid
    return value


# Initialize some charsets
ID = Charset["abcdefghijklmnopqrstuvwxyz0123456789"]
Binary = Charset["01"]
Decimal = Charset["0123456789"]
Hexadecimal = Charset["0123456789ABCDEFabcdef"]
