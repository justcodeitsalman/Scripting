#!/usr/bin/python
import os
import time

def remove_file(path):

    if not os.remove(path):
        print(path,"is removed successfully")
    else:
        print("Unable to delete the",path)


def get_file_or_folder_age(path):
    ctime = os.stat(path).st_mtime
    return ctime

def main():

        deleted_files_count = 0
        path = "/extkciarch01/shared/inzone/OV/ADR_LETTER"
        extension = ".gz"
        days = 260
        seconds = time.time() - (days * 24 * 60 * 60)
        print(time.ctime(seconds))
        if os.path.exists(path):
            for root_folder, folders, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root_folder, file)
                    file_extension = os.path.splitext(file_path)[1]
                    if seconds >= get_file_or_folder_age(file_path) and extension == file_extension:
                        remove_file(file_path)
                        deleted_files_count += 1

        else:
            print(path,"not found")
            deleted_files_count += 1

        print("Total files deleted:",deleted_files_count)


if __name__ == '__main__':
        main()
