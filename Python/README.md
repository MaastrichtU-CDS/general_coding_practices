# Python best practices

This is an example project demonstrating best practices for python. The game 
tic-tac-toe was implemented, intending to show how to write clean and easy to 
read code in python. The code for the game comes from the Real Python 
tutorial [1].

## Dependencies

- [required] Tcl/Tk
- [required] python 3.7 or greater
- [optional] pyenv
- [optional] virtualenv
- [optional] Anaconda

## Virtual environment

We recommend that virtual environments should be created per project. There 
are several ways to create a virtual environment in python. Here we will 
show how to create environments with `virtualenv` and manage the python 
version with `pyenv`.

You can install a particular python version by doing the following:

``` shell
$ pyenv install 3.7.11
```

Now that you have the correct python version, you can create your environment:

``` shell
$ virtualenv -p ~/.pyenv/versions/3.7.11/bin/python .venv
```

Next, you should activate your environment and install the dependencies:

``` shell
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt
```

This method works for Linux and MacOS users, if you are a Windows user you 
can achieve the same with Anaconda.

## How to run

You can run the game by executing the following in the command line:

``` shell
(.venv) $ python main.py
```

Another option is to run `main.py` directly from your favourite IDE. In both 
cases, make sure that you are running the code within the correct virtual 
environment.

## Code style

It is very important to write clean code to improve readability. The most 
popular style guide for python is PEP8. An easy way to make sure that you are 
following the PEP8 guidelines is by using a tool for style guide enforcement.
We recommend you to use `flake8`. In order to check whether your code is 
compliant, you can run:

``` shell
(.venv) $ flake8 .
```

This will check all python code in your current directory recursively. The 
file `.flake8` contains local configurations for `flake8`. You can edit it 
to account for your personal preferences.

## Unit tests

An important aspect of writing robust code, is to make sure that it works as 
expected. A common way to ensure that your code is doing what it is meant to do 
is by writing unit tests. These tests are also useful to make sure that new 
releases of your code do not lead to unexpected behaviours or break things 
that were previously working. The `tests` directory in this project, contains 
some unit tests for the tic-tac-toe game, which exemplifies how to write a 
unit test and which types of cases are useful to cover. 

We use the `pytest` library to automate unit-testing of our game. You can check 
whether the code is passing all the tests by executing the following in the 
command line:

``` shell
(.venv) $ pytest
```

## General remarks

Besides what was mentioned before, we encourage you to check how the game 
was implemented. The writing style is supposed to be clean and easy to 
understand. An important aspect of writing good code is to know how to break 
pieces of code in logical parts and make use of functions, classes and 
methods where appropriate.

The project structure you use can also help others to easily navigate through 
your code. So make use of appropriate names for your directories and files 
and remember to break up elements in logical parts.

Also, remember to add enough comments in your code, but do not overdo it.
Code that is properly writen and well styled is often self-explanatory. But 
do add comments when you think they are necessary to guide others and also 
your future self to understand your thought process and reasoning. 
Furthermore, make use of docstrings, specially for functions and methods 
with inputs and outputs. This will help others in using them and also 
in debugging should something go wrong.

Finally, the general advice is that you should be self-consistent and clean. If 
your project is small or a one-off analysis, you might consider unnecessary to 
follow all guidelines, this is okay, but please make sure to write code that 
is readable. 

## References

- [1. Tic-Tac-Toe game in Python](https://realpython.com/tic-tac-toe-python/)
