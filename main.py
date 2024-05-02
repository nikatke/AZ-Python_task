import os
import sys

def main():
    def run_files(folder):
        parent_dir = os.getcwd()
        folder_path = os.path.join(parent_dir, folder)
        try:
            files = os.listdir(folder_path)
        except FileNotFoundError:
            print(f"Folder '{folder}' does not exist in {os.path.dirname(folder_path)}.")
            return
        for file_name in files:
            if file_name.endswith(".py"):
                file_path = os.path.join(folder_path, file_name)
                exit_code = os.system(f"python {file_path}")
                if exit_code != 0:
                    print(f"Error running file: {file_path}")

    config_folders = {
        'config_1': [],
        'config_2': [],
        'config_3': [],
        'config_4': [],
        'config_5': ['config_2']
    }

    executed_folders = set()

    # Function to recursively execute folders and dependencies
    def execute_folder(folder):
        # Execute dependencies first
        for dependency in config_folders[folder]:
            if dependency not in executed_folders:
                execute_folder(dependency)
        # Execute current folder if not already executed
        if folder not in executed_folders:
            print("-----------------------------------------")
            run_files(folder)
            executed_folders.add(folder)

    # Check if command-line argument is provided
    if len(sys.argv) == 1:
        print("Please provide the name of the config folder.")
        return

    # Get the config folder from command-line argument
    config_folders_list = sys.argv[1].split(',')

    # Check if provided config folder exists
    for config_folder in config_folders_list:
        if config_folder not in config_folders:
            print(f"Config folder '{config_folder}' is not valid.")
            continue
        execute_folder(config_folder)

if __name__ == "__main__":
    main()
 
     