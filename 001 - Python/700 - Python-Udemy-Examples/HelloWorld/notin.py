# https://docs.python.org/3/library/stdtypes.html

activity = input("What would you like to do today? ")

if "cineam" not in activity.casefold():
    print("But I want to go to the cinema")