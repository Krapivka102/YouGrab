REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
    },
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'YouGrab API',
    'DESCRIPTION': 'API для скачивания видео с платформ',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
