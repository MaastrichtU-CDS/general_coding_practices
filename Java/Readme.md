# This is an example project for Java best practices

## How to create and run a Java project

Java projects require the following:

- A JDK (java development kit) installation
- A JRE (Java runtime enviroment) installation
- A Maven installation
- An IDE such as intellij.

The IDE is the editor in which you write your code. Modern IDE's such as intellij come with many fancy tools. For
example, it may come with integrated tools for Git, Maven and even tools to manage the JDK & JRE.

For a more manual installation the JDK can be downloaded from
oracle: https://www.oracle.com/java/technologies/downloads/
Maven can be installed from Apache: https://maven.apache.org/download.cgi
And you can use your favorite IDE.

The JDK is what is needed to develop and compile java programs. Your IDE needs to point to a valid JDK. A modern IDE
like Intellij can download a JDK for you.

The JRE is what is needed to execute Jar files, which is the executable file Java normally uses. It is possible to
create a .exe file as well using various tools (maven plugins, 3th party software, etc.)

The Maven is a tool that is used to build your program. It has many plugins, for example it can automaticly run
unit-tests when building, it handles dependencies, it checks the code style, etc.

## How to build & run a Java Maven project:

A modern IDE can handle this for you.

Outside of an IDE you will use the following commands:

- mvn clean install
    - This command needs to be executed in the folder containing the pom.xml file for your project. It will run the
      maven install process which will result in a .jar file. It will also run any maven plugins that are configured,
      such as the plugin for running unit-tests and checking codestyle.
- java -jar project.jar
    - This command will run the jar file.

There are many more maven commands, but these are the two most basics you will need.

## Advantages of using Java

Java projects have the following advantages:

- Mature language commonly used in enterprise software.
    - Because of this there are many well-developed and easy to use tools & libraries to use. The use in enterprise
      software means that these libraries and tools are held to a relativly high standard of quality. For example,
      dependency management using maven is far simpler than anything Python has to offer.
- Reasonably fast performance (faster than C#, slower than C++, magnitudes faster than Python)
- The strict verbosity forces a programmer to follow good practises & protects against certain mistakes.
- Backwards compatible between Java versions.
- Very stable language.
- Supports OOP & FP paradigm (FP has been significantly improved in Java 8 with the introduction of Lambdas)

## Disadvantages of using Java

Java projects have the following disadvantages

- Java is very verbose. If you just want to write extremely basic scripts this may be annoying.
- If you dislike OOP you will not like Java

### When to use Java
These advantages and disadvantages mean that Java is an excellent language for bigger projects that need to be maintained over a longer lifespan.
This especially holds when there is a lot of code you need to implement yourself.

However, small scripts that rely on libraries for 99.99% of the heavy lifting might be easier to implement in other languages such as Python.

## Example project

In this project we show some of the best practices for a Java maven project. The code in this project is not intended to
be perfectly optimized, it is simply an example of how to write "clean" code and use several maven plugins to check the
quality of your code.

The pom of this project can be used as the basis of your own maven project. It contains the necessary dependencies to
set up:

1) Unit testing
2) Test coverage
3) Checkstyle checks
4) Dependency checks.

### Dependency checks

The dependency check plugin checks if all dependencies you've declared in your pom are actually used. It will complain
if you include dependencies that are not used. It will also throw an error if you use dependencies implicitly, you
should declare them explicitly.

### Checkstyle checks

The checkstyle plugin checks if the code you've written fulfills the checkstyle rules you have defined. The rules
included in checkstyle.xml are based on a set of commonly accepted rules (https://checkstyle.org/config_coding.html)
This is similar to PEP in python.

The rules contained in this set fall in two categories:

1) Code-style that is pure personal preference (e.g., do I place a space after { or not?)
2) Code-style that is indicative of common bugs (e.g., magic numbers)

It is important to note that these are merely guidelines and that the rules can be suppressed if needed for specific
cases in case you have a false positive. However, you should avoid this if at all possible as the main goal of these
rules is to create consistency. The benefits of these consistencies are worth the inconvenience of a few false
positives. It is also important to realize it is possible to set up most IDEA's to automatically apply as much of the
code-style as possible. Things like the correct amount of spaces around brackets can easily be automated, and this is
far less annoying than needing to this manually.

However, the style you should use in your project is not set in stone; you can change the checkstyle rules if you notice
a certain rule does not work for you. However, you should always be consistent within a given project.

#### Naming conventions

Checkstyle also covers naming conventions. Like with all rules this is open to personal preference although Java does
have some generally used conventions (i.e., classes use PascalCase and methods use camelCase).

However, there are 2 rules that should always hold:

1) Names should be descriptive. Others should be able to understand at a glance what a variable is purely based on its
   name
2) Avoid acronyms if possible. Your IDEA will auto-complete anyway, do not create unreadable names because you want to
   be lazy. This is especially relevant when it's acronyms you've made up yourself. Commonly known domain specific
   acronyms are acceptable.

#### Comments

Although good code is in theory self-explanatory without any extra information, this does not always hold in practise.
Adding in comments to explain what is going on can be very useful.

This can be form of javadoc comments, but it can also be very useful to add in-line comments in bits of code where
you're doing a complicated calculation. This is especially true when using more complex constructs, like recursion or
lambdas which are generally more difficult to read.

### Test coverage

The plugin for test-coverage tests how much of your code base is covered by your unit-tests As a general rule of thumb
people aim for 70-80% coverage. A high coverage is good because it means you will quickly find out if a new change
breaks some old code. However, bear in mind that a 100% coverage is unrealistic and not necessarily useful.

Again it is possible to suppress the coverage for specific classes or even packages, for example in this project the
packages game.gui and game.main are exempt from test coverage. Use this ability sparingly. More on what should be tested
can be found in the Unit-test section.

### Unit-tests

The unit-test plugin allows you to automatically run all your unit-tests when you build the project.

#### What is important to unit-test?

Unit-tests are important to ensure a developer doesn't accidentally break things with an update. However, not every
single line of code is worth writing a unit-test for.

Unit-tests should be written to test specific behaviours, not the implementations of that behaviour. If you test the
implementations then unit-tests will become extremely annoying during refactor-steps.

This means that you do not want to test methods like getters & setters. Nor do you want to test methods like
MainLoop.main that do nothing of significance on their own. You want to test methods that actually do something useful.

This also means that unit-testing a GUI is not particularly useful as a unit-test for the GUI would mostly concern the
implementation (i.e., is the right amount of buttons created?). It is possible to automate GUI-testing, and this is
important for integration-tests, but far less relevant for unit-tests.

This is why these two packages are excluded in this example project. Other examples of classes that are not particularly
interesting to unit-tests independently would be POJO's.

#### Test Driven Development
A good approach to programming any larger project is to use Test Driven Development (TDD).
The idea behind TDD is that first you design a unit test, which will initially fail. Then you implement your code. Your code is considered finished once the test can be succesfully run. This allows you to work towards a predefined goal. As opposed to defining the test after you finish your code, and simply accepting whatever output your code currently gives.

Try to follow this principle of predefined test-results as much as possible.

# Architecture:

In this project the basics of good architecture can be seen. These principles are not Java specific, but also hold for
other languages. The project is divided into three logical parts:

- The game logic
- The GUI
- The main loop for the program as a whole

These parts have as few dependencies on another as possible. Whenever you write code, you should try to make similar
divisions in your code. This division is important for three main reasons.

First you do not want to create a giant behemoth of a file that is responsible for everything. Dividing things up makes
the project far easier to maintain and work with.

Secondly, by dividing the code into logical subsets you can guarantee the various functions are independent of another.
The game logic should be able to work regardless of how the GUI is implemented.

Third, dividing the code up makes it easier to write small unit-tests. While a single unit-test that covers your entire
code-base can be useful in certain cases, it is often also very useful to have unittests that cover smaller steps in
your code. By testing smaller steps it'll be easier to determine where your error is happening. This is why this project
both has a GameTest, which tests basically everything, and individual unit-tests for the different player variants & the
board itself

Within these logical parts the code is further subdivided. The game-logic contains a class that keeps track of the main
game, a class that keeps track of the state of the board, and a package that implements various types of players.

In the implementation of players you can further see how this division can help you plugin different variants into a
generic framework. The core of players is the Player class, which is abstract, and there are three actual types of
players: HumanPlayer, RandomAi and AlphaBetaAi. Each of these players determines what move to play differently, but
thanks to the shared generic parent class they can be used interchangeably.


