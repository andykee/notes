# Python notes

#### Unpack unknown number of return values
```python
foo, bar, *rest = func()
```

#### Delete items from a dictionary
```python
del d['key']        # Raises KeyError if key not in d
d.pop('key')        # Returns popped value. Raises KeyError if key not in d
d.pop('key', None)  # Returns popped value. None is default value if key not in d
```

#### Convert bytes to a string
```python
b'hello'.decode('utf-8')
b'hello'.decode()  # utf-8 is default encoding
```
