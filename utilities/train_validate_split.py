import os
import shutil
import random

def copy_random_files(source_folder, destination_folder, percentage):
    # Get a list of all files in the source folder
    file_list = os.listdir(source_folder)
    
    # Calculate the number of files to copy (30% of the total files)
    num_files_to_copy = int(len(file_list) * percentage)

    #num_files_to_copy = 741

    print(f'num_files_to_MOVE={num_files_to_copy}')

    print(f'From {source_folder_path} to {destination_folder_path}')

    input("Press any key to continue...")

    
    # Randomly select 'num_files_to_copy' files from the file list
    selected_files = random.sample(file_list, num_files_to_copy)
    
    # Copy selected files to the destination folder
    for filename in selected_files:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        print(destination_path)
        shutil.move(source_path, destination_path)

# Set the source and destination folder paths with forward slashes (/)
source_folder_path = r'H:\My Drive\robocar\dataset\kitti\val\images'
destination_folder_path = r'H:\My Drive\robocar\dataset\kitti\test\images'


# Specify the percentage of files to copy (30%)
percentage_to_copy = 0.5

# Call the function to copy random files
copy_random_files(source_folder_path, destination_folder_path, percentage_to_copy)
