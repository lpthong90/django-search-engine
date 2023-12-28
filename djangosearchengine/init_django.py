import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosearchengine.settings_dev")

django.setup()
