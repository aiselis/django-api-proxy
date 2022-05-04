# Django API Proxy

[![PyPI version](https://badge.fury.io/py/django-api-proxy.svg)](http://badge.fury.io/py/django-api-proxy)

Provides views to redirect incoming request to another API server.

**Features:**

* Masquerade paths
* HTTP Basic Auth (between your API and backend API)
* Token Auth
* Supported methods: GET/POST/PUT/PATCH/DELETE
* File uploads

**TODO:**
* Pass auth information from original client to backend API

## Installation

```bash
$ pip install django-api-proxy
```

## Usage
There are couple of ways to use proxies. You can either use provided views as is or subclass them.

### Settings
```python
# settings.py
API_PROXY = {
    'HOST': 'https://api.example.com',
    'AUTH': {
        'user': 'myuser',
        'password': 'mypassword',
        # Or alternatively:
        'token': 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b',
    },
}
```


### Simple way
```python
# urls.py
from django_api_proxy.views import ProxyView

# Basic
url(r'^item/$', ProxyView.as_view(source='items/'), name='item-list'),

# With captured URL parameters
url(r'^item/(?P<pk>[0-9]+)$', ProxyView.as_view(source='items/%(pk)s'), name='item-detail'),
```
### Complex way
```python
# views.py
from django_api_proxy.views import ProxyView

class ItemListProxy(ProxyView):
  """
  List of items
  """
  source = 'items/'

class ItemDetailProxy(ProxyView):
  """
  Item detail
  """
  source = 'items/%(pk)s'

```
```python
# urls.py
from views import ProxyListView, ProxyDetailView

url(r'^item/$', ProxyListView.as_view(), name='item-list'),
url(r'^item/(?P<pk>[0-9]+)$', ProxyDetailView.as_view(), name='item-detail'),
```

## Settings
| Setting           | Default                                         | Comment                                                                                                                                         |
|-------------------|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
 | HOST              | None                                            | Proxy request to this host (e.g. https://example.com/api/)                                                                                      |
| AUTH              | {'user': None, 'password': None, 'token': None} | Proxy requests using HTTP Basic or Token Authentication. <br/>Token is only used if user &amp; password are not provided.                       |
| TIMEOUT           | None                                            | Timeout value for proxy requests.                                                                                                               |
| ACCEPT_MAPS       | {'text/html': 'application/json'}               | Modify Accept-headers before proxying them. You can use this to disallow certain types. By default text/html is translated to return JSON data. |
| DISALLOWED_PARAMS | ('format',)                                     | Remove defined query parameters from proxy request.                                                                                             |

## SSL Verification
By default, `django-api-proxy` will verify the SSL certificates when proxying requests, defaulting
to security. In some cases, it may be desirable to not verify SSL certificates. This setting can be modified
by overriding the `VERIFY_SSL` value in the `REST_PROXY` settings.

Additionally, one may set the `verify_proxy` settings on their proxy class:

```python
# views.py
from django_api_proxy.views import ProxyView

class ItemListProxy(ProxyView):
  """
  List of items
  """
  source = 'items/'
  verify_ssl = False

```

Finally, if there is complex business logic needed to determine if one should verify SSL, then
you can override the `get_verify_ssl()` method on your proxy view class:

```python
# views.py
from django_api_proxy.views import ProxyView

class ItemListProxy(ProxyView):
  """
  List of items
  """
  source = 'items/'

  def get_verify_ssl(self, request):
    host = self.get_proxy_host(request)
    if host.startswith('intranet.'):
      return True
    return False

```

## Permissions
You can limit access by using Permission classes and custom Views.
See http://django-rest-framework.org/api-guide/permissions.html for more information
```python
# permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class AdminOrReadOnly(BasePermission):
    """
    Read permission for everyone. Only admins can modify content.
    """
    def has_permission(self, request, view, obj=None):
        if (request.method in SAFE_METHODS or
            request.user and request.user.is_staff):
            return True
        return False

```
```python
# views.py
from django_api_proxy.views import ProxyView
from permissions import AdminOrReadOnly

class ItemListProxy(ProxyView):
    permission_classes = (AdminOrReadOnly,)
```

## License
`django_api_proxy` is offered under the Simplified BSD License

## Credits
`django_api_proxy` is a fork of django-rest-framework-proxy (https://github.com/eofs/django-rest-framework-proxy) created by Tomi Pajunen