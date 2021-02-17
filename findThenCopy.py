from sys import exit
import os
import shutil

# 1- Enter the path of the dir you want to search in
user_input_path= input('What is the name of your directory')
print(user_input_path)


if os.path.exists(user_input_path):
    print("Source directory exists")
    directory = os.listdir(user_input_path)
else:
    print("Source directory is not found")
    exit(1)

# 2- Enter the string you are searching about
searchstring = input('What word are you trying to find?')

# 3- Enter the path of the dir you want to save the file in
dstpath = input('Enter the path you want to save the file in')
print(dstpath)
if os.path.exists(dstpath):
    print("directory exists")
else:
    print("destination dir is not found")
    exit(1)

# 4- find the string
for fname in directory:
    if os.path.isfile(user_input_path + os.sep + fname):
        # Full path
        f = open(user_input_path + os.sep + fname, 'rb')

        if searchstring in f.read().decode(errors='replace'):
            print('found string in file %s' % fname)
            filepath = user_input_path+"/"+fname
            print(filepath)
            if os.path.exists(dstpath):
                print("directory exists")
                try:
                    shutil.copyfile(filepath, dstpath+"/"+fname)
                except IOError as e:
                    print("Unable to copy file. %s" % e)
                    exit(1)
                print("\nFile copy done!\n")

        else:
            print('string not found')
        f.close()
