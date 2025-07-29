# https://pynative.com/python-basic-exercise-for-beginners/
class Solutions:
    def multiply(self, number1, number2):
        product = number1*number2
        if product <= 1000:
            return product
        else:
            return number1 + number2

solution = Solutions()
result = solution.multiply(40,30)
# print("The result is", result)

# 2
PreviousNumber = 0

for i in range(10):
    sum = i + PreviousNumber
    print("Current Number", i, "Previous Number", PreviousNumber, "Sum", sum)
    PreviousNumber = i

# 3
string = "pynative"

for i in range(0, 8, 2):
    print("Original string is", string, string[i])

# 4

# my solution:
input = "pynative"
n = 2

print("removing first characters:", input[n:len(input)])

# proposed solution
def remove_chars(word, n)
    print("Original string:", word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))

# 5
def firstnumber_is_lastnumber(given_list):
    first_num = given_list[0]
    last_num = given_list[-1]

    if first_num == last_num:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]

print("result is", firstnumber_is_lastnumber(numbers_x))

# 6
class Solution:
    def divisible_five(self, given_list):
        print("Given list is", given_list)
        print("Divisable by 5:")

        for i in range(len(given_list)):
            if given_list[i] % 5 == 0:
                print(given_list[i])

solution = Solution()
numbers = [10, 20, 33, 46, 55]
solution.divisible_five(numbers)

# 7
str_x = "Emma is good developer. Emma is a writer"
var = "Emma"

num = str_x.count(var)

print(var, "appeared", num, "times")