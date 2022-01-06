import os

os.chdir("c:\\Users\\Jeff Clapper\\Documents\\programming\\Code_Projects\\general_py_practice\\os_work\\actual_os_work")
curr_dir = os.getcwd()

direct = curr_dir.split('\\')
for ind in range(len(direct)):
    direct[ind] = f"{direct[ind]}\\"

previous = direct.pop()

curr_dir = "".join(direct)
os.chdir(curr_dir)
curr_dir = os.getcwd()

def get_subfolder_count(directory,count=0):
    # Recursively counts all subfolders in a folder, including those in sub-folders. This fails what I hoped would work because not all files end in a .XXXX
    # So maybe there is a type feature in OS
    for child in os.listdir(directory):
        if child == "Pipfile":
            continue
        elif "." not in child:
            count+=1
            count = get_subfolder_count(f'{directory}\\{child}',count)

    return count

print(get_subfolder_count(curr_dir))

os.chdir(f"{curr_dir}\\{previous}")
stats = os.stat("new_file_2.txt")
print(stats)