import requests
import os

# Constants for the API and Telegram Bot
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")  # Add this to GitHub Secrets
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")        # Add this to GitHub Secrets
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")            # Add this to GitHub Secrets

# Nifty 50 Ticker Symbol (Example: "^NSEI" on Yahoo Finance or as per your API provider)
NIFTY_TICKER = "^NSEI"

# Function to fetch Nifty 50 data
def get_nifty_data():
    base_url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": NIFTY_TICKER,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        raise Exception("Failed to fetch Nifty 50 data")
    
    data = response.json()
    
    # Extracting today's open and 52-week high
    time_series = data.get("Time Series (Daily)")
    if not time_series:
        raise Exception("Time Series data not found")
    
    latest_date = max(time_series.keys())
    latest_data = time_series[latest_date]
    today_open = float(latest_data["1. open"])
    
    # Calculate 52-week high
    highs = [float(day["2. high"]) for day in time_series.values()]
    high_52_week = max(highs)
    
    return today_open, high_52_week

# Function to send message to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise Exception("Failed to send message to Telegram")

# Main Function
def main():
    try:
        today_open, high_52_week = get_nifty_data()
        difference = high_52_week - today_open
        message = (
            f"Nifty 50 Update:\n"
            f"52-Week High: {high_52_week}\n"
            f"Today's Open: {today_open}\n"
            f"Difference: {difference:.2f} points\n"
        )
        send_telegram_message(message)
        print("Notification sent successfully.")
    except Exception as e:
        print(f"Error: {e}")
        send_telegram_message(f"Error fetching Nifty 50 data: {e}")

if __name__ == "__main__":
    main()
