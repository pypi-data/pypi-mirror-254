from django.http import HttpResponse
from django.shortcuts import render
from PPM.finder import packages_finder, list_packages


def packages_details(request, package_name=None):
    packages_list = packages_finder(package_name)
    if request.method == "POST":
        return render(request, 'list_version.html', context={"packages_list": packages_list})



def packages(request):
    packages_list = list_packages()
    return render(request, 'list_packages.html', context={"packages_list": packages_list})

