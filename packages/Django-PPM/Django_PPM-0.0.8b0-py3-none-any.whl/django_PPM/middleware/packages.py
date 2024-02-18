from django.conf import settings
from django.http import FileResponse, HttpResponse

from PPM.access_manager.access_manager import AccessManager
from PPM.middleware.md_file_handler import markdown_file_handler
from PPM.middleware.pip_handler import pip_handler


# export PIP_INDEX_URL=http://root:root@127.0.0.1:8000/packages/

class PackagesManagerDownloaderMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith(f"{settings.PPM_CONFIG['PACKAGES_URL']}"):
            return self.get_response(request)
        checker = AccessManager(request)
        # if not AccessManager.check_access():
        #     return HttpResponse("Access Denied", status=403)

        if request.method == 'POST':

            if request.path.startswith(f"{settings.PPM_CONFIG['PACKAGES_URL']}versions/"):
                path = request.path.split(f"{settings.PPM_CONFIG['PACKAGES_URL']}versions/")[1]
                file_path = f"{settings.BASE_DIR}{settings.PPM_CONFIG['PACKAGES_URL']}{path}"
                return FileResponse(open(file_path, 'rb'))

            return self.get_response(request)

        if request.method == 'GET':

            user_agent = request.headers.get('User-Agent', None)
            if user_agent is None:
                return self.get_response(request)
            pip = user_agent.split("{")[0]

            if pip.__contains__("pip"):
                pip_response = pip_handler(request)
                if pip_response is not None:
                    return pip_response
            else:
                return markdown_file_handler(request)

            return self.get_response(request)
