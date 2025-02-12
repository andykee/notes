# SQL notes

#### Connect to SQL server
```bash
$ mysql -u <username> -p
```

#### Create user
```sql
CREATE USER <username>@localhost
IDENTIFIED BY '<password>';
```

#### Change password
```sql
CREATE USER <username>@localhost
IDENTIFIED BY '<password>'; -- new password
```

#### List all databases
```sql
SHOW DATABASES;
```

#### Create new database
```sql
CREATE DATABASE <name>;
```
