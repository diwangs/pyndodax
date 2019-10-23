import pytest

from pyndodax import api_request
import asyncio

@pytest.mark.asyncio
async def test_aio_api_request():
    url = "https://indodax.com/api/btc_idr/ticker"
    assert await api_request.aio_api_request(url)