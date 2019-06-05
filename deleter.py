import os
import sys

# needed functions: prefix, zero result handling

# File delete function with fault exception
def delete(file):
    try:
        print("Deleting " + file)
        bsize = os.path.getsize(addpath + file) #Size in bytes
        os.remove(addpath + file)
        return bsize
    except:
        print("Error: File" + file + " is missing. Moving on.")
        return 0

# Determines the right unit for a filesize and calculates for the unit.
# Output is an array.
def filesize(bsize):
# Decide what unit to use
    if bsize >= 1024**3:
        size = str(round(bsize / 1024**3, 3))
        unit = "GB"
    elif bsize >= 1024**2:
        size = str(round(bsize / 1024**2, 3))
        unit = "MB"
    elif bsize >= 1024:
        size = str(round(bsize / 1024, 3))
        unit = "KB"
    else:
        size = str(bsize)
        unit = "B"
# Build and return array
    array = [size, unit]
    return array


print("The Deleter\nby Bryce Villanueva\n")
addpath = "Unknown folder/"
path = os.path.dirname(sys.argv[0]) + "/" + addpath
print("Accessing " + path)


sess_total = 0 # Total of files deleted for the session

ans = "y"
while ans == "y" or ans =="": # Repeat until ans is valid
    dir = os.listdir(path)
    suffix = input("\nWhat extension are you looking for?\n")

    print("\nSearching for files ending in \"" + suffix + "\"...")
    list = []

    for file in dir:
        if file.endswith(suffix):
            list.append(file)

    # Declare/reset running totals
    select_total = 0 # Files selected
    del_total = 0 # Files deleted
    for file in list:
        bsize = os.path.getsize(addpath + file) # Size in bytes
        fsize = filesize(bsize) # Filesize value is obtained and turned into int value
        print("{0:50}     {1:3} {2:3}".format(file, fsize[0], fsize[1]))
        select_total += bsize

    select_size = filesize(select_total)

    if select_total == 0:
        print("\nNo files found.")
    else:
        while True:
            ans = input("\nWould you like to delete all files? {} {} selected. (y/n)\n".format(select_size[0], select_size[1]))
            if ans == "y":
                for file in list:
                    bsize = delete(file)
                    del_total += bsize
                del_size = filesize(del_total)
                print("\nDeletion complete. Deleted {} {} out of {} {} selected.".format(del_size[0], del_size[1], select_size[0], select_size[1]))
                sess_total += del_total
                break
            elif ans == "n":
                break
            else:
                print("Invalid input.")


    while True:
        ans = input("\nRestart? (y/n)\n")
        if ans == "n" or ans == "y" or ans == "":
            break
        else:
            print("Invalid input.\n")

sess_size = filesize(sess_total)
ans = input("\nProgram finished. {} {} worth of files deleted during this session. Press enter to exit.\n".format(sess_size[0], sess_size[1]))
