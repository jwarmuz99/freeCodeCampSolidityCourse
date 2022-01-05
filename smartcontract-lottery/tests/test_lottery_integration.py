from brownie import accounts, network, Lottery, config, exceptions
from scripts.deploy_lottery import deploy_lottery
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    fund_with_link,
)
import time
import pytest


def test_can_pick_winner():
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    lottery.startLottery({"from": account})
    lottery.enter(
        {"from": account, "value": lottery.getEntranceFee(), "allow_revert": True}
    )
    lottery.enter(
        {"from": account, "value": lottery.getEntranceFee(), "allow_revert": True}
    )
    # Act
    fund_with_link(lottery)
    lottery.endLottery({"from": account})
    time.sleep(60)
    # Assert
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0
