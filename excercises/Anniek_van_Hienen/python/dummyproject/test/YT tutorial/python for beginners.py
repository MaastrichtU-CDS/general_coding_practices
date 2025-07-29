# https://www.youtube.com/watch?v=kqtD5dpn9C8&t=2444s
weight = float(input("Weight: "))
print(weight)

unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))


