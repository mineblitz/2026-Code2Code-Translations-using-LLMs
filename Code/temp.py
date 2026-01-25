import os
import shutil

BASE_DIR = "./Projects"
TARGET_SUBSTRING = "ExecutionsExp6Run2"

for root, dirs, _ in os.walk(BASE_DIR, topdown=False):
    for d in dirs:
        if d == TARGET_SUBSTRING:
            folder_path = os.path.join(root, d)
            shutil.rmtree(folder_path)
            print(f"Deleted: {folder_path}")


# for root, _, files in os.walk(BASE_DIR):
#     for f in files:
#         if f == TARGET_SUBSTRING:
#             file_path = os.path.join(root, f)
#             os.remove(file_path)
#             print(f"Deleted file: {file_path}")