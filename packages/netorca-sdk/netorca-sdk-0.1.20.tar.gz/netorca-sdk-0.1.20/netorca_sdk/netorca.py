import json
from typing import Dict, Union

from requests import RequestException

from netorca_sdk.auth import AbstractNetorcaAuth
from netorca_sdk.config import API_VERSION, URL_PREFIX
from netorca_sdk.exceptions import (
    NetorcaAPIError,
    NetorcaAuthenticationError,
    NetorcaException,
    NetorcaGatewayError,
    NetorcaInvalidContextError,
    NetorcaNotFoundError,
    NetorcaServerUnavailableError,
    NetorcaValueError,
)
from netorca_sdk.validations import ContextIn


class Netorca:
    """
    Netorca

    A class to manage API calls to various endpoints in the Netorca API using the provided authentication method.

    Attributes:
    - auth (AbstractNetorcaAuth): The authentication object used for making API requests.
    - endpoints (Dict): A dictionary containing the supported API endpoints and their corresponding methods.

    Methods:

    __init__(self, auth: AbstractNetorcaAuth)
    Initializes the NetorcaEndpointCaller with the provided authentication object.

    caller(self, endpoint: str, operation: str, id: Union[str, int] = None, filters: Dict = None, data: Dict = None, context: ContextIn = None) -> Dict
    Performs the specified operation on the specified endpoint using the provided arguments.

    _get(self, endpoint: str, id: Union[str, int] = None, filters: Dict = None, context: ContextIn = None) -> Dict
    Performs a GET request on the specified endpoint using the provided arguments.

    _create(self, endpoint: str, data: Dict, context: ContextIn = None) -> Dict
    Performs a CREATE request on the specified endpoint using the provided arguments.

    _update(self, endpoint: str, id: Union[str, int], data: Dict, context: ContextIn = None) -> Dict
    Performs an UPDATE request on the specified endpoint using the provided arguments.

    _delete(self, endpoint: str, id: Union[str, int], context: ContextIn = None) -> Dict
    Performs a DELETE request on the specified endpoint using the provided arguments.

    create_url(self, endpoint: str, context: ContextIn = ContextIn.SERVICEOWNER.value, id: Union[str, int] = None)
    Creates the appropriate URL for the specified endpoint, context, and optional ID.
    """

    def __init__(self, auth: AbstractNetorcaAuth):
        self.auth = auth
        self.endpoints = {
            "services": {
                "get": self._get,
            },
            "service_items": {
                "get": self._get,
            },
            "service_items_dependant": {
                "get": self._get,
                "url": "service_items/dependant",
            },
            "deployed_items": {
                "get": self._get,
                "create": self._create,
                "update": self._update,
                "patch": self._update,
                "delete": self._delete,
            },
            "deployed_items_dependant": {
                "get": self._get,
                "url": "deployed_items/dependant",
            },
            "change_instances": {
                "get": self._get,
                "create": self._create,
                "update": self._update,
                "patch": self._update,
            },
            "change_instances_dependant": {
                "get": self._get,
                "url": "change_instances/dependant",
            },
            "change_instances_referenced": {
                "get": self._get,
                "url": "change_instances/referenced",
            },
            "service_configs": {
                "get": self._get,
                "create": self._create,
            },
            "charges": {
                "get": self._get,
                "patch": self._update,
                "update": self._update,
                "prefix": "marketplace",
            },
            "charges_accumulated": {
                "get": self._get,
                "url": "charges/accumulated",
                "prefix": "marketplace",
            },
        }

    def caller(
        self,
        endpoint: str,
        operation: str,
        id: Union[str, int] = None,
        filters: Dict = None,
        data: Dict = None,
        context: ContextIn = None,
    ) -> Dict:
        if endpoint not in self.endpoints:
            raise NetorcaValueError(f"Invalid endpoint: {endpoint}")

        if operation not in self.endpoints[endpoint]:
            raise NetorcaValueError(f"Invalid operation: {operation}")

        if operation == "create":
            return self.endpoints[endpoint][operation](endpoint, data=data, context=context)
        elif operation in {"update", "patch"}:
            return self.endpoints[endpoint][operation](endpoint, id=id, data=data, context=context)
        elif operation == "delete":
            return self.endpoints[endpoint][operation](endpoint, id=id, context=context)
        else:
            return self.endpoints[endpoint][operation](endpoint, id=id, filters=filters, context=context)

    def _get(self, endpoint: str, id: Union[str, int] = None, filters: Dict = None, context: ContextIn = None) -> Dict:
        try:
            url = self.create_url(endpoint=endpoint, context=context, id=id)
            if filters:
                self.validate_filters(url=url, filters=filters)
            response = self.auth.get(url=url, authentication_required=True, filters=filters)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                raise NetorcaNotFoundError(f"{endpoint} not found.")
            elif response.status_code == 401:
                raise NetorcaAuthenticationError("Authentication failed.")
            elif response.status_code == 502:
                raise NetorcaGatewayError("Load balancer or webserver is down.")
            elif response.status_code == 503:
                raise NetorcaServerUnavailableError("Server is temporarily unavailable.")
            else:
                raise NetorcaAPIError(f"Error {response.status_code} - {response.text}")

        except RequestException as e:
            print(f"RequestException: {e}")
            raise NetorcaException(f"Could not fetch data from {endpoint} due to a network error.")

        except NetorcaException as e:
            print(f"Netorca Exception: {e}")

    def _create(self, endpoint: str, data: Dict, context: ContextIn = None) -> Dict:
        try:
            url = self.create_url(endpoint=endpoint, context=context)
            response = self.auth.post(url=url, data=json.dumps(data), authentication_required=True)
            if response.status_code == 201:
                return response.json()
            elif response.status_code == 404:
                raise NetorcaNotFoundError(f"{endpoint} not found.")
            elif response.status_code == 401:
                raise NetorcaAuthenticationError("Authentication failed.")
            elif response.status_code == 502:
                raise NetorcaGatewayError("Load balancer or webserver is down.")
            elif response.status_code == 503:
                raise NetorcaServerUnavailableError("Server is temporarily unavailable.")
            else:
                raise NetorcaAPIError(f"Error {response.status_code} - {response.json()}")

        except RequestException as e:
            print(f"RequestException: {e}")
            raise NetorcaException(f"Could not create data in {endpoint} due to: {response.text}")

        except NetorcaException as e:
            print(f"Netorca Exception: {e}")

    def _update(self, endpoint: str, id: Union[str, int], data: Dict, context: ContextIn = None) -> Dict:
        try:
            url = self.create_url(endpoint=endpoint, context=context, id=id)
            response = self.auth.patch(url=url, data=json.dumps(data), authentication_required=True)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                raise NetorcaNotFoundError(f"{endpoint} not found.")
            elif response.status_code == 401:
                raise NetorcaAuthenticationError("Authentication failed.")
            elif response.status_code == 502:
                raise NetorcaGatewayError("Load balancer or webserver is down.")
            elif response.status_code == 503:
                raise NetorcaServerUnavailableError("Server is temporarily unavailable.")
            else:
                raise NetorcaAPIError(f"Error {response.status_code} - {response.json()}")

        except RequestException as e:
            print(f"RequestException: {e}")
            raise NetorcaException(f"Could not create data in {endpoint} due to: {response.text}")

        except NetorcaException as e:
            print(f"Netorca Exception: {e}")

    def _delete(self, endpoint: str, id: Union[str, int], context: ContextIn = None) -> Dict:
        try:
            url = self.create_url(endpoint=endpoint, context=context, id=id)
            response = self.auth.delete(url=url, authentication_required=True)
            if response.status_code == 204:
                return {"status": "deleted"}
            elif response.status_code == 404:
                raise NetorcaNotFoundError(f"{endpoint} not found.")
            elif response.status_code == 401:
                raise NetorcaAuthenticationError("Authentication failed.")
            elif response.status_code == 502:
                raise NetorcaGatewayError("Load balancer or webserver is down.")
            elif response.status_code == 503:
                raise NetorcaServerUnavailableError("Server is temporarily unavailable.")
            else:
                raise NetorcaAPIError(f"Error {response.status_code} - {response.text}")

        except RequestException as e:
            print(f"RequestException: {e}")
            raise NetorcaException(f"Could not delete data from {endpoint} due to: {response.text}")

        except NetorcaException as e:
            print(f"Netorca Exception: {e}")

    def validate_filters(self, url: str, filters: Dict):
        try:
            options_resp = self.auth.options(authentication_required=True, url=url)
        except RequestException as e:
            print(f"RequestException: {e}")
            raise NetorcaException(f"Could not get filter options for {url}")

        try:
            options = options_resp.json().get("filters", [])
        except NetorcaValueError as e:
            print(f"NetorcaValueError: {e}")
            raise NetorcaException(f"Could not get filter options for {url}")
        options.append("limit")

        for filter_item in filters:
            if filter_item not in options:
                raise NetorcaException(f"{filter_item} is not a valid filter for {url}. Options are {options}")

    def create_url(self, endpoint: str, context: ContextIn = ContextIn.SERVICEOWNER.value, id: Union[str, int] = None):
        id_str = f"{str(id).replace('/', '')}/" if id else ""

        context = ContextIn.SERVICEOWNER.value if context is None else context
        if context not in (ContextIn.SERVICEOWNER.value, ContextIn.CONSUMER.value):
            raise NetorcaInvalidContextError(
                f"{context} is not a valid ContextIn value. Options are {ContextIn.SERVICEOWNER.value} and {ContextIn.CONSUMER.value}"
            )
        custom_url = self.endpoints.get(endpoint, {}).get("url", "")
        url_prefix = self.endpoints.get(endpoint, {}).get("prefix", URL_PREFIX)
        if custom_url:
            url = f"{self.auth.fqdn}{API_VERSION}/{url_prefix}/{context}/{custom_url}/{id_str}"
        else:
            url = f"{self.auth.fqdn}{API_VERSION}/{url_prefix}/{context}/{endpoint}/{id_str}"

        return url

    def create_deployed_item(self, change_instance_id: int, description: dict) -> dict:
        data = {"deployed_item": description}
        return self.caller("change_instances", "patch", id=change_instance_id, data=data)

    def get_deployed_item(self, change_instance_id: int) -> dict:
        return self.caller("deployed_items", "get", id=change_instance_id)

    def get_deployed_items(self, filters: dict = None) -> dict:
        return self.caller("deployed_items", "get", filters=filters)

    def get_service_items(self, filters: dict = None) -> dict:
        return self.caller("service_items", "get", filters=filters)

    def get_services(self, filters: dict = None) -> dict:
        return self.caller("services", "get", filters=filters)

    def get_service_item(self, service_item_id: int) -> dict:
        return self.caller("service_items", "get", id=service_item_id)

    def get_change_instance(self, change_instance_id: int) -> dict:
        return self.caller("change_instances", "get", id=change_instance_id)

    def get_change_instances(self, filters: dict = None) -> dict:
        return self.caller("change_instances", "get", filters=filters)

    def update_change_instance(self, change_instance_id: int, data: dict) -> dict:
        return self.caller("change_instances", "update", id=change_instance_id, data=data)

    def get_service_config(self, service_config_id: int) -> dict:
        return self.caller("service_configs", "get", id=service_config_id)

    def get_service_configs(self, filters: dict = None) -> dict:
        return self.caller("service_configs", "get", filters=filters)

    def create_service_config(self, data: dict) -> dict:
        return self.caller("service_configs", "create", data=data)

    def get_service_items_dependant(self, filters: dict = None) -> dict:
        return self.caller("service_items_dependant", "get", filters=filters)

    def get_charges(self, filters: dict = None) -> dict:
        return self.caller("charges", "get", filters=filters)

    def update_charges(self, charge_id: int, data: dict) -> dict:
        return self.caller("charges", "patch", id=charge_id, data=data)

    def get_deployed_items_dependant(self, filters: dict = None) -> dict:
        return self.caller("deployed_items_dependant", "get", filters=filters)
