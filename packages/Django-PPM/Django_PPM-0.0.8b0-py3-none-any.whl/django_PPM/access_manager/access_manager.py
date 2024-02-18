import base64

from django.contrib.auth import get_user_model
from django.http import HttpRequest

from PPM.models import *

user_model = get_user_model()

class AccessManager:

    def __init__(self, request: HttpRequest):
        package_name = request.path.split('/packages/')[1]
        try:
            self.package = Packages.objects.get(name=package_name)
        except Packages.DoesNotExist:
            self.package = None
        if request.user.is_authenticated:
            self.user = request.user
        else:
            self.user = None
        auth_header = request.META.get('HTTP_AUTHORIZATION', None)

        encoded_credentials = auth_header.split(' ')[1]  # Removes "Basic " to isolate credentials
        decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
        token_pass = decoded_credentials[1]
        token_user = decoded_credentials[0]

        try:
            self.token = AccessTokens.objects.get(token_pass=token_pass, token_user=token_user,
                                                  package=self.package)
        except AccessTokens.DoesNotExist:
            self.token = None
        try:
            self.user_access = UserAccess.objects.get(user=self.user, access_tokens__in=[self.token])
        except UserAccess.DoesNotExist:
            self.user_access = None
        try:
            self.team = Teams.objects.get(members__in=[self.user], access_tokens__in=[self.token])
        except Teams.DoesNotExist:
            self.team = None

        self.ip_address = request.META.get('REMOTE_ADDR')
        self.action = request.META.get('HTTP_USER_AGENT','') + " " + request.META.get(
            'HTTP_REFERER','') + " " + request.META.get('HTTP_ACCEPT_LANGUAGE','')

        # self.token_user = token_user

    def check_access(self):

        if self.token == None or self.user == None or self.package == None or (
                self.team == None and self.user_access == None):
            return False

        user = UserAccess.objects.filter(user=self.user, access_tokens__in=self.token)
        AccessUsersLogs.objects.create(user=self.user, access_token=self.token,
                                       accessed_from=self.ip_address,
                                       access_details=self.action,
                                       project_accessed=self.token.project,
                                       packages_accessed=self.package,
                                       package_version_accessed=self.package_version)

        if user:

            project = self.token.project
            if project:
                AccessUsersLogs.objects.create(user=self.user, access_token=self.token,
                                               accessed_from=self.ip_address,
                                               access_details=self.action,
                                               project_accessed=project,
                                               packages_accessed=self.package,
                                               package_version_accessed=self.package_version)
            else:
                AccessUsersLogs.objects.create(user=self.user, access_token=self.token,
                                               accessed_from=self.ip_address,
                                               access_details=self.action,
                                               packages_accessed=self.package,
                                               package_version_accessed=self.package_version)
            return True

        team = Teams.objects.filter(
            access_tokens=self.token,
            members__in=self.user
        )
        if team:
            project = self.token.project
            if project:
                AccessTeamsLogs.objects.create(user=self.user, access_token=self.token, team=team,
                                               accessed_from=self.ip_address,
                                               access_details=self.action,
                                               project_accessed=project,
                                               packages_accessed=self.package,
                                               package_version_accessed=self.package_version)
            else:
                AccessTeamsLogs.objects.create(user=self.user, access_token=self.token, team=team,
                                               accessed_from=self.ip_address,
                                               access_details=self.action,
                                               packages_accessed=self.package,
                                               package_version_accessed=self.package_version
                                               )
            return True

        return False
