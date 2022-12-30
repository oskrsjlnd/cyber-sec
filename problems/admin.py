from django.contrib import admin
from .models import Diary, Account

# Register your models here.

admin.site.register(Diary)
admin.site.register(Account)