from django.contrib import admin
from .models import User, Portfolio, Resume, Skill, Job, Education, Accomplishments, Company
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class MyUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_startup_founder')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, MyUserAdmin)
admin.site.register(Portfolio)
admin.site.register(Resume)
admin.site.register(Skill)
admin.site.register(Job)
admin.site.register(Education)
admin.site.register(Accomplishments)
admin.site.register(Company)
