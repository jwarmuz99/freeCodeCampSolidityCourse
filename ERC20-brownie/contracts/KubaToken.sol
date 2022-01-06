// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract KubaToken is ERC20, ERC20Burnable, Ownable {
    //add minter variable
    address public minter;

    constructor(uint256 initialSupply) ERC20("KubaToken", "QBA") {
        minter = msg.sender;
        _mint(minter, initialSupply);
    }

    function mint(address to, uint256 amount) public onlyOwner {
        require(msg.sender==minter, 'Error, msg.sender does not have minter role');
        _mint(to, amount);
    }
}