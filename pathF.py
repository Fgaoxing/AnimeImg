import os
from pathlib import Path


dirls = os.listdir(".")
dirls2 = []
for i in dirls:
    if Path(i).suffix[1:] in "png|gif|jpg|jpeg|bmp|ico|svg" and os.path.isfile(i):
        dirls2.append(i)
dirls = dirls2
print(f"目标{len(dirls)}个")
for i in range(len(dirls)):
    os.rename(dirls[i], str(i) + Path(dirls[i]).suffix)
    print(f"{i} {dirls[i]} -> {str(i) + Path(dirls[i]).suffix}")
