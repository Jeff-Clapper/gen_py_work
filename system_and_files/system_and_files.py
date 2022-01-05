# lines = []

# with open('.\\new_file.txt', "r") as new_file:
#     for line in new_file:
#         if line == "\n":
#             continue
#         else:
#             lines.append(line[:-1])
#             print(line)

#     print(lines)
#     print("------------------------------------------------------------")
    


with open('new_file.txt',"r") as file:
    contents2 = file.readlines()
    # while contents2:
    #     print(contents2, end="")
    #     contents2 = file.read(25)

    # file.seek(0)
    # contents2 = file.read(25)
    # print("\n\nthis is a second run")
    # print(contents2)
    

    with open('.\\new_file_2.txt', "w") as new_file:
        new_file.writelines(contents2)
    with open('.\\new_file_2.txt', "a") as edit_file:
        edit_file.write("\nthis is new...")

with open('.\\new_file_2.txt', "r") as theFile:
    contents = theFile.read()
    print(contents)

with open('.\\new_file.txt', "r") as file:
    contents = file.read()
    print(contents)