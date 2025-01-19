# Nifty Notification Bot

This project checks the **NIFTY 50** stock index from Monday to Friday, compares all-time high and previous close, and sends a notification via Telegram. The workflow is automated using **GitHub Actions** and runs every day at a scheduled time.

## Features
- Scrapes stock data from [Google Finance](https://www.google.com/finance).
- Compares the 52-week high and the previous close.
- Sends a Telegram message with the analysis.
- Runs from Monday to Friday using GitHub Actions.
```
## Project Structure
.
├── .github
│   └── workflows
│       └── nifty-notification.yml  # GitHub Actions workflow
├── nifty-checker.py                # Main Python script
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```
## Prerequisites
1. A **Telegram Bot**:
   - Create a bot using [BotFather](https://t.me/botfather) and get the `BOT_TOKEN`.
   - Add the bot to a group or chat and retrieve the `CHAT_ID` (refer to Telegram API documentation for details).
2. **GitHub Repository**:
   - Create a GitHub repository and enable Actions.
3. **GitHub Secrets**:
   - Add the following secrets in your repository:
     - `TELEGRAM_BOT_TOKEN` (your Telegram bot token).
     - `TELEGRAM_CHAT_ID` (your chat or group ID for notifications).

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/imsandeepreddy/nifty-checker.git
cd nifty-notification-bot
```

### 2. Install Dependencies
Install Python dependencies locally for testing:
```bash
pip install -r requirements.txt
```

### 3. Test Locally
Run the script locally to ensure it works as expected:
```bash
python nifty-checker.py
```

### 4. Set Up GitHub Actions
1. Push your code to the `main` branch.
2. Edit the `.github/workflows/main.yml` file to set the schedule.
3. GitHub Actions will trigger automatically at the specified time.

## Usage

### GitHub Actions Workflow
The workflow triggers and includes:
- Setting up Python.
- Installing dependencies.
- Running the script.
- Sending the Telegram notification.

### Manual Trigger
You can manually trigger the workflow using the **`workflow_dispatch`** option in GitHub Actions.

## Example Output
A sample Telegram notification:
```
*Nippon India ETF Nifty 50 BeES*
Previous Close: ₹259.93
1-Year High: ₹291.97
Difference: ₹32.04 (10.97%)
```

## Customization
- Modify the URL or logic in `nifty-checker.py` to track different indices or compare against custom thresholds.
- Adjust the **cron schedule** in `.github/workflows/main.yml` to suit your preferred timings.

## Contribution
Feel free to contribute by submitting issues or pull requests. For major changes, please open a discussion first.

## License
This project is licensed under the MIT License. See `LICENSE` for details.
