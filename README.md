# NFTemplateSVG

This project serves as a starting point for building an on-chain SVG NFT with a dynamic renderer, inspired by Dom's Corruption(s*) [contract](https://etherscan.io/address/0x5BDf397bB2912859Dbd8011F320a222f79A28d2E).

The project is built using the Python-based [brownie framework](https://eth-brownie.readthedocs.io/en/stable/).

Once you have brownie installed, run brownie init, and then you can run commands like the following:
- brownie compile (to compile contracts)
- brownie test --gas -vv (to run the tests in the tests/ directory)
- brownie run scripts/gen_svgs.py (to generate SVGs for all tokens and store them in the gen_svgs directory for quick inspection)
