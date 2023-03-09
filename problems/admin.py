from django.contrib import admin
from .models import Diary, Account#, UserLogs
# Register your models here.

# FIX FOR LOGGING
# @admin.register(UserLogs)
# class UserLogAdmin(admin.ModelAdmin):
    # list_display = ["time", "user", "event",]
    # list_filter = ["event",]

admin.site.register(Diary)
admin.site.register(Account)