import os
print(os.name)
print(os.getcwd())

print(os.path.abspath("Scripting.py"))

print(os.listdir('.'))



print("=======================================")

try:
    file="aaagfg.txt"
    f=open(file,'r')
    text=f.read()
    f.close()
except IOError:
    print('problem reading,'+file)    

