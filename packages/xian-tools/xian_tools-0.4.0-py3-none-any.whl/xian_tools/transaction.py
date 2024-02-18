import requests
import json

from xian_tools.wallet import Wallet
from xian_tools.utils import get_utc_timestamp, decode_dict, decode_int, decode_data
from xian_tools.xian_formating import format_dictionary, check_format_of_payload
from xian_tools.xian_encoding import encode, decode
from typing import Dict, Any


def get_nonce(node_url: str, address: str) -> int:
    """ Return next nonce """
    r = requests.post(f'{node_url}/abci_query?path="/get_next_nonce/{address}"')
    nonce = decode_int(r.json()['result']['response']['value'])
    return nonce


def get_tx(node_url: str, tx_hash: str) -> Dict[str, Any]:
    """ Return transaction with encoded content """
    r = requests.get(f'{node_url}/tx?hash=0x{tx_hash}')
    return r.json()


def decode_tx(tx: Dict[str, Any]) -> Dict[str, Any]:
    """ Return transaction with decoded content """
    if 'result' in tx:
        tx['result']['tx'] = decode_dict(tx['result']['tx'])
        tx['result']['tx_result']['data'] = decode_data(tx['result']['tx_result']['data'])
    return tx


def create_tx(
        contract: str,
        function: str,
        kwargs: Dict[str, Any],
        stamps: int,
        private_key: str,
        nonce: int) -> Dict[str, Any]:
    """ Create transaction to be later broadcast """

    wallet = Wallet(private_key)

    payload = {
        "contract": contract,
        "function": function,
        "kwargs": kwargs,
        "nonce": nonce,
        "sender": wallet.public_key,
        "stamps_supplied": stamps,
    }

    payload = format_dictionary(payload)
    assert check_format_of_payload(payload), "Invalid payload provided!"

    tx = {
        "payload": payload,
        "metadata": {
            "signature": wallet.sign_msg(encode(payload)),
            "timestamp": get_utc_timestamp()
        }
    }

    tx = encode(format_dictionary(tx))
    return json.loads(tx)


def broadcast_tx(node_url: str, tx: Dict[str, Any]) -> Dict[str, Any]:
    """ Broadcast transaction to the network """
    payload = json.dumps(tx).encode().hex()
    r = requests.post(f'{node_url}/broadcast_tx_commit?tx="{payload}"')
    return r.json()
