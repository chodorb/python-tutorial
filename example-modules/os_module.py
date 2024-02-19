# Potrzebny jest skrypt który przeniesie dane z folderu 1 do 2
import os
import sys

src = sys.argv[1]
dest = sys.argv[2]

if os.path.exists(src) and os.path.isdir(src):
    os.rename(src, dest)
else:
    print("Folder doenst exist")
    
