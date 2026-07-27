message = "Hello Linux!"

with open("test.txt", "w") as file:
    file.write(message)

print("File created successfully!")