from django.contrib import admin

from . import models

admin.site.register(models.Messages)
admin.site.register(models.Conversations)