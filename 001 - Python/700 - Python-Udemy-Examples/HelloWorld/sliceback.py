letters = "abcdefghijklmnopqrstuvwxyz"

# backwards = letters[25:0:-1]
# backwards1 = letters[25::-1]
# print(backwards)
# print(backwards1)

letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[-10:-13:-1])  # qpo
print(letters[16:13:-1])
print(letters[4::-1])  # edcba

print(letters[-1:-9:-1])  # zyxwvuts

print(letters[-4:])  # brings the last 4 letters
print(letters[-1:])  # brings last item
print(letters[:1])  # brings the first item
print(letters[0])