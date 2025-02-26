# So you think you understand Python lambda functions?

At some point over the last few years I coded myself into a corner. Consider the following Python class:

```python
class Foo:
    def __init__(self, a=1, b=0):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, value):
        self._b = value
```

In the library I'm working on, ``Foo`` has several subclasses and users may further develop 
new custom subclasses of ``Foo`` or its children. In particular, these subclasses tend to 
involve redefining one or more of ``Foo``'s properties with getters that are state-based 
and/or require heavy computations before returning a value. Maybe something like this:

```python
import time

class Bar(Foo):

    @property
    def a(self):
        time.sleep(5)
        return 25
    
    @property
    def b(self):
        time.sleep(2)
        return 3
```

This isn't inherently a problem, but a separate part of the codebase operates on instances 
of ``Foo`` (or its subclasses) by repeatedly accessing its properties in a way that assumes 
they are static during process execution:

```python
def run(f: Foo):
    for n in range(1000):
        print(n + f.a + f.b)
```

Recomputing their values each time is unnecessarily slow and providing some temporary chache 
mechanism would greatly improve performance. Because the property return values are free to 
change at any time and only need to be cached (optionally) before the ``run()`` function is
called, a traditional cache won't work here. Instead, the user will need to explicitly ask for
this temporary "freezing" to occur by calling a new ``freeze()`` method. A brute force 
solution looks something like this:

```python
class Foo:
    def __init__(self, a=1, b=0):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a
    
    ...

    def freeze(self):
        name = 'Frozen' + self.__class__.__name__
        bases = (self.__class__,)
        attrs = {'a': property(fget=lambda x: getattr(x, '_a')),
                 'b': property(fget=lambda x: getattr(x, '_b'))}
        cls = type(name, bases, attrs)  # dynamically construct a new type
        frozenself = cls() # new instance of cls

        # copy over all of self's attributes to frozenself
        frozenself.__dict__.update(self.__dict__)

        # create static copies of the attributes we want to freeze
        frozenself._a = self.a
        frozenself._b = self.b

        return frozenself
```

Calling ``Foo.freeze()`` dynamically constructs a new type that looks exacly like
``Foo`` but has redefined the properties ``a`` and ``b`` to return ``self._a`` and
``self._b``, respecively. It then creates a new instance of this class, copies over
all of the original object's attributes, and forces the creation of static copies
of the return values for ``a`` and ``b``. Calling ``freeze()`` on an instance of
``Foo`` doesn't have any effect since ``Foo``'s properties already return
``self._a`` and ``self._b``, but calling ``freeze()`` on an instance of ``Bar``
redefines the behavior of its ``a`` and ``b`` properties.

This does exactly what I want:

```pycon
# object construction is fast
>>> bar = Bar()

# but property access is slow
>>> bar.a  
25 
>>> bar.b
3

# creating a frozen instance of bar is slow because we're making 
# static copies of bar.a and bar.b
>>> barf = bar.freeze()

# but property access is now instant since we're just returning the frozen value
>>> barf.a
25
>>> barf.b
3
```

Unfortunately we need to support an arbitrary set of properties and probably want to 
allow users to specify any additional properties to freeze. We'll add a 
``__freeze_attrs__`` list and make ``freeze()`` more general:

```python
class Foo:

    ...

    __freeze_attrs__ = ['a', 'b']

    def freeze(self, *attrs):
        freeze_attrs = [*self.__freeze_attrs__, *attrs]

        name = 'Frozen' + self.__class__.__name__
        bases = (self.__class__,)
        attrs = {f'{attr}': property(fget=lambda x: getattr(x, f'_{attr}'))
                 for attr in freeze_attrs}
        cls = type(name, bases, attrs)  # dynamically construct a new type
        frozenself = cls() # new instance of cls

        # copy over all of self's attributes to frozenself
        frozenself.__dict__.update(self.__dict__)

        # create static copies of the attributes we want to freeze
        frozenself._a = self.a
        frozenself._b = self.b

        return frozenself
```


We've made two changes to ``freeze()``:

1. Construct a complete list of the attributes to freeze from ``self.__frozen_attrs__`` and any ``*args`` provided to ``freeze()``
2. Dynamically construct the ``attrs`` dict via dict comprehension from the attributes in ``freeze_attrs``

Aaaaand we're done:

```pycon
>>> bar = Bar()
>>> barf = bar.freeze()
>>> barf.a  # should return 25
3
>>> barf.b  # should return 3
3
```

<img src="blink.gif">


It appears the getter for ``a`` is the same as the getter for ``b``, 
but they are in fact different (property) objects in memory:

```pycon
>>> print(hex(id(barf.a)))
0x101348170
>>> print(hex(id(barf.b)))
0x1013480d0
```

What's more, switching the order of ``a`` and ``b`` in ``__freeze_attrs__`` 
shows that whichever attribute is iterated over last in the ``attrs`` dict 
comprehension is returned for all frozen attributes. I've confirmed this is 
the case for more than two frozen attributes as well. <ins>**I have no idea why 
this happens.**</ins> At some point I'll have to dig in to the bytecode to see what 
is going on behind the scenes.

In the meantime, I worked around this nonsense by writing a simple closure 
that is used in place of the lambda function in the ``attrs`` dict comprehension:

```python
def frozen_getter(self, attr):
    def fget(self):
        return getattr(self, f'_{attr}')
    return fget

class Foo:
    
    ...

    def freeze(self, *attrs):
        ...
        attrs = {f'{attr}': property(fget=frozen_getter(self, attr))
                 for attr in freeze_attrs}
```


Except [closures don't work with multiprocessing](https://www.stevenengelhardt.com/2013/01/16/python-multiprocessing-module-and-closures/) 
and I may want that someday. Fine, I'll use a callable class instead:

```python
class _FrozenGetter:
    def __init__(self, attr):
        self.attr = attr
    
class Foo:
    
    ...

    def freeze(self, *attrs):
        ...
        attrs = {f'{attr}': property(fget=_FrozenGetter(attr))
                 for attr in freeze_attrs}
```

Great success!
