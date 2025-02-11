import os
import shutil
import re

MAIN_FOLDER = r"C:\Users\Simona\ProtonDrive\simonamit\My files\Documents\CODE\LevelUp1\tmcdata\mooc-programming-24"  # Change this if needed

def move_with_prompt(src, dst):
    """Moves a file, prompting the user if a duplicate exists."""
    if os.path.exists(dst):
        choice = input(f"File {os.path.basename(dst)} already exists. Overwrite? (y/n): ").strip().lower()
        if choice != 'y':
            return  # Skip moving if user does not agree
    shutil.move(src, dst)

def extract_exercise_name(subfolder_name):
    """
    Extracts the formatted exercise name from the subfolder.
    Handles cases where "part" appears in the exercise name.
    """
    match = re.match(r"part(\d+)-(\d+)_(.+)", subfolder_name)
    if match:
        part1, part2, exercise_name = match.groups()
        formatted_name = f"{part1}-{part2}_{exercise_name}"
        return formatted_name
    return None  # Return None if the format is incorrect

def process_subfolder(subfolder_path, subfolder_name):
    """Processes a single subfolder."""
    formatted_name = extract_exercise_name(subfolder_name)
    if not formatted_name:
        print(f"Skipping malformed folder: {subfolder_name}")
        return

    # Move and rename Python files from 'src' folder
    src_path = os.path.join(subfolder_path, "src")
    if os.path.exists(src_path):
        for file in os.listdir(src_path):
            file_path = os.path.join(src_path, file)
            if os.path.isfile(file_path) and file.endswith(".py"):  # Rename all .py files
                new_name = f"{formatted_name}.py"
                dest_path = os.path.join(MAIN_FOLDER, new_name)
            else:
                dest_path = os.path.join(MAIN_FOLDER, file)

            move_with_prompt(file_path, dest_path)

        # Remove now-empty "src" folder
        os.rmdir(src_path)

    # Move other files (but not directories) from the subfolder
    for file in os.listdir(subfolder_path):
        file_path = os.path.join(subfolder_path, file)
        if os.path.isfile(file_path):  # Only move files, not folders
            dest_path = os.path.join(MAIN_FOLDER, file)
            move_with_prompt(file_path, dest_path)

    # Delete the now-empty subfolder
    shutil.rmtree(subfolder_path, ignore_errors=True)

def process_subfolders(main_folder):
    subfolders = [f for f in os.listdir(main_folder) if f.startswith("part") and os.path.isdir(os.path.join(main_folder, f))]

    for subfolder in subfolders:
        subfolder_path = os.path.join(main_folder, subfolder)

        print(f"\nReady to process: {subfolder}")
        choice = input("Continue? (y/n): ").strip().lower()
        if choice != 'y':
            print("Skipping...")
            continue

        process_subfolder(subfolder_path, subfolder)

if __name__ == "__main__":
    process_subfolders(MAIN_FOLDER)
