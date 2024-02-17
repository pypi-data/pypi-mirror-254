import logging
from functools import wraps
from typing import Optional, Callable, Any, Union, Dict, Tuple

import requests
from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakError
from requests import HTTPError


def flask_keycloak_authenticate(
    server_url: str,
    client_id: str,
    client_secret_key: str = None,
    tenant_extractor: Optional[Callable[[], str]] = lambda: "",
    token_extractor: Optional[Callable[[], str]] = lambda: "",
) -> Callable[
    [Callable[..., Any]],
    Callable[..., Union[Dict[str, Any], Tuple[Dict[str, Any], int]]],
]:
    """
    Method to be used as decorator, which accepts instance of KeycloakOpenID
    :param server_url: the URL of keycloak.
    :param client_id: The client_id of keycloak.
    :param client_secret_key: secret key of keycloak.
    :param tenant_extractor: Function that will return tenant name.
    :param token_extractor: Function that will return token.
    :return: Error message | original function
    """

    def funct_decorator(org_function):
        @wraps(org_function)
        def authorize(*args, **kwargs):
            subdomain = tenant_extractor()
            token = token_extractor()
            if not token:
                logging.error("Bearer Token was not found.")
                return {"statusCode": 401, "message": "Token is missing"}, 401
            try:
                oidc = KeycloakOpenID(
                    server_url=server_url,
                    client_id=client_id,
                    realm_name=subdomain,
                    client_secret_key=client_secret_key,
                )
                token = token.replace("Bearer ", "")
                oidc.userinfo(token)
                logging.info("Successfully authorized")
                return org_function(*args, **kwargs)
            except KeycloakError as e:
                logging.error(f"Error: {e.__doc__} Status code: {e.response_code}")
                return {
                    "statusCode": e.response_code,
                    "message": e.__doc__,
                }, e.response_code

        return authorize

    return funct_decorator


def flask_keycloak_permissions(
    url: str,
    json: dict,
    token_extractor: Optional[Callable[[], str]] = lambda: "",
    origin_extractor: Optional[Callable[[], str]] = lambda: "",

) -> Callable[
    [Callable[..., Any]],
    Callable[..., Union[Dict[str, Any], Tuple[Dict[str, Any], int]]],
]:
    """
    Method to be used as decorator, which accepts instance of KeycloakOpenID
    :param url: the URL to which send a JSON and check permissions.
    :param json: The JSON that should be sent.
    :param token_extractor: Function that will return token.
    :param origin_extractor: Function that will return origin value from header.
    :return: Error message | original function
    """

    def funct_decorator(org_function):
        @wraps(org_function)
        def permission_check(*args, **kwargs):
            try:
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                    "Origin": origin_extractor(),
                    "Authorization": token_extractor(),
                }
                response = requests.post(url=url, json=json, headers=headers)
                response.raise_for_status()
                logging.info(
                    f"Successfully checked permissions. Response - {response.json()}"
                )
                return org_function(*args, **kwargs)
            except HTTPError as err:
                logging.error(
                    f"Error: {err.response.json()} Status code: {err.response.status_code}"
                )
                return err.response.json(), err.response.status_code

        return permission_check

    return funct_decorator

def flask_user_permissions(
        url: str,
        token_extractor: Optional[Callable[[], str]] = lambda: "",
        origin_extractor: Optional[Callable[[], str]] = lambda: "",

) -> Callable[
    [Callable[..., Any]],
    Callable[..., Union[Dict[str, Any], Tuple[Dict[str, Any], int]]],
]:
    """
    Method to be used as decorator, sends a request to get user permissions dictionary
    :param url: the URL to which send a token to retrieve permissions.
    :param token_extractor: Function that will return token.
    :param origin_extractor: Function that will return origin value from header.
    :return: Error message | original function
    """

    def funct_decorator(org_function):
        @wraps(org_function)
        def permission_check(*args, **kwargs):
            try:
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                    "Origin": origin_extractor(),
                    "Authorization": token_extractor(),
                }
                response = requests.get(url=url, headers=headers)
                response.raise_for_status()

                logging.info(
                    f"Successfully checked permissions. Response - {response.json()}"
                )
                return org_function(permissions=response.json(), *args, **kwargs)
            except HTTPError as err:
                logging.error(
                    f"Error: {err.response.json()} Status code: {err.response.status_code}"
                )
                return err.response.json(), err.response.status_code

        return permission_check

    return funct_decorator