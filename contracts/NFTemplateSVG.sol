pragma solidity ^0.8.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "./Base64.sol";
import "./NFTemplateSVGMetadata.sol";

/**
       NFTemplateSVG.sol
**/

contract NFTemplateSVG is ERC721, ReentrancyGuard, Ownable {
    uint256 public totalSupply;
    uint256 public constant maxSupply = 100;
    address public metadataAddress;
    
    constructor() public ERC721("NFTemplateSVG", "TEMPLATE") Ownable() { 
    }

    function mint() payable external nonReentrant {
        require(totalSupply < maxSupply, 'Template: all blocks minted');
        require(msg.value == 0.001 ether, "Template: 0.001 ETH to mint");
        _mint(msg.sender, ++totalSupply);
    }

    function traitValue(uint256 tokenId) public view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(tokenId))) % 10;
    }

    function setMetadataAddress(address addr) public onlyOwner {
        metadataAddress = addr;
    }

    function withdrawAll() public payable onlyOwner {
        require(payable(_msgSender()).send(address(this).balance));
    }

    function tokenURI(uint256 tokenID) override public view returns (string memory) {
        require(metadataAddress != address(0), "NFTemplateSVG: no metadata address");
        require(tokenID < maxSupply, "NFTemplateSVG: token doesn't exist");
        return INFTemplateSVGMetadata(metadataAddress).tokenURI(tokenID, traitValue(tokenID));
    }           
}
