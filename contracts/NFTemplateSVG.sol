pragma solidity 0.8.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "./Base64.sol";

/**
       NFTemplateSVG.sol
**/

contract NFTemplateSVG is ERC721, ReentrancyGuard, Ownable {
    uint256 public totalSupply;
    uint256 public constant maxSupply = 100;
    
    constructor() public ERC721("NFTemplateSVG", "TEMPLATE") Ownable() { 
    }

    function mint() payable external nonReentrant {
        require(totalSupply < maxSupply, 'Template: all blocks minted');
        require(msg.value == 0.001 ether, "Template: 0.001 ETH to mint");
        _mint(msg.sender, ++totalSupply);
    }

    function withdrawAll() public payable onlyOwner {
        require(payable(_msgSender()).send(address(this).balance));
    }

    function tokenURI(uint256 tokenId) public override view returns(string memory) {
        string memory json = Base64.encode(bytes(string(abi.encodePacked(
            '{"name": "', 
            Strings.toString(tokenId), 
            '", "description": "', 
            'This is a template for SVG NFTs.', 
            '", "image": "data:image/svg+xml;base64,', 
            Base64.encode(drawSVG(tokenId)), 
            '", "attributes": [{"trait_type": "Template Trait Random", "value": "', 
            Strings.toString(uint256(keccak256(abi.encodePacked(tokenId))) % 10), 
            '"}]}'))));
        
        return string(abi.encodePacked("data:application/json;base64,", json));
    } 

    function drawSVG(uint256 tokenId) internal view returns (bytes memory) {
        string[8] memory parts;
        parts[0] = '<svg version="1.1" shape-rendering="optimizeSpeed" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"';
        parts[1] = ' x="0px" y="0px" viewBox="0 0 1000 1000" xml:space="preserve">';
        parts[2] = styles();
        parts[3] = '<rect x="0" y="0" fill="black"></rect>';
        parts[4] = '<text x="0" y="100" fill="white">NFTemplate SVG: ';
        parts[5] = Strings.toString(tokenId);
        parts[6] = '</text>';
        parts[7] = '</svg>';

        return abi.encodePacked(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]);
    }

    function styles() internal view returns (string memory) {   
        bytes memory stylesMarkup = abi.encodePacked(
            '<style type="text/css">', 
            'rect{width: 1000px; height: 1000px;}text{font-size: 100px; alignment-baseline:text-after-edge}',
            '</style>');
        return string(stylesMarkup);
    }                
}
    