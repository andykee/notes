# datetime formatting

* `datetime.strftime(format)` returns a string according to *format*
* `datetime.isoformat()` returns a string formatted as YYYY-MM-DDTHH:MM:SS.ffffff
* `datetime.strptime(date_string, format)` returns a `datetime` object corresponding to *date_string*, parsed according to *format*
* `<datetime>.date()` recasts a `datetime` object to a `date` object

### datetime format codes

|           | Meaning                                         | Example                          |
|:----------|:------------------------------------------------|:---------------------------------|
| `%y`      | Year (2 digit)                                  | 00, 01, ..., 99                  |
| `%Y`      | Year (4 digit)                                  | 2024, 2025, ...., 9999           |
| `%b`      | Month (abbreviated)                             | Jan, Feb, ..., Dec               |
| `%B`      | Month (full)                                    | January, February, ..., December |
| `%m`      | Month (zero padded number)                      | 01, 02, ..., 12                  |
| `%d`      | Day of the month (zero padded number)           | 01, 02, ..., 31                  |
| `%j`      | Day of the year (zero padded number)            | 001, 002, ..., 365               |
| `%a`      | Weekday (abbreviated)                           | Sun, Mon, ..., Sat               |
| `%A`      | Weekday (full)                                  | Sunday, Monday, ..., Saturday    |
| `%H`      | Hour (24 hour, zero padded)                     | 00, 01, ..., 23                  |
| `%I`      | Hour (12 hour, zero padded)                     | 01, 02, ..., 12                  |
| `%p`      | AM or PM                                        | AM, PM                           |
| `%M`      | Minute (zero padded)                            | 00, 01, ..., 59                  |
| `%S`      | Second (zero padded)                            | 00, 01, ..., 59                  |
| `%f`      | Microsecond (zero padded to 6 digits)           | 000000, 000001, ..., 999999      |
| `%z`      | UTC offset (+/-HHMM)                            | +0000, -0400, +1030, ...         |
| `%Z`      | Time zone name                                  | (empty), UTC, GMT                |
