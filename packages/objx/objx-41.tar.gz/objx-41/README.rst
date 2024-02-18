OBJX
####


NAME

::

    OBJX - objects library


INSTALL

::

    $ pip install objx


SYNOPSIS

::

    >>> from objx import Object, read, write
    >>> o = Object()
    >>> o.a = "b"
    >>> write(o, "test")
    >>> oo = Object()
    >>> read(oo, "test")
    >>> oo
    {"a": "b"}


DESCRIPTION

::

    OBJX provides an objx namespace that allows for easy json save//load
    to/from disk of objects. It provides an "clean namespace" Object class
    that only has dunder methods, so the namespace is not cluttered with
    method names. This makes storing and reading to/from json possible.

    OBJX has all the python3 code to program a unix cli program, such as
    disk perisistence for configuration files, event handler to
    handle the client/server connection, code to introspect modules
    for commands, deferred exception handling to not crash on an
    error, a parser to parse commandline options and values, etc.

    OBJX is Public Domain.

AUTHOR

::

    Bart Thate <objx@proton.me>


COPYRIGHT

::

    OBJX is Public Domain.
