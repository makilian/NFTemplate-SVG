from brownie import NFTemplateSVG, accounts, config, network

def main():
	dev = accounts.add(config['wallets']['from_key'])
	dev2 = accounts.add(config['wallets']['from_key_2'])

	nft = NFTemplateSVG[len(NFTemplateSVG) - 1]

	for i in range(0, nft.maxSupply()):
		tx = nft.mint({"from":dev, "amount":1e15})
		tx.wait(1)