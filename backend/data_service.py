import requests

def get_coingecko_prices(coin_ids, vs_currency="usd"):
    """
    Fetch current prices for a list of coins from CoinGecko.
    :param coin_ids: List of CoinGecko coin IDs (e.g., ['bitcoin', 'ethereum'])
    :param vs_currency: The fiat currency to compare against (default: 'usd')
    :return: Dict of coin prices
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(coin_ids),
        "vs_currencies": vs_currency
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()