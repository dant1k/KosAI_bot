# solana_client.py
from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from solana.keypair import Keypair
from solana.rpc.types import TxOpts

class SolanaClient:
    def __init__(self, rpc_url):
        self.client = Client(rpc_url)

    def get_balance(self, public_key):
        """Get the balance of a Solana wallet."""
        response = self.client.get_balance(PublicKey(public_key))
        if response.get("result") is None:
            raise Exception("Failed to fetch balance")
        return response["result"]["value"] / 1e9  # Convert lamports to SOL

    def transfer_sol(self, sender_private_key, recipient_public_key, amount):
        """Transfer SOL from one wallet to another."""
        sender_keypair = Keypair.from_secret_key(bytes.fromhex(sender_private_key))
        recipient_pubkey = PublicKey(recipient_public_key)
        amount_lamports = int(amount * 1e9)  # Convert SOL to lamports

        # Create and send transaction
        txn = Transaction().add(
            transfer(
                TransferParams(
                    from_pubkey=sender_keypair.public_key,
                    to_pubkey=recipient_pubkey,
                    lamports=amount_lamports,
                )
            )
        )
        response = self.client.send_transaction(txn, sender_keypair, opts=TxOpts(skip_preflight=True))
        if response.get("result") is None:
            raise Exception("Failed to send transaction")
        return response["result"]