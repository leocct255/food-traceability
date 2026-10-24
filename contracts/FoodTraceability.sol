// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract FoodTraceability {

    uint256 public nextBatchId = 1;

    mapping(uint256 => string) public batchNames;
    mapping(uint256 => string) public batchProducers;
    mapping(uint256 => string) public batchOrigins;
    mapping(uint256 => uint256) public batchTimestamps;
    mapping(uint256 => address) public batchOwners;
	
    function registerBatch(
        string memory _name,
        string memory _producer,
        string memory _origin
    ) public {
	

	 // Validate that all fields are filled
        require(bytes(_name).length > 0, "Food name is required");
        require(bytes(_producer).length > 0, "Producer is required");
        require(bytes(_origin).length > 0, "Origin is required");

        
        uint256 id = nextBatchId;
	batchOwners[id] = msg.sender;

        
        batchNames[id] = _name;
        batchProducers[id] = _producer;
        batchOrigins[id] = _origin;
        batchTimestamps[id] = block.timestamp;

        nextBatchId++;
    }

function transferBatch(uint256 _batchId, address _newOwner) public {
    require(_batchId > 0 && _batchId < nextBatchId, "Batch does not exist");

    require(
        batchOwners[_batchId] == msg.sender,
        "Only the current owner can transfer this batch"
    );

    require(_newOwner != address(0), "Invalid receiver address");
    require(_newOwner != msg.sender, "Receiver must be different");

    batchOwners[_batchId] = _newOwner;
}
}
