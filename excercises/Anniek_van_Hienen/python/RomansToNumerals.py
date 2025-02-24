# roman numerals
# while loopje, true/false iets met uitkomsten
# unit tests
# getal = "I"
# getal += "I"
# getal = getal + "I"

roman = "V"

class Solution:
    def romanToInt(self, roman: str) -> int:

        dict_romans = {"I":1, "V":2, "X":10, "L":50, "C":100, "D":500, "M":1000}

        getal = 0
        done = False
        index_start = 0

        while not done: # goed punt om te beginnen...
            s = roman[index_start:index_start + 1]
            if s == list(dict_romans.keys())[0]:
                getal += dict_romans[s]
            if s == list(dict_romans.keys())[1]:
                if roman[index_start-1:index_start] == list(dict_romans.keys())[0]:
                    getal -= 2*dict_romans[roman[index_start-1:index_start]]
                getal += dict_romans[s]
            if s == list(dict_romans.keys())[2]:
                if roman[index_start-1:index_start] == list(dict_romans.keys())[0]:
                    getal -= 2*dict_romans[roman[index_start-1:index_start]]
                getal += dict_romans[s]
            if s == list(dict_romans.keys())[3]:
                if roman[index_start-1:index_start] == list(dict_romans.keys())[2]:
                    getal -= 2*dict_romans[roman[index_start-1:index_start]]
                getal += dict_romans[s]
            if s == list(dict_romans.keys())[4]:
                if roman[index_start-1:index_start] == list(dict_romans.keys())[2]:
                    getal -= 2*dict_romans[roman[index_start-1:index_start]]
                getal += dict_romans[s]
            if s == list(dict_romans.keys())[5]:
                if roman[index_start-1:index_start] == list(dict_romans.keys())[4]:
                    getal -= 2*dict_romans[roman[index_start-1:index_start]]
                getal += dict_romans[s]
            if s == list(dict_romans.keys())[6]:
                if roman[index_start-1:index_start] == list(dict_romans.keys())[4]:
                    getal -= 2*dict_romans[roman[index_start-1:index_start]]
                getal += dict_romans[s]

            if index_start == len(roman):
                done = True
            else:
                index_start += 1

        return getal

solution = Solution()
print(solution.romanToInt("MCD"))
