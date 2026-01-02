# Python datetime Module

## Overview

The `datetime` module is Python's built-in library for working with dates, times, and time intervals.

### Main Purpose and Use Cases
- Working with dates and times (birthdays, deadlines, timestamps)
- Calculating time differences and durations
- Formatting dates for display or storage
- Timezone-aware datetime operations
- Scheduling and time-based logic

### Import
```python
from datetime import date, time, datetime, timedelta
# Or
import datetime as dt
```

---

## Core Components

| Component | Purpose | Example |
|-----------|---------|---------|
| `date` | Dates only (year, month, day) | `2025-12-20` |
| `time` | Times only (hour, minute, second) | `14:30:45` |
| `datetime` | Both date and time combined | `2025-12-20 14:30:45` |
| `timedelta` | Duration/difference between dates | `5 days, 2 hours` |

**How They Relate:**
- `datetime` = `date` + `time` combined
- `timedelta` = result of subtracting two `datetime` or `date` objects
- Most common: Use `datetime` for timestamps, `timedelta` for calculations

---

## Date Object

### Creating Dates
```python
from datetime import date

# Create specific date
d = date(2025, 12, 25)
print(d)  # 2025-12-25

# Today's date
today = date.today()
print(today)  # Current date
```

### Accessing Components
```python
today = date.today()

print(today.year)   # 2025
print(today.month)  # 12
print(today.day)    # 25
print(today.weekday())  # 0-6 (Mon-Sun)
print(today.isoweekday())  # 1-7 (Mon-Sun)
```

### Date Methods
```python
d = date(2025, 12, 25)

print(d.isoformat())      # '2025-12-25'
print(d.strftime("%B %d, %Y"))  # 'December 25, 2025'
print(d.replace(year=2026))     # 2026-12-25
```

---

## Time Object

### Creating Times
```python
from datetime import time

# Create time
t = time(14, 30, 45)  # 2:30:45 PM
print(t)  # 14:30:45

# With microseconds
t = time(14, 30, 45, 123456)
print(t)  # 14:30:45.123456
```

### Accessing Components
```python
t = time(14, 30, 45, 123456)

print(t.hour)        # 14
print(t.minute)      # 30
print(t.second)      # 45
print(t.microsecond) # 123456
```

---

## DateTime Object

### Creating DateTime
```python
from datetime import datetime

# Current date and time
now = datetime.now()
print(now)  # 2025-12-20 14:30:45.123456

# Specific datetime
dt = datetime(2025, 12, 25, 14, 30, 45)
print(dt)  # 2025-12-25 14:30:45

# UTC time
from datetime import timezone
utc_now = datetime.now(timezone.utc)
```

### Accessing Components
```python
now = datetime.now()

print(now.year)    # 2025
print(now.month)   # 12
print(now.day)     # 20
print(now.hour)    # 14
print(now.minute)  # 30
print(now.second)  # 45
print(now.date())  # date object
print(now.time())  # time object
```

### DateTime Methods
```python
now = datetime.now()

# Get just date or time
print(now.date())  # date object
print(now.time())  # time object

# Replace components
new_dt = now.replace(year=2026, hour=10)

# Timestamp (Unix epoch)
timestamp = now.timestamp()  # Seconds since Jan 1, 1970
dt_from_ts = datetime.fromtimestamp(timestamp)
```

---

## Timedelta

### Creating Timedelta
```python
from datetime import timedelta

# Various durations
delta1 = timedelta(days=7)
delta2 = timedelta(hours=24)
delta3 = timedelta(weeks=2, days=3, hours=5)

print(delta1)  # 7 days, 0:00:00
print(delta2)  # 1 day, 0:00:00
print(delta3)  # 17 days, 5:00:00
```

### Parameters
| Argument | Description |
|----------|-------------|
| `days` | Number of days |
| `weeks` | Number of weeks |
| `hours` | Number of hours |
| `minutes` | Number of minutes |
| `seconds` | Number of seconds |
| `milliseconds` | Number of milliseconds |
| `microseconds` | Number of microseconds |

### Date Arithmetic
```python
from datetime import datetime, timedelta

now = datetime.now()

# Add time
future = now + timedelta(days=30)
print(future)

# Subtract time
past = now - timedelta(weeks=2)
print(past)

# Difference between dates
date1 = datetime(2025, 12, 25)
date2 = datetime(2025, 1, 1)
diff = date1 - date2
print(diff.days)  # 358
```

### Real-World Examples
```python
# Schedule reminder 3 days before deadline
deadline = datetime(2025, 12, 31, 17, 0)
reminder = deadline - timedelta(days=3)
print(f"Send reminder on: {reminder.strftime('%B %d at %I:%M %p')}")
# Output: Send reminder on: December 28 at 05:00 PM

# Calculate project duration
project_start = datetime(2025, 12, 1)
project_end = datetime(2025, 12, 20)
duration = project_end - project_start
print(f"Project took {duration.days} days")
# Output: Project took 19 days

# Days until event
event = datetime(2025, 12, 31)
now = datetime.now()
days_left = (event - now).days
print(f"{days_left} days until event")

# Calculate age
birth = date(1990, 5, 15)
today = date.today()
age = (today - birth).days // 365
print(f"Age: {age}")
```

---

## Formatting and Parsing

### Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | Year (4 digit) | 2025 |
| `%y` | Year (2 digit) | 25 |
| `%m` | Month (01-12) | 12 |
| `%d` | Day (01-31) | 20 |
| `%H` | Hour 24h (00-23) | 14 |
| `%I` | Hour 12h (01-12) | 02 |
| `%M` | Minute (00-59) | 30 |
| `%S` | Second (00-59) | 45 |
| `%p` | AM/PM | PM |
| `%B` | Month name | December |
| `%b` | Month abbr | Dec |
| `%A` | Weekday name | Saturday |
| `%a` | Weekday abbr | Sat |

### strftime() - Format to String
```python
now = datetime.now()

print(now.strftime("%Y-%m-%d"))          # 2025-12-20
print(now.strftime("%d/%m/%Y"))          # 20/12/2025
print(now.strftime("%B %d, %Y"))         # December 20, 2025
print(now.strftime("%I:%M %p"))          # 02:30 PM
print(now.strftime("%A, %B %d, %Y"))     # Saturday, December 20, 2025
print(now.strftime("%Y-%m-%d %H:%M:%S")) # 2025-12-20 14:30:45
```

### strptime() - Parse from String
```python
# Parse string to datetime
date_string = "2025-12-20"
dt = datetime.strptime(date_string, "%Y-%m-%d")
print(dt)  # 2025-12-20 00:00:00

# Various formats
dt1 = datetime.strptime("20/12/2025", "%d/%m/%Y")
dt2 = datetime.strptime("December 20, 2025", "%B %d, %Y")
dt3 = datetime.strptime("2025-12-20 14:30:00", "%Y-%m-%d %H:%M:%S")
```

### ISO Format
```python
now = datetime.now()

# To ISO format
iso_string = now.isoformat()
print(iso_string)  # 2025-12-20T14:30:45.123456

# From ISO format
dt = datetime.fromisoformat("2025-12-20T14:30:45")
```

---

## Commonly Confused Concepts

### strftime() vs strptime()

| Method | Direction | Memory Trick |
|--------|-----------|--------------|
| `strftime()` | datetime → string | **f**ormat = output for display |
| `strptime()` | string → datetime | **p**arse = input from text |

```python
# strftime: format datetime to string
dt = datetime(2025, 12, 20, 14, 30)
formatted = dt.strftime('%Y-%m-%d')
print(formatted)  # "2025-12-20" (string)

# strptime: parse string to datetime
date_string = "2025-12-20"
dt = datetime.strptime(date_string, '%Y-%m-%d')
print(dt)  # 2025-12-20 00:00:00 (datetime object)
```

### datetime.now() vs date.today()

| Method | Returns | Use When |
|--------|---------|----------|
| `datetime.now()` | Date + time | Need timestamps, time calculations |
| `date.today()` | Date only | Only date matters (birthdays, deadlines) |

```python
now = datetime.now()
print(now)  # 2025-12-20 14:30:45.123456

today = date.today()
print(today)  # 2025-12-20
```

### weekday() vs isoweekday()

| Method | Monday | Sunday |
|--------|--------|--------|
| `weekday()` | 0 | 6 |
| `isoweekday()` | 1 | 7 |

```python
dt = datetime(2025, 12, 22)  # Monday
print(dt.weekday())     # 0
print(dt.isoweekday())  # 1
```

### replace() vs timedelta arithmetic

| Method | Use For | Example |
|--------|---------|---------|
| `replace()` | Set exact values | "change to day 25" |
| `timedelta` | Relative changes | "add 5 days" |

```python
dt = datetime(2025, 12, 20, 14, 30)

# replace: set specific value
new_dt = dt.replace(day=25)
print(new_dt)  # 2025-12-25 14:30:00

# timedelta: add duration
new_dt = dt + timedelta(days=5)
print(new_dt)  # 2025-12-25 14:30:00
```

---

## Common Mistakes

### Mistake 1: Mutable Default Arguments
```python
# Wrong - datetime.now() evaluated once at function definition
def log_event(event, timestamp=datetime.now()):
    print(f"{event} at {timestamp}")

# Correct - evaluate at each call
def log_event(event, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()
    print(f"{event} at {timestamp}")
```

### Mistake 2: Modifying Immutable Objects
```python
# Wrong - datetime objects are immutable
dt = datetime(2025, 12, 20, 14, 30)
dt.hour = 10  # AttributeError!

# Correct - use replace()
new_dt = dt.replace(hour=10)
```

### Mistake 3: String Comparison Instead of Datetime
```python
# Wrong - string comparison is lexicographic
date3_str = "12/20/2025"
date4_str = "12/5/2025"
print(date3_str > date4_str)  # False (WRONG!)

# Correct - compare datetime objects
date3 = datetime.strptime("12/20/2025", '%m/%d/%Y')
date4 = datetime.strptime("12/5/2025", '%m/%d/%Y')
print(date3 > date4)  # True (CORRECT)
```

### Mistake 4: Not Handling strptime Exceptions
```python
# Wrong - crashes on invalid input
user_input = input("Enter date (YYYY-MM-DD): ")
dt = datetime.strptime(user_input, '%Y-%m-%d')  # CRASH!

# Correct - handle exceptions
def get_date_from_user():
    while True:
        user_input = input("Enter date (YYYY-MM-DD): ")
        try:
            dt = datetime.strptime(user_input, '%Y-%m-%d')
            return dt
        except ValueError:
            print("Invalid format. Please use YYYY-MM-DD")
```

---

## Best Practices

### 1. Always Use strftime() for Display
```python
# Bad
print(f"Meeting: {now}")  # 2025-12-20 14:30:45.123456

# Good
print(f"Meeting: {now.strftime('%B %d, %Y at %I:%M %p')}")
# Meeting: December 20, 2025 at 02:30 PM
```

### 2. Use ISO Format for Data Exchange
```python
# Universal standard, unambiguous, sortable
iso_string = dt.isoformat()  # 2025-12-20T14:30:45
```

### 3. Use timedelta for Date Math
```python
# Good - handles edge cases correctly
today = datetime(2025, 1, 31)
next_month = today + timedelta(days=30)

# Bad - manual addition breaks
# today.day += 30  # This doesn't work!
```

---

## Useful Patterns

### Check if Weekend
```python
today = datetime(2025, 12, 20)
if today.weekday() < 5:  # Monday-Friday are 0-4
    print("It's a workday")
else:
    print("It's the weekend!")
```

### First Day of Month
```python
today = datetime(2025, 12, 20)
first_day = today.replace(day=1)
print(first_day)  # 2025-12-01 00:00:00
```

### Last Day of Month
```python
from datetime import datetime, timedelta

today = datetime(2025, 12, 20)
if today.month == 12:
    next_month = today.replace(year=today.year + 1, month=1, day=1)
else:
    next_month = today.replace(month=today.month + 1, day=1)
last_day = next_month - timedelta(days=1)
print(last_day)  # 2025-12-31 00:00:00
```

### Find Next Monday
```python
current = datetime(2025, 12, 20)  # Saturday
days_until_monday = (7 - current.weekday()) % 7
if days_until_monday == 0:
    days_until_monday = 7
next_monday = current + timedelta(days=days_until_monday)
print(f"Next Monday: {next_monday.strftime('%B %d, %Y')}")
```

### Calculate Working Days
```python
start = datetime(2025, 12, 15)
end = datetime(2025, 12, 22)
working_days = 0
current_day = start

while current_day <= end:
    if current_day.weekday() < 5:
        working_days += 1
    current_day += timedelta(days=1)

print(f"Working days: {working_days}")
```

---

## Quick Reference

### Creating Objects
```python
date(2025, 12, 20)              # Date
time(14, 30, 45)                # Time
datetime(2025, 12, 20, 14, 30)  # DateTime
datetime.now()                  # Current datetime
date.today()                    # Current date
timedelta(days=7)               # Duration
```

### Common Operations

| Operation | Code |
|-----------|------|
| Current datetime | `datetime.now()` |
| Current date | `date.today()` |
| Add days | `dt + timedelta(days=n)` |
| Subtract days | `dt - timedelta(days=n)` |
| Difference | `dt1 - dt2` |
| Format | `dt.strftime(format)` |
| Parse | `datetime.strptime(str, format)` |
| Replace | `dt.replace(year=2026)` |
| To timestamp | `dt.timestamp()` |
| From timestamp | `datetime.fromtimestamp(ts)` |

### Method Comparison Table

| Method | Parameters | Returns | Use When |
|--------|-----------|---------|----------|
| `datetime.now()` | tz (optional) | datetime | Need current date+time |
| `date.today()` | None | date | Need current date only |
| `strftime()` | format (required) | str | Format for display |
| `strptime()` | string, format | datetime | Parse string to datetime |
| `timestamp()` | None | float | Convert to Unix time |
| `fromtimestamp()` | timestamp | datetime | Convert from Unix time |
| `timedelta()` | days, hours, etc | timedelta | Date arithmetic |
| `replace()` | year, month, etc | datetime | Set specific values |
| `weekday()` | None | int (0-6) | Get day of week |
| `isoweekday()` | None | int (1-7) | Get day of week (ISO) |
| `total_seconds()` | None | float | Duration to seconds |
