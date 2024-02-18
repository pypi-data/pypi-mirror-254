
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from django.utils.crypto import get_random_string


from PPM.models import AccessTokens, Projects, Packages, PackageVersions, UserAccess, Teams, AccessUsersLogs, \
    AccessTeamsLogs
from PPM.access_manager.access_manager import AccessManager
User = get_user_model()


class TestAccess(TestCase):

    def test_user_access_ok(self):
        model_user = get_user_model()
        user = model_user.objects.get(username="testuser")
        package = Packages.objects.get(name="Test Package")
        token = AccessTokens.objects.get(
            token_user="12345678910",
            token_pass="abcdefghijklmnopqrstuvwx",
            package=package)

        user_access = UserAccess.objects.get(user=user, access_tokens=token )
        # package, package_version, user, token_pass, token_user, action
        access_manager = AccessManager(request=None)


        self.assertEqual(check_access(request=access_request), True)
    def test_user_access_failure(self):
        model_user = get_user_model()
        user = model_user.objects.get(username="testuser")
        package = Packages.objects.get(name="Test Package2")
        token = AccessTokens.objects.get(
            token_user="12345678910",
            token_pass="abcdefghijklmnopqrstuvwx",
            package=package)

        user_access = UserAccess.objects.get(user=user, access_tokens=token )
        # package, package_version, user, token_pass, token_user, action
        access_request = AccessRequest(
            token_user=token.token_user,
            token_pass=token.token_pass,
            package=token.package,
            # package_version=token.project.packages.versions.first(),
            user=user,
            ip_address="10.0.0.2",
            action="Test Action")


        self.assertEqual(check_access(request=access_request), False)
    def test_team_access(self):
        model_user = get_user_model()
        user = model_user.objects.get(username="testuser1")
        package = Packages.objects.get(name="Test Package")
        token = AccessTokens.objects.get(
            token_user="12345678910",
            token_pass="abcdefghijklmnopqrstuvwx",
            package=package)

        user_access = UserAccess.objects.get(user=user, access_tokens=token )
        # package, package_version, user, token_pass, token_user, action
        access_request = AccessRequest(
            token_user=token.token_user,
            token_pass=token.token_pass,
            package=token.package,
            # package_version=token.project.packages.versions.first(),
            user=user,
            ip_address="10.0.0.2",
            action="Test Action")


        self.assertEqual(check_access(request=access_request), True)
    def test_team_access_failure(self):
        model_user = get_user_model()
        user = model_user.objects.get(username="testuser1")
        package = Packages.objects.get(name="Test Package2")
        token = AccessTokens.objects.get(
            token_user="12345678910",
            token_pass="abcdefghijklmnopqrstuvwx",
            package=package)

        user_access = UserAccess.objects.get(user=user, access_tokens=token )
        # package, package_version, user, token_pass, token_user, action
        access_request = AccessRequest(
            token_user=token.token_user,
            token_pass=token.token_pass,
            package=token.package,
            # package_version=token.project.packages.versions.first(),
            user=user,
            ip_address="10.0.0.2",
            action="Test Action")


        self.assertEqual(check_access(request=access_request), False)

    def setUp(self):
        user = User.objects.create_user(username="testuser", password="testpass")
        users = [
            User.objects.create_user(username="testuser1", password="testpass"),
            User.objects.create_user(username="testuser2", password="testpass"),
            User.objects.create_user(username="testuser3", password="testpass"),
            User.objects.create_user(username="testuser4", password="testpass"),
        ]
        package_versions = []
        package_version = PackageVersions.objects.create(
            file="Test File",
            version="1.0",
            description="Test Package Version",
            created_at=timezone.now(),
            updated_at=timezone.now(),
            user_uploaded=user,
            shown_on_package=True,

        )
        package_versions.append(package_version)
        package_version = PackageVersions.objects.create(
            description="Test Package Version",
            created_at=timezone.now(),
            updated_at=timezone.now(),
            user_uploaded=user,
            shown_on_package=True,
        )
        package_versions.append(package_version)
        package = Packages.objects.create(
            name="Test Package",
            description="Test Package",
            is_active=True, created_at=timezone.now(), updated_at=timezone.now(),
            allow4all=True, allow_md4all=True, allow_md4=True,
        )
        package2 = Packages.objects.create(
            name="Test Package2",
            description="Test Package",
            is_active=True, created_at=timezone.now(), updated_at=timezone.now(),
            allow4all=True, allow_md4all=True, allow_md4=True,
        )
        package.versions.set(package_versions)
        project = Projects.objects.create(
            name="Test Project",
            description="Test Project", manager=user, packages=package,
            created_at=timezone.now(), updated_at=timezone.now(), is_active=True,
        )

        access_token = AccessTokens.objects.create(
            description="Test Token",
            token_user="12345678910",
            token_pass="abcdefghijklmnopqrstuvwx",
            project=project,
            package=package,
            hourly_access=True,
            hourly_access_start="00:00:00",
            hourly_access_end="23:59:59",
            saturday=True,
            sunday=True,
            monday=True,
            tuesday=True,
            wednesday=True,
            thursday=True,
            friday=True,
            start_date=timezone.now() - timezone.timedelta(days=30),
            end_date=timezone.now() + timezone.timedelta(days=30),
        )
        user_access = UserAccess.objects.create(
            uid=get_random_string(length=64),

            description="Test User Access",
            user=user,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            is_active=True,
        )
        user_access.access_tokens.set([access_token])
        team = Teams.objects.create(
            name="Test Team",
            description="Test Team",

            manager=user,

            created_at=timezone.now(),
            updated_at=timezone.now(),
            is_active=True,
        )
        team.members.set(users)
        team.access_tokens.set([access_token])


