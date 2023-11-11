import os
import shutil

from_dir = "D:\Jemi's folder"
to_dir = "D:\Jemi's folder\Document_files"
#you will need to change the file locations above to make the code below work, and you must also create a file called Document files so there is a location to put the segregated files

list_of_files = os.listdir(from_dir)
#print(list_of_files)
print("top")
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    print()
    if extension == "":
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = from_dir + '/' + file_name                             
        path2 = to_dir + '/' + "Document_Files"                        
        path3 = to_dir + '/' + "Document_Fieles" + '/' + file_name

        if os.path.exists(path2):
          print("Moving this file:" + file_name)

          # Move from path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving this file:" + file_name)
          shutil.move(path1, path3)
