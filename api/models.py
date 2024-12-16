from uuid import uuid4

from django.db import models

from api import consts


class DownloadTask(models.Model):
    url = models.URLField('YouTube URL')
    format = models.CharField('Формат', choices=consts.DownloadTaskConstants.CHOICES, max_length=255)
    quality = models.CharField(
        'Качество',
        max_length=255,
        null=True,
        blank=True,
    )
    status = models.CharField(
        'Статус', max_length=20, choices=consts.TaskStatusConstants.CHOICES, default=consts.TaskStatusConstants.PENDING
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Задача на скачивание'
        verbose_name_plural = 'Задачи на скачивание'

    def __str__(self) -> str:
        return f'{self.url} ({self.status})'


class UserSession(models.Model):
    session_id = models.UUIDField('ID сессии', default=uuid4, unique=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Сессия пользователя'
        verbose_name_plural = 'Сессии пользователей'

    def __str__(self) -> str:
        return str(self.session_id)


class DownloadResult(models.Model):
    task = models.OneToOneField('DownloadTask', on_delete=models.CASCADE, related_name='result')
    file_url = models.URLField('Ссылка на файл', max_length=500)
    file_size = models.PositiveIntegerField('Размер файла (в байтах)', null=True, blank=True)

    class Meta:
        verbose_name = 'Результат скачивания'
        verbose_name_plural = 'Результаты скачивания'

    def __str__(self) -> str:  # noqa
        return self.file_url
