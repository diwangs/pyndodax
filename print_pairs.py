from pyndodax import api_request
import asyncio

x = asyncio.run(api_request.aio_api_request("https://indodax.com/api/tickers"))
for key in x['tickers'].keys():
    if key[-4:] == "_btc":
        print(key.upper() + " = \"" + key + "\"")
    else:
        print(key.split("_")[0].upper() + " = \"" + key + "\"")

