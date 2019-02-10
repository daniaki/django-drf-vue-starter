import json
import os

from django.core.exceptions import ImproperlyConfigured


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_DIR = BASE_DIR + '/settings/'

# Read the secrets file
try:
    with open(SETTINGS_DIR + '/secrets.json', 'rt') as handle:
        secrets = json.load(handle)
except FileNotFoundError:
    raise FileNotFoundError("You must create a 'secrets.json' file in the "
                            "project settings directory.")


def get_secret(setting, secrets=secrets):
    """
    Retrieve a named setting from the secrets dictionary read from the JSON.

    Adapted from Two Scoops of Django, Example 5.21
    """
    try:
        return secrets[setting]
    except KeyError:
        error_message = "Unable to retrieve setting: '{}'".format(setting)
        raise ImproperlyConfigured(error_message)
