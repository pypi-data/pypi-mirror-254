import os
import random
from datetime import datetime

exit(0)
# Configs
program_path = r""
exclude_files = [
    'random-open.cmd', 
]
# record open history
log_file = "./openLog.txt"

# Convert excludeFiles into a set for better search
exclude_files = set(exclude_files)

# List files, count valid files
file_name_list = [file for file in os.listdir() if os.path.isfile(file)]
valid_files = [name for name in file_name_list if name not in exclude_files]
valid_num = len(valid_files)

index = random.randint(0, valid_num - 1)
name = valid_files[index]
print(f'chosen file: {name}')


with open(log_file, 'a', encoding='utf-8') as log:
    log.write(f"{datetime.now()}\n")
    log.write(f"chosen file: {name}\n")
    log.write("============================\n\n")


if program_path == "":
    os.system(f'"{name}"')
else:
    os.system(f'{program_path} "{name}"')

print("all done")
