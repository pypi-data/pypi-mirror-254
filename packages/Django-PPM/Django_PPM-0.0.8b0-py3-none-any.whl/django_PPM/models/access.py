from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

user_class = get_user_model()


class AccessTokensManager(models.Manager):
    def get_queryset(self):
        time_now = timezone.now()
        qs = super().get_queryset().filter(active=True, start_date__lte=time_now.date(),
                                           end_date__gte=time_now.date(),
                                           hourly_access_start__lte=time_now.time(),
                                           hourly_access_end__gte=time_now.time(), )
        #     filter by days
        if time_now.weekday() == 0:
            qs = qs.filter(monday=True)
        elif time_now.weekday() == 1:
            qs = qs.filter(tuesday=True)
        elif time_now.weekday() == 2:
            qs = qs.filter(wednesday=True)
        elif time_now.weekday() == 3:
            qs = qs.filter(thursday=True)
        elif time_now.weekday() == 4:
            qs = qs.filter(friday=True)
        elif time_now.weekday() == 5:
            qs = qs.filter(saturday=True)
        elif time_now.weekday() == 6:
            qs = qs.filter(sunday=True)

        return qs



    def get(self,token_user: str, token_pass: str, package, projects=None, ):
        if token_user is None or token_pass is None or package is None:
            return None
        if projects is None:
            return super(AccessTokensManager, self).get(token_user=token_user, token_pass=token_pass, package=package, )

        return super(AccessTokensManager, self).get(token_user=token_user, token_pass=token_pass, package=package, project=projects, )

    def filter(self,token_user, token_pass, package, project=None, ):
            if token_user is None or token_pass is None or package is None:
                return None  # Corrected this line

            if project is None:
                return super(AccessTokensManager, self).filter(token_user=token_user, token_pass=token_pass, package=package,)

            return super(AccessTokensManager, self).filter(token_user=token_user, token_pass=token_pass, package=package, project=project,)


class AccessTokens(models.Model):
    # uid, token_user, token_pass, project, package
    uid = models.AutoField(verbose_name=_("UID"), primary_key=True, editable=False, unique=True, )

    description = models.TextField(
        blank=True,
        null=True,
        help_text=_("Enter a brief description of the access token", ))
    ############################################################################################
    active = models.BooleanField(default=True, verbose_name=_("Is Active"),
                                 help_text=_("Is this access token active or not"), )
    token_user = models.CharField(max_length=64, null=False, verbose_name=_("Token User"),
                                  help_text=_("User of this token"), unique=True)
    token_pass = models.CharField(max_length=64, null=False, verbose_name=_("Token Pass"),
                                  help_text=_("Pass of this token"), unique=True)
    ############################################################################################
    project = models.ForeignKey('PPM.Projects', on_delete=models.CASCADE, related_name='team_project',
                                verbose_name=_("Team Project"),
                                help_text=_("Select the project for this team"))
    package = models.ForeignKey('PPM.Packages', on_delete=models.CASCADE, related_name='team_package',
                                verbose_name=_("Team Package"),
                                help_text=_("Select the package for this team"))
    ###########################################  Limiting Access  #################################################

    start_date = models.DateTimeField(verbose_name=_("Start Date"),
                                      default=timezone.now,
                                      help_text=_("Date and time will be start this token"), )
    end_date = models.DateTimeField(verbose_name=_("End Date"),
                                    default=timezone.now,
                                    help_text=_("Date and time will be expired this token"), )

    hourly_access = models.BooleanField(default=False, verbose_name=_("Daily Access"),
                                        help_text=_("Is this token will be closed in specific times"), )

    hourly_access_start = models.TimeField(null=True, blank=True, verbose_name=_("Start Hourly Access"),
                                           help_text=_("Start time of hourly access"))

    hourly_access_end = models.TimeField(null=True, blank=True, verbose_name=_("End Daily Access"),
                                         help_text=_("End time of daily access"))

    saturday = models.BooleanField(default=False, verbose_name=_("Saturday"),
                                   help_text=_("Is this token will be closed in Saturday"), )
    sunday = models.BooleanField(default=False, verbose_name=_("Sunday"),
                                 help_text=_("Is this token will be closed in Sunday"), )
    monday = models.BooleanField(default=False, verbose_name=_("Monday"),
                                 help_text=_("Is this token will be closed in Monday"), )
    tuesday = models.BooleanField(default=False, verbose_name=_("Tuesday"),
                                  help_text=_("Is this token will be closed in Tuesday"), )
    wednesday = models.BooleanField(default=False, verbose_name=_("Wednesday"),
                                    help_text=_("Is this token will be closed in Wednesday"), )
    thursday = models.BooleanField(default=False, verbose_name=_("Thursday"),
                                   help_text=_("Is this token will be closed in Thursday"), )
    friday = models.BooleanField(default=False, verbose_name=_("Friday"),
                                 help_text=_("Is this token will be closed in Friday"), )
    access_type_choice = (
        ('PIP_UPLOAD', 'PIP_UPLOAD'),
        ('PIP_DOWNLOAD', 'PIP_DOWNLOAD'),
        ('ALL', '*'),
    )

    access_type = models.CharField(max_length=64, choices=access_type_choice, verbose_name="نوع المستخدمين",
                                   blank=True)

    objects = AccessTokensManager()
