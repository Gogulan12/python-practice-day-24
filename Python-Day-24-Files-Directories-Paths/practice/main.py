# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")


# with open("C:\\Users\gogul\Desktop\\100 Days of Code The Complete Python Pro Bootcamp for 2022\\2. Intermediate Python\Python-Day-24-Files-Directories-Paths\practice\my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("..\practice\my_file.txt") as file:
    contents = file.read()
    print(contents)