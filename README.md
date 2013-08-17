Span
====

Span is a simply utility that lets you easily compare spans (ranges) of time in Python.  It let's you determine if span touch, intersect, etc.

Installation
====

Span can be installed from pip:

`pip install span`

Intersects
====

Check to see if two spans intersect:

```python
>>> from span import Span
>>> from datetime import datetime, timedelta

>>> now = datetime.now()

>>> s1 = Span(start=now, end=now+timedelta(minutes=60))
>>> s2 = Span(start=now+timedelta(minutes=30), end=now+timedelta(minutes=90))

>>> s1.lintersects(s2) #check if s1 intersects the left (start) side of s2
True

>>> s1.rintersects(s2) #check if s1 intersects the right (end) side of s2
False

>>> s1.intersects(s2) #check if s1 intersects either side of s2
True
```

Touches
====

Check to see if two spans touch:

```python
>>> from span import Span
>>> from datetime import datetime, timedelta

>>> now = datetime.now()

>>> s1 = Span(now, now + timedelta(minutes=60))
>>> s2 = Span(now + timedelta(minutes=60), now + timedelta(minutes=120))

>>> s1.ltouches(s2) #check if s1 touches the left (start) side of s2
True

>>> s1.rtouches(s2) #check if s1 touches the right (end) side of s2
False

>>> s1.touches(s2) #check if s1 touches either side of s2
True
```