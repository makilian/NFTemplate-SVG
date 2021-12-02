# NFTemplateSVG

This project serves as a starting point for building an on-chain SVG NFT with a dynamic renderer, inspired by Dom's Corruption(s*) [contract](https://etherscan.io/address/0x5BDf397bB2912859Dbd8011F320a222f79A28d2E).

The contracts are written in solidity, and the scripts use the Python-based [brownie framework](https://eth-brownie.readthedocs.io/en/stable/) to interact with the smart contracts.

Once you have brownie installed and environment variables configured, run brownie init, and then you can run commands such as:
- brownie compile (to compile contracts)
- brownie test --gas -vv (to run the tests in the tests/ directory)
- brownie run scripts/gen_svgs.py (to generate SVGs for all tokens and store in ./token_svgs, upgrade contract to second rendering contract and regenerates the second half of the tokens in ./token_svgs using the new rendering contract)
