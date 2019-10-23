import pytest

import os
from pyndodax import private
import asyncio

@pytest.fixture
def handle():
    skey = os.environ['PYNDODAX_SECRET_KEY']
    pkey = os.environ['PYNDODAX_API_KEY']
    return private.PrivateAPIHandle(api_key=pkey, secret_key=skey)

@pytest.mark.asyncio
async def test_aio_get_info(handle):
    response = await handle.aio_get_info()
    assert response["success"] == 1

@pytest.mark.asyncio
async def test_aio_trans_history(handle):
    response = await handle.aio_trans_history()
    assert response["success"] == 1