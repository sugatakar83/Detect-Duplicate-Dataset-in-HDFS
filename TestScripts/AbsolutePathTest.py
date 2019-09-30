from pathlib import Path
import yaml
import pathlib


# this function will find the absolute path of a file in the system
def find_path_to_file(file_name):
    globa_path = pathlib.Path.home()
    for path in sorted(globa_path.rglob('*')):
        if str(file_name) in str(path):
            return str(path)


# YAML load testing
with open('../CommonScripts/config.yaml', 'r') as f:
    config = yaml.safe_load(f)
    print(config['tablefilepath'])

# Get the absolute path from a relative path
relative = Path("CommonScripts/config.yaml")
absolute = relative.absolute()
print(absolute)