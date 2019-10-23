# pyndodax
[![Build Status](https://travis-ci.com/diwangs/pyndodax.svg?branch=master)](https://travis-ci.com/diwangs/pyndodax)

An unofficial Python wrapper for indodax.com API with support for async i/o

[Original API documentation](https://indodax.com/downloads/INDODAXCOM-API-DOCUMENTATION.pdf)

## Public API
Indodax provides 4 public endpoint that can be accessed by the public. This library will provide those 4 endpoints in the `pyndodax.public` module, which consisted of:

* Get current price of all markets (`aio_get_all_tickers()`) 
* Get current price of a given market (`aio_get_ticker(pair)`)
* Get last few trade history of a given market (`aio_get_trades(pair)`)
* Get bids and asks of a given market (`aio_get_depth(pair)`)

You can describe a trade pair with `Pair`, custom enum type that can be accessed at `pyndodax.pair`. If you want to pick a currency that is traded against IDR, just refer it with the currency symbol, all uppercase. For BTC traded currencies, add `_BTC` as a postfix. e.g.:
* btc-idr is `Pair.BTC`
* bat-idr is `Pair.BAT`
* eth-btc is `Pair.ETH_BTC`
* etc.

## Private API
TBA

## Want to add something?
You can clone this repo and setup a dev environment by running these commands
```
python setup.py install
pip install -e .[dev]
```
Code something and create a pull request!