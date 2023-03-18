import os
import shutil
import hashlib

# set the file permissions to read and write for owner

def get_file_hash(file_path):
    os.chmod(file_path, 0o600)
    # Read the file contents in binary mode
    with open(file_path, 'rb') as file:
        file_contents = file.read()
    # Use the SHA-256 hash function to generate a hash of the file contents
    file_hash = hashlib.sha256(file_contents).hexdigest()
    return file_hash

def organize_files(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            # Get the full path of the file

            file_path = os.path.join(root, filename)
            os.chmod(file_path, 0o600)

            # Get the file extension
            extension = os.path.splitext(filename)[1]
            
            # Define the destination directory based on the file extension
            if extension in ['.txt', '.doc', '.docx' , '.md','.rtf','.pdf','.csv','.xls','.xlsx','.ppt','.pptx']:
                destination_dir = os.path.join(directory_path, 'documents')
            elif extension in ['.jpg', '.png', '.gif','.bmp']:
                destination_dir = os.path.join(directory_path, 'images')
            elif extension in ['.mp3', '.wav', '.flac','.aac']:
                destination_dir = os.path.join(directory_path, 'music')
            elif extension in ['.mp4', '.avi', '.mov','.flv','.mkv',]:
                destination_dir = os.path.join(directory_path, 'videos')            
            elif extension in ['.zip', '.tar', '.rar','.bin','.iso','.jar','.cab','.gzip']:
                destination_dir = os.path.join(directory_path, 'misc') 
            

            else:
                destination_dir = os.path.join(directory_path, 'other')
        
            # Create the destination directory if it doesn't exist
            if not os.path.exists(destination_dir):
                os.mkdir(destination_dir)
# Check if the file already exists in the destination directory
            dest_file_path = os.path.join(destination_dir, filename)
            if os.path.exists(dest_file_path):
                # If the file exists, compare the file hashes to check if the contents are the same
                src_file_hash = get_file_hash(file_path)
                dest_file_hash = get_file_hash(dest_file_path)
                if src_file_hash == dest_file_hash:
                    # If the file contents are the same, remove the source file
                    os.remove(file_path)
                else:
                    # If the file contents are different, append a counter to the filename
                    counter = 1
                    while True:
                        new_filename = os.path.splitext(filename)[0] + f"_{counter}" + os.path.splitext(filename)[1]
                        dest_file_path = os.path.join(destination_dir, new_filename)
                        if not os.path.exists(dest_file_path):
                            break
                        counter += 1
                    # Move the file to the new destination file path
                    shutil.move(file_path, dest_file_path)
            else:
                # If the file doesn't exist in the destination directory, move it to the destination directory
                shutil.move(file_path, dest_file_path)
    
    # Delete empty directories
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

organize_files('G:/Python apps/organization/folder')