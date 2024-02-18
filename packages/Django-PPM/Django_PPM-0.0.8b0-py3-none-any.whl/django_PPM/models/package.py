# package and package version models
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

user_class = get_user_model()


class PackageVersionsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(shown_on_package=True)

    def filter(self, *args, **kwargs):
        # we will passing the request object to the filter method

        return super().get_queryset().filter(*args, **kwargs).filter(shown_on_package=True)


class PackageVersions(models.Model):
    # PackageVersion, file, version, description, created_at, updated_at, user_upload, shown_on_package
    id = models.AutoField(primary_key=True)

    file = models.FileField(upload_to='packages/', blank=False, null=False, verbose_name=_("Package File"),
                            help_text=_("Upload the package file"))
    version = models.CharField(max_length=32, verbose_name=_("Version"),
                               help_text=_("Enter the version of the package"),
                               unique=True, )
    description = models.TextField(blank=True, null=True,
                                   help_text=_("Enter a brief description of the package version", ),
                                   verbose_name=_("Description"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"),
                                      help_text=_("Date and time at which this package version was created"), )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"),
                                      help_text=_("Date and time at which this package version was last updated"), )
    user_uploaded = models.ForeignKey(user_class, on_delete=models.SET_NULL, null=True,
                                      related_name='package_version_user_uploaded',
                                      verbose_name=_("User Uploaded"),
                                      help_text=_("Select the user who uploaded this package version"), )
    shown_on_package = models.BooleanField(default=False, verbose_name=_("Shown on Packages"))
    objects = PackageVersionsManager()

    def __str__(self):
        return self.version

    class Meta:
        verbose_name = 'Package Version'
        verbose_name_plural = 'Package Versions'
        ordering = ('-created_at',)
        unique_together = ('version', 'description')


class PackagesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def filter(self, *args, **kwargs):
        # we will passing the request object to the filter method
        if 'request' in kwargs:
            request = kwargs.pop('request')
            qs = super().get_queryset().filter(*args, **kwargs)
            qs.filter(is_active=True)
            if request.user.is_anonymous:
                qs.filter(allow4all=True)
                return qs
            # elif request.is_authenticated:

        return self.none()


class Packages(models.Model):
    # Packages name, description, versions, created_at, updated_at, is_active, allow4all, allow_md4all, allow_md4
    name = models.CharField(max_length=64, unique=True, verbose_name=_("Package Name"),
                            help_text=_("Enter the name of the package"), )
    description = models.TextField(blank=True, null=True, help_text=_("Enter a brief description of the package", ),
                                   verbose_name=_("Description"))
    versions = models.ManyToManyField(PackageVersions, related_name='package_version',
                                      verbose_name=_("Package Versions"),
                                      help_text=_("Select the versions for this package"), )
    ############################################################################################
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    allow4all = models.BooleanField(default=False, verbose_name=_("Allow All"),
                                    help_text=_("Allow all users to access this package"), )
    ############################################################################################
    allow_md4all = models.BooleanField(default=False, verbose_name=_("Allow MD for all"))
    allow_md4 = models.BooleanField(default=False, verbose_name=_("Allow MD"),
                                    help_text=_("Allow MD for specific users and groups"))
    objects = PackagesManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'
        ordering = ('-created_at',)
        unique_together = ('name', 'description')
