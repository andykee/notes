# SQLAlchemy query LIKE statement

SQLAlchemy provides a number of methods for generating a `LIKE` clause in a query:

#### like
```python
select(User).where(User.name.like(f'%{some_term}%'))
```

#### contains
Search term inside % wildcards
```python
select(User).where(User.name.contains('i'))
```

#### startswith
Search term followed by % wildcard
```python
select(User).where(User.name.startswith('a'))
```

#### endswith
Search term preceeded by % wildcard
```python
select(User).where(User.name.endswith('e'))
```

Note that each of these has a case-insensitivt counterpart:
* `like` -> `ilike`
* `contains` -> `icontains`
* `startswith` -> `istartswith`
* `endswith` -> `iendswith`

Ref: https://stackoverflow.com/a/77111773
