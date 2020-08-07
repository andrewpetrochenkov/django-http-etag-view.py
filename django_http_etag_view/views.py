__all__ = ['HttpEtagMixin']


class HttpEtagMixin:
    http_etag = None

    def get_http_etag(self):
        return self.http_etag

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        if response.status_code in [200, 304]:
            http_etag = self.get_http_etag()
            if http_etag:
                response['ETag'] = http_etag
        return response
