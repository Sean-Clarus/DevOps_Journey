# parrot = "Norwegian Blue"
# print(parrot)
#
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
#
# print()
#
# print(parrot[-1])
# print(parrot[-14])
#
# print()
#
# print(parrot[-11])
# print(parrot[-1])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])
#
# print()
#
# parrot = "Norwegian Blue"
#
# print(parrot[0:6]) # Norweg
# print(parrot[3:5]) # we
# print(parrot[0:9])
# print(parrot[:9])
#
# print(parrot[10:14])
# print(parrot[10:])
#
# print(parrot[:6])
# print(parrot[6:])
# print(parrot[:6] + parrot[6:])
#
# print(parrot[:]) # prints entire of the variable
#
# print(parrot[-4:-2])
# print(parrot[-4:12])
#
# print(parrot[-14:-8])
#
# parrot = "Norwegian Blue"
#
# print(parrot[0:6:2])
# print(parrot[0:6:3])
#
# number = "9,223,372,036,854,775,807"
#
# print(number[1::4])

# number = "9,223;372:036 854,775;807"
# separators = ""
#
# for char in number:
#     if not char.isnumeric():
#         separators = separators + char
#
# print(separators)
#
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])


number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

# print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))