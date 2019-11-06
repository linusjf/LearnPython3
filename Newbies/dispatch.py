#!/usr/bin/env python3
"""Dispatch via dictionary emulating switch."""
# Because Python has first-class functions they can
# be used to emulate switch/case statements


def dispatch_if(operator, _x, _y):
    """Use switch to call operator."""
    if operator == 'add':
        return _x + _y
    if operator == 'sub':
        return _x - _y
    if operator == 'mul':
        return _x * _y
    if operator == 'div':
        return _x / _y
    return None


def dispatch_dict(operator, _x, _y):
    """Use dictionary to dispatch operator."""
    return {
        'add': lambda: _x + _y,
        'sub': lambda: _x - _y,
        'mul': lambda: _x * _y,
        'div': lambda: _x / _y,
    }.get(operator, lambda: None)()


print(dispatch_if('mul', 2, 8))

print(dispatch_dict('mul', 2, 8))

print(dispatch_if('unknown', 2, 8))

print(dispatch_dict('unknown', 2, 8))
