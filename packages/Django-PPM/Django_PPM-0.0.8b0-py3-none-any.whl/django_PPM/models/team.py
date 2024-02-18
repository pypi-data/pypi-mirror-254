from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

user_class = get_user_model()


class TeamManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Teams(models.Model):
    # Teams name, description, access_tokens, manager, members, created_at, updated_at, is_active
    tid = models.CharField(max_length=64, editable=True, unique=True, )
    name = models.CharField(max_length=64)
    description = models.TextField(
        blank=True,
        null=True,
        help_text=_("Enter a brief description of the team", )
    )
    ############################################################################################
    access_tokens = models.ManyToManyField('PPM.AccessTokens', related_name='team_access_token',
                                           verbose_name=_("Access Token"),
                                           help_text=_("Select the access tokens for this team"), )
    manager = models.ForeignKey(user_class, on_delete=models.SET_NULL, null=True,
                                related_name='team_manager', verbose_name=_("Team Manager"),
                                help_text=_("Select the user who will be the manager of this team"), )
    members = models.ManyToManyField(user_class, related_name='project_team_members', verbose_name=_("Team Members"),
                                     help_text=_("Select the users who will be the members of this team"),
                                     blank=True, )
    ############################################################################################
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"),
                                      help_text=_("Date and time at which this team was created"), )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"),
                                      help_text=_("Date and time at which this team was last updated"), )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"),
                                    help_text=_("Is this team active or not"), )
    ############################################################################################
    objects = TeamManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ('-created_at',)
