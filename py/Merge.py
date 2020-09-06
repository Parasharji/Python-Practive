import os , sys, pathlib , shutil
from pathlib import Path

file1=Path(r'C:\Users\ultim\Documents\Python\txt\sample.txt')
file2=Path(r'C:\Users\ultim\Documents\Python\txt\untitled.txt')

new=input("Enter the name of new file")
print('')
print("The merged content of the file will be in ",new)

with open(new,'wb') as wfd:
    for f in [file1,file2]:
        with open(f,'rb') as fd:
            shutil.copyfileobj(fd,wfd,1024*1024*10)

print('\n Merge Operation Successfull !')
print('Do you want to view it ? [y/n]:')
ans=input()
if ans=='y':
    print()
    c=open(new,'r')
    print(c.read())
    c.close()
else:
    print("Bye Bye")
    exit()
        
