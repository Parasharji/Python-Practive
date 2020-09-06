import os,shutil
print(os.name)
print(os.getcwd())
print(os.path.abspath("Scripting.py"))
print(os.listdir('.'))
path='C:\\Users\\ultim\\Documents\\Python'
list_=os.listdir(path)
for file_ in list_:
    name,ext=os.path.splitext(file_)
    ext=ext[1:]
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)
        
