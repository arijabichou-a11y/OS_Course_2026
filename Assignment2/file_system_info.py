import os
import stat
import sys

def list_file_details(directory_path):
    # Check if the path exists
    if not os.path.exists(directory_path):
        print(f"Error: The path '{directory_path}' does not exist.")
        return

    print(f"{'File Name':<25} | {'Size (Bytes)':<12} | {'Permissions'}")
    print("-" * 55)

    # Iterate through the directory
    try:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            
            # We only want to analyze files
            if os.path.isfile(file_path):
                # Get file metadata (System Call)
                file_info = os.stat(file_path)
                
                size = file_info.st_size
                # Convert permissions to a readable string (like -rwxr-xr-x)
                permissions = stat.filemode(file_info.st_mode)
                
                print(f"{filename:<25} | {size:<12} | {permissions}")
    except PermissionError:
        print("Error: Permission denied to access this directory.")

if __name__ == "__main__":
    # Get directory path from user input
    path = input("Enter the directory path to scan (e.g., . for current): ")
    list_file_details(path)