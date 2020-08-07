<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-http-etag-view.svg?maxAge=3600)](https://pypi.org/project/django-http-etag-view/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-http-etag-view.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-http-etag-view.py/actions)

### Installation
```bash
$ [sudo] pip install django-http-etag-view
```

#### Examples
`get_http_etag`
```python
from django_http_etag_view.views import HttpEtagMixin

class MyView(HttpEtagMixin,...):

    def get_http_etag(self):
        return 'XXX'
```

`dispatch`, `self.http_etag`:
```python
class MyView(HttpEtagMixin,...):
    def dispatch(self, *args, **kwargs):
        self.http_etag = 'XXX'
        return super().dispatch(*args, **kwargs)
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>