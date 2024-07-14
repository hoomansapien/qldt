from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from st_mn_sys_app.models import nguoiDung

# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(nguoiDung,UserModel)