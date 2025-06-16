import os
import subprocess

def open_app(app_name):
    try:
        subprocess.Popen(app_name)
        return f"Opening {app_name}..."
    except Exception as e:
        return f"Couldn't open {app_name}: {e}"

def search_files(folder_path, keyword):
    results = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if keyword.lower() in file.lower():
                results.append(os.path.join(root, file))
    return results
