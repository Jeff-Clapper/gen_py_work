import os


current_dir = os.getcwd()
# print(current_dir)

"""This didn't work for now. More accurately, I do not know what this does"""

curr_user = os.getlogin()
# print(curr_user)

process_id = os.getpid()
# print(process_id)

"""THE STUFF ABOVE IS DEALING WITH THINGS ABOVE MY HEAD REGARDING SYSTEM FILES"""
"""BELOW WORKING ON OS FILES AND DIRECTORIES SECTION"""

print(f'current directory: {current_dir}')

os.chdir('')
print(os.getcwd())