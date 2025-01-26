# Telegram Trading Bot on Solana

This is a Telegram bot that interacts with the Solana blockchain to check wallet balances and transfer SOL.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/telegram_trading_bot.git
   cd telegram_trading_bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your credentials:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   SOLANA_RPC_URL=https://api.mainnet-beta.solana.com
   WALLET_PRIVATE_KEY=your_wallet_private_key
   WALLET_PUBLIC_KEY=your_wallet_public_key
   ```

4. Run the bot:
   ```bash
   python bot.py
   ```

## Commands
- `/start`: Welcome message.
- `/help`: List of available commands.
- `/balance`: Check your Solana wallet balance.
- `/transfer <recipient> <amount>`: Transfer SOL to another wallet.