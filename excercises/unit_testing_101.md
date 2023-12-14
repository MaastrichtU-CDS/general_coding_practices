# Unit testing 101:

In this project we will practise with unit testing. We will follow the excercises depicted in here.
The goal of these excercises is to get into the habit of writing unit-tests and to practise debugging.
The examples are trivial tasks, and normally you might not implement things this way, but for the sake of practising unit testing they are set up this.

Target audience:
- Researchers who want to improve their scripts & ability to analysis their code: excercise 1 & 2
- Programmers who want to release full libraries: all exercises 

The project serves as a baseline, that already contains the necesary dependencies.

During this project we are going to train a decision tree using information gain. The We will be using the Iris dataset.

These excercises have been setup using an OO approach to programming. While you can of course implement everyhing in a functional manner we suggest you take the OO approach as the questions provided in this exercise are made to guide you in the correct direction.

If you are doing these excercises in Java you can use the pom.xml provided in this project to import the necesary dependencies in a maven project.
Additionally checkstyle.xml can be used as the code-style file.
No other dependencies should be needed.

If you are doing these excercises in Python you can use the libary "csv" and the method csv.reader(file, delimiter) to read the csv. For the unittests you can use the libary "unittest"
No other python libraries should be needed.

Try to avoid other libraries, and especially avoid libraries such as Pandas which already do a lot of error handling for you. The goal of these excercises is to learn how to debug yourself, not to have libraries do this for you.

If you have questions contact someone from CDS informatics for help!

## Excercise 1): reading the data

During excercise 1 we will implement the framework for reading the data.
This framework will consist of the following:

- An Attribute class, which will contain the attribute name and value. 
- An Individual class, which contains the attributes belonging to an individual record, represented using the Attribute class.
- A readCSV method, which can read a csv file and transforms eachs row into a list of String values
- A parseCSV method, which takes the output of readCSV and transforms each row from a list of String values into an object of the Individual class which contains its attributes represented using the Attribute class.

Using the first row of the Iris dataset it means we transform the data from a CSV format:
```
sepallength,sepalwidth,petallength,petalwidth,label
5.1,3.5,1.4,0.2,Iris-setosa
```

into an Individual, represented here using a python dictoniary: 

```
{
    'attributes': [
        {'name': 'sepallength', 'type': 'float', 'value': 5.1},
        {'name': 'sepalwidth', 'type': 'float', 'value': 3.5},
        {'name': 'petallength', 'type': 'float', 'value': 1.4}
        {'name': 'petalwidth', 'type': 'float', 'value': 0.2}
        {'name': 'label', 'type': 'String', 'value': Iris-setosa}
    ]
}
```

Follow the following steps while implementing:

1) Create a package "data"
2) Put the class "Attribute" in this package
3) Implement an enum "Type" for the various attribute types (Enums in python: https://docs.python.org/3/library/enum.html, Enums in Java: https://www.w3schools.com/java/java_enums.asp)
4) Implement three fields: name, value, type in the class "Attribute"
5) Add the class "Individual" to the "data" package
6) Implement the field "attributes" in the class "Individual" so you can add individual attributes to an Individual.


7) Create a second package "Util" and implement a class "util.CSVReader"
    - In the class "Parser" implement a method "ReadCSV"
        - This method takes as input the path to the CSV, as output it returns the content of the CSV.
        - Each row in the CSV becomes a List of String values
        - The full CSV will be a List of rows
    - Implement a method "ParseCSV"
        - This method takes as input the path to the CSV, the output is a list of Individuals
        - This method uses the ReadCSV method we implemented before


8) Implement unit tests for these methods The following needs to be checked at minimum:
    - Check the methods you implemented to check the AttributeType of a value, create at least 1 test per Type
    - Check the parser works:
        - Does it return the correct number of records?
        - Does each record have the correct number of attributes?
        - Are the attributes the correct type?
        - Do the attributes have the correct name?
        - Do they have the correct value? (Check a small sample)
	- What is the best way to solve the problems you encounter? Are the problems you find because of bad code or is the CSV wrong? Can you solve everything programaticly or do you to solve some things manually?

#### Questions:

1) What types should the various fields in Attribute be to use this class in a generic setting?
2) Why do we need an enum for AttributeType?
3) What type should the field "Attributes" be in the class "Individual"
4) How do we make sure that "ParseCSV" sets the types correctly for each attribute?

#### Debugging:

Several of the records do not have the correct number of attributes. Let's find out why.

1) Place a breakline in "Parser" in either the readCSV or parseCSV method. Can you find the broken record this way?
2) Add an if-statment in an oppertune place to try to catch the record of incorrect length (e.g.
   add `in.getAttributes().size() < EXPECTED_LENGTH`) and put a breakpoint in the if-statement to catch the correct
   record.
3) What is the reason these record have the incorrect amount of attributes?
4) Fix it.

## Excercise 2): Comparing attributes:

To be able to build a decision tree we will need to compare attributes. In the Attribute class implement a method to
compare two attribute values. The method takes two Attributes as its input and returns the following:

- -1 if the first value is smaller than the second, 0 if the values are equal, 1 if the second value is bigger

Write unit tests to check the correct functioning of this attribute. Include the following:

- A unit test for each AttributeType
- A unit test for edge-cases of the various types (e.g. comparing to zero, comparing to -inf etc.)
- A unit test for comparing different AttributeTypes

### Questions:

- How could you handle different AttributeTypes being compared?

## Excercise 3) The parts needed to build a tree:

To build a tree we will use the InformationGain ( https://en.wikipedia.org/wiki/Information_gain_(decision_tree) )

To implement this we will first need to create the individual parts of our tree.

1) Create a new class "AttributeRequirement" in the package "data"
2) Add a field "requirement" to this class, this field represent the Attribute value against which you will test if you
   fullfill the requirement
3) Create a new package "tree", and add a class "Node"
4) Add two fields, leftChild and rightChild of the type "Node"
5) Add a field "requirement" of the type "AttributeRequirement" to the class "Node"
    - The leftChild will be used if `value <= AttributeRequirement` for a given individual, the rightChild
      if `value > AttributeRequirement`
6) Implement a method in AttributeRequirement to determine if the requirement is fullfilled by an individual, make sure
   to use the method you implemented earlier to compare attributes
7) Write unit tests to check AttributeRequirement works correctly.

### Excercise 4) Implementing informationgain

To implement informationgain follow the following steps:

1) Add a class "DecisionTree" to the package "tree"
2) Add a field "root", of the type "Node", this is the root Node of the tree
3) Add a method "calculateInformationGain", the input of this method is a list of AttributeRequirements, the
   AttributeRequirement under consideration to be added and a list of Individuals. The output is the informationgain of
   adding this new AttributeRequirement. Informationgain is equal to the different in Shannon Entropy before and after
   adding the new requirement ( https://en.wikipedia.org/wiki/Entropy_(information_theory) )
5) Implement unit tests check the informationgain is calculated correctly. Make sure the following is contained:
    - At least one unit test per attribute in the Iris dataset. Use a sample of attributeRequirements.

#### Questions:

- When you implement the informationgain tests you should notice some attributes appear to contain mixed AttributeTypes.
  What happened here?
- Debug this problem.

### Excercise 5) training a tree:

To implement the training of a tree we will use a recursive method "DetermineChildNode"
DetermineChildNode will use the structure given in the following bit of pseudocode:

```
DetermineChildNode(List<Individuals> individuals){
if(individuals.size < minimum){
   return new LeafNode(DetermineMajorityLabel(individuals))
} else if(Entropy(individuals) < minimumEntropy){
   return new LeafNode(DetermineMajorityLabel(individuals))
}else{
   Node n = new Node()
   n.setRequirement(DetermineRequirementWithBestInformationGain(Individuals))
   n.setLeftChild(DetermineChildNode(determineLeftIndividuals(individuals, n.getRequirement()))
   n.setRightChild(DetermineChildNode(determineRightIndividuals(individuals, n.getRequirement()))
   return n;
}
```

By calling it with the full list of individuals representing the entire dataset you will gain the rootnode.

Don't forget to implement unit tests that check if you get the correct decision tree consistently.

#### Questions:

- How do you implement a LeafNode? Can you reuse the code for the Node Class?
- InformationGain is a deterministic method, do you get the same trees as other PhD's? What about when you use a
  publicly available library (e.g. WEKA: https://www.cs.waikato.ac.nz/ml/weka/ )



