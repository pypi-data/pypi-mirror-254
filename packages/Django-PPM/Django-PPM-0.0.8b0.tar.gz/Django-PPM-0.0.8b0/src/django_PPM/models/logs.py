from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _



user_class = get_user_model()


class AccessUsersLogs(models.Model):
    # user,access_token,accessed_from,access_details,project_accessed,packages_accessed,package_version_accessed
    alid = models.CharField(max_length=64, editable=True, unique=True,
                            help_text=_("Unique ID for this access log"),
                            verbose_name=_("Access Log ID"))
    # user
    user = models.ForeignKey(user_class, on_delete=models.CASCADE, related_name='user_log_user_token_accessed',
                             verbose_name=_("User Accessed"), help_text=_("User Accessed this token"))

    access_token = models.ForeignKey('PPM.AccessTokens', on_delete=models.CASCADE,
                                     related_name='access_token_accessed_by_user',
                                     verbose_name=_("Token Accessed"),
                                     help_text=_("Token Accessed by this user")
                                     )
    # accessed at
    accessed_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Accessed At"),
                                       help_text=_("Date and time at which this token was accessed"),
                                       )
    # accessed from
    accessed_from = models.GenericIPAddressField(verbose_name=_("Accessed From"),
                                                 help_text=_("IP Address of the user who accessed this token"),
                                                 blank=True, null=True, )
    access_details = models.TextField(
        blank=True,
        null=True,
        help_text=_(" Details of the access", )
    )

    # accessed to

    project_accessed = models.ForeignKey('PPM.Projects', on_delete=models.CASCADE,
                                         related_name='user_log_project_accessed',
                                         verbose_name=_("Project Accessed", ),
                                         help_text=_("Project Accessed by this user"),
                                         blank=True, null=True,
                                         )
    packages_accessed = models.ForeignKey('PPM.Packages', on_delete=models.CASCADE,
                                          related_name='user_log_packages_accessed',
                                          verbose_name=_("Packages Accessed"),
                                          help_text=_("Packages Accessed by this user"))
    # accessed to package version
    package_version_accessed = models.ForeignKey('PPM.PackageVersions', on_delete=models.CASCADE,
                                                 related_name='user_log_package_version_accessed',
                                                 verbose_name=_("Package Version Accessed"),
                                                 help_text=_("Package Version Accessed by this user"))




class AccessTeamsLogs(models.Model):
    # user,access_token,accessed_from,access_details,project_accessed,packages_accessed,package_version_accessed
    alid = models.CharField(max_length=64, editable=True, unique=True,
                            help_text=_("Unique ID for this access log"),
                            verbose_name=_("Access Log ID"))
    # user
    user = models.ForeignKey(user_class, on_delete=models.CASCADE, related_name='team_log_user_accessed',
                             verbose_name=_("User Accessed"), help_text=_("User Accessed this token"))
    team = models.ForeignKey(user_class, on_delete=models.CASCADE, related_name='team_log_user_token_accessed',
                             verbose_name=_("User Accessed"), help_text=_("User Accessed this token"))
    # token
    access_token = models.ForeignKey('PPM.AccessTokens', on_delete=models.CASCADE,
                                     related_name='team_log_oken_accessed',
                                     verbose_name=_("Token Accessed"), help_text=_("Token Accessed by this user"))
    # accessed at
    accessed_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Accessed At"),
                                       help_text=_("Date and time at which this token was accessed"), )
    # accessed from
    accessed_from = models.GenericIPAddressField(verbose_name=_("Accessed From"),
                                                 help_text=_("IP Address of the user who accessed this token"), )
    access_details = models.TextField(
        blank=True,
        null=True,
        help_text=_(" Details of the access", )
    )

    # accessed to

    project_accessed = models.ForeignKey('PPM.Projects', on_delete=models.CASCADE,
                                         related_name='team_log_project_accessed',
                                         verbose_name=_("Project Accessed"),
                                         help_text=_("Project Accessed by this user"))
    packages_accessed = models.ForeignKey('PPM.Packages', on_delete=models.CASCADE,
                                          related_name='team_log_packages_accessed',
                                          verbose_name=_("Packages Accessed"),
                                          help_text=_("Packages Accessed by this user"))
    # accessed to package version
    package_version_accessed = models.ForeignKey('PPM.PackageVersions', on_delete=models.CASCADE,
                                                 related_name='team_log_package_version_accessed',
                                                 verbose_name=_("Package Version Accessed"),
                                                 help_text=_("Package Version Accessed by this user"))
