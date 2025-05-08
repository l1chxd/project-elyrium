from dotenv import load_dotenv
import os
load_dotenv()

from fastapi import FastAPI

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from datetime import datetime, timedelta
import random

@app.get("/forecast")
def get_forecast():
    now = datetime.now()
    # Runde auf nächsten vollen 30-Minuten-Block
    minute = 30 if now.minute >= 30 else 0
    if minute == 0:
        now = now.replace(minute=30, second=0, microsecond=0)
    else:
        now = now.replace(hour=now.hour + 1, minute=0, second=0, microsecond=0)

    forecast = {}

    for i in range(4):
        time_slot = (now + timedelta(minutes=30 * i)).strftime("%H:%M")
        prob_up = round(random.uniform(0.4, 0.7), 2)

        if prob_up >= 0.6:
            confidence = "hoch"
        elif prob_up >= 0.5:
            confidence = "mittel"
        else:
            confidence = "niedrig"

        forecast[time_slot] = {
            "prob_up": prob_up,
            "confidence": confidence
        }

    return forecast

from binance.client import Client

@app.get("/btc-prices")
def get_btc_prices():
    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_SECRET_KEY")

    if not api_key or not secret_key:
        return {"error": "API-Schlüssel nicht gesetzt"}

    client = Client(api_key, secret_key)

    try:
        klines = client.get_klines(symbol="BTCUSDT", interval=Client.KLINE_INTERVAL_1HOUR, limit=24)
        prices = [
            {
                "time": datetime.fromtimestamp(k[0] / 1000).strftime("%H:%M"),
                "price": float(k[4])
            }
            for k in klines
        ]
        return prices
    except Exception as e:
        print("❌ Binance API Fehler:", str(e))
        return {"error": "Fehler beim Abrufen der Binance-Daten"}

@app.get("/btc-prices-binance")
def get_btc_prices_binance():
    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_SECRET_KEY")

    if not api_key or not secret_key:
        return {"error": "API-Schlüssel nicht gesetzt"}

    client = Client(api_key, secret_key)

    try:
        klines = client.get_klines(symbol="BTCUSDT", interval=Client.KLINE_INTERVAL_1HOUR, limit=24)
        prices = []
        for k in klines:
            prices.append({
                "time": datetime.fromtimestamp(k[0] / 1000).strftime("%H:%M"),
                "price": float(k[4])  # Schlusskurs
            })
        return prices
    except Exception as e:
        print("❌ Fehler beim Binance Abruf:", str(e))
        return {"error": "Fehler beim Abrufen der Binance-Daten"}