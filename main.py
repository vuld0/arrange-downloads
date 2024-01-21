import commands
import banner

# Printing the banner
banner.script_banner()

# let's get to the Downloads folder
current_dir = commands.change_dir_to_downloads()

dir_list = commands.list_files()

# to get the current working directory:
current_path = commands.current_dir()

# getting the list of file extensions
file_extensions = commands.get_files_with_extensions(dir_list)


# create the directory for the files
list_of_directories = ["images", "softwares", "videos", "documents", "zips"]

# for directory in list_of_directories:
#     commands.make_directory(directory, commands.current_dir())

commands.move_files(dir_list)


