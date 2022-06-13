from django.contrib import admin

from .models import UserProfile, UserType, UserInterest, UserStudent

admin.site.register(UserProfile)
admin.site.register(UserType)
admin.site.register(UserInterest)
admin.site.register(UserStudent)


