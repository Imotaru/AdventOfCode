f = open("day7input.txt", "r")

all_lines = f.readlines()

line_count = 0

current_directory = "."
last_command = ""

maximum_dir_size = 100000
size_sum = 0

total_disk_space = 70000000
space_required = 30000000

dir_list = []

class file:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

class dir:
    def __init__(self, name: str, sub_directories: list, files: list[file], size: int, parent):
        self.name = name
        self.sub_directories = sub_directories
        self.files = files
        self.size = size
        self.parent = parent

root = dir(name=".", sub_directories=[], files=[], size=-1,parent=None)

def get_current_dir() -> dir:
    path = current_directory.split("/")
    current_dir = root
    i = 0
    for dir_name in path:
        if i == 0 and dir_name == ".":
            continue
        for dir in current_dir.sub_directories:
            if dir.name == dir_name:
                current_dir = dir
                break
    return current_dir

# build file system
for line in all_lines:
    line = line[:-1]
    if line == "$ cd /":
        current_directory = "."
        last_command = "cd"
        print(f"{line} => {current_directory}")
    elif line == "$ cd ..":
        last_slash = current_directory.rindex("/")
        current_directory = current_directory[:-(len(current_directory) - last_slash)]
        last_command = "cd"
        print(f"{line} => {current_directory}")
    elif line.startswith("$ cd "):
        current_directory += "/" + line[len("$ cd "):]
        last_command = "cd"
        print(f"{line} => {current_directory}")
    elif line == "$ ls":
        last_command = "ls"
    elif line[0] != "$":
        if last_command == "ls":
            current_dir = get_current_dir()
            file_desc = line.split(" ")
            if line[0].isnumeric():
                current_dir.files.append(file(name=file_desc[1], size=int(file_desc[0])))
            else:
                current_dir.sub_directories.append(dir(name=file_desc[1], sub_directories=[], files=[], size=-1, parent=current_dir))
        else:
            print(f"unhandled line: {line}")

    line_count += 1

space_to_free = 0

# set sizes of all directories
def recursive_set_size(directory: dir):
    dir_size = 0
    for sub_dir in directory.sub_directories:
        if sub_dir.size == -1:
            recursive_set_size(sub_dir)
        dir_size += sub_dir.size
    for f in directory.files:
        dir_size += f.size
    directory.size = dir_size
    if (directory.size <= maximum_dir_size and directory.parent != None):
        global size_sum
        size_sum += dir_size

    dir_list.append(directory)

    if directory.parent is None:
        print(f"root size: {directory.size}")
        print(f"unused space: {total_disk_space - directory.size}")
        global space_to_free
        space_to_free = space_required - (total_disk_space - directory.size)
        print(f"space required: {space_to_free}")

recursive_set_size(root)

smallest_dir = space_required
for d in dir_list:
    if d.size >= space_to_free and d.size < smallest_dir:
        smallest_dir = d.size

print(f"result 1: {size_sum}, result 2: {smallest_dir}")