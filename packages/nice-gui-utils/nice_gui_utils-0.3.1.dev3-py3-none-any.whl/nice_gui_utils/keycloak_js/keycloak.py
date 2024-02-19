"""
Implementation of the keycloak wrapper class.
See keycloak-js api reference for more info.
"""
from dataclasses import dataclass
from typing import AnyStr, Dict, Any

from nicegui import ui
from nicegui.awaitable_response import AwaitableResponse


@dataclass
class KeycloakConfig:
    """
    Base Keycloak config.
    """
    url: AnyStr
    realm: AnyStr
    client_id: AnyStr


class Keycloak(ui.element, component='keycloak.js'):
    """
    Wrapper class. Exposes part of the api of keycloak-js.
    Will automatically refresh tokens after initialization.
    """

    config: KeycloakConfig = None
    require_login: bool = None

    def __init__(self,
                 config: KeycloakConfig,
                 js_source: AnyStr = '/static/keycloak.js',
                 init_options: Dict = None):
        """

        :param config: base keycloak config
        :param js_source: url of keycloak-js source
        :param init_options: options used for initialization
        """
        super().__init__()

        ui.add_head_html(f'<script src="{js_source}"></script>')

        props: Dict[str, Any] = self._props
        props['url'] = config.url
        props['realm'] = config.realm
        props['clientId'] = config.client_id

        props['initOptions'] = init_options if init_options else {}

    def token(self) -> AwaitableResponse:
        """
        Get a token that can be sent in the Authorization header in requests to services.

        :return: base64 encoded token
        """
        return self.run_method('token')

    def refresh_token(self) -> AwaitableResponse:
        """
        Get a refresh token that can be used to retrieve a new token.

        :return: base64 encoded refresh token
        """
        return self.run_method('refreshToken')

    def authenticated(self) -> AwaitableResponse:
        """
        Returns true if the user is authenticated, false otherwise.

        :return: whether the used is authenticated
        """
        return self.run_method('authenticated')

    async def login(self, options: Dict = None) -> None:
        """
        Redirects to login form.
        See keycloak-js api reference
        for more info about available options.

        :param options: optional object
        """
        await self.run_method('login', options if options else {})

    async def logout(self, options: Dict = None) -> None:
        """
        Redirects to logout.
        See keycloak-js api reference
        for more info about available options.

        :param options: optional object
        """
        await self.run_method('logout', options if options else {})
