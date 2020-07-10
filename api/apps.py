from django.apps import AppConfig
from django.db import OperationalError


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from django.contrib.auth.models import User

        try:
            username = os.environ['USER']
            password = os.environ['PASSWORD']
        except:
            from .secrets import *

        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password)
            user.save()

        except OperationalError:
            pass