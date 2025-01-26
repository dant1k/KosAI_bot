# bot.py
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from solana_client import SolanaClient
import config

# Initialize bot and dispatcher
bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Initialize Solana client
solana_client = SolanaClient(config.SOLANA_RPC_URL)

# Command: /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply(
        "Welcome to the Solana Trading Bot! Use /help to see available commands."
    )

# Command: /help
@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    help_text = """
Available Commands:
/balance - Check your Solana wallet balance.
/transfer <recipient> <amount> - Transfer SOL to another wallet.
"""
    await message.reply(help_text, parse_mode=ParseMode.MARKDOWN)

# Command: /balance
@dp.message_handler(commands=["balance"])
async def check_balance(message: types.Message):
    try:
        wallet_public_key = config.WALLET_PUBLIC_KEY
        balance = solana_client.get_balance(wallet_public_key)
        await message.reply(f"Your balance: {balance} SOL")
    except Exception as e:
        await message.reply(f"Error: {str(e)}")

# Command: /transfer
@dp.message_handler(commands=["transfer"])
async def transfer_sol(message: types.Message):
    try:
        args = message.get_args().split()
        if len(args) != 2:
            await message.reply("Usage: /transfer <recipient> <amount>")
            return

        recipient, amount = args
        amount = float(amount)

        if amount <= 0:
            await message.reply("Amount must be greater than 0")
            return

        sender_private_key = config.WALLET_PRIVATE_KEY
        tx_id = solana_client.transfer_sol(sender_private_key, recipient, amount)
        await message.reply(f"Transaction successful! TX ID: {tx_id}")
    except Exception as e:
        await message.reply(f"Error: {str(e)}")

# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)