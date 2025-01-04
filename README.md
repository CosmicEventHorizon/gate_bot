# Gate.io Trading Bot 🤖💰

Hello there! Welcome to the **Gate.io Trading Bot** repository. This is an open-source Python project designed to automate your cryptocurrency trading experience on [Gate.io](https://www.gate.io/). Whether you're a seasoned trader or just starting out, this bot aims to make your life easier by providing an intuitive command-line interface for buying, selling, and automatically managing your trades. 🚀

## Table of Contents

1. [Features](#features-)
2. [Getting Started](#getting-started-)
3. [How It Works](#how-it-works-)
4. [Usage](#usage-)
5. [Warning: Risks of Trading](#warning-risks-of-trading-️)

## Features 🌟

The Gate.io Trading Bot offers a range of functionalities to help you manage your trades efficiently:

1. **Show current total balance** 💲
   - Display the available total balance in USDT on your Gate.io wallet.

2. **List all currencies** 📝
   - Display all available currency pairs on Gate.io.

3. **Buy a currency** 💵
   - Specify the currency, amount in USD, and desired price.
   - The bot will place a market buy order at the specified price.

4. **Sell a currency** 💰
   - Specify the currency to sell.
   - The bot will sell all available quantity of the chosen currency at the current market price using a market sell order.

5. **Place an automatic order** ⚙️🔄
   - Enter the currency, buy amount in USD, buy trigger price, and sell trigger price.
   - The bot will continuously monitor the market price:
     - When the market price falls below the buy trigger price, it buys the specified amount of the chosen currency.
     - When the market price rises above the sell trigger price, it sells all available quantity of the chosen currency.

## Getting Started 💻

To use this bot on your local machine, follow these steps:

1. Clone this repository:
   ```
   git clone https://github.com/CosmicEventHorizon/gate_bot.git
   ```

2. Run the bot using the command:
   ```
   python run_bot.py
   ```
3. Follow the instructions to create a `token` file in the project root directory containing your Gate.io API key and secret. Delete the `token` file to restore default settings.

## How It Works 🔧

The bot consists of three main files:

- `run_bot.py`: The entry point for the bot, containing the user interface and menus.
- `file_io.py`: Handles input/output operations related to reading/writing API keys and secrets.
- `gate_io.py`: Contains functions for interacting with Gate.io's API, including fetching currency pairs, prices, and placing orders.

## Usage 📊

Once the bot is running, you'll be presented with a menu offering five choices:

1. Show current total balance
2. List all currencies
3. Buy a currency
4. Sell a currency
5. Place an automatic order

Enter your choice using numeric input (e.g., `2` for listing currencies) and press Enter to proceed.

## Warning: Risks of Trading ⚠️

**Trading cryptocurrencies involves substantial risks, including but not limited to price volatility, illiquidity, regulatory changes, and technological issues. Before trading, please carefully consider these risks and make sure you understand them.**

- **Never risk more than you can afford to lose.**
- **Always use stop-loss orders to manage your risk.**
- **Stay informed about the latest market trends and news.**
- **Be aware of the potential dangers of using automated trading tools.**

By using this bot, you acknowledge that you are solely responsible for any gains or losses resulting from your trades.

Happy trading! 🎉💰