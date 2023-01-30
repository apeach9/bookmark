from django.apps import AppConfig


class BookmarkConfig(AppConfig):
    name = 'bookmark'


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'users'