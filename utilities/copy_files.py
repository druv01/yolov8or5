import os
import shutil

def copy_files(source_folder, destination_folder):
    try:
       
        # Get a list of all files in the source folder
        files = os.listdir(source_folder)

        # Copy each file from the source to the destination folder
        for file in files:
            source_file = os.path.join(source_folder, file)
            destination_file = os.path.join(destination_folder, file)
            shutil.copy2(source_file, destination_file)

        print("Files copied successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    source_folder = "H:/My Drive/robocar/dataset/training/label_2"
    destination_folder = "H:/My Drive/robocar/dataset/training/image_2"

    copy_files(source_folder, destination_folder)
