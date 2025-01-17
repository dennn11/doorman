# -*- coding: utf-8 -*-
"""Python 2/3 compatibility module."""
import sys


text_type = str
binary_type = bytes
string_types = (str,)
unicode = str
basestring = (str, bytes)


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)

    return type.__new__(metaclass, 'temp_class', (), {})
