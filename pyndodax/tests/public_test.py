import pytest

from pyndodax import public
from pyndodax.pair import Pair
import asyncio

@pytest.mark.asyncio
async def test_aio_get_all_tickers():
    assert await public.aio_get_all_tickers()

@pytest.mark.asyncio
async def test_aio_get_ticker(event_loop):
    assert await asyncio.gather(*[public.aio_get_ticker(pair) for pair in list(Pair)], loop=event_loop)