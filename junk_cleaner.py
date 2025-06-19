import os
import shutil
import getpass

WINDOWS_TEMP = r"C:\\Windows\\Temp"
USER_TEMP = os.path.join("C:\\Users", os.getenv("USERNAME"), "AppData\\Local\\Temp") #gets the username from ur pc
PREFETCH = r"C:\\Windows\\Prefetch"

def count_files(folder): #counting the files
    count = 0
    for root, dirs, files in os.walk(folder):
        count += len(files)
    return count

def clean_folder(folder): #walking in and wiping them 
    deleted = 0
    errors = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                deleted += 1
            except Exception:
                errors += 1
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                shutil.rmtree(dir_path, ignore_errors=True)
            except Exception:
                pass
    return deleted, errors

def confirm(prompt): #making sure
    ans = input(f"{prompt} (y/n): ").strip().lower()
    return ans == 'y'

def main_menu():
    while True:
        print("\n==== WINDOWS JUNK CLEANER ====")
        print(f"1. Clean Windows Temp ({WINDOWS_TEMP})")
        print(f"2. Clean User Temp ({USER_TEMP})")
        print(f"3. Clean Prefetch ({PREFETCH})")
        print("4. Clean All")
        print("5. Exit")
        choice = input("Select an option (1-5): ").strip()
        if choice == '1':
            if confirm(f"Are you sure you want to clean {WINDOWS_TEMP}?"):
                before = count_files(WINDOWS_TEMP)
                deleted, errors = clean_folder(WINDOWS_TEMP)
                print(f"Deleted {deleted} files from Windows Temp. Errors: {errors}")
        elif choice == '2':
            if confirm(f"Are you sure you want to clean {USER_TEMP}?"):
                before = count_files(USER_TEMP)
                deleted, errors = clean_folder(USER_TEMP)
                print(f"Deleted {deleted} files from User Temp. Errors: {errors}")
        elif choice == '3':
            if confirm(f"Are you sure you want to clean {PREFETCH}?"):
                before = count_files(PREFETCH)
                deleted, errors = clean_folder(PREFETCH)
                print(f"Deleted {deleted} files from Prefetch. Errors: {errors}")
        elif choice == '4':
            if confirm("Are you sure you want to clean ALL folders?"):
                total_deleted = 0
                total_errors = 0
                for folder, name in [(WINDOWS_TEMP, "Windows Temp"), (USER_TEMP, "User Temp"), (PREFETCH, "Prefetch")]:
                    deleted, errors = clean_folder(folder)
                    print(f"Deleted {deleted} files from {name}. Errors: {errors}")
                    total_deleted += deleted
                    total_errors += errors
                print(f"Total deleted: {total_deleted}. Total errors: {total_errors}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    
    main_menu() 
