with open('learning_python_read.txt') as file_object:
    contents = file_object.read()
    print(contents)

file_name = 'learning_python_read.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

file_name = 'learning_python_read.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())