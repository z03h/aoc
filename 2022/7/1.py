from __future__ import annotations
from typing import Optional

from collections import deque

filename = 'input.txt'

with open(filename) as f:
    data = f.read()

class File:
    def __init__(self, name: str, parent: Folder, size: int) -> None:
        self.name = name
        self.parent = parent
        self.size = size

class Folder:
    def __init__(
        self,
        name: str,
        parent: Optional[Folder] = None
    ) -> None:
        self.name: str = name
        self.parent = parent
        self.subfolders: dict[str, Folder] = {}
        self.files: dict[str, File] = {}
        self.size = 0

    def calculate_size(self):
        for folder in self.subfolders.values():
            folder.calculate_size()
            self.size += folder.size

        for file in self.files.values():
            self.size += file.size

    @property
    def small(self):
        return self.size <= 100000


root: Folder = Folder('/', None)

current_folder: Folder = root

commands = iter(data.split('\n'))
next(commands)

while True:
    try:
        cmd = next(commands)
    except StopIteration:
        break
    if cmd[0] == '$':
        # command
        action = cmd.split()
        if action[1] == 'cd':
            # change directory
            new_directory = action[2]
            if new_directory == '/':
                current_folder = root
            elif new_directory == '..':
                current_folder = current_folder.parent or root
            else:
                current_folder = current_folder.subfolders[new_directory]
        elif action[1] == 'ls':
            pass
    elif cmd.startswith('dir'):
        # add sub directory to current folder
        _, folder = cmd.split()
        if folder not in current_folder.subfolders:
            current_folder.subfolders[folder] = Folder(folder, current_folder)
    else:
        # file
        size, filename = cmd.split()
        current_folder.files[filename] = File(filename, current_folder, int(size))


root.calculate_size()
dirs: deque[Folder] = deque([root])
total_size = 0
while True:
    if not dirs:
        break
    node = dirs.popleft()
    if node.small:
        total_size += node.size
    dirs.extend(node.subfolders.values())
print(total_size)
