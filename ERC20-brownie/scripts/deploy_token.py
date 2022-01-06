from scripts.helpful_scripts import get_account, INITIAL_SUPPLY
from brownie import KubaToken, network, config
from web3 import Web3


def deploy_token():
    account = get_account()
    token = KubaToken.deploy(
        INITIAL_SUPPLY,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    return token


def mint_tokens():
    account = get_account()
    token = KubaToken[-1]
    minting_tx = token.mint(account, INITIAL_SUPPLY, {"from": account})
    minting_tx.wait(1)
    print("Minted some tokens and funded the account!")


"""
This will not work on testnet because I do not have another account linked
def mint_to_new_account():
    account = get_account()
    account2 = get_account(index=1)
    token = KubaToken[-1]
    minting_tx = token.mint(account2, INITIAL_SUPPLY, {"from": account})
    minting_tx.wait(1)
    print("Minted some tokens and sent them to a new account!")
"""


def main():
    deploy_token()
    mint_tokens()
    # mint_to_new_account()
