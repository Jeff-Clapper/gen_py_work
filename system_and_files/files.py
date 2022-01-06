import os

os.chdir("c:\\Users\\Jeff Clapper\\Documents\\programming\\Code_Projects\\general_py_practice\\os_work\\actual_os_work")
curr_dir = os.getcwd()

with open("new_file.txt", "r") as file:
    lines = file.readlines()
    for ind in range(len(lines)):
        lines[ind] = "Haha! I've stolen all of your day-tas\n"

    with open("new_file_2.txt","w") as newFile:
        newFile.writelines(lines)

with open("new_file_2.txt","r") as file:
    for line in file:
        print(line)

alter_dir = curr_dir.split("\\")
alter_dir.pop(-1)
new_dir = ""

for value in alter_dir:
    new_dir = (f"{new_dir}{value}\\")

children = os.listdir(new_dir)


# print(children)
# print("------------------------------------------\n")

# print(f"{new_dir}{children[2]}\\")
# print("--------------------------------------------")
# print(os.listdir(f"{new_dir}{children[2]}\\"))

with open(f"{new_dir}{children[2]}\\hello.txt", "w") as file:
    contents = file.write("Hello World! \nI'm editing this from ad different program!\n")

with open(f"{new_dir}{children[2]}\\hello.txt", "r") as file:
    contents = file.read()
    print(contents)
