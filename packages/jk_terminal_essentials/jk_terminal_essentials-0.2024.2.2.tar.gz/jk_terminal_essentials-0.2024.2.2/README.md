jk_terminal_essentials
==========

Introduction
------------

This module provides essential constants and information about the terminal. This module is intended for implementing CLI tools and other applications running in a terminal.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/....)
* [pypi.python.org](https://pypi.python.org/pypi/jk_terminal_essentials)

How to use this module
----------------------

### Import this module

Please include this module into your application using the following code:

```python
import jk_terminal_essentials as te
```

### Colors

This module provides a variety of color constants. For example:

```python
print(te.FGCOLOR_RED + "Error!" + te.STYLE_RESET)
```

The following colors are supported:

```python
FGCOLOR_BLACK = "\x1b[30m"
FGCOLOR_RED = "\x1b[31m"
FGCOLOR_GREEN = "\x1b[32m"
FGCOLOR_YELLOW = "\x1b[33m"
FGCOLOR_BLUE = "\x1b[34m"
FGCOLOR_MAGENTA = "\x1b[35m"
FGCOLOR_CYAN = "\x1b[36m"
FGCOLOR_LIGHT_GRAY = "\x1b[37m"

FGCOLOR_DARK_GRAY = "\x1b[90m"
FGCOLOR_LIGHT_RED = "\x1b[91m"
FGCOLOR_LIGHT_GREEN = "\x1b[92m"
FGCOLOR_LIGHT_YELLOW = "\x1b[93m"
FGCOLOR_LIGHT_BLUE = "\x1b[94m"
FGCOLOR_LIGHT_MAGENTA = "\x1b[95m"
FGCOLOR_LIGHT_CYAN = "\x1b[96m"
FGCOLOR_WHITE = "\x1b[97m"

BGCOLOR_BLACK = "\x1b[40m"
BGCOLOR_RED = "\x1b[41m"
BGCOLOR_GREEN = "\x1b[42m"
BGCOLOR_YELLOW = "\x1b[43m"
BGCOLOR_BLUE = "\x1b[44m"
BGCOLOR_MAGENTA = "\x1b[45m"
BGCOLOR_CYAN = "\x1b[46m"
BGCOLOR_LIGHT_GRAY = "\x1b[47m"

BGCOLOR_DARK_GRAY = "\x1b[100m"
BGCOLOR_LIGHT_RED = "\x1b[101m"
BGCOLOR_LIGHT_GREEN = "\x1b[102m"
BGCOLOR_LIGHT_YELLOW = "\x1b[103m"
BGCOLOR_LIGHT_BLUE = "\x1b[104m"
BGCOLOR_LIGHT_MAGENTA = "\x1b[105m"
BGCOLOR_LIGHT_CYAN = "\x1b[106m"
BGCOLOR_WHITE = "\x1b[107m"
```

### Check for Color Support

To check if the current terminal supports colors:

```python
print(te.checkTerminalSupportsColors())
```

Author(s)
-------------------

* Jürgen Knauth: pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



