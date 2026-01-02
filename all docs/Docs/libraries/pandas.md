# Pandas Complete Guide

A comprehensive reference guide for the Pandas library in Python.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Core Components](#2-core-components)
3. [Fundamentals](#3-fundamentals)
4. [Functions and Methods Documentation](#4-functions-and-methods-documentation)
5. [Exception Handling](#5-exception-handling)
6. [Best Practices](#6-best-practices)
7. [Common Mistakes](#7-common-mistakes)
8. [Commonly Confused Concepts](#8-commonly-confused-concepts)
9. [Better Alternatives from Other Libraries](#9-better-alternatives-from-other-libraries)
10. [Method Comparison Table](#10-method-comparison-table)
11. [Quick Reference Summary](#11-quick-reference-summary)

---

## 1. Overview

### What is Pandas?

Pandas is a powerful, open-source Python library for data manipulation and analysis. Built on top of NumPy, it provides high-performance, easy-to-use data structures and tools for working with structured (tabular) data.

The name "Pandas" is derived from "Panel Data" - an econometrics term for multidimensional structured datasets.

### Main Purpose and Use Cases

- **Data Cleaning**: Handle missing values, duplicates, inconsistent formats
- **Data Transformation**: Reshape, merge, pivot, and aggregate data
- **Data Analysis**: Statistical analysis, grouping, filtering
- **Data I/O**: Read/write CSV, Excel, SQL, JSON, and more
- **Time Series Analysis**: Handle datetime data, resampling, rolling windows

### When to Use Pandas vs Alternatives

| Scenario | Use Pandas | Use Alternative |
|----------|------------|-----------------|
| Tabular data < 10GB | Yes | - |
| Large datasets > 10GB | - | Polars, Dask, PySpark |
| Numerical computing only | - | NumPy |
| Simple CSV reading | Yes | csv module (if minimal) |
| Real-time streaming | - | PySpark Streaming |
| GPU acceleration needed | - | cuDF (RAPIDS) |

### Installation

```python
# Using pip
pip install pandas

# Using conda
conda install pandas

# With all optional dependencies
pip install pandas[all]

# Verify installation
import pandas as pd
print(pd.__version__)
```

---

## 2. Core Components

### The Two Main Data Structures

#### Series (1-Dimensional)

A one-dimensional labeled array capable of holding any data type.

```python
import pandas as pd

# Creating a Series
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)
# Output:
# a    10
# b    20
# c    30
# d    40
# dtype: int64
```

#### DataFrame (2-Dimensional)

A two-dimensional labeled data structure with columns of potentially different types - like a spreadsheet or SQL table.

```python
import pandas as pd

# Creating a DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
})
print(df)
# Output:
#       name  age     city
# 0    Alice   25      NYC
# 1      Bob   30       LA
# 2  Charlie   35  Chicago
```

### How They Relate

DataFrame = Collection of Series (each column is a Series)

```
┌─────────────────────────────────────┐
│           DataFrame                 │
├──────────┬──────────┬───────────────┤
│  Series  │  Series  │    Series     │
│  (col1)  │  (col2)  │    (col3)     │
├──────────┼──────────┼───────────────┤
│   val1   │   val1   │     val1      │  ← Row (also accessible as Series)
│   val2   │   val2   │     val2      │
│   val3   │   val3   │     val3      │
└──────────┴──────────┴───────────────┘
```

### Most Common Workflow

```python
import pandas as pd

# 1. Load data
df = pd.read_csv('data.csv')

# 2. Explore data
df.head()           # First 5 rows
df.info()           # Data types and memory
df.describe()       # Statistical summary

# 3. Clean data
df.dropna()         # Remove missing values
df.drop_duplicates() # Remove duplicates

# 4. Transform data
df['new_col'] = df['col1'] * 2  # Create new column
df_filtered = df[df['col1'] > 10]  # Filter rows

# 5. Analyze data
df.groupby('category').mean()  # Group and aggregate

# 6. Export data
df.to_csv('output.csv', index=False)
```

---

## 3. Fundamentals

### 3.1 Basic Concepts

#### Importing Pandas

```python
import pandas as pd  # Standard convention
import numpy as np   # Often used together
```

#### Index - The Foundation

Every Pandas object has an Index - labels that identify each row.

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3]})
print(df.index)
# Output: RangeIndex(start=0, stop=3, step=1)

# Custom index
df = pd.DataFrame({'A': [1, 2, 3]}, index=['x', 'y', 'z'])
print(df)
# Output:
#    A
# x  1
# y  2
# z  3
```

#### Data Types (dtypes)

```python
import pandas as pd

df = pd.DataFrame({
    'integers': [1, 2, 3],
    'floats': [1.1, 2.2, 3.3],
    'strings': ['a', 'b', 'c'],
    'booleans': [True, False, True],
    'dates': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03'])
})

print(df.dtypes)
# Output:
# integers              int64
# floats              float64
# strings              object
# booleans               bool
# dates        datetime64[ns]
```

### 3.2 Creating DataFrames

#### From Dictionary

```python
import pandas as pd

# Dictionary of lists
df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30]
})

# Dictionary of Series
df = pd.DataFrame({
    'name': pd.Series(['Alice', 'Bob']),
    'age': pd.Series([25, 30])
})
```

#### From List of Dictionaries

```python
import pandas as pd

data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30}
]
df = pd.DataFrame(data)
```

#### From NumPy Array

```python
import pandas as pd
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
```

### 3.3 Viewing Data

```python
import pandas as pd

df = pd.DataFrame({
    'A': range(1, 101),
    'B': range(101, 201)
})

# First/last rows
df.head()      # First 5 rows (default)
df.head(10)    # First 10 rows
df.tail()      # Last 5 rows
df.tail(3)     # Last 3 rows

# Random sample
df.sample(5)   # 5 random rows
df.sample(frac=0.1)  # 10% of rows

# Shape and info
df.shape       # (100, 2) - rows, columns
df.columns     # Index(['A', 'B'], dtype='object')
df.index       # RangeIndex(start=0, stop=100, step=1)
df.info()      # Detailed info including memory usage
df.describe()  # Statistical summary
```

### 3.4 Selecting Data

#### Column Selection

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
})

# Single column (returns Series)
df['name']
df.name  # Dot notation (not recommended for new columns)

# Multiple columns (returns DataFrame)
df[['name', 'age']]
```

#### Row Selection with loc and iloc

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}, index=['a', 'b', 'c'])

# loc - Label-based selection
df.loc['a']              # Single row by label
df.loc[['a', 'b']]       # Multiple rows by label
df.loc['a':'b']          # Slice (inclusive!)
df.loc['a', 'name']      # Specific cell
df.loc['a':'b', 'name']  # Rows a-b, column 'name'

# iloc - Integer position-based selection
df.iloc[0]               # First row
df.iloc[[0, 1]]          # First two rows
df.iloc[0:2]             # Slice (exclusive end!)
df.iloc[0, 0]            # First cell
df.iloc[0:2, 0:1]        # Subset
```

#### Boolean Indexing (Filtering)

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'NYC']
})

# Single condition
df[df['age'] > 25]

# Multiple conditions (use & for AND, | for OR)
df[(df['age'] > 25) & (df['city'] == 'NYC')]

# Using isin()
df[df['city'].isin(['NYC', 'LA'])]

# Using query() - cleaner syntax
df.query('age > 25 and city == "NYC"')
```

### 3.5 Series Operations

#### Create Series with Custom Index

```python
import pandas as pd

data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)
print(series)
# Output:
# a    10
# b    20
# c    30
# d    40
# e    50
```

#### Access Values using loc (Location by Label)

```python
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# Access single value
print(series.loc['a'])  # Output: 10

# Access multiple values
print(series.loc[['a', 'c', 'e']])
# Output:
# a    10
# c    30
# e    50

# Change value using loc
series.loc['a'] = 100
print(series.loc['a'])  # Output: 100
```

#### Access Values using iloc (Integer Location)

```python
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# Access by position
print(series.iloc[0])  # Output: 10 (first element)
print(series.iloc[2])  # Output: 30 (third element)

# Access multiple positions
print(series.iloc[[0, 2, 4]])
# Output:
# a    10
# c    30
# e    50

# Slicing by position
print(series.iloc[1:4])
# Output:
# b    20
# c    30
# d    40
```

#### Filter Series by Value

```python
series = pd.Series([5, 15, 25, 35, 45], index=['a', 'b', 'c', 'd', 'e'])

# Filter values less than 30
filtered = series[series < 30]
print(filtered)
# Output:
# a     5
# b    15
# c    25

# Filter values greater than 20
filtered = series[series > 20]
print(filtered)
# Output:
# c    25
# d    35
# e    45
```

#### Create Series from Dictionary

```python
data_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
series = pd.Series(data_dict)
print(series)
# Output:
# a    10
# b    20
# c    30
# d    40
```

### 3.6 DataFrame Operations

#### Add New Column

```python
df = pd.DataFrame({
    'Name': ['John', 'Sarah', 'Mike'],
    'Age': [25, 30, 35]
})

# Add new column with same value for all
df['Country'] = 'USA'

# Add new column with calculation
df['Age_Plus_10'] = df['Age'] + 10
print(df)
# Output:
#     Name  Age Country  Age_Plus_10
# 0   John   25     USA           35
# 1  Sarah   30     USA           40
# 2   Mike   35     USA           45
```

#### Add New Row using concat()

```python
df = pd.DataFrame({
    'Name': ['John', 'Sarah'],
    'Age': [25, 30]
})

# Create new row as DataFrame
new_row = pd.DataFrame({'Name': ['Mike'], 'Age': [35]})

# Concatenate (append row)
df = pd.concat([df, new_row], ignore_index=True)
print(df)
# Output:
#     Name  Age
# 0   John   25
# 1  Sarah   30
# 2   Mike   35
```

#### Filter by Exact Value

```python
df = pd.DataFrame({
    'Name': ['John', 'Sarah', 'Mike', 'Emma'],
    'Age': [25, 30, 35, 28],
    'City': ['NY', 'LA', 'Chicago', 'NY']
})

# Filter exact value
ny_people = df[df['City'] == 'NY']
print(ny_people)
# Output:
#     Name  Age City
# 0   John   25   NY
# 3   Emma   28   NY
```

#### Multiple Conditions with Operators

```python
df = pd.DataFrame({
    'Name': ['John', 'Sarah', 'Mike', 'Emma'],
    'Age': [25, 30, 35, 28],
    'City': ['NY', 'LA', 'Chicago', 'Boston']
})

# OR condition (|)
result = df[(df['City'] == 'NY') | (df['City'] == 'LA')]
print(result)
# Output:
#     Name  Age City
# 0   John   25   NY
# 1  Sarah   30   LA

# AND condition (&)
result = df[(df['Age'] > 25) & (df['City'] == 'Chicago')]
print(result)
# Output:
#     Name  Age     City
# 2   Mike   35  Chicago

# NOT condition (~)
result = df[~(df['City'] == 'NY')]
print(result)
# Output:
#     Name  Age     City
# 1  Sarah   30       LA
# 2   Mike   35  Chicago
# 3   Emma   28   Boston
```

---

## 4. Functions and Methods Documentation

### 4.1 Data Loading Functions

#### pd.read_csv()

**Purpose**: Read a comma-separated values (CSV) file into a DataFrame.

**Syntax**:
```python
pd.read_csv(filepath, sep=',', header=0, names=None, index_col=None,
            usecols=None, dtype=None, na_values=None, parse_dates=False,
            nrows=None, skiprows=None, encoding='utf-8')
```

**Key Parameters**:
- `filepath` (str/path): Path to CSV file or URL - **REQUIRED**
- `sep` (str): Delimiter to use - Optional (default: ',')
- `header` (int/list): Row(s) to use as column names - Optional (default: 0)
- `names` (list): Column names to use - Optional (default: None)
- `index_col` (int/str/list): Column(s) to set as index - Optional (default: None)
- `usecols` (list): Columns to read - Optional (default: None, reads all)
- `dtype` (dict): Data types for columns - Optional (default: inferred)
- `na_values` (list): Additional values to treat as NA - Optional
- `parse_dates` (list/bool): Columns to parse as dates - Optional (default: False)
- `nrows` (int): Number of rows to read - Optional (default: None, reads all)
- `skiprows` (int/list): Rows to skip - Optional (default: None)
- `encoding` (str): File encoding - Optional (default: 'utf-8')

**Returns**: DataFrame containing the CSV data.

**Basic Example**:
```python
import pandas as pd

df = pd.read_csv('sales.csv')
print(df.head())
# Output:
#    product  quantity  price
# 0   Widget       100  19.99
# 1   Gadget        50  29.99
```

**Real-World Example**:
```python
import pandas as pd

# Reading a complex CSV with various options
df = pd.read_csv(
    'sales_data.csv',
    sep=';',                          # Semicolon-separated
    usecols=['date', 'product', 'revenue'],  # Only specific columns
    parse_dates=['date'],             # Parse date column
    dtype={'revenue': float},         # Ensure revenue is float
    na_values=['N/A', 'missing'],     # Treat these as NA
    nrows=1000                        # Read only first 1000 rows
)
```

**When to Use**: Loading tabular data from CSV files - the most common data import method.

---

#### pd.read_excel()

**Purpose**: Read an Excel file into a DataFrame.

**Syntax**:
```python
pd.read_excel(filepath, sheet_name=0, header=0, names=None,
              index_col=None, usecols=None, dtype=None, na_values=None)
```

**Key Parameters**:
- `filepath` (str/path): Path to Excel file - **REQUIRED**
- `sheet_name` (str/int/list): Sheet to read - Optional (default: 0, first sheet)
- `header` (int/list): Row(s) for column names - Optional (default: 0)
- `usecols` (str/list): Columns to read (e.g., 'A:C' or [0,1,2]) - Optional

**Returns**: DataFrame or dict of DataFrames (if multiple sheets).

**Basic Example**:
```python
import pandas as pd

df = pd.read_excel('report.xlsx')
print(df.head())
```

**Real-World Example**:
```python
import pandas as pd

# Read specific sheet with column selection
df = pd.read_excel(
    'quarterly_report.xlsx',
    sheet_name='Q1 Sales',
    usecols='A:D',
    header=1,
    na_values=['#N/A', '-']
)

# Read all sheets into dictionary
all_sheets = pd.read_excel('report.xlsx', sheet_name=None)
for sheet_name, data in all_sheets.items():
    print(f"{sheet_name}: {len(data)} rows")
```

---

#### pd.read_json()

**Purpose**: Read a JSON file or string into a DataFrame.

**Syntax**:
```python
pd.read_json(path_or_buf, orient=None, dtype=None, lines=False)
```

**Key Parameters**:
- `path_or_buf` (str/path): JSON file path, URL, or string - **REQUIRED**
- `orient` (str): Expected JSON format - Optional (default: inferred)
  - `'records'`: list of dicts `[{col1: val1, col2: val2}, ...]`
  - `'columns'`: dict of dicts `{col: {idx: val}}`
  - `'index'`: dict of dicts `{idx: {col: val}}`
- `lines` (bool): Read file as JSON Lines - Optional (default: False)

**Returns**: DataFrame containing the JSON data.

**Basic Example**:
```python
import pandas as pd

df = pd.read_json('data.json')
print(df)
```

**Real-World Example**:
```python
import pandas as pd

# Reading JSON Lines (common in log files and APIs)
df = pd.read_json('events.jsonl', lines=True)
```

---

#### pd.read_sql()

**Purpose**: Read SQL query or table into a DataFrame.

**Syntax**:
```python
pd.read_sql(sql, con, index_col=None, params=None, parse_dates=None)
```

**Key Parameters**:
- `sql` (str): SQL query or table name - **REQUIRED**
- `con` (connection): Database connection object - **REQUIRED**
- `index_col` (str/list): Column(s) for index - Optional (default: None)
- `params` (list/dict): Parameters for SQL query - Optional

**Returns**: DataFrame containing the query results.

**Basic Example**:
```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('database.db')
df = pd.read_sql('SELECT * FROM customers', conn)
conn.close()
```

**Real-World Example**:
```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://user:pass@localhost/mydb')

# Parameterized query (safe from SQL injection)
query = """
    SELECT customer_id, name, total_orders
    FROM customers
    WHERE signup_date > %(start_date)s
    AND region = %(region)s
"""
params = {'start_date': '2023-01-01', 'region': 'East'}

df = pd.read_sql(query, engine, params=params, parse_dates=['signup_date'])
```

---

### 4.2 Data Exploration Methods

#### df.head() / df.tail()

**Purpose**: View the first/last n rows of the DataFrame.

**Syntax**:
```python
df.head(n=5)
df.tail(n=5)
```

**Key Parameters**:
- `n` (int): Number of rows to return - Optional (default: 5)

**Returns**: DataFrame with first/last n rows.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({'A': range(100), 'B': range(100, 200)})

print(df.head())     # First 5 rows
print(df.tail(3))    # Last 3 rows
```

---

#### df.info()

**Purpose**: Print concise summary of DataFrame including dtypes, non-null counts, and memory usage.

**Syntax**:
```python
df.info(verbose=True, show_counts=True, memory_usage=True)
```

**Returns**: None (prints to console).

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', None],
    'age': [25, 30, 35],
    'salary': [50000.0, 60000.0, 70000.0]
})

df.info()
# Output:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   name    2 non-null      object
#  1   age     3 non-null      int64
#  2   salary  3 non-null      float64
# dtypes: float64(1), int64(1), object(1)
# memory usage: 200.0+ bytes
```

---

#### df.describe()

**Purpose**: Generate descriptive statistics of numerical columns.

**Syntax**:
```python
df.describe(percentiles=None, include=None, exclude=None)
```

**Key Parameters**:
- `percentiles` (list): Percentiles to include - Optional (default: [.25, .5, .75])
- `include` (list/'all'): Data types to include - Optional (default: numeric only)

**Returns**: DataFrame with statistical summary.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'age': [25, 30, 35, 40, 45],
    'salary': [50000, 60000, 70000, 80000, 90000]
})

print(df.describe())
# Output:
#              age        salary
# count   5.000000      5.000000
# mean   35.000000  70000.000000
# std     7.905694  15811.388301
# min    25.000000  50000.000000
# 25%    30.000000  60000.000000
# 50%    35.000000  70000.000000
# 75%    40.000000  80000.000000
# max    45.000000  90000.000000
```

---

#### df.value_counts()

**Purpose**: Count unique values in a column/Series.

**Syntax**:
```python
df['column'].value_counts(normalize=False, sort=True, ascending=False, dropna=True)
```

**Key Parameters**:
- `normalize` (bool): Return proportions instead of counts - Optional (default: False)
- `sort` (bool): Sort by counts - Optional (default: True)
- `dropna` (bool): Exclude NA values - Optional (default: True)

**Returns**: Series with counts of unique values.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'city': ['NYC', 'LA', 'NYC', 'Chicago', 'NYC', 'LA']
})

print(df['city'].value_counts())
# Output:
# NYC        3
# LA         2
# Chicago    1
# Name: city, dtype: int64
```

---

#### df.unique() / df.nunique()

**Purpose**: Get unique values or count of unique values.

**Syntax**:
```python
df['column'].unique()     # Returns array of unique values
df['column'].nunique()    # Returns count of unique values
df.nunique()              # Count uniques for all columns
```

**Returns**:
- `unique()`: ndarray of unique values
- `nunique()`: int (for Series) or Series (for DataFrame)

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'city': ['NYC', 'LA', 'NYC', 'Chicago'],
    'state': ['NY', 'CA', 'NY', 'IL']
})

print(df['city'].unique())
# Output: array(['NYC', 'LA', 'Chicago'], dtype=object)

print(df['city'].nunique())
# Output: 3

print(df.nunique())
# Output:
# city     3
# state    3
# dtype: int64
```

---

### 4.3 Data Selection and Filtering

#### df.loc[]

**Purpose**: Access rows and columns by labels/boolean arrays.

**Syntax**:
```python
df.loc[row_label]                    # Single row
df.loc[row_label, col_label]         # Single cell
df.loc[row_labels, col_labels]       # Multiple rows/cols
df.loc[boolean_array]                # Filter rows
df.loc[start:end]                    # Slice (inclusive!)
```

**Returns**: Series, DataFrame, or scalar depending on selection.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}, index=['a', 'b', 'c'])

# Single row
print(df.loc['a'])
# Output:
# name    Alice
# age        25
# city      NYC
# Name: a, dtype: object

# Specific cell
print(df.loc['a', 'name'])
# Output: Alice

# Multiple rows and columns
print(df.loc[['a', 'b'], ['name', 'age']])
# Output:
#     name  age
# a  Alice   25
# b    Bob   30
```

---

#### df.iloc[]

**Purpose**: Access rows and columns by integer position.

**Syntax**:
```python
df.iloc[row_pos]                     # Single row
df.iloc[row_pos, col_pos]            # Single cell
df.iloc[row_positions, col_positions]  # Multiple
df.iloc[start:end]                   # Slice (exclusive end!)
```

**Returns**: Series, DataFrame, or scalar depending on selection.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
})

# First row
print(df.iloc[0])

# First two rows, first two columns
print(df.iloc[0:2, 0:2])
# Output:
#     name  age
# 0  Alice   25
# 1    Bob   30

# Last row
print(df.iloc[-1])
```

---

#### df.query()

**Purpose**: Filter DataFrame using a query string expression.

**Syntax**:
```python
df.query(expr, inplace=False)
```

**Key Parameters**:
- `expr` (str): Query expression - **REQUIRED**
- `inplace` (bool): Modify in place - Optional (default: False)

**Returns**: Filtered DataFrame.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
})

# Simple query
result = df.query('age > 25')
print(result)
# Output:
#       name  age  salary
# 1      Bob   30   60000
# 2  Charlie   35   70000
```

**Real-World Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'product': ['Widget', 'Gadget', 'Gizmo', 'Tool'],
    'category': ['A', 'B', 'A', 'B'],
    'price': [19.99, 29.99, 9.99, 49.99],
    'in_stock': [True, True, False, True]
})

# Complex query with variable
min_price = 15
result = df.query('price > @min_price and in_stock == True')
print(result)
```

---

#### df.isin()

**Purpose**: Check if values are contained in a list.

**Syntax**:
```python
df['column'].isin(values)
df.isin(values)  # For entire DataFrame
```

**Returns**: Boolean Series/DataFrame.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'city': ['NYC', 'LA', 'Chicago', 'Boston', 'Miami'],
    'region': ['East', 'West', 'Central', 'East', 'South']
})

# Filter for specific cities
mask = df['city'].isin(['NYC', 'LA', 'Miami'])
print(df[mask])
# Output:
#    city region
# 0   NYC   East
# 1    LA   West
# 4  Miami  South
```

---

### 4.4 Data Cleaning Methods

#### df.isna() / df.isnull() / df.notna()

**Purpose**: Detect missing values.

**Syntax**:
```python
df.isna()     # True where values are NA
df.isnull()   # Alias for isna()
df.notna()    # True where values are NOT NA
```

**Returns**: Boolean DataFrame/Series of same shape.

**Basic Example**:
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan]
})

print(df.isna())
# Output:
#        A      B
# 0  False  False
# 1   True  False
# 2  False   True

# Count missing values per column
print(df.isna().sum())
# Output:
# A    1
# B    1
# dtype: int64

# Percentage of missing values
print(df.isna().mean() * 100)
```

---

#### df.dropna()

**Purpose**: Remove missing values.

**Syntax**:
```python
df.dropna(axis=0, how='any', subset=None, thresh=None, inplace=False)
```

**Key Parameters**:
- `axis` (0 or 1): 0 = drop rows, 1 = drop columns - Optional (default: 0)
- `how` ('any'/'all'): 'any' = drop if any NA, 'all' = drop if all NA - Optional (default: 'any')
- `subset` (list): Only consider these columns - Optional (default: all)
- `thresh` (int): Require this many non-NA values - Optional

**Returns**: DataFrame with NA values removed.

**Basic Example**:
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3, 4],
    'B': [5, 6, np.nan, 8],
    'C': [9, 10, 11, 12]
})

# Drop rows with any NA
print(df.dropna())
# Output:
#      A    B   C
# 0  1.0  5.0   9
# 3  4.0  8.0  12
```

---

#### df.fillna()

**Purpose**: Fill missing values with specified value or method.

**Syntax**:
```python
df.fillna(value=None, method=None, axis=None, inplace=False, limit=None)
```

**Key Parameters**:
- `value` (scalar/dict/Series/DataFrame): Value to fill - Optional
- `method` ('ffill'/'bfill'): Forward/backward fill - Optional
- `inplace` (bool): Modify in place - Optional (default: False)

**Returns**: DataFrame with NA values filled.

**Basic Example**:
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [np.nan, 5, np.nan]
})

# Fill with a constant
print(df.fillna(0))
# Output:
#      A    B
# 0  1.0  0.0
# 1  0.0  5.0
# 2  3.0  0.0
```

**Real-World Example**:
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'product': ['Widget', 'Gadget', 'Gizmo'],
    'price': [19.99, np.nan, 9.99],
    'category': ['A', 'B', np.nan],
    'rating': [4.5, np.nan, np.nan]
})

# Fill different columns with different values
fill_values = {
    'price': df['price'].median(),
    'category': 'Unknown',
    'rating': df['rating'].mean()
}
df_filled = df.fillna(fill_values)
print(df_filled)
```

---

#### df.drop_duplicates()

**Purpose**: Remove duplicate rows.

**Syntax**:
```python
df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
```

**Key Parameters**:
- `subset` (list): Columns to consider for duplicates - Optional (default: all)
- `keep` ('first'/'last'/False): Which duplicate to keep - Optional (default: 'first')
- `ignore_index` (bool): Reset index after drop - Optional (default: False)

**Returns**: DataFrame with duplicates removed.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Alice', 'Charlie'],
    'age': [25, 30, 25, 35]
})

print(df.drop_duplicates())
# Output:
#       name  age
# 0    Alice   25
# 1      Bob   30
# 3  Charlie   35
```

---

#### df.replace()

**Purpose**: Replace values in DataFrame.

**Syntax**:
```python
df.replace(to_replace=None, value=None, inplace=False, regex=False)
```

**Key Parameters**:
- `to_replace` (str/list/dict/regex): Values to replace - **REQUIRED**
- `value` (scalar/dict/list): Replacement value(s) - Optional
- `regex` (bool): Interpret to_replace as regex - Optional (default: False)

**Returns**: DataFrame with replaced values.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'status': ['active', 'inactive', 'pending', 'active'],
    'code': [1, 2, 3, 1]
})

# Simple replacement
df_replaced = df.replace('inactive', 'disabled')

# Multiple replacements with dict
df_replaced = df.replace({'active': 1, 'inactive': 0, 'pending': -1})
```

---

#### df.rename()

**Purpose**: Rename columns or index labels.

**Syntax**:
```python
df.rename(mapper=None, columns=None, index=None, inplace=False)
```

**Key Parameters**:
- `columns` (dict): Column renaming {old: new} - Optional
- `index` (dict): Index renaming {old: new} - Optional

**Returns**: DataFrame with renamed labels.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'old_name': [1, 2, 3],
    'another_col': [4, 5, 6]
})

# Rename specific columns
df_renamed = df.rename(columns={'old_name': 'new_name'})

# Using a function
df_renamed = df.rename(columns=str.upper)
# Output: Columns are now 'OLD_NAME', 'ANOTHER_COL'
```

---

#### df.astype()

**Purpose**: Cast DataFrame columns to a specified data type.

**Syntax**:
```python
df.astype(dtype, copy=True, errors='raise')
```

**Key Parameters**:
- `dtype` (type/dict): Data type or {column: type} - **REQUIRED**
- `errors` ('raise'/'ignore'): Handle conversion errors - Optional (default: 'raise')

**Returns**: DataFrame with converted types.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'A': ['1', '2', '3'],
    'B': [1.5, 2.5, 3.5]
})

# Convert single column
df['A'] = df['A'].astype(int)

# Convert multiple columns
df = df.astype({'A': int, 'B': int})
print(df.dtypes)
```

---

### 4.5 Data Transformation Methods

#### df.apply()

**Purpose**: Apply a function along an axis of the DataFrame.

**Syntax**:
```python
df.apply(func, axis=0, raw=False, result_type=None, args=(), **kwargs)
```

**Key Parameters**:
- `func` (function): Function to apply - **REQUIRED**
- `axis` (0 or 1): 0 = apply to columns, 1 = apply to rows - Optional (default: 0)

**Returns**: Series or DataFrame depending on function output.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Apply to each column
print(df.apply(sum))
# Output:
# A     6
# B    15
# dtype: int64

# Apply to each row
print(df.apply(sum, axis=1))
# Output:
# 0    5
# 1    7
# 2    9
# dtype: int64
```

---

#### Series.map()

**Purpose**: Map values of Series using a dict, function, or Series.

**Syntax**:
```python
series.map(arg, na_action=None)
```

**Key Parameters**:
- `arg` (dict/function/Series): Mapping correspondence - **REQUIRED**
- `na_action` (None/'ignore'): How to handle NA - Optional (default: None)

**Returns**: Series with mapped values.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'grade': ['A', 'B', 'C', 'A', 'B']
})

# Map using dictionary
grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0}
df['gpa'] = df['grade'].map(grade_points)
print(df)
# Output:
#   grade  gpa
# 0     A  4.0
# 1     B  3.0
# 2     C  2.0
# 3     A  4.0
# 4     B  3.0
```

---

#### df.sort_values()

**Purpose**: Sort DataFrame by values of one or more columns.

**Syntax**:
```python
df.sort_values(by, axis=0, ascending=True, inplace=False,
               na_position='last', ignore_index=False)
```

**Key Parameters**:
- `by` (str/list): Column(s) to sort by - **REQUIRED**
- `ascending` (bool/list): Sort order - Optional (default: True)
- `na_position` ('first'/'last'): Position of NAs - Optional (default: 'last')

**Returns**: Sorted DataFrame.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Charlie', 'Alice', 'Bob'],
    'age': [35, 25, 30]
})

# Sort by single column
print(df.sort_values('age'))
# Output:
#       name  age
# 1    Alice   25
# 2      Bob   30
# 0  Charlie   35
```

---

#### df.groupby()

**Purpose**: Group DataFrame by one or more columns and apply aggregate functions.

**Syntax**:
```python
df.groupby(by=None, axis=0, as_index=True, sort=True, dropna=True)
```

**Key Parameters**:
- `by` (str/list/dict): Column(s) to group by - **REQUIRED**
- `as_index` (bool): Use group keys as index - Optional (default: True)

**Returns**: DataFrameGroupBy object (apply aggregation methods).

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A'],
    'value': [10, 20, 30, 40, 50]
})

# Group and aggregate
print(df.groupby('category').sum())
# Output:
#           value
# category
# A            90
# B            60

# Multiple aggregations
print(df.groupby('category').agg(['sum', 'mean', 'count']))
```

**Real-World Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'region': ['East', 'West', 'East', 'West', 'East'],
    'product': ['Widget', 'Widget', 'Gadget', 'Gadget', 'Widget'],
    'sales': [100, 150, 200, 175, 125],
    'quantity': [10, 15, 20, 18, 12]
})

# Named aggregations
summary = df.groupby('region').agg(
    total_sales=('sales', 'sum'),
    avg_sales=('sales', 'mean'),
    order_count=('sales', 'count')
)
print(summary)
```

---

#### df.pivot_table()

**Purpose**: Create a spreadsheet-style pivot table as a DataFrame.

**Syntax**:
```python
pd.pivot_table(df, values=None, index=None, columns=None,
               aggfunc='mean', fill_value=None, margins=False)
```

**Key Parameters**:
- `values` (str/list): Column(s) to aggregate - Optional
- `index` (str/list): Row grouping - Optional
- `columns` (str/list): Column grouping - Optional
- `aggfunc` (func/dict): Aggregation function - Optional (default: 'mean')
- `margins` (bool): Add row/column totals - Optional (default: False)

**Returns**: Pivot table as DataFrame.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'region': ['East', 'West', 'East', 'West'],
    'product': ['A', 'A', 'B', 'B'],
    'sales': [100, 150, 200, 175]
})

pivot = pd.pivot_table(df, values='sales', index='region', columns='product')
print(pivot)
# Output:
# product      A      B
# region
# East     100.0  200.0
# West     150.0  175.0
```

---

#### df.melt()

**Purpose**: Unpivot DataFrame from wide to long format.

**Syntax**:
```python
pd.melt(df, id_vars=None, value_vars=None, var_name=None, value_name='value')
```

**Key Parameters**:
- `id_vars` (list): Columns to keep as identifiers - Optional
- `value_vars` (list): Columns to unpivot - Optional (default: all not in id_vars)
- `var_name` (str): Name for variable column - Optional (default: 'variable')
- `value_name` (str): Name for value column - Optional (default: 'value')

**Returns**: Unpivoted DataFrame (long format).

**Basic Example**:
```python
import pandas as pd

# Wide format
df_wide = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'math': [90, 85],
    'english': [88, 92],
    'science': [95, 80]
})

# Convert to long format
df_long = pd.melt(
    df_wide,
    id_vars=['name'],
    value_vars=['math', 'english', 'science'],
    var_name='subject',
    value_name='score'
)
print(df_long)
# Output:
#     name  subject  score
# 0  Alice     math     90
# 1    Bob     math     85
# 2  Alice  english     88
# 3    Bob  english     92
# 4  Alice  science     95
# 5    Bob  science     80
```

---

#### pd.merge()

**Purpose**: Merge DataFrame objects by performing database-style joins.

**Syntax**:
```python
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, suffixes=('_x', '_y'))
```

**Key Parameters**:
- `left` (DataFrame): Left DataFrame - **REQUIRED**
- `right` (DataFrame): Right DataFrame - **REQUIRED**
- `how` ('inner'/'outer'/'left'/'right'): Join type - Optional (default: 'inner')
- `on` (str/list): Columns to join on (must exist in both) - Optional
- `left_on` (str/list): Left DataFrame join columns - Optional
- `right_on` (str/list): Right DataFrame join columns - Optional

**Returns**: Merged DataFrame.

**Basic Example**:
```python
import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'id': [1, 2, 4],
    'salary': [50000, 60000, 70000]
})

# Inner join (only matching rows)
result = pd.merge(df1, df2, on='id', how='inner')
print(result)
# Output:
#    id   name  salary
# 0   1  Alice   50000
# 1   2    Bob   60000
```

---

#### pd.concat()

**Purpose**: Concatenate DataFrames along an axis.

**Syntax**:
```python
pd.concat(objs, axis=0, join='outer', ignore_index=False, keys=None)
```

**Key Parameters**:
- `objs` (list): Sequence of DataFrames - **REQUIRED**
- `axis` (0 or 1): 0 = stack vertically, 1 = stack horizontally - Optional (default: 0)
- `ignore_index` (bool): Reset index - Optional (default: False)

**Returns**: Concatenated DataFrame.

**Basic Example**:
```python
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Vertical concatenation (stack rows)
result = pd.concat([df1, df2], ignore_index=True)
print(result)
# Output:
#    A  B
# 0  1  3
# 1  2  4
# 2  5  7
# 3  6  8

# Horizontal concatenation (stack columns)
result = pd.concat([df1, df2], axis=1)
print(result)
```

---

### 4.6 String Methods

#### Series.str accessor

**Purpose**: Access string methods for Series containing string data.

**Common String Methods**:
```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice Smith', 'Bob Jones', 'Charlie Brown'],
    'email': ['alice@example.com', 'BOB@EXAMPLE.COM', 'charlie@example.com']
})

# Case conversion
df['name'].str.lower()           # 'alice smith'
df['name'].str.upper()           # 'ALICE SMITH'
df['name'].str.title()           # 'Alice Smith'

# String operations
df['name'].str.len()             # Length of each string
df['name'].str.strip()           # Remove whitespace
df['name'].str.replace(' ', '_') # Replace characters
df['name'].str.split(' ')        # Split into list

# Extraction and matching
df['name'].str.contains('Smith')      # Boolean mask
df['name'].str.startswith('A')        # Boolean mask
df['name'].str.endswith('Brown')      # Boolean mask

# Getting parts
df['name'].str[0]               # First character
df['name'].str[:5]              # First 5 characters
df['name'].str.split(' ').str[0]  # First word
```

**Real-World Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'full_name': ['  John DOE  ', 'jane SMITH', 'Bob Brown Jr.'],
    'email': ['john@company.com', 'jane@company.com', 'bob.brown@company.com'],
    'phone': ['(123) 456-7890', '987-654-3210', '555.123.4567']
})

# Clean and standardize names
df['clean_name'] = df['full_name'].str.strip().str.title()

# Extract domain from email
df['domain'] = df['email'].str.split('@').str[1]

# Clean phone numbers (remove non-digits)
df['phone_clean'] = df['phone'].str.replace(r'[^\d]', '', regex=True)

# Extract first name
df['first_name'] = df['clean_name'].str.split().str[0]
```

---

### 4.7 Date/Time Methods

#### pd.to_datetime()

**Purpose**: Convert argument to datetime.

**Syntax**:
```python
pd.to_datetime(arg, format=None, errors='raise', dayfirst=False, yearfirst=False)
```

**Key Parameters**:
- `arg` (str/list/Series): Date(s) to convert - **REQUIRED**
- `format` (str): Strftime format string - Optional (auto-inferred)
- `errors` ('raise'/'coerce'/'ignore'): Error handling - Optional (default: 'raise')
- `dayfirst` (bool): Interpret as day first (DD/MM) - Optional (default: False)

**Returns**: Datetime object, DatetimeIndex, or Series.

**Basic Example**:
```python
import pandas as pd

# Single date
date = pd.to_datetime('2023-01-15')
print(date)
# Output: 2023-01-15 00:00:00

# Series of dates
dates = pd.to_datetime(['2023-01-15', '2023-02-20', '2023-03-25'])
print(dates)
```

**Real-World Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'date_str': ['01/15/2023', '02/20/2023', 'invalid', '03/25/2023'],
    'timestamp': [1673740800, 1676851200, 1679702400, 1679961600]
})

# Convert string dates (with error handling)
df['date'] = pd.to_datetime(df['date_str'], format='%m/%d/%Y', errors='coerce')
# Note: 'invalid' becomes NaT (Not a Time)

# Convert Unix timestamps
df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')
```

---

#### Series.dt accessor

**Purpose**: Access datetime properties and methods.

**Common Datetime Properties**:
```python
import pandas as pd

df = pd.DataFrame({
    'datetime': pd.to_datetime(['2023-06-15 14:30:00', '2023-12-25 09:00:00'])
})

# Date components
df['datetime'].dt.year          # 2023
df['datetime'].dt.month         # 6, 12
df['datetime'].dt.day           # 15, 25
df['datetime'].dt.hour          # 14, 9
df['datetime'].dt.minute        # 30, 0

# Derived properties
df['datetime'].dt.dayofweek     # 0-6 (Monday=0)
df['datetime'].dt.day_name()    # 'Thursday', 'Monday'
df['datetime'].dt.month_name()  # 'June', 'December'
df['datetime'].dt.quarter       # 2, 4
df['datetime'].dt.is_month_end  # False, False
df['datetime'].dt.is_leap_year  # False

# Date only
df['datetime'].dt.date          # date object
df['datetime'].dt.normalize()   # Midnight timestamp
```

**Real-World Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'order_date': pd.date_range('2023-01-01', periods=100, freq='D')
})

# Extract date components for analysis
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df['week'] = df['order_date'].dt.isocalendar().week
df['day_of_week'] = df['order_date'].dt.day_name()
df['is_weekend'] = df['order_date'].dt.dayofweek >= 5

# Group by month
monthly_counts = df.groupby(df['order_date'].dt.to_period('M')).size()
print(monthly_counts)
```

---

### 4.8 Data Export Methods

#### df.to_csv()

**Purpose**: Write DataFrame to a CSV file.

**Syntax**:
```python
df.to_csv(path, sep=',', header=True, index=True, columns=None,
          encoding='utf-8', na_rep='', date_format=None)
```

**Key Parameters**:
- `path` (str/path): File path or None (returns string) - **REQUIRED**
- `sep` (str): Field separator - Optional (default: ',')
- `header` (bool/list): Write column names - Optional (default: True)
- `index` (bool): Write row index - Optional (default: True)
- `na_rep` (str): String for missing values - Optional (default: '')

**Returns**: None (writes file) or string if path is None.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30]
})

# Write to file (no index column)
df.to_csv('output.csv', index=False)
```

---

#### df.to_excel()

**Purpose**: Write DataFrame to an Excel file.

**Syntax**:
```python
df.to_excel(path, sheet_name='Sheet1', index=True, header=True,
            startrow=0, startcol=0, engine=None)
```

**Key Parameters**:
- `path` (str/ExcelWriter): File path - **REQUIRED**
- `sheet_name` (str): Name of sheet - Optional (default: 'Sheet1')
- `index` (bool): Write row index - Optional (default: True)

**Returns**: None (writes file).

**Real-World Example**:
```python
import pandas as pd

# Multiple sheets in one file
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})

with pd.ExcelWriter('multi_sheet.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
```

---

#### df.to_json()

**Purpose**: Convert DataFrame to JSON string or file.

**Syntax**:
```python
df.to_json(path=None, orient='columns', date_format='epoch',
           lines=False, indent=None)
```

**Key Parameters**:
- `path` (str): File path or None (returns string) - Optional
- `orient` (str): JSON format - Optional (default: 'columns')
  - `'records'`: `[{col1: val1, col2: val2}, ...]`
  - `'columns'`: `{col1: {idx1: val1, ...}, ...}`
- `lines` (bool): Write JSON Lines format - Optional (default: False)

**Returns**: None (writes file) or JSON string.

**Basic Example**:
```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30]
})

# To JSON string
json_str = df.to_json(orient='records', indent=2)
print(json_str)
# Output:
# [
#   {"name": "Alice", "age": 25},
#   {"name": "Bob", "age": 30}
# ]
```

---

### 4.9 Aggregate Functions

#### Aggregate Functions for Entire DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    'Sales': [100, 150, 200, 175],
    'Profit': [20, 30, 50, 40],
    'Quantity': [5, 10, 15, 12]
})

# Sum of all numeric columns
print(df.sum())
# Output:
# Sales       625
# Profit      140
# Quantity     42

# Mean of all numeric columns
print(df.mean())
# Output:
# Sales       156.25
# Profit       35.00
# Quantity     10.50

# Maximum values
print(df.max())

# Minimum values
print(df.min())

# Count non-null values
print(df.count())

# Standard deviation
print(df.std())

# Median
print(df.median())
```

#### Aggregate Functions for Single Column

```python
import pandas as pd

df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [100, 150, 200, 175],
    'Profit': [20, 30, 50, 40]
})

# Sum of single column
print(df['Sales'].sum())        # Output: 625

# Mean of single column
print(df['Sales'].mean())       # Output: 156.25

# Median
print(df['Sales'].median())     # Output: 162.5

# Min and Max
print(df['Sales'].min())        # Output: 100
print(df['Sales'].max())        # Output: 200

# Quantile (percentile)
print(df['Sales'].quantile(0.25))  # 25th percentile

# Mode (most frequent value)
print(df['Sales'].mode())
```

#### Multiple Aggregations at Once using agg()

```python
import pandas as pd

df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [100, 150, 200, 175],
    'Profit': [20, 30, 50, 40]
})

# Multiple aggregations on single column
result = df['Sales'].agg(['sum', 'mean', 'max', 'min'])
print(result)
# Output:
# sum     625.00
# mean    156.25
# max     200.00
# min     100.00

# Different aggregations for different columns
result = df.agg({
    'Sales': ['sum', 'mean'],
    'Profit': ['min', 'max']
})
print(result)
```

---

## 5. Exception Handling

### 5.1 File Reading Errors

**Basic Usage**:
```python
import pandas as pd

df = pd.read_csv('data.csv')  # May fail
```

**Problem**: File might not exist, be corrupted, or have wrong encoding.

**Recommended Approach**:
```python
import pandas as pd
import os

filepath = 'data.csv'

try:
    # Check if file exists first
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    df = pd.read_csv(filepath, encoding='utf-8')
    print(f"Successfully loaded {len(df)} rows")

except FileNotFoundError as e:
    print(f"Error: {e}")
    df = pd.DataFrame()  # Empty DataFrame as fallback

except pd.errors.EmptyDataError:
    print("Error: The file is empty")
    df = pd.DataFrame()

except pd.errors.ParserError as e:
    print(f"Error parsing file: {e}")
    # Try with different settings
    df = pd.read_csv(filepath, on_bad_lines='skip')

except UnicodeDecodeError:
    print("Encoding error, trying latin-1...")
    df = pd.read_csv(filepath, encoding='latin-1')
```

---

### 5.2 Type Conversion Errors

**Basic Usage**:
```python
df['price'] = df['price'].astype(float)  # May fail
```

**Problem**: Column might contain non-numeric values like '$19.99' or 'N/A'.

**Recommended Approach**:
```python
import pandas as pd

df = pd.DataFrame({
    'price': ['19.99', '$29.99', 'N/A', '9.99']
})

# Method 1: Clean then convert
df['price_clean'] = df['price'].str.replace(r'[$,]', '', regex=True)
df['price_clean'] = pd.to_numeric(df['price_clean'], errors='coerce')
# 'coerce' turns errors into NaN

# Method 2: Using try-except for custom handling
def safe_float(value):
    try:
        cleaned = str(value).replace('$', '').replace(',', '').strip()
        return float(cleaned) if cleaned not in ['N/A', '', 'nan'] else None
    except (ValueError, TypeError):
        return None

df['price_converted'] = df['price'].apply(safe_float)
```

---

### 5.3 Merge/Join Errors

**Basic Usage**:
```python
result = pd.merge(df1, df2, on='id')  # May produce unexpected results
```

**Problem**: Duplicate keys can cause row explosion; missing keys silently drop data.

**Recommended Approach**:
```python
import pandas as pd

df1 = pd.DataFrame({'id': [1, 2, 2], 'value1': [10, 20, 30]})
df2 = pd.DataFrame({'id': [2, 2, 3], 'value2': [100, 200, 300]})

# Check for duplicates before merge
def safe_merge(left, right, on, how='inner'):
    left_dupes = left[on].duplicated().sum()
    right_dupes = right[on].duplicated().sum()

    if left_dupes > 0 or right_dupes > 0:
        print(f"Warning: Duplicates found - left: {left_dupes}, right: {right_dupes}")
        print("This may cause row multiplication!")

    before_rows = len(left)
    result = pd.merge(left, right, on=on, how=how)
    after_rows = len(result)

    print(f"Rows: {before_rows} -> {after_rows}")

    if after_rows > before_rows * 2:
        print("Warning: Significant row increase - check for duplicates!")

    return result

result = safe_merge(df1, df2, on='id')
```

---

## 6. Best Practices

### 1. Use Vectorized Operations

Avoid loops; use built-in operations for speed.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'value': range(1000000)})

# SLOW - using loop
# result = []
# for val in df['value']:
#     result.append(val * 2)

# FAST - vectorized
df['doubled'] = df['value'] * 2

# FAST - vectorized with condition
df['category'] = np.where(df['value'] > 500000, 'high', 'low')
```

---

### 2. Use Appropriate Data Types

Optimize memory by using correct types.

```python
import pandas as pd

df = pd.DataFrame({
    'id': range(1000),
    'category': ['A', 'B', 'C'] * 333 + ['A']
})

# Check initial memory
print(f"Before: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")

# Optimize types
df['id'] = df['id'].astype('int32')  # Smaller integer
df['category'] = df['category'].astype('category')  # For repeated strings

print(f"After: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
```

---

### 3. Chain Operations with Method Chaining

Write cleaner, more readable code.

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['alice', 'bob', 'charlie'],
    'age': [25, None, 35],
    'salary': [50000, 60000, 70000]
})

# Method chaining - clean and readable
result = (
    df
    .dropna(subset=['age'])
    .assign(
        name=lambda x: x['name'].str.title(),
        tax=lambda x: x['salary'] * 0.2
    )
    .query('age > 20')
    .sort_values('salary', ascending=False)
)
print(result)
```

---

### 4. Avoid Chained Indexing (SettingWithCopyWarning)

Use `.loc` for assignment to avoid warnings and bugs.

```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# WRONG - Chained indexing - may not work as expected
# df[df['A'] > 1]['B'] = 10  # Warning!

# CORRECT - Use .loc
df.loc[df['A'] > 1, 'B'] = 10
```

---

### 5. Use .copy() When Creating Subsets

Prevent unintended modifications to original data.

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# WRONG - Creates a view - modifying subset affects original
# subset = df[df['A'] > 1]

# CORRECT - Creates independent copy
subset = df[df['A'] > 1].copy()
subset['B'] = 999  # Won't affect original df
```

---

## 7. Common Mistakes

### Mistake 1: Modifying While Iterating

**Wrong Approach**:
```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3]})

for idx, row in df.iterrows():
    df.loc[idx, 'A'] = row['A'] * 2  # Slow and dangerous
```

**Correct Approach**:
```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3]})
df['A'] = df['A'] * 2  # Vectorized - fast and safe
```

**Why Wrong**: Modifying during iteration can cause unexpected behavior and is extremely slow.

---

### Mistake 2: Not Handling Missing Values Before Operations

**Wrong Approach**:
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'price': [10, np.nan, 30]})
total = df['price'].sum()  # Works but may hide data quality issues
```

**Correct Approach**:
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'price': [10, np.nan, 30]})

# Check for missing values first
missing_count = df['price'].isna().sum()
if missing_count > 0:
    print(f"Warning: {missing_count} missing values")

# Then decide how to handle
total = df['price'].fillna(0).sum()
# OR
total = df['price'].dropna().sum()
```

---

### Mistake 3: Incorrect Boolean Operators

**Wrong Approach**:
```python
import pandas as pd

df = pd.DataFrame({'age': [25, 30, 35], 'salary': [50000, 60000, 70000]})

# Using Python's 'and' instead of '&'
# result = df[df['age'] > 25 and df['salary'] > 55000]  # Error!
```

**Correct Approach**:
```python
import pandas as pd

df = pd.DataFrame({'age': [25, 30, 35], 'salary': [50000, 60000, 70000]})

# Use & for AND, | for OR, ~ for NOT
# Parentheses are REQUIRED
result = df[(df['age'] > 25) & (df['salary'] > 55000)]
```

---

### Mistake 4: Not Resetting Index After Operations

**Wrong Approach**:
```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
filtered = df[df['A'] > 2]
print(filtered.iloc[0])  # Gets row with index 2, not first filtered row
```

**Correct Approach**:
```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
filtered = df[df['A'] > 2].reset_index(drop=True)
print(filtered.iloc[0])  # Gets first filtered row (value 3)
```

---

### Mistake 5: Using inplace=True Excessively

**Wrong Approach**:
```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3]})
df.drop(columns=['A'], inplace=True)
df.reset_index(inplace=True)
df.rename(columns={'index': 'id'}, inplace=True)
# Hard to debug, can't see intermediate results
```

**Correct Approach**:
```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3]})
df = (
    df
    .drop(columns=['A'])
    .reset_index()
    .rename(columns={'index': 'id'})
)
# Method chaining - cleaner and easier to debug
```

---

## 8. Commonly Confused Concepts

### Within Pandas

#### loc vs iloc

| Feature | loc | iloc |
|---------|-----|------|
| Selection | Label-based | Integer position-based |
| Slice end | Inclusive | Exclusive |
| Use when | You know row/column names | You know positions |

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3]}, index=['x', 'y', 'z'])

# loc - by label
print(df.loc['x':'y'])  # Rows x AND y (inclusive)

# iloc - by position
print(df.iloc[0:2])     # Rows 0 and 1 only (exclusive end)
```

---

#### apply vs map vs applymap

| Method | Works on | Purpose |
|--------|----------|---------|
| `apply` | DataFrame or Series | Apply function to rows/columns |
| `map` | Series only | Element-wise substitution |
| `applymap` | DataFrame only | Element-wise (deprecated - use `map`) |

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# apply - to columns (default axis=0)
df.apply(sum)  # Sum of each column

# apply - to rows (axis=1)
df.apply(sum, axis=1)  # Sum of each row

# map - for Series substitution
df['A'].map({1: 'one', 2: 'two'})

# map on DataFrame (replaces applymap)
df.map(lambda x: x * 2)  # Every cell doubled
```

---

#### merge vs join vs concat

| Method | Purpose | Matching Logic |
|--------|---------|----------------|
| `merge` | SQL-style joins | On column values |
| `join` | Join on index | Convenience method |
| `concat` | Stack DataFrames | No matching logic |

```python
import pandas as pd

df1 = pd.DataFrame({'key': [1, 2], 'A': [10, 20]})
df2 = pd.DataFrame({'key': [1, 2], 'B': [30, 40]})

# merge - on column values
pd.merge(df1, df2, on='key')

# join - on index
df1.set_index('key').join(df2.set_index('key'))

# concat - stack vertically or horizontally
pd.concat([df1, df1])  # Stack rows
pd.concat([df1, df2], axis=1)  # Stack columns
```

---

#### dropna vs fillna

| Method | Action | Data |
|--------|--------|------|
| `dropna` | Remove rows/columns with missing values | Data is removed |
| `fillna` | Replace missing values with specified value | Data is imputed |

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})

# dropna - removes rows
df.dropna()  # Only row 0 remains

# fillna - keeps all rows
df.fillna(0)  # NaN replaced with 0
```

---

### Across Libraries

#### Pandas vs NumPy

| Feature | Pandas | NumPy |
|---------|--------|-------|
| Data type | Labeled, mixed types | Homogeneous arrays |
| Focus | Data analysis | Numerical computation |
| Use when | Tabular data | Pure numerical operations |

```python
import pandas as pd
import numpy as np

# NumPy - pure numerical operations
arr = np.array([1, 2, 3, 4, 5])
mean = np.mean(arr)

# Pandas - labeled, mixed-type data
df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'score': [90, 85]
})
mean = df['score'].mean()
```

---

#### Pandas vs Polars

| Feature | Pandas | Polars |
|---------|--------|--------|
| Execution | Eager | Lazy (can be eager) |
| Speed | Good | Faster (5-10x for large datasets) |
| Ecosystem | Mature, extensive | Growing |

```python
# Pandas
import pandas as pd
df = pd.read_csv('large_file.csv')
result = df.groupby('category')['value'].mean()

# Polars (alternative for large data)
import polars as pl
df = pl.read_csv('large_file.csv')
result = df.group_by('category').agg(pl.col('value').mean())
```

---

## 9. Better Alternatives from Other Libraries

### Scenario: Processing Very Large CSV Files

**Using Pandas**:
```python
import pandas as pd

# May crash with memory error for very large files
df = pd.read_csv('huge_file.csv')  # Loads entire file into memory
```

**Better: Using Polars**:
```python
import polars as pl

# Lazy evaluation - only computes what's needed
df = (
    pl.scan_csv('huge_file.csv')  # Doesn't load entire file
    .filter(pl.col('value') > 100)
    .group_by('category')
    .agg(pl.col('value').mean())
    .collect()  # Execute only at the end
)
```

**Why Better**: Polars uses lazy evaluation and multi-threading, handling files larger than memory.

---

### Scenario: Complex String Operations

**Using Pandas str methods (can be slow)**:
```python
import pandas as pd

df = pd.DataFrame({'text': ['hello world'] * 1000000})
df['processed'] = df['text'].str.upper().str.replace('HELLO', 'HI')
```

**Better: Using Python's re module with apply**:
```python
import pandas as pd
import re

pattern = re.compile(r'hello', re.IGNORECASE)

df = pd.DataFrame({'text': ['hello world'] * 1000000})
df['processed'] = df['text'].apply(lambda x: pattern.sub('HI', x).upper())
```

**Why Better**: Compiled regex patterns are faster for complex string operations.

---

## 10. Method Comparison Table

| Method | Key Parameters | Returns | Use When | Confused With |
|--------|----------------|---------|----------|---------------|
| `loc[]` | label, column | Series/DF | Label-based selection | iloc |
| `iloc[]` | position, column | Series/DF | Position-based selection | loc |
| `query()` | expr | DataFrame | Complex filtering | boolean indexing |
| `apply()` | func, axis | Series/DF | Custom row/col ops | map |
| `map()` | arg | Series | Value substitution | apply |
| `merge()` | left, right, on, how | DataFrame | SQL-style joins | concat |
| `concat()` | objs, axis | DataFrame | Stack DataFrames | merge |
| `groupby()` | by | GroupBy | Aggregations | pivot_table |
| `pivot_table()` | values, index, columns | DataFrame | Cross-tabulation | groupby |
| `melt()` | id_vars, value_vars | DataFrame | Wide to long | pivot |
| `dropna()` | axis, how, subset | DataFrame | Remove missing | fillna |
| `fillna()` | value | DataFrame | Replace missing | dropna |
| `astype()` | dtype | Series/DF | Type conversion | pd.to_numeric |

---

## 11. Quick Reference Summary

### Data Loading

| Method | Purpose | Example |
|--------|---------|---------|
| `read_csv()` | Load CSV file | `pd.read_csv('file.csv')` |
| `read_excel()` | Load Excel file | `pd.read_excel('file.xlsx')` |
| `read_json()` | Load JSON | `pd.read_json('file.json')` |
| `read_sql()` | Load from database | `pd.read_sql(query, conn)` |

### Data Exploration

| Method | Purpose | Example |
|--------|---------|---------|
| `head()/tail()` | View first/last rows | `df.head(10)` |
| `info()` | Summary info | `df.info()` |
| `describe()` | Statistics | `df.describe()` |
| `value_counts()` | Count uniques | `df['col'].value_counts()` |
| `shape` | Dimensions | `df.shape` |

### Data Selection

| Method | Purpose | Example |
|--------|---------|---------|
| `loc[]` | By label | `df.loc['row', 'col']` |
| `iloc[]` | By position | `df.iloc[0, 0]` |
| `query()` | Filter string | `df.query('age > 25')` |
| `isin()` | Check membership | `df[df['col'].isin([1,2])]` |

### Data Cleaning

| Method | Purpose | Example |
|--------|---------|---------|
| `isna()` | Find missing | `df.isna().sum()` |
| `dropna()` | Remove missing | `df.dropna()` |
| `fillna()` | Replace missing | `df.fillna(0)` |
| `drop_duplicates()` | Remove dupes | `df.drop_duplicates()` |
| `replace()` | Replace values | `df.replace('old', 'new')` |
| `astype()` | Change type | `df['col'].astype(int)` |

### Data Transformation

| Method | Purpose | Example |
|--------|---------|---------|
| `apply()` | Apply function | `df.apply(func)` |
| `groupby()` | Group & aggregate | `df.groupby('col').sum()` |
| `merge()` | Join DataFrames | `pd.merge(df1, df2, on='key')` |
| `concat()` | Stack DataFrames | `pd.concat([df1, df2])` |
| `pivot_table()` | Pivot data | `df.pivot_table(...)` |
| `melt()` | Unpivot data | `pd.melt(df, id_vars=['id'])` |
| `sort_values()` | Sort by column | `df.sort_values('col')` |

### Data Export

| Method | Purpose | Example |
|--------|---------|---------|
| `to_csv()` | Save as CSV | `df.to_csv('out.csv')` |
| `to_excel()` | Save as Excel | `df.to_excel('out.xlsx')` |
| `to_json()` | Save as JSON | `df.to_json('out.json')` |

---

## Coverage Checklist

- [x] All frequently used functions/methods
- [x] Must-know core concepts (Series, DataFrame, Index)
- [x] Mandatory vs optional parameters clearly marked
- [x] Real-world examples with output
- [x] Exception handling (file I/O, type conversion)
- [x] Common mistakes with anti-patterns explained
- [x] Best practices with reasoning
- [x] Confusing similar methods clarified
- [x] Alternatives from other libraries (Polars, NumPy)
- [x] Comparison table for covered methods
- [x] Quick reference table at end


//////////////
---

## Pandas DataFrame Filtering & Row Iteration

### Basic Information

**Data Type(s):** pandas.DataFrame, pandas.Series

**Purpose:** Filter DataFrames to extract specific rows based on conditions, and iterate through rows to process data one row at a time.

**Syntax:**

**Boolean Filtering:**
```python
filtered_df = df[df['column'] == value]
```

**`.item()` Method:**
```python
single_value = series_with_one_element.item()

# Key Parameters:
# None

# Returns:
# Type: scalar (int, float, str, etc.)
# Behavior: Extracts the single scalar value from a Series/DataFrame with exactly one element
# Important: Raises ValueError if Series/DataFrame contains more than one element
```

**`.iterrows()` Method:**
```python
for index, row in df.iterrows():
    # process row
    
# Key Parameters:
# None

# Returns:
# Type: Iterator of (index, Series) tuples
# Behavior: Returns each row as a Series object with column names as index
# Important: Creates copies of data (slower), row values can be accessed like row['column_name']
```

---

### Examples

**Basic Example - Boolean Filtering:**
```python
import pandas as pd

# Sample data
data = {'day': [20, 21, 21, 22], 
        'sales': [100, 150, 200, 120]}
df = pd.DataFrame(data)

# Filter for day 21
filtered = df[df['day'] == 21]
print(filtered)
# Output:
#    day  sales
# 1   21    150
# 2   21    200
```

**Basic Example - Using .item():**
```python
# Get single value from filtered result
single_row = df[df['day'] == 20]
sales_value = single_row['sales'].item()
print(sales_value)
# Output: 100

# Type of result
print(type(sales_value))
# Output: <class 'numpy.int64'> (or int)
```

**Basic Example - Using .iterrows():**
```python
# Iterate through rows
for index, row in df.iterrows():
    print(f"Index: {index}, Day: {row['day']}, Sales: {row['sales']}")
# Output:
# Index: 0, Day: 20, Sales: 100
# Index: 1, Day: 21, Sales: 150
# Index: 2, Day: 21, Sales: 200
# Index: 3, Day: 22, Sales: 120
```

**Real-World Example:**
```python
# Customer orders dataset
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104],
    'customer': ['Alice', 'Bob', 'Alice', 'Charlie'],
    'amount': [250, 400, 150, 600],
    'day': [21, 21, 22, 23]
})

# Find all orders on day 21
day21_orders = orders[orders['day'] == 21]
print(day21_orders)
# Output:
#    order_id customer  amount  day
# 0       101    Alice     250   21
# 1       102      Bob     400   21

# Get single customer's total (when you know there's only one result)
alice_day22 = orders[(orders['customer'] == 'Alice') & (orders['day'] == 22)]
alice_amount = alice_day22['amount'].item()
print(f"Alice spent ${alice_amount} on day 22")
# Output: Alice spent $150 on day 22

# Calculate daily totals using iterrows
daily_summary = []
for idx, row in day21_orders.iterrows():
    summary = f"{row['customer']} ordered ${row['amount']}"
    daily_summary.append(summary)
    print(summary)
# Output:
# Alice ordered $250
# Bob ordered $400
```

**Exception Handling:**
```python
# ❌ Basic approach (may fail)
filtered = df[df['day'] == 99]  # No matching rows
value = filtered['sales'].item()  # ValueError!

# ✅ Recommended approach
try:
    filtered = df[df['day'] == 21]
    if len(filtered) == 1:
        value = filtered['sales'].item()
    elif len(filtered) == 0:
        print("No matching rows found")
    else:
        print(f"Multiple rows found: {len(filtered)}")
        # Use .iloc[0] for first row or handle multiple results
        value = filtered['sales'].iloc[0]
except ValueError as e:
    print(f"Error extracting value: {e}")
# Output: (depends on data)
# Why: .item() only works with exactly one element; check length first
```

---

### When to Use This

**Use Boolean Filtering When:**
- Extracting rows based on conditions (sales > 100, day == 21)
- Creating subsets of data for analysis
- Filtering before performing calculations

**Use .item() When:**
- You filtered down to exactly ONE row and need a scalar value
- Converting a single-element Series to a native Python type
- You want cleaner code than `.iloc[0]` for single values

**Use .iterrows() When:**
- Performing row-by-row operations that can't be vectorized
- Generating reports or formatted strings for each row
- Applying complex logic that varies by row

**Don't Use When:**
- **Filtering:** Don't use loops when boolean indexing works (slower)
- **.item():** Don't use with multiple rows (use `.tolist()` or `.values` instead)
- **.iterrows():** Don't use for calculations pandas can vectorize (use `.apply()`, `.sum()`, etc.)

---

### Important Notes

- **Boolean filtering returns a DataFrame**, even if only one row matches; use `.item()` to extract the scalar value
- **.item() fails with ValueError** if the Series/DataFrame has 0 or 2+ elements; always verify you have exactly one element
- **iterrows() is slow** because it creates Series objects for each row; use only when necessary (vectorized operations are 100x faster)
- **Row in iterrows() is a Series**, not a dict; access values with `row['column']` or `row.column`
- **Multiple conditions** require parentheses and `&` (AND) or `|` (OR): `df[(df['day'] == 21) & (df['sales'] > 100)]`

---

### Best Practices

```python
# ✅ Good Practice: Vectorized operations (fast)
df['total'] = df['quantity'] * df['price']
# Why: Pandas applies operation to entire column at once (efficient)

# ❌ Avoid This: Loop for simple operations (slow)
for idx, row in df.iterrows():
    df.at[idx, 'total'] = row['quantity'] * row['price']
# Why: 100x slower than vectorized; only use iterrows when unavoidable

# ✅ Good Practice: Check before using .item()
filtered = df[df['id'] == 123]
if len(filtered) == 1:
    value = filtered['amount'].item()
# Why: Prevents ValueError from empty or multi-row results

# ❌ Avoid This: Assuming .item() always works
value = df[df['id'] == 999]['amount'].item()  # May crash!
# Why: No validation; fails silently if filter returns 0 or 2+ rows
```

---

### Common Mistakes

**Mistake 1: Using .item() on Multiple Rows**
```python
# ❌ Wrong Approach
filtered = df[df['day'] == 21]  # Returns 2 rows
value = filtered['sales'].item()
# Output: ValueError: can only convert an array of size 1 to a Python scalar

# ✅ Correct Approach
filtered = df[df['day'] == 21]
if len(filtered) == 1:
    value = filtered['sales'].item()
else:
    # Handle multiple rows
    values = filtered['sales'].tolist()  # [150, 200]
# Output: [150, 200]
# Why Wrong: .item() requires exactly one element; check length or use .iloc[0] for first row
```

**Mistake 2: Modifying DataFrame During iterrows()**
```python
# ❌ Wrong Approach
for idx, row in df.iterrows():
    row['new_column'] = row['sales'] * 2  # Doesn't modify df!
# Output: df remains unchanged

# ✅ Correct Approach
for idx, row in df.iterrows():
    df.at[idx, 'new_column'] = row['sales'] * 2
# Or better: use vectorized operation
df['new_column'] = df['sales'] * 2
# Output: new_column added to df
# Why Wrong: row is a copy; changes don't affect original DataFrame
```

**Mistake 3: Forgetting Parentheses in Complex Filters**
```python
# ❌ Wrong Approach
filtered = df[df['day'] == 21 & df['sales'] > 100]
# Output: ValueError or unexpected results

# ✅ Correct Approach
filtered = df[(df['day'] == 21) & (df['sales'] > 100)]
# Output: Correctly filtered DataFrame
# Why Wrong: Operator precedence; & binds tighter than ==, causing errors
```

---

### Similar Methods (Easy to Confuse)

**Most Confusing: `.item()` vs `.iloc[0]` vs `.values[0]`**

**`.item()`:**
- What it does: Extracts single scalar value from one-element Series/DataFrame
- Key difference: **Strict validation** - raises error if not exactly one element
- When to use: When you're **certain** there's only one value and want type safety

```python
single = df[df['id'] == 123]['amount']
value = single.item()
print(value, type(value))
# Output: 250 <class 'numpy.int64'>
# Clean scalar extraction with validation
```

**`.iloc[0]`:**
- What it does: Gets first row/element by integer position
- Key difference: **No validation** - works with any size, just takes first
- When to use: When you want the **first item** regardless of total count

```python
multiple = df[df['day'] == 21]['amount']
value = multiple.iloc[0]
print(value, type(value))
# Output: 150 <class 'numpy.int64'>
# Gets first value even if many exist
```

**`.values[0]`:**
- What it does: Converts to numpy array, then gets first element
- Key difference: **Array conversion** - extra step, returns numpy type
- When to use: When working with **numpy arrays** or need array operations

```python
multiple = df[df['day'] == 21]['amount']
value = multiple.values[0]
print(value, type(value))
# Output: 150 <class 'numpy.int64'>
# Array-based extraction
```

**Key Difference:** `.item()` validates one element (safe but strict), `.iloc[0]` grabs first (flexible but permissive), `.values[0]` converts to array first (extra overhead).

---

### Related Methods & Alternatives

| Method | Data Type | Purpose | Use When | Performance |
|--------|-----------|---------|----------|-------------|
| `.item()` | Series | Extract scalar | Exactly 1 element | O(1) |
| `.iloc[0]` | Series/DF | Get first by position | Want first of many | O(1) |
| `.values` | Series/DF | Convert to array | Need numpy array | O(n) |
| `.tolist()` | Series | Convert to list | Multiple values | O(n) |
| `.apply()` | DataFrame | Row-wise function | Complex logic | O(n) |
| `.itertuples()` | DataFrame | Faster iteration | Alternative to iterrows | O(n) |

---

### Performance Notes

**Time Complexity:**
- Boolean filtering: O(n) - must check every row
- `.item()`: O(1) - direct extraction after filtering
- `.iterrows()`: O(n) - creates Series object per row (slow)

**Space Complexity:**
- Boolean filtering: O(k) where k = matching rows
- `.iterrows()`: O(m) where m = row size (copies data)

**Performance Tip:** Use `.itertuples()` instead of `.iterrows()` for 2-3x speedup - it returns named tuples instead of Series objects. For calculations, always prefer vectorized operations over any iteration.

```python
# Fast alternative to iterrows
for row in df.itertuples():
    print(row.day, row.sales)  # Access as attributes
# 2-3x faster than iterrows()
```

---

### Quick Reference Summary

| Aspect | Details |
|--------|---------|
| **Data Type(s)** | DataFrame, Series |
| **Purpose** | Filter rows by condition, extract values, iterate rows |
| **Returns** | Filtering: DataFrame; .item(): scalar; iterrows: iterator |
| **Key Parameters** | None for these methods |
| **Similar To** | .iloc[0], .values[0], .apply(), .itertuples() |
| **Use When** | Filtering: conditional extraction; .item(): single value; iterrows: row logic |
| **Avoid When** | Vectorized ops possible, performance critical |
| **Performance** | Filtering: O(n); .item(): O(1); iterrows: O(n) slow |
| **Common Mistake** | Using .item() on multiple rows, modifying during iterrows |