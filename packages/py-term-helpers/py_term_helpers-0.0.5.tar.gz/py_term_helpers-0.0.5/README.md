# py-term-helpers

Published package on pypi

https://pypi.org/project/py-term-helpers/

## Overview

The **py-term-helpers** is a lightweight Python terminal debug helper tool designed to streamline the debugging process for developers. Creates a more dynamic output for the terminal with star lines and any console testing visuals. It provides essential functions and utilities to assist in identifying and resolving issues in Python applications directly from the terminal.

## Features

- **.term_size**:
  - Returns current size of terminal in characters
- **.star_line(_char="\*"_)** :
  - Prints terminal wide `char`
- **.center_string_stars(string, _char="\*"_)** :

  - Prints the `string` in the center of terminal wide `char`

- **.term_wrap(string, _char="\*"_)** :

  - Prints the `string` in the center of terminal wide `char` with 2 `.star_line` above and below
  - Essentially: `.star_line() => .center_string_stars() => .star_line()`

- **.top_wrap(string, char="\*"*)** :

  - Clears console and runs `.term_wrap()`

- **.kv_print(arg)** :
  - Prints any given arg as '{arg_variable_name} => {arg_value}'
  - Similar to JavaScript's `console.log({ arg }) => "{arg_name: arg_value}"`

## Getting Started

1. **Installation:**

   ```bash
   pip install py-term-helpers
   ```

2. **Usage:**

  ```python
    from py_term_helpers import term_wrap, star_line, kv_print

    term_wrap("TerminalWrap")
    # Output:
    #****************************TerminalWrap***********************************

    star_line()
    # Output:
    #***************************************************************************

    my_dict = dict({'key': 'value'})
    kv_print(my_dict)
    # Output:
    # key => 'value'

  ```
