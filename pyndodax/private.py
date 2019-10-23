from pyndodax import api_request

import hmac
from hashlib import sha512
from urllib.parse import urlencode
from time import time

class PrivateAPIHandle:
    url = 'https://indodax.com/tapi'

    def __init__(self, api_key, secret_key):
        self.__api_key = api_key
        self.__secret_key = secret_key

    def __sign(self, params):
        return hmac.new(self.__secret_key.encode(), urlencode(params).encode(), sha512).hexdigest()

    async def __make_request(self, params):
        params["nonce"] = str(int(time()*1000))
        return await api_request.aio_api_request(self.url, 
            api_key=self.__api_key,
            params=params,
            signature=self.__sign(params)
        )

    async def aio_get_info(self):
        params = {
            "method" : "getInfo"
        }

        return await self.__make_request(params)

    async def aio_trans_history(self):
        params = {
            "method" : "transHistory"
        }

        return await self.__make_request(params)