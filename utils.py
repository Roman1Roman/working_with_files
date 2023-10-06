import os, zipfile


PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, 'resources')
TMP_PATH = os.path.join(PROJECT_ROOT_PATH, 'tmp')

def zip_dir(input_dir, output_zip, count=0):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                fullpath = os.path.join(root, file)
                archive_path = os.path.relpath(fullpath, input_dir)
                zipf.write(fullpath, archive_path)



