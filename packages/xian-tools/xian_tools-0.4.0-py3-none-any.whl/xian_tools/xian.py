import requests
import xian_tools.utils as utl
import xian_tools.transaction as tr

from xian_tools.wallet import Wallet
from typing import Dict, Any


class Xian:
    def __init__(self, node_url: str, wallet: Wallet = None):
        self.wallet = wallet if wallet else Wallet()
        self.node_url = node_url

    def get_balance(self, address: str = None, contract: str = 'currency') -> [int, float]:
        address = address if address else self.wallet.public_key

        r = requests.get(f'{self.node_url}/abci_query?path="/get/{contract}.balances:{address}"')
        balance_byte_string = r.json()['result']['response']['value']

        try:
            balance = utl.decode_int(balance_byte_string)
        except:
            balance = utl.decode_float(balance_byte_string)

        return balance

    def get_tx(self, tx_hash: str) -> Dict[str, Any]:
        """ Return transaction with decoded content """
        encoded_tx = tr.get_tx(self.node_url, tx_hash)
        return tr.decode_tx(encoded_tx)

    def deploy_contract(self, name: str, code: str, stamps: int = 1000):
        """ Deploy a contract to the network """
        tx = tr.create_tx(
            contract="submission",
            function="submit_contract",
            kwargs={
                "name": name,
                "code": code,
            },
            nonce=tr.get_nonce(self.node_url, self.wallet.public_key),
            stamps=stamps,
            private_key=self.wallet.private_key,
        )

        return tr.broadcast_tx(self.node_url, tx)
