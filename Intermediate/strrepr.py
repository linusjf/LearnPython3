#!/usr/bin/env python
"""When To Use __repr__ vs __str__."""
# Emulate what the std lib does.
import datetime

TODAY = datetime.date.today()

# Result of __str__ should be readable."""

print(str(TODAY))

# Result of __repr__ should be unambiguous:

print(repr(TODAY))

# Python interpreter sessions use
# __repr__ to inspect objects:

print(TODAY)
