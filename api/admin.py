from django.contrib import admin

from api import models


@admin.register(models.DownloadTask)
class DownloadTask(admin.ModelAdmin):
    list_display = (
        'id',
        'quality',
        'status',
    )


@admin.register(models.DownloadResult)
class DownloadResult(admin.ModelAdmin):
    list_display = (
        'id',
        'file_url',
    )


@admin.register(models.UserSession)
class UserSession(admin.ModelAdmin):
    list_display = (
        'id',
        'session_id',
    )
