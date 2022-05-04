from django.conf import settings

from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'API_PROXY', None)

DEFAULTS = {
    'HOST': None,
    'AUTH': {
        'user': None,
        'password': None,
        'token': None,
    },
    'TIMEOUT': None,
    'DEFAULT_HTTP_ACCEPT': 'application/json',
    'DEFAULT_HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.8',
    'DEFAULT_CONTENT_TYPE': 'application/json',

    # Return response as-is if enabled
    'RETURN_RAW': False,

    # Return failure response as-is if code >= 400
    'RETURN_RAW_ERROR': False,

    # Used to translate Accept HTTP field
    'ACCEPT_MAPS': {
        'text/html': 'application/json',
    },

    # Do not pass following parameters
    'DISALLOWED_PARAMS': ('format',),

    # Perform a SSL Cert Verification on URI requests are being proxied to
    'VERIFY_SSL': True,
}

api_proxy_settings = APISettings(USER_SETTINGS, DEFAULTS)
