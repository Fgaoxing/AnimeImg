import os
from pathlib import Path
tmp = {}
for i in os.listdir("."):
    if Path(i).suffix[1:] in "png|gif|jpg|jpeg|bmp|ico|svg" and os.path.isfile(i):
        tmp[int(Path(i).stem)] = Path(i).suffix
tmp2= list(tmp.keys())
tmp2.sort()
for k in tmp2:
   print(str(k)+tmp[k])