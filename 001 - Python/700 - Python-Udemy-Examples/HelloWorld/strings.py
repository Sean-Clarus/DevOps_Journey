print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quoates" in the strings')
print("hello" + " world")
greeting = "Hello"
# name = input("Please enter your name: ")
name = "Sean"

# if we want a space, we can add that too
print(greeting + " " + name)
print(greeting + name)

age = 44
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(name + " is " + str(age) + " years old")
print(type(age))

age_in_words = "2 years"
print(name + f" is {age} years old")

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")