class DownloadTaskConstants:
    CHOICES = (
        ('mp3', 'Audio (MP3)'),
        ('mp4', 'Video (MP4)'),
    )


class TaskStatusConstants:
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    FAILED = 'failed'

    CHOICES = (
        (PENDING, 'В ожидании'),
        (IN_PROGRESS, 'В процессе'),
        (COMPLETED, 'Завершено'),
        (FAILED, 'Ошибка'),
    )
