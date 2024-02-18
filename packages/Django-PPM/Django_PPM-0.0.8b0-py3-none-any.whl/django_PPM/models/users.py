from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
# import lazy translation
from django.utils.translation import gettext_lazy as _

user_class = get_user_model()


class UserAccessTokenManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset().filter(is_active=True)
        return qs.filter(Q(Q(access_tokens__isnull=False) | Q(access_tokens__isnull=False)))



class UserAccess(models.Model):
    # UserAccessToken, uid, access_tokens, description, user, created_at, updated_at
    uid=models.CharField(max_length=64, editable=True, unique=True, )
    access_tokens = models.ManyToManyField('PPM.AccessTokens', related_name='user_access_token',
                                           verbose_name=_("Access Tokens"),
                                           help_text=_("Select the access tokens for this user"), )

    description = models.TextField(
        blank=True,
        null=True,
        help_text=_("Enter a brief description of the team", )
    )
    user = models.ForeignKey(user_class, on_delete=models.SET_NULL, null=True,
                             related_name='project_user', verbose_name=_("Project User"),
                             help_text=_("Select the user who will can access this project"), )
    # this fields not unnecessary  for this request [project, package, package_version, created_at, updated_at]


    # this fields not unnecessary  for this request [created_at, updated_at]
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"),
                                      help_text=_("Date and time at which this team was created"), )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"),
                                      help_text=_("Date and time at which this team was last updated"), )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"),
                                    help_text=_("Is this team active or not"), )
    objects = UserAccessTokenManager()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ('-created_at',)
