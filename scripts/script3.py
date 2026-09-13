#context mangers
with open ("students.txt", "w") as file :
    file.write("Ali\n")
    file.write("Sara\n")
    file.write("Rehab\n")


with open ("students.txt", "r") as file :
    content = file.read()
print(content)
