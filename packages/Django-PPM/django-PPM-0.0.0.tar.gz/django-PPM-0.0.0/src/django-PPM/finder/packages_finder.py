import os
import django
from django.conf import settings

from PPM.classes.version_file import VersionFile


def packages_finder(package_name=None):
    packages = []
    BASE_DIR = settings.BASE_DIR
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    list_of_packages = os.listdir(os.path.join(BASE_DIR, 'packages'))
    for package in list_of_packages:
        temp_package = package.split('.')[0]
        temp_package = temp_package.split('-')[:-1]
        temp_package = '-'.join(temp_package)
        if package_name.upper() == temp_package.upper():
            packages.append(VersionFile(name=package_name, link=package))

    return packages
def list_packages():
    packages = []
    BASE_DIR = settings.BASE_DIR
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    list_of_packages = os.listdir(os.path.join(BASE_DIR, 'packages'))
    for package in list_of_packages:
        temp_package = package.split('.')[0]
        temp_package = temp_package.split('-')[:-1]
        temp_package = '-'.join(temp_package)
        # if package_name.upper() == temp_package.upper():
        packages.append(temp_package.lower())
    # remove duplicates
    packages = list(dict.fromkeys(packages))
    return packages





