from django.contrib import admin
from .models import *

admin.site.register(Signin)
admin.site.register(User)

class SigninAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'file')
    search_fields = ('user__email',)
    list_filter = ('user__is_active',)
    readonly_fields = ('user_email',)  # Optionally, make some fields read-only

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User Email'
# Register your models here.

