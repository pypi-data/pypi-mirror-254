# Ini File Uts
#
### Installation

```sh
pip install iniUts
```

## Usage
#
<!-- //==================================================== -->
## read
##### test.ini file
```ini
[Person]
name    = myname
age     = 31
amount  = 20.3
friends = friend1,friend2,friend3
dob     = 1991-12-23
```
##### python code
```py
from iniUts import IniUts

ini = IniUts('test.ini')
data = ini.read('Person','name')

print(result)
```
##### output
```py
"myname"
```

<!-- //==================================================== -->
## write
##### test.ini file
```ini
[PERSON]
name    = myname
```
##### python code
```py
from iniUts import IniUts

ini = IniUts('test.ini')
ini.write('PERSON','last_name','mylastname')

```
##### test.ini file
```ini
[PERSON]
name      = myname
last_name = mylastname
```
<!-- //==================================================== -->
## getKeys
##### test.ini file
```ini
[PERSON]
name      = myname
last_name = mylastname
```
##### python code
```py
from iniUts import IniUts

ini = IniUts('test.ini')
keys = ini.getKeys("PERSON")
print(keys)
```
##### output
```py
['name','last_name']
```

<!-- //==================================================== -->
## Section2Dict
##### test.ini file
```ini
[PERSON]
name    = myname
age     = 31
amount  = 20.3
friends = friend1,friend2,friend3
dob     = 1991-12-23
```
##### python code
```py
from iniUts import IniUts

ini = IniUts('test.ini')
ini.Section2Dict('PERSON')
print(Person)

```
##### output
```py
{
    "name"    = "myname"
    "age"     = "31"
    "amount"  = "20.3"
    "friends" = "friend1,friend2,friend3"
    "dob"     = "1991-12-23"
}

```
<!-- //==================================================== -->
## section2DataClass
##### test.ini file
```ini
[PERSON]
name    = myname
age     = 31
amount  = 20.3
friends = friend1,friend2,friend3
dob     = 1991-12-23
```
##### python code
```py
from iniUts import IniUts
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Person():
    name   : str
    age    : int
    amount : float
    friends: tuple = ','
    dob    : datetime = "%Y-%m-%d"

ini = IniUts('test.ini')
ini.section2DataClass('PERSON',Person)

print(Person.name)
print(Person.age)
print(Person.amount)
print(Person.friends)
print(Person.dob)

```
##### output
```py
myname
31
20.3
("friend1","friend2","friend3")
datetime.datetime(1991, 12, 2, 0, 0)

```

# ENVIORNMENT CHANGING

<!-- //==================================================== -->
## section2DataClass
##### prd.ini file
```ini
[PERSON] # Will be changed in DEV
name    = myName
age     = 31
amount  = 20.3
friends = friend1,friend2,friend3
dob     = 1991-12-23

[CONFIG] # Will not be changed in DEV
ip    = <some_ip>
path  = <some_path>

```
##### dev.ini file
```ini
[PERSON] #change only PERSON section when in DEV
name    = myOtherName
age     = 16
amount  = 30.1
friends = friend10,friend20,friend30
dob     = 2023-11-10

```

##### python code
```py
from iniUts import IniUts
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Person():
    name   : str
    age    : int
    amount : float
    friends: tuple = ','
    dob    : datetime = "%Y-%m-%d"

@dataclass
class Config():
    ip   : str
    path : str


ini = IniUts('prd.ini','dev.ini',in_prd=True)
ini.section2DataClass('PERSON',Person)
ini.section2DataClass('CONFIG',Config)


print(Person.name)
print(Person.age)
print(Config.ip)
print(Config.path)

ini = IniUts('prd.ini','dev.ini',in_prd=False)
ini.section2DataClass('PERSON',Person)
ini.section2DataClass('CONFIG',CONFIG)

print(Person.name)
print(Person.age)
print(Config.ip)
print(Config.path)


```
##### output
```py
#==================== IN PRD
myName
31
<some_ip>
<some_path>
#==================== IN DEV
myOtherName
16
<some_ip>
<some_path>

```



