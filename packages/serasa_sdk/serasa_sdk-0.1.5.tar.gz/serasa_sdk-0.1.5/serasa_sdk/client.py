import os

import requests

from .enums import APIErrorMessage, APIReturnCode
from .exceptions import APIError, AuthenticationError, ClientError
from .routes import Digitalizacao


class Client(object):
    """
    A client for accessing Serasa API.
    """

    def __init__(
        self,
        credentials: str = None,
        login: str = None,
        env: str = None,
    ):
        """Initializes the serasa_sdk Client
        :param str credentials: Base64 encoded Basic Authentication bearer
        :param str login: Login ID used to check if credentials are right
        :param str env: The environment in which API calls will be made
        :rtype: serasa_sdk.client.Client
        """

        self.env = env or os.environ.get('SERASA_SDK_ENV', 'prod')
        self.credentials = credentials or os.environ.get('SERASA_SDK_CREDENTIALS')
        self.login = login or os.environ.get('SERASA_SDK_LOGIN')

        base_url = {
            'prod': 'https://www.brflow.com.br/ws',
            'staging': 'https://www.brflow.com.br/ws',
        }

        try:
            self.base_url = base_url[self.env.strip().lower()]
        except KeyError as e:
            raise ClientError("Use 'prod' or 'staging' as env") from e

        if not self.credentials:
            raise AuthenticationError('Undefined credentials')

        if not self.login:
            raise AuthenticationError('Undefined login ID')

        self.authenticate()

        self._digitalizacao = None

    @property
    def digitalizacao(self):
        if not self._digitalizacao:
            self._digitalizacao = Digitalizacao(self)
        return self._digitalizacao

    def authenticate(self):
        response = requests.get(
            url=f'{self.base_url}/autenticacao/autenticar-oauth',
            headers={'Authorization': f'Basic {self.credentials}'},
        )

        if response.json()['error']:
            raise AuthenticationError(response.json()['return'])

        self.token = response.json()['Token']
        self.set_session()

    def set_session(self):
        self.session = requests.Session()
        self.session.headers.update({'Authorization': self.token})

    def post(self, path, original_data):
        data = {**original_data, 'codLogin': self.login}

        response = self.session.post(url=f'{self.base_url}/{path}', json=data)
        data = response.json()

        if response.status_code == 401:
            self.authenticate()
            return self.post(path, original_data)

        if data.get('error'):
            raise APIError(data.get('result') or data.get('errorMessage'))

        if res := data.get('res'):
            if res['status'] == APIReturnCode.ERROR.value:
                match res['message']:
                    case APIErrorMessage.EXPIRED_TOKEN.value:
                        self.authenticate()
                        return self.post(path, data)
                    case APIErrorMessage.INVALID_TOKEN.value:
                        raise AuthenticationError('Wrong credentials')
                    case APIErrorMessage.INVALID_FILES.value:
                        raise APIError('Invalid Files')
                    case _:
                        raise APIError(res['message'])

            return res

        return data.get('return')
