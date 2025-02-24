
# Een ugly number is een nummer dat een positief en heel getal is, en alleen 2, 3 of 5 als priemfactor heeft

class UglyNumber:
    def isugly_number(self, input):
        if input <=1:
            return False

        done = False
        while not done:
            if input %2==0:
                input = input / 2
            if input %3==0:
                input = input / 3
            if input %5==0:
                input = input / 5

            if input % 2 != 0 and input %3 != 0 and input % 5 != 0:
                done = True
            if input == 1:
                done= True

        if input == 1:
            return True
        else:
            return False


object = UglyNumber()
print(object.isugly_number(1))


# exercise ugly number
# roman numerals
# while loopje, true/false iets met uitkomsten
# unit tests
getal = "I"
getal += "I"
getal = getal + "I"
