import pytest

from pyndodax import public
from pyndodax.pair import Pair
# import asyncio

@pytest.mark.asyncio
async def test_aio_get_all_tickers():
    assert await public.aio_get_all_tickers()

@pytest.mark.asyncio
async def test_aio_get_ticker():
    assert await public.aio_get_ticker(Pair.BTC)
    
    # TODO: test all the pairs
    # Somehow if multiple request were running (serial and parallel), 
    # it always return with some TimeoutError 
    # assert await asyncio.gather(*[public.aio_get_ticker(pair) for pair in list(Pair)], loop=event_loop)

@pytest.mark.asyncio
async def test_aio_get_trades():
    # TODO: test all the pairs
    assert await public.aio_get_trades(Pair.BTC)

@pytest.mark.asyncio
async def test_aio_get_depth():
    # TODO: test all the pairs
    assert await public.aio_get_depth(Pair.BTC)
