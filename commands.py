import os
from shutil import move


def current_dir():
    return os.getcwd()


# ! Don't forget to add downloads path here -
def change_dir_to_downloads():
    os.chdir(r"/mnt/c/Users/sach9/Downloads")
    return os.getcwd()


def list_files():
    temp_dir_list = os.listdir()
    dir_list = []
    for name_of_files in temp_dir_list:
        # x.__eq__(__file__) -> checks if the x file is not as the current script name
        if os.path.isfile(name_of_files) and not name_of_files.startswith(".") and not name_of_files.__eq__(
                "main.py") and not name_of_files.__eq__(__file__):
            dir_list.append(name_of_files)
    return dir_list


def get_files_with_extensions(dir_list):
    file_extensions = []
    for i in dir_list:
        split_tup = os.path.splitext(i)
        file_extensions.append(split_tup[1])

    file_extensions = set(file_extensions)
    return file_extensions


# def make_directory(directory_name, path):
#     if os.path.exists(path) and os.path.isdir(path + '/' + directory_name):
#         print(f"The directory {directory_name} already exists")
#     else:
#         os.mkdir(directory_name)
#         print(f"The directory {directory_name} has been created")

#     return directory_name


def move_files(files):
    # let's define the categories of the files first
    doc_files = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx', '.md', '.csv', '.TXT')
    img_files = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff', '.HEIC', '.JPG')
    software_files = ('.exe', '.pkg', '.dmg')
    vid_files = ('.MP4', '.MOV', '.mp4')
    zip_files = '.zip'

    # moving the files using the shutil module:
    for file in files:
        if file.endswith(doc_files):
            print(f"Moving {file} to documents")
            move(file, change_dir_to_downloads() + "/documents")
        elif file.endswith(img_files):
            print(f"Moving {file} to images")
            move(file, change_dir_to_downloads() + "/images")
        elif file.endswith(software_files):
            print(f"Moving {file} to softwares")
            move(file, change_dir_to_downloads() + "/softwares")
        elif file.endswith(vid_files):
            print(f"Moving {file} to videos")
            move(file, change_dir_to_downloads() + '/videos')
        elif file.endswith(zip_files):
            print(f"Moving {file} to zips")
            move(file, change_dir_to_downloads() + '/zips')
    return "files moved!!"
