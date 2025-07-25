# TwineW

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
[![PyPI](https://img.shields.io/pypi/v/TwineW?color=green)](https://pypi.org/project/TwineW/)
[![GitHub](https://img.shields.io/github/license/wilsonnnlol/TwineW)](https://github.com/wilsonnnlol/TwineW/blob/main/LICENSE)
## Overview

*(Replace this section with a concise description of what TwineW does. What problem does it solve? What are its main features?)*

TwineW is a Python package designed to simplify macroing endurance. It provides super easy building blocks to construct a working macro, with the ability to make changes easily.

## Installation

This guide explains how to install and get started with the `TwineW` Python package.

### Prerequisites

* **Python 3.8+:** Ensure you have Python version 3.8 or newer installed on your system. You can check your Python version by running:
    ```bash
    python --version
    # or
    python3 --version
    ```
    If you don't have Python installed, please download it from [python.org](https://www.python.org/downloads/).

### Installing TwineW

`TwineW` can be installed directly from the Python Package Index (PyPI) using `pip`.

1.  **Open your terminal or command prompt.**

2.  **Install `TwineW` using pip:**
    ```bash
    pip install TwineW
    ```
    * **Note:** If you have multiple Python versions installed, you might need to use `pip3` instead of `pip`:
        ```bash
        pip3 install TwineW
        ```

3.  *(Optional but Recommended)* **Using a Virtual Environment:**
    It's highly recommended to install Python packages within a virtual environment to avoid conflicts with other projects and system-wide packages.

    ```bash
    # 1. Create a virtual environment (e.g., named 'venv')
    python -m venv venv

    # 2. Activate the virtual environment
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    .\venv\Scripts\activate

    # 3. Install TwineW inside the activated environment
    pip install TwineW

    # To deactivate the environment later:
    deactivate
    ```

## Basic Usage

After installation, you can import and use `TwineW` in your Python scripts or interactive sessions.

```python
from TwineW import TwineW as macro

try:        # Use 'try' to be able to get out of the infinite loop
    while True:         # Infinite Loop begins here.
        macro.main_screen.begin()
        macro.main_screen.main_screen_actions()
        macro.main_screen.launch_and_load()
        macro.in_game.move_to_console()
        macro.in_game.endurance_wait_reset()
except KeyboardInterrupt:
    print("Ctrl + C will end the macro here!")

print("TwineW package imported successfully! Start building with it.")
```

If you would like to run the macro a specific amount of times, utilize `range`.

```python
from TwineW import TwineW as macro

try:        # Use 'try' to be able to get out of the infinite loop
    for i in range(10)        # Will loop the macro ten times.
        macro.main_screen.begin()
        macro.main_screen.main_screen_actions()
        macro.main_screen.launch_and_load()
        macro.in_game.move_to_console()
        macro.in_game.endurance_wait_reset()
except KeyboardInterrupt:
    print("Ctrl + C will end the macro here!")
```

To edit specific data inside of each macro, do so inside the parentheses.

ex.)
```python
macro.main_screen.begin(begin_time=5, name='Joeballz')
```

Which wil return with the intended values.
