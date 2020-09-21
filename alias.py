import os
import sys

location=str(os.getcwdb())[2:-1]
path="alias cryptologer='python3 %s/cryptologer.py'" % location
with open('/root/.bash_aliases','w') as f1:
        f1.write(path)
f1.close()

with open('/root/directory.txt','w') as f2:
        f2.write(location)
f2.close()

sys.exit()

