import os
import sys

#needed functions: prefix
# addpath = "Unknown folder/"

#File delete function with fault exception
def delete(file):
    try:
        print("Deleting " + file)
        os.remove(addpath + file)
    except:
        print("Error: File" + file + " is missing. Moving on.")

def filesize(file):
    size = os.path.getsize(addpath + file)
# Decide what unit to use
    if size >= 1024**3:
        size = str(round(size / 1024**3, 3))
        unit = "GB"
    elif size >= 1024**2:
        size = str(round(size / 1024**2, 3))
        unit = "MB"
    elif size >= 1024:
        size = str(round(size / 1024, 3))
        unit = "KB"
    else:
        size = str(size / 1024) + " B"
    return size


addpath = "Unknown folder/"
path = os.path.dirname(sys.argv[0]) + "/" + addpath
print(path)
dir = os.listdir(path)

ans = "y"
while ans == "y": # Repeat until ans is valid
    suffix = input("\nWhat extension are you looking for?\n")

    print("\nSearching for files ending in \"" + suffix + "\"...")
    list = []
    for file in dir:
        if file.endswith(suffix):
            list.append(file)

    dtotal = 0
    for file in list:
        fsize = filesize(file) #Filesize value is obtained and turned into int value
        print("{0:50}      {1:10}".format(file, fsize))

    if input("\nWould you like to delete all files?\n") == "y":
        for file in list:
            delete(file) #Call on delete function
        print("\nDeletion complete.")

    while True:
        ans = input("Restart? (y/n)\n")
        if ans == "n" or ans == "y":
            break
        else:
            print("Invalid input.\n")

ans = input("\nProgram finished.\n")
