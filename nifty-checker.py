import requests
from bs4 import BeautifulSoup

# Constants
BOT_TOKEN = "TELEGRAM_BOT_TOKEN"  # Replace with your bot token
CHAT_ID = "TELEGRAM_CHAT_ID"      # Replace with your chat ID
URL = "https://www.google.com/finance/quote/NIFTYBEES:NSE?window=1Y"

def get_finance_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. HTTP Status: {response.status_code}")
    
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract values for previous close and 1-year high
    try:
        prev_close = float(soup.find("div", {"class": "YMlKec fxKbKc"}).text.replace(",", "").strip("₹"))
        high_1y = float(soup.find("div", {"class": "P6K39c"}).text.replace(",", "").strip("₹"))
    except AttributeError as e:
        raise Exception("Failed to parse finance data. HTML structure might have changed.")
    
    return prev_close, high_1y

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"  # Optional: Use Markdown or HTML for formatting
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")

def main():
    try:
        prev_close, high_1y = get_finance_data(URL)
        difference = high_1y - prev_close
        percentage_diff = (difference / high_1y) * 100
        
        # Create a message
        message = (
            f"*Google Finance Scraper*\n"
            f"Previous Close: ₹{prev_close}\n"
            f"1-Year High: ₹{high_1y}\n"
            f"Difference: ₹{difference:.2f} ({percentage_diff:.2f}%)\n"
        )
        print(message)  # Log the message
        send_telegram_message(BOT_TOKEN, CHAT_ID, message)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
