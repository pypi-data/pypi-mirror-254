from django.contrib import admin

from PPM.models import AccessTokens

from PPM.models import AccessTokens, Projects, Packages, PackageVersions, UserAccess, Teams, AccessUsersLogs, \
    AccessTeamsLogs

class AccessTokensAdmin(admin.ModelAdmin):
    # token_user, token_pass, project, package
    list_display = ('token_user', 'token_pass', 'project', 'package')
    list_filter = ('project', 'package')
    search_fields = ('token_user', 'token_pass', 'project__name', 'package__name')
    raw_id_fields = ('project', 'package')

    def get_queryset(self, request):
        qs = super(AccessTokensAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.none()
admin.site.register(AccessTokens, AccessTokensAdmin)
admin.site.register(Projects)
admin.site.register(Packages)
admin.site.register(PackageVersions)
admin.site.register(UserAccess)
admin.site.register(Teams)
admin.site.register(AccessUsersLogs)
admin.site.register(AccessTeamsLogs)
# Register your models here.
