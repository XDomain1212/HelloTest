from pathlib import Path
cwd=Path.cwd()
print(cwd)
new_file=Path.joinpath(cwd,'new_file.txt')
print(new_file)
file_name=new_file.stem
# print(file_name)
parent=cwd.parent
a=parent.parts
print(a)
# for child in parent.iterdir():
#     print(child)
