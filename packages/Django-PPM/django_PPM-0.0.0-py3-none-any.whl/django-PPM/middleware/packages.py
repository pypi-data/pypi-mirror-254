import os

from django.conf import settings
from django.contrib.auth import authenticate
from django.http import FileResponse, HttpResponse
import base64
import markdown2
from django.shortcuts import render

from PPM.finder.get_name import get_package_name


# export PIP_INDEX_URL=http://root:root@127.0.0.1:8000/packages/


class PackagesManagerDownloaderMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        path = request.path
        if path.endswith('favicon'):
            return self.get_response(request)
        auth_header = request.META.get('HTTP_AUTHORIZATION', None)

        if not auth_header and request.method == 'POST':
            return HttpResponse("not allowed", status=403)

        if request.method == 'POST':
            encoded_credentials = auth_header.split(' ')[1]  # Removes "Basic " to isolate credentials
            decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
            print(decoded_credentials)
            username = decoded_credentials[0]
            password = decoded_credentials[1]
            if path.startswith("/packages/versions/"):
                path = path.split("/packages/versions/")[1]
                file_path = f"{settings.BASE_DIR}/packages/{path}"
                return FileResponse(open(file_path, 'rb'))
            return self.get_response(request)

        if request.method == 'GET':
            file_path = f"{settings.BASE_DIR}{path}"

            # Read content from the Markdown file
            file = open(file_path + 'README.md', 'r', encoding='utf-8')
            markdown_content = file.read()
            return render(request, 'md_viewer.html', context={
                'md_content': markdown_content

            })
            # return HttpResponse(markdown2.markdown(markdown_content))
