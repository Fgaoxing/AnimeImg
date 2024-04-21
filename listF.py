import os
from pathlib import Path

for i in os.listdir("."):
    if Path(i).suffix[1:] in "png|gif|jpg|jpeg|bmp|ico|svg" and os.path.isfile(i):
        print(i)