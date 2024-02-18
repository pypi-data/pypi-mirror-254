from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

user_class = get_user_model()


class ProjectsManager(models.Manager):
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
            else:
                qs.filter(members__in=request.user)
                return qs
        return self.none()


class Projects(models.Model):
    # Projects name, description, manager, packages, created_at, updated_at, is_active
    name = models.CharField(max_length=50)
    description = models.TextField(
        blank=True,
        null=True,
        help_text=_("Enter a brief description of the project", ),
        verbose_name=_("Description of the project")
    )
    manager = models.ForeignKey(user_class, on_delete=models.SET_NULL, null=True, related_name='project_manager',
                                verbose_name=_("Project Manager"),
                                help_text=_("Select the user who will be the manager of this project")
                                )

    packages = models.ForeignKey('PPM.Packages', on_delete=models.CASCADE, related_name='project_package',
                                 verbose_name=_("Team Package"),
                                 help_text=_("Select the package for this team"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"),
                                      help_text=_(
                                          "Date and time at which this project was created"), )

    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name=_("Updated At"),
                                      help_text=_("Date and time at which this project was last updated"), )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"),
                                    help_text=_("Is this project active or not"), )
    objects = ProjectsManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('-created_at',)
