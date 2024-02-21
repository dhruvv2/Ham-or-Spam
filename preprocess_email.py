import os
import email
import re
import pandas as pd

# Function to extract main content from an email file
def extract_main_content_from_email(file_path):
    with open(file_path, 'rb') as f:  # Open the file in binary mode
        email_content = f.read()

    # Parse the email message
    msg = email.message_from_bytes(email_content)

    # Extract the main content
    main_content = ''

    # Walk through the message parts
    for part in msg.walk():
        # Check if the part is text/plain or text/html
        if part.get_content_type() == 'text/plain' or part.get_content_type() == 'text/html':
            # Decode the payload (body) if it's encoded
            payload = part.get_payload(decode=True)
            if isinstance(payload, bytes):
                payload = payload.decode('utf-8', errors='replace')
                payload = payload.encode('utf-8', errors='ignore').decode('utf-8')
                
                payload = re.sub(r'<[^>]+>', '', payload) # remove html tags
                                
                payload = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', payload) # removes email addresses
                
                payload = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', payload) # removes urls
                
                payload = re.sub(r'[^a-zA-Z0-9\s]', '', payload) # removes non alphanumeric characters
                
                payload = payload.replace('nbsp', ' ') # replace nbsp with empty strings
                
                payload = payload.replace("\xa0", ' ') # removing nbsps
                
                payload = payload.replace('\r', '').replace('\n', '') # replace /r and /n with empty strings
                
                payload = payload.replace('- %  - %  - % - % ', '') # replace /r and /n with empty strings
                
                payload = payload.replace('-', '').replace('_', '') # replace '-' and '_' with empty strings
                
                
                #try replacing nbsp with spaces
                
                payload = re.sub(r'\s+', ' ', payload).strip()
                
                payload = payload.lstrip('0')
                
                payload = payload.split("Irish Linux Users")[0] # Only content before "Irish Linux Users"
                
            main_content += payload
        else:
            # If it's not text/plain or text/html, handle it as attachment or other content
            # You can skip or process it according to your requirements
            pass

    return main_content.strip()

# Path to the folder containing email files
ham_path = r'C:\Users\vishw\OneDrive\Desktop\BCT Python Files\Ham Texts'
spam_path = r'C:\Users\vishw\OneDrive\Desktop\BCT Python Files\Spam Texts'

ham_main_content = []
spam_main_content = []

def iterate_over_files(folder_path, arr):
    # Iterate over each file in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Check if the file is a regular file
        if os.path.isfile(file_path):
            # Extract main content from the email file
            main_content = extract_main_content_from_email(file_path)
            
            arr.append(main_content)
    
    return arr

ham_main_content = iterate_over_files(ham_path, ham_main_content)
spam_main_content = iterate_over_files(spam_path, spam_main_content)

ham_df = pd.DataFrame({'Main_Content': ham_main_content})
spam_df = pd.DataFrame({'Main_Content': spam_main_content})
# output_excel_path = r'c:\Users\vishw\OneDrive\Desktop\Ham_texts_main2.csv'
# ham_df.to_csv(output_excel_path, index=False)
# print(ham_df.shape)
# print(spam_df.shape)
# print(spam_df)
# print(df)

ham_df['Label'] = 0
spam_df['Label'] = 1

combined_df = pd.concat([ham_df, spam_df], ignore_index=True)

final_excel_path = r'c:\Users\vishw\OneDrive\Desktop\Combined_texts_main.csv'
combined_df.to_csv(final_excel_path, index=False)

print(combined_df.shape)
print(combined_df)

# - %  - %  - % - % 