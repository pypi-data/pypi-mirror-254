# Python Utils
This repository contains wrapper functions and code snippets for the most common python dtypes. Truth is I'm tired of searching on Stack Overflow the same problems over and over again, so I am just gathering them here :)

### Installation
python_utils_tdinoto is OS independent and compatible with Python >= 3.7. 
To install it, ensure you have python installed and then run:
```python
python3 -m pip install python3_utils_tdinoto
```

### Example usage
```python
>>> from utils_tdinoto.utils_lists import find_common_elements
>>> list_1 = [1, 2, 3]
>>> list_2 = [3, 4, 5]
>>> find_common_elements(list_1, list_2)
[3]

>>> from utils_tdinoto.utils_strings import keep_only_digits
>>> s = 'ses-20221026'
>>> keep_only_digits(s)
'20221046'
```