from brownie import accounts, network, KubaToken, config, exceptions
from scripts.deploy_token import deploy_token, INITIAL_SUPPLY
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
)
import time
import pytest


def test_mints_tokens_upon_deployment():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    # Arrange
    token = deploy_token()
    # Act
    initial_supply = token.totalSupply()
    # Assert
    assert initial_supply == INITIAL_SUPPLY


def test_sender_can_mint_tokens():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    # Arrange
    account = get_account()
    token = deploy_token()
    # Act
    token.mint(account, INITIAL_SUPPLY, {"from": account})
    # Assert
    new_supply = token.totalSupply()
    assert new_supply == INITIAL_SUPPLY + INITIAL_SUPPLY


def test_non_sender_cant_mint_tokens():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    # Arrange
    new_account = get_account(index=1)
    token = deploy_token()
    # Act / Assert
    with pytest.raises(exceptions.VirtualMachineError):
        token.mint(new_account, INITIAL_SUPPLY, {"from": new_account})
