import os

from django.conf import settings

from PPM.classes.version_file import VersionFile


def get_package_name(package_name: str):
    print(package_name)
    BASE_DIR = settings.BASE_DIR
    # BASE_DIR = '/Users/slahaldynalhaj/PycharmProjects/test-pypiserver/'
    # SSubdomains-0.0.8b0
    package_name_temp = package_name.split('.')[0].split('-')[:-1]
    # emp_package = '-'.join(temp_package)
    package_name_temp = '-'.join(package_name_temp).lower()
    print(package_name_temp)
    package_folder_path=os.path.join(BASE_DIR,package_name_temp)
    return package_folder_path



