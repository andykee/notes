# SQLAlchemy ORM notes

### Basic column types
Numeric: `Float` `Integer` `Double` `Numeric`

Text: `String` `Text`

Date/time: `Datetime` `Date` `Time` `Interval`

Logical: `Boolean`

Other: `JSON` `PickleType` `Unicode` `UUID`     

### Basic table structure
```python
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id: mapped_column(primary_key=True)
    name: mapped_column(String(30))
    age = mapped_column(Integer)
```

### Schema creation
```python
Base.metadata.create_all(engine)
```

