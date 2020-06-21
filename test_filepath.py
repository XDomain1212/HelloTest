from pathlib import Path
cwd=Path.cwd()
print(cwd)
new_file=Path.joinpath(cwd,'new_file.txt')
print(new_file)
parent=cwd.parent
for child in parent.iterdir():
    print(child)
