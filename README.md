# import-pypi

One dependency to rule them all.

[![asciicast](https://asciinema.org/a/173095.png)](https://asciinema.org/a/173095)

# Installation

Copy `pypi.py` into your site-packages directory or straight into your project.
Don't bother using pip, requirements.txt and all that crap.

Requires Python 3.4+.

# Usage

```python
import pypi
```

That's it. You can now import Django, NumPy, or whatever and it will always
be there.

You can also pin your dependencies _before_ importing them

```python
import pypi

pypi.install('Django', '2.0.3')

import django

print(django.__version__)  # 2.0.3
```

For loose version specification use comparison operator as with regular pip 
command

```python
import pypi

pypi.install('Django', '>=2.0.1')
pypi.install('Django', '<1.9')
# all <=, <, ==, >, >= operators works as well

```

# License

GNU GPLv3.
