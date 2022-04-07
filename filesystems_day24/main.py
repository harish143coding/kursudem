

# with open("my_file.txt") as file:
#     contents = file.read()
#     x = 6
#     print(contents)
#     print(type(x))

with open("my_file.txt", mode = 'w') as file:
    # modes 'w' write, 'r' read, 'a' append
    file.write(input("what is the input"))

