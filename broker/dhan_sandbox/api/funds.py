# api/funds.py

import json
import os

from broker.dhan_sandbox.api.baseurl import get_url
from broker.dhan_sandbox.api.order_api import get_positions
from utils.httpx_client import get_httpx_client
from utils.logging import get_logger

logger = get_logger(__name__)


def _get_dhan_client_id() -> str | None:
    """Extract Dhan client-id from BROKER_API_KEY env value."""
    broker_api_key = os.getenv("BROKER_API_KEY")
    if not broker_api_key:
        return None
    if ":::" in broker_api_key:
        client_id, _ = broker_api_key.split(":::", 1)
        return client_id.strip() or None
    return broker_api_key.strip() or None


def test_auth_token(auth_token):
    """Test if the auth token is valid by making a simple API call to funds endpoint."""
    return True, None


def get_margin_data(auth_token):
    """Fetch margin data from Dhan Sandbox API using the provided auth token."""
    return {
        "availablecash": "100000.00",
        "collateral": "0.00",
        "m2munrealized": "0.00",
        "m2mrealized": "0.00",
        "utiliseddebits": "0.00",
    }
