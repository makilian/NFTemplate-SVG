from brownie import NFTemplateSVG, NFTemplateSVGMetadata, NFTemplateSVGMetadata2, accounts, config, network
import json
import base64
import time
import os

def main():

	dev = accounts[0]
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

	for i in range(0, nft.maxSupply()):
		tx = nft.mint({"from":dev, "amount":1e15})
		tx.wait(1)

	for i in range(0, nft.totalSupply()):
		t = nft.tokenURI(i)
		decoded = base64.b64decode(t[29:])
		tokenURIJson = json.loads(decoded)
		a = tokenURIJson['image'][26:]
		svg_bytes = base64.b64decode(a)

		file_name = './token_svgs/token' + str(i) + '.svg'
		os.makedirs(os.path.dirname(file_name), exist_ok=True)
		with open(file_name, "w") as f:
		    f.write(svg_bytes.decode('utf-8'))

	time.sleep(5)

	nft_m_2 = NFTemplateSVGMetadata2.deploy(
		{"from": dev},
		publish_source = publish_source
	)
	tx = nft.setMetadataAddress(nft_m_2, {"from":dev})
	tx.wait(1)

	for i in range(50, nft.totalSupply()):
		t = nft.tokenURI(i)
		decoded = base64.b64decode(t[29:])
		tokenURIJson = json.loads(decoded)
		a = tokenURIJson['image'][26:]
		svg_bytes = base64.b64decode(a)

		file_name = './token_svgs/token' + str(i) + '.svg'
		os.makedirs(os.path.dirname(file_name), exist_ok=True)
		with open(file_name, "w") as f:
		    f.write(svg_bytes.decode('utf-8'))