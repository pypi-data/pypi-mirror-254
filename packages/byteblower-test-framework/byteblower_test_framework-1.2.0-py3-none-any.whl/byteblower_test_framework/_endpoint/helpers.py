"""Helpers related to handling endpoint configuration."""
from typing import Union

from .._traffic.constants import VLAN_HEADER_LENGTH
from ..exceptions import FeatureNotSupported
from .endpoint import Endpoint
from .port import Port


def vlan_header_length(endpoint: Union[Port, Endpoint]) -> int:
    """Return the total length of all VLAN headers on the endpoint.

    :param endpoint: Endpoint to check the VLAN configuration on
    :type endpoint: Union[Port, Endpoint]
    :raises FeatureNotSupported: When an unsupported endpoint type is given
    :return: Total length of layer 2.5 headers in packets sent by the endpoint
    :rtype: int
    """
    if not isinstance(endpoint, (Port, Endpoint)):
        raise FeatureNotSupported(
            'Unsupported endpoint'
            f' type: {type(endpoint).__name__!r}'
        )

    try:
        vlan_config = list(endpoint.vlan_config)
        return len(vlan_config) * VLAN_HEADER_LENGTH
    except FeatureNotSupported:
        # (currently) not supported for Endpoint
        return 0
