from django.contrib import admin
from django.contrib.auth.models import User
admin.site.unregister(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin): list_display=('username','email','first_name','last_name','is_staff'); search_fields=('email','first_name','last_name')
