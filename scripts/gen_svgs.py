from brownie import NFTemplateSVG, accounts, config, network
import json
import base64

def main():

	dev = accounts[0]
	print(network.show_active())
	publish_source = False
	nft = NFTemplateSVG.deploy(
		{"from": dev},
		publish_source = publish_source
	)

	for i in range(0, nft.maxSupply()):
		tx = nft.mint({"from":dev, "amount":1e15})
		tx.wait(1)

	for i in range(0, nft.totalSupply()+1):
		t = nft.tokenURI(i)
		decoded = base64.b64decode(t[29:])
		tokenURIJson = json.loads(decoded)
		a = tokenURIJson['image'][26:]
		svg_bytes = base64.b64decode(a)

		file_name = './token_svgs/token' + str(i) + '.svg'
		with open(file_name, 'w') as f:
			f.write(svg_bytes.decode('utf-8'))