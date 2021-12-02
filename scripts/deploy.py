from brownie import NFTemplateSVG, NFTemplateSVGMetadata, accounts, network, config

def main():
	dev = accounts.add(config['wallets']['from_key'])
	print(network.show_active())
	publish_source = False

	nft_m = NFTemplateSVGMetadata.deploy(
        {"from": dev},
        publish_source = publish_source
    )

	nft = NFTemplateSVG.deploy(
		{"from": dev},
		publish_source = publish_source
	)

	tx = nft.setMetadataAddress(nft_m, {"from":dev})
	tx.wait(1)

	return nft