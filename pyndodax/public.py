from pyndodax import api_request
from pyndodax.pair import Pair

import asyncio

async def aio_get_all_tickers():
    url = "https://indodax.com/api/tickers"
    return await api_request.aio_api_request(url)

async def aio_get_ticker(pair):
    assert isinstance(pair, Pair), "Please use one of pyndodax.pair.Pair's member as argument"
    
    url = "https://indodax.com/api/" + pair.value + "/ticker"
    return await api_request.aio_api_request(url)

async def aio_get_trades(pair):
    assert isinstance(pair, Pair), "Please use one of pyndodax.pair.Pair's member as argument"
    
    url = "https://indodax.com/api/" + pair.value + "/trades"
    return await api_request.aio_api_request(url)

async def aio_get_depth(pair):
    assert isinstance(pair, Pair), "Please use one of pyndodax.pair.Pair's member as argument"
    
    url = "https://indodax.com/api/" + pair.value + "/depth"
    return await api_request.aio_api_request(url)