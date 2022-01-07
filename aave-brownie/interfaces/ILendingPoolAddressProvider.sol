// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

interface ILendingPoolAddressProvider {
    function getLendingPool() external view returns (address);
}