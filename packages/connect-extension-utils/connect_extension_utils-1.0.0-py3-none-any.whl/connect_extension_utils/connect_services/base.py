import os
from logging import Logger

from connect.client import ConnectClient
from connect.client.rql import R
from connect.eaas.core.logging import RequestLogger


def get_extension_owner_client(logger: Logger):
    """
    A `ConnectClient` instance with credentials of extension owner. This
    could be useful for the cases when make api call to Connect is needed, but
    outside the request-response cycle of Applications (Web or Event).

        :param logging.Logger:
        :return: Instance of the connect-python-openapi-client
        :rtype: connect.client.ConnectClient
    """
    return ConnectClient(
        os.getenv("API_KEY"),
        endpoint=f"https://{os.getenv('SERVER_ADDRESS')}/public/v1",
        use_specs=False,
        logger=RequestLogger(logger),
    )


def get_extension_owner_installation(client: ConnectClient):
    """
    Helper function to retrieve installation data `on_startup` of
    WebApplication base on `ENVIRONMENT_ID` environment variable
    available by default in every EaaS extension.

        :param connect.client.ConnectClient:
        :return: Dict containing installation information
        :rtype: dict[str, Any]
    """
    rql = R().environment.id.eq(os.getenv("ENVIRONMENT_ID"))
    return client("devops").installations.filter(rql).first()
