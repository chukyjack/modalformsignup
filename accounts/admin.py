from django.contrib.auth import get_user_model
from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin




CustomUser = get_user_model()
admin.site.unregister(CustomUser)
admin.site.register(CustomUser)
#admin.site.register(Profile)
