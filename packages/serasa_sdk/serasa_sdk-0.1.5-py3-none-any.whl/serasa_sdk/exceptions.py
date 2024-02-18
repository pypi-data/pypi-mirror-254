from six import python_2_unicode_compatible


@python_2_unicode_compatible
class SerasaSDKError(Exception):
    def __init__(
        self,
        message=None,
        http_body=None,
        http_status=None,
        json_body=None,
        headers=None,
        code=None,
    ):
        super(SerasaSDKError, self).__init__(message)

        self._message = message
        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body
        self.headers = headers or {}
        self.code = code
        self.request_id = self.headers.get('request-id', None)


class AuthenticationError(SerasaSDKError):
    pass


class APIError(SerasaSDKError):
    pass


class ClientError(SerasaSDKError):
    pass
