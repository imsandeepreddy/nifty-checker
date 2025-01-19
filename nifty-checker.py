import requests
from bs4 import BeautifulSoup

# URL to scrape
URL = "https://www.google.com/finance/quote/NIFTYBEES:NSE?window=1Y"

def get_finance_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. HTTP Status: {response.status_code}")
    
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract values for previous close and all-time high
    try:
        prev_close = float(soup.find("div", {"class": "YMlKec fxKbKc"}).text.replace(",", "").strip("₹"))
        #high_1y = float(soup.find("div", {"class": "P6K39c"}).text.replace(",", "").strip("₹"))
        high_1y = 291.55
    except AttributeError as e:
        raise Exception("Failed to parse finance data. HTML structure might have changed.")
    
    return prev_close, high_1y

def main():
    try:
        prev_close, high_1y = get_finance_data(URL)
        difference = high_1y - prev_close
        percentage_diff = (difference / high_1y) * 100
        
        # Create a message
        message = (
            f"Google Finance Scraper:\n"
            f"Previous Close: ₹{prev_close}\n"
            f"1-Year High: ₹{high_1y}\n"
            f"Difference: ₹{difference:.2f} ({percentage_diff:.2f}%)\n"
        )
        print(message)  # This will log to GitHub Actions

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
