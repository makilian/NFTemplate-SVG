import pytest
import brownie
from brownie import NFTemplateSVG, NFTemplateSVGMetadata, NFTemplateSVGMetadata2, accounts, config, network
import time
import json
import base64

def test_mints():
    dev = accounts[0]
    dev2 = accounts[1]
    dev3 = accounts[2]
    dev4 = accounts[3]

    publish_source = False
    
    nft_m = NFTemplateSVGMetadata.deploy(
        {"from": dev},
        publish_source = publish_source
    )

    nft = NFTemplateSVG.deploy(
        {"from": dev},
        publish_source = publish_source
    )

    print(nft_m)

    transaction = nft.setMetadataAddress(nft_m, {"from":dev})
    transaction.wait(1)


    transaction = nft.mint( 
       {"from":dev, "amount":1e15})
    transaction.wait(1)
    assert nft.totalSupply() == 1
    assert nft.tokenURI(1)

    transaction = nft.mint( 
        {"from":dev2, "amount":1e15})
    transaction.wait(1)

    assert nft.totalSupply() == 2
    assert nft.tokenURI(2)

    transaction = nft.mint( 
        {"from":dev, "amount":1e15})
    transaction.wait(1)
    assert nft.totalSupply() == 3
    assert nft.tokenURI(3)

    transaction = nft.mint( 
        {"from":dev2, "amount":1e15})
    transaction.wait(1)
    assert nft.totalSupply() == 4
    assert nft.tokenURI(4)

    transaction = nft.mint( 
        {"from":dev, "amount":1e15})
    transaction.wait(1)
    assert nft.totalSupply() == 5
    assert nft.tokenURI(5)

    transaction = nft.mint( 
        {"from":dev2, "amount":1e15})
    transaction.wait(1)
    assert nft.totalSupply() == 6
    assert nft.tokenURI(6)

    transaction = nft.mint( 
        {"from":dev3, "amount":1e15})
    transaction.wait(1)
    assert nft.totalSupply() == 7
    assert nft.tokenURI(7)

    t = nft.tokenURI(7)
    decoded = base64.b64decode(t[29:])
    tokenURIJson = json.loads(decoded)

    assert int(tokenURIJson['attributes'][0]['value']) <= 10

    a = tokenURIJson['image'][26:]
    svg_bytes = base64.b64decode(a)
    utf = svg_bytes.decode('utf-8')
        
    assert '<text x="0" y="100" fill="white">NFTemplate SVG:' in utf

    with brownie.reverts("Template: 0.001 ETH to mint"):
        transaction = nft.mint( 
        {"from":dev, "amount":5e15})

    start_bal = dev.balance()
    transaction = nft.withdrawAll({"from":dev})
    transaction.wait(1)
    assert dev.balance() - 7*1e15 == start_bal

    with brownie.reverts("Ownable: caller is not the owner"):
        transaction = nft.withdrawAll({"from":dev2})

    nft_m_2 = NFTemplateSVGMetadata2.deploy(
        {"from": dev},
        publish_source = publish_source
    )

    transaction = nft.setMetadataAddress(nft_m_2, {"from":dev})
    transaction.wait(1)

    t = nft.tokenURI(7)
    decoded = base64.b64decode(t[29:])
    tokenURIJson = json.loads(decoded)

    assert int(tokenURIJson['attributes'][0]['value']) <= 10

    a = tokenURIJson['image'][26:]
    svg_bytes = base64.b64decode(a)
    utf = svg_bytes.decode('utf-8')
        
    assert '<text x="0" y="100" fill="black">NFTemplate SVG:' in utf
