import os
import pandas as pd

# Function to read text files into a DataFrame
def read_txt_files_to_dataframe(folder_path):
    data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                content = file.read()
                # Append each file's content as a single row in the data list
                data.append([file_name, content])
    # Create DataFrame with columns 'File' and 'Content'
    df = pd.DataFrame(data, columns=['File', 'Content'])
    return df




# Example usage
ham_folder_path = r'C:\Users\vishw\OneDrive\Desktop\BCT Python Files\Ham Texts'
spam_folder_path = r'C:\Users\vishw\OneDrive\Desktop\BCT Python Files\Spam Texts'
# output_excel_path = r'c:\Users\vishw\OneDrive\Desktop\Ham_texts.csv'

# Read files and process them
df_ham = read_txt_files_to_dataframe(ham_folder_path)
df_spam = read_txt_files_to_dataframe(spam_folder_path)


