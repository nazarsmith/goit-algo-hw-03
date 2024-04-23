from pathlib import Path, PurePath
import shutil
import os
import time

def copy_sort(src_path: Path, dest_path: str = "dist", args: list = [0, 0, 0]) -> None:
    
    try:
        if src_path.is_dir():
            for child in src_path.iterdir():
                copy_sort(child, dest_path, args)
        elif src_path.is_file():
            extension = os.path.basename(src_path).split(".")[-1]
            sub_dir = os.path.join(dest_path, extension)
            if not os.path.exists(sub_dir):
                os.makedirs(sub_dir)
                args[1] += 1
                os.chmod(sub_dir, mode = 0o777)
            try:
                shutil.copy(src_path, sub_dir, )
                args[0] += 1
            except PermissionError:
                print(f"Couldn't copy {src_path} due to insufficient permissions.")
                args[2] += 1
    except FileNotFoundError:
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
            os.chmod(dest_path, mode = 0o777)

    except Exception as err:
        print(
            f"{err} caught. Something went wrong."
        )
    
    return args[0], args[1], args[2]

if __name__ == "__main__":
    src_path = Path("C:\Projects\goitneo-python-hw-2-group-3")
    dest_path = Path("C:\Projects_2")
    time_now = time.time()
    file_count, folder_count, failed_to_copy = copy_sort(src_path, dest_path)
    print(
        f"{file_count} files copied into {folder_count} folders. {failed_to_copy} files failed to be copied.",
        f"The operation took {round(time.time() - time_now, 1)} seconds.", sep = "\n"
        )
