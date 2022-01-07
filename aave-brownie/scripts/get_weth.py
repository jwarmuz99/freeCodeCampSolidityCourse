from scripts.helpful_scripts import get_account
from brownie import interface, config, network


def get_weth():
    """
    Mints WETH by depositing ETH
    """
    account = get_account()
    # alternatively you could use the get_contract() function to replace the line below
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    tx.wait(1)
    return tx


def withdraw_weth():
    """
    Converts WETH to ETH
    """
    account = get_account()
    # alternatively you could use the get_contract() function to replace the line below
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.withdraw({"from": account, "value": 0.1 * 10 ** 18})
    tx.wait(1)
    return tx


def main():
    get_weth()
