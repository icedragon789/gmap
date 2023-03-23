import os
import uuid

DATASET_PATH = "C:/Users/Owner/Code/py/datasets/runway/no_fod/"

# gets total size of directory, needs full file path to work
def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

def rename_with_stamp(path, stamp):
    for filename in os.listdir(path):
        my_dest = path + stamp + "_" + filename
        os.rename(path + filename, my_dest)

def give_unique_uuid(path):
    for filename in os.listdir(path):
        my_dest = path + str(uuid.uuid1()) + ".png"
        os.rename(path + filename, my_dest)

# file will be cleared out and written to with a 
# listing of all the file names and the count at the bottom
def directory_report(path, write_to):
    count = 0

    open(write_to, "w").close() # clear file
    f = open(write_to, "a")
    for x in os.listdir(path):
        f.write(x + '\n')
        count = count + 1
    f.write("\nNumber of files: " + str(count) + '\n')
    f.write("Size: " + str(get_size(path)/1e+9) + ' GB')
    f.close()

def load_file_names_into_list(path):
    

        

directory_report(DATASET_PATH, "C:/Users/Owner/Code/py/gmap/intermediary.txt")
# print(how_many_files("C:/Users/Owner/Code/py/datasets/runway/no_fod/"))
# give_unique_uuid("C:/Users/Owner/Code/py/datasets/runway/no_fod/")
# rename_with_stamp("C:/Users/Owner/Code/py/datasets/runway/r2/", "r1")