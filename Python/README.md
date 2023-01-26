# Python best practices

This is an example project demonstrating best practices for python. The game 
tic-tac-toe was implemented, intending to show how to write clean and easy to 
read code in python. The code for the game comes from the Real Python 
tutorial [1].

## Dependencies

- [required] Tcl/Tk
- [required] Python 3.7 or greater
- [optional] Pyenv
- [optional] Virtualenv
- [optional] Anaconda

## Virtual environment

We recommend that virtual environments should be created per project. There 
are several ways to create a virtual environment for python. Here we will 
show how to create environments with `virtualenv` [2] and manage the python 
version with `pyenv` [3].

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

This method works in Linux and MacOS and should also work for Windows 
with some tweaks. Another option to manage environments and python versions 
is by using Anaconda [4].

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
popular style guide for python is PEP8 [5, 6]. An easy way to make sure that 
you are following the PEP8 guidelines is by using a tool for style guide 
enforcement. We recommend you to use `flake8` [7]. Then you can execute the 
following to check whether your code is compliant:

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

We use the `pytest` library [8] to automate unit-testing for our game. You can 
check whether the code is passing all the tests by executing the following 
in the command line:

``` shell
(.venv) $ pytest
```

## GitHub actions

You can use GitHub actions to automate testing and linting (style checking) 
when pulling/pushing from/to GitHub [9]. The file `github_actions.yml` 
contains an example of a Python workflow [10]. This file has to be placed in 
the `.github/workflows` directory in the root of your repository.

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

- [[1] Tic-Tac-Toe game in Python](https://realpython.com/tic-tac-toe-python/)
- [[2] Virtualenv documentation](https://virtualenv.pypa.io/)
- [[3] Pyenv documentation](https://github.com/pyenv/pyenv#installation)
- [[4] Anaconda documentation](https://docs.anaconda.com/anaconda/install/)
- [[5] PEP8 - the Style Guide for Python Code](https://pep8.org/)
- [[6] PEP8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [[7] Flake8: Your Tool For Style Guide Enforcement](https://flake8.pycqa.org/)
- [[8] Pytest documentation](https://docs.pytest.org)
- [[9] GitHub Actions documentation](https://docs.github.com/en/actions)
- [[10] GitHub Actions example](https://gist.github.com/riccardo1980/11a92a0bfac23306b91d7ea7b4104605)
