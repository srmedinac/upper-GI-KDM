import os
import openslide

def check_slides(folder_path):
    failed_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.svs') or filename.endswith('.tif'):
            file_path = os.path.join(folder_path, filename)
            try:
                with openslide.OpenSlide(file_path) as slide:
                    if slide.level_count < 1:
                        print(f"Warning: {filename} has less than 1 level.")
            except openslide.OpenSlideError:
                print(f"Failed to open {filename}")
                failed_files.append(filename)
            except Exception as e:
                print(f"An error occurred while checking {filename}: {e}")
                failed_files.append(filename)
    return failed_files

if __name__ == "__main__":
    folder_path = "/home/smedin7/data/KDM/urkunina_hun_slides/slides_hun"  # Replace with your folder path
    failed_files = check_slides(folder_path)
    if failed_files:
        print("Failed to open the following slides:")
        for f in failed_files:
            print(f)
    else:
        print("All slides could be opened successfully.")
    folder_path = "/home/smedin7/data/KDM/urkunina_hun_slides/slides_urkunina"  # Replace with your folder path
    failed_files = check_slides(folder_path)
    if failed_files:
        print("Failed to open the following slides:")
        for f in failed_files:
            print(f)
    else:
        print("All slides could be opened successfully.")