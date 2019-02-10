"""
Url patterns for the all versioned API endpoints.
"""

from django.conf import settings
from django.urls import path, include

# Each application with API endpoints should define a module named 'api'
# This module should define sub modules relating to version numbers. Each
# version should define a router file which contains the URL configurations
# for that application and version.

# You can use this configuration if you would like to manage versions this way,
# otherwise feel free to delete this application and use your own
# preferred method.

# Example:
# from account.api.v1.router import urlpatterns as account_api_v1

# urlpatterns_v1 = [
#     path(
#         '^v1/',
#         include(account_api_v1, namespace='account-api-v1'),
#         name='account-api-v1',
#     ),
# ]


# Tuples of urlpatterns, namespace, name
version_map = {
    'v1':  (
        # (account_api_v1, 'account-api-v1', 'account-api-v1'),
    ),
}


urlpatterns_current = []
for urls, name, namespace in version_map.get(settings.CURRENT_API_VERSION):
    name = name.replace(settings.CURRENT_API_VERSION, 'current')
    namespace = namespace.replace(settings.CURRENT_API_VERSION, 'current')
    urlpatterns_current.append(
        path('', view=include(urls, namespace=namespace), name=name)
    )

urlpatterns = []
urlpatterns.extend(urlpatterns_current)
# urlpatterns.extend(urlpatterns_v1)
