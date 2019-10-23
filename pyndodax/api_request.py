import time
import aiohttp

async def aio_api_request(url, api_key=None, params=None, signature=None):
    # Make request
    async with aiohttp.ClientSession() as session:
        if api_key: # POST, for private API
            response = await session.post(url, headers={
                "Key": api_key,
                "Sign": signature
            }, data=params, raise_for_status=True)
        else: # GET, for public API
            response = await session.get(url, raise_for_status=True)
    response = await response.json()

    # Check for API level error
    if "error" in response:
        raise ValueError(response["error"])

    return response