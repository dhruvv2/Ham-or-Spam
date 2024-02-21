import os
import shutil

# Function to move text files from one folder to another
def move_text_files(source_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Iterate through files in the source folder
    for file_name in os.listdir(source_folder):
        # Check if it's a file and if it has a .txt extension
        if os.path.isfile(os.path.join(source_folder, file_name)) and file_name.endswith('.txt'):
            # Move the file to the destination folder
            shutil.move(os.path.join(source_folder, file_name), os.path.join(destination_folder, file_name))

# Example usage
source_folder = r'C:\Users\vishw\Downloads\20030228_spam_2.tar\spam_2'
destination_folder = r'C:\Users\vishw\OneDrive\Desktop\BCT Python Files\Spam Texts'
move_text_files(source_folder, destination_folder)
