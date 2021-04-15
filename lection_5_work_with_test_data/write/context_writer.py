with open("new_writer.txt", "w") as file:
    for n in range(10):
        file.write(str(n) + "\n")

# For append text in file
with open("new_writer.txt", "a") as file:
    for n in range(20):
        file.write(str(n) + "\n")
