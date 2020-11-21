import os

folderdir=r'E:\Coding\Python\Python-Practice'


def process_rename(folderdir):
    for item in os.listdir(folderdir):
        if('.git' in item):
            continue
        _name=folderdir+ '\\'+item
        if(os.path.isdir(_name)):
            process_rename(_name)

        
        newname=folderdir+ '\\'+item.replace(' ','')
        os.rename(_name,newname)
process_rename(folderdir)
print("done")