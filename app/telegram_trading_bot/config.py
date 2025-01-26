# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Solana RPC URL
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")

# Wallet Private Key (for demo purposes only; use secure storage in production)
WALLET_PRIVATE_KEY = os.getenv("WALLET_PRIVATE_KEY")

# Wallet Public Key
WALLET_PUBLIC_KEY = os.getenv("WALLET_PUBLIC_KEY")