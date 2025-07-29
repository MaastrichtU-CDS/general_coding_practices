#

class Solution:
    def num_to_romans(self, num: int, ):

        roman = ""

        while num >= 1000:
            roman += "M"
            num -= 1000
        while num >= 900:
            roman += "CM"
            num -= 900
        while num >= 500:
            roman += "D"
            num -= 500
        while num >= 400:
            roman += "CD"
            num -= 400
        while num >= 100:
            roman += "C"
            num -= 100
        while num >= 90:
            roman += "XC"
            num -= 90
        while num >= 50:
            roman += "L"
            num -= 50
        while num >= 40:
            roman += "XL"
            num -= 40
        while num >= 10:
            roman += "X"
            num -= 10
        while num >= 5:
            if num == 9:
                roman += "IX"
                num -= 9
            else:
                roman += "V"
                num -= 5
        while num >= 1:
            if num == 4:
                roman += "IV"
                num -= 4
            else:
                roman += "I"
                num -= 1
        return roman

solution = Solution()
print(solution.num_to_romans(3900))

### GPT improvement suggestion:

class Solution:
    def num_to_romans(self, num: int):
        if num <= 0 or num >= 4000:
            raise ValueError("Roman numerals are not negative or larger than 4000")

        roman_numerals = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV",
            1: "I"
        }

        roman = ""
        for value, numeral in roman_numerals.items():
            while num >= value:
                roman += numeral
                num -= value

        return roman

solution = Solution()
print(solution.num_to_romans(3900))