from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from django.utils.crypto import get_random_string

from PPM.models import AccessTokens, Projects, Packages, PackageVersions, UserAccessToken, Teams, AccessUsersLogs, \
    AccessTeamsLogs

User = get_user_model()


class TestAccessTokens(TestCase):
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
            file="Test File",
            version="1.1",
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
            is_active=True,

            created_at=timezone.now(),
            updated_at=timezone.now(),

            allow4all=True,
            allow_md4all=True,
            allow_md4=True,
        )
        package.versions.set(package_versions)
        project = Projects.objects.create(
            name="Test Project",
            description="Test Project",
            manager=user,
            packages=package,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            is_active=True,
        )

        access_token = AccessTokens.objects.create(
            description="Test Token",
            token_user=get_random_string(length=64),
            token_pass=get_random_string(length=64),
            projects=project,
            packages=package,
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
        user_access = UserAccessToken.objects.create(
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

    def test_create_users(self):
        self.assertEqual(User.objects.count(), 5)

    def test_create_package_version(self):
        self.assertEqual(PackageVersions.objects.count(), 2)

    def test_create_packages(self):
        self.assertEqual(Packages.objects.count(), 1)

    def test_create_project(self):
        self.assertEqual(Projects.objects.count(), 1)

    def test_create_access_tokens(self):
        self.assertEqual(AccessTokens.objects.count(), 1)

    def test_create_user_access(self):
        self.assertEqual(UserAccessToken.objects.count(), 1)

    def test_create_teams_access(self):
        self.assertEqual(Teams.objects.count(), 1)

    #
    # def test_create_package_version(self):
    #     # PackageVersion, file, version, description, created_at, updated_at, user_upload, shown_on_package
    #
    # def test_create_packages(self):
    #     # Packages name, description, versions, created_at, updated_at, is_active, allow4all, allow_md4all, allow_md4

    # def test_create_project(self):
    #     # Projects name, description, manager, packages, created_at, updated_at, is_active
    #
    #
    #
    # def test_create_access_tokens(self):
    #     # AccessTokens description, active, token_user, token_pass, projects, packages, start_date, end_date,
    #     # hourly_access, hourly_access_start, hourly_access_end, saturday, sunday, monday, tuesday, wednesday, thursday,
    #     # friday, access_type
    #
    #
    # def test_create_user_access(self):
    #     #UserAccessToken, uid, access_tokens, description, user, created_at, updated_at
    #
    #
    # def test_create_teams_access(self):
    #     # Teams  name, description, access_tokens, manager, members, created_at, updated_at, is_active
    #
    #
    # def test_insert(self):
    #     # uid, description, active, token_user, token_pass, projects, packages, start_date, end_date, hourly_access,
    #     # hourly_access_start, hourly_access_end, saturday, sunday, monday, tuesday, wednesday, thursday, friday, access_type
    #
    #     # random string text
    #
    #
    #
    # def test_get_access_token(self):
    #     pass
