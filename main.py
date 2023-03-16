import os
import shutil

def organize_files(directory_path):
    for filename in os.listdir(directory_path):
        # Get the full path of the file
        file_path = os.path.join(directory_path, filename)
        
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
        
        # Move the file to the destination directory
        shutil.move(file_path, os.path.join(destination_dir, filename))

# Example usage
organize_files('G:/Python apps/organization/folder')