# true_or_false
A simple python funciton to determine whether an input is True or False

Determine (educated guess) whether an input value is True
or False.  Input can be a bool, dict, int or str.  This is
useful for determining the value of a parameter as passed
in via environment variable, cli, config file or plain
python code.

Examples of True values:
  str: ['true', 't', '1', 'yes', 'y', 't', 'oui']
  bool: True
  dict: {'a': 1} # any non empty dictionary
  list: [0]  # any list not zero length

Examples of False values:
  str FALSES = ['false', 'f', '0', 'no', 'n', 'non']
  bool: False
  dict: {}  # empty dictionary
  list: []  # empty list

## Installation

  pip install true-or-false

## Usage

```
from true_or_false import true_or_false

b = true_or_false(1)
print(b)
>> True
```