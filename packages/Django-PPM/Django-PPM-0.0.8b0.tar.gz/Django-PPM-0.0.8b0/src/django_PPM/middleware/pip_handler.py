import os

from django.conf import settings
from django.http import FileResponse, HttpResponse

from PPM.finder.get_name import get_package_name


def pip_handler(request):
    if request.path.__contains__(f"{settings.PPM_CONFIG['PACKAGES_DIR']}versions"):
        package_version_file = request.path.split(f"{settings.PPM_CONFIG['PACKAGES_DIR']}versions")[1]
        package_name = get_package_name(package_version_file)
        file_dir = f"{settings.PPM_CONFIG['PACKAGES_DIR']}{package_name}{package_version_file}"

        if os.path.exists(file_dir):
            return FileResponse(open(file_dir, 'rb'))
        else:
            HttpResponse("Not found", status=404)

