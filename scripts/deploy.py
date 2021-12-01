from brownie import NFTemplateSVG, accounts, network, config

def main():
	dev = accounts.add(config['wallets']['from_key'])
	print(network.show_active())
	publish_source = False
	cypher = NFTemplateSVG.deploy(
		{"from": dev},
		publish_source = publish_source
	)
	return cypher