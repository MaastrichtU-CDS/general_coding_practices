# TDD Example excericses

This project is based on the example Java project. However, this project is incomplete and broken in various ways.

To practise TDD development, improve the implementation of this project. If you get stuck you can use the example
project as a reference.

Good luck

## Excercise 1:

- Fix the failing unit tests

## Exercise 2:

- Implement a human player

## Excercise 3:

- Implement the alpha-beta player: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

Alpha-beta is a search algorith used for playing games. It is a fairly straightforward algoritm where the AI looks a
number of moves ahead and scores the gamestates.It will then pick the move that will lead to the best state it can
reach. Since three in a row is relativly simple, Alpha-beta will be able to play perfectly when implemented correctly
and should never lose, draws are still possible.

To implement it you will need to implement it scoring system for moves. The current implementation of the class will
already select the move that has the best alpha-beta score.

## Exercise 4:

- Improve test coverage until you reach at least 70% coverage. GUI elements are excluded from test-coverage.

The level of test coverage can be checked by ruining "test with coverage in Intellij"
Alternativly, build the project in maven to get an overview of the test coverage


