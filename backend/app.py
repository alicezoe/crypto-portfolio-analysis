from fastapi import FastAPI, Query
from data_service import get_coingecko_prices

app = FastAPI()

@app.get("/api/prices")
def get_prices(
    coins: str = Query("bitcoin,ethereum", description="Comma-separated CoinGecko coin IDs"),
    vs_currency: str = Query("usd", description="Fiat currency to compare against")
):
    coin_list = [coin.strip() for coin in coins.split(",")]
    prices = get_coingecko_prices(coin_list, vs_currency)
    return prices