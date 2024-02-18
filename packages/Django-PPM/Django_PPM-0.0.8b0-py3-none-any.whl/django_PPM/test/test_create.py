from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from django.utils.crypto import get_random_string

from PPM.access_manager.access_manager import AccessManager
from PPM.models import AccessTokens, Projects, Packages, PackageVersions, UserAccess, Teams, AccessUsersLogs, \
    AccessTeamsLogs

user_model = get_user_model()


class TestCreate(TestCase):
    def setUp(self):
        user = user_model.objects.create_user(username="testuser", password="testpass")
        self.assertEqual(user_model.objects.count(),1)
        users = [
            user_model.objects.create_user(username="testuser1", password="testpass"),
            user_model.objects.create_user(username="testuser2", password="testpass"),
            user_model.objects.create_user(username="testuser3", password="testpass"),
            user_model.objects.create_user(username="testuser4", password="testpass"),
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

    def test_create_users(self):
        self.assertEqual(user_model
                         .objects.count(), 5)
    #
    def test_create_package_version(self):
        self.assertEqual(PackageVersions.objects.count(), 2)

    def test_create_packages(self):
        self.assertEqual(Packages.objects.count(), 1)

    def test_create_project(self):
        self.assertEqual(Projects.objects.count(), 1)

    def test_create_access_tokens(self):
        self.assertEqual(AccessTokens.objects.count(), 1)

    def test_create_user_access(self):
        self.assertEqual(UserAccess.objects.count(), 1)

    def test_create_teams_access(self):
        self.assertEqual(Teams.objects.count(), 1)
