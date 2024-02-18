from django.conf import settings
from django.shortcuts import render


def markdown_file_handler(request):
    md_file_path = (
            settings.PPM_CONFIG['PACKAGES_DIR'] + '/' +
            request.path.replace(settings.PPM_CONFIG['PACKAGES_URL'], '') +
            '/' + 'README.md')

    file = open(md_file_path, 'r', encoding='utf-8')
    markdown_content = file.read()
    return render(request, 'md_viewer.html', context={
        'md_content': markdown_content

    })
