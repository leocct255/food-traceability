// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract FoodTraceability {

    uint256 public nextBatchId = 1;

    mapping(uint256 => string) public batchNames;
    mapping(uint256 => string) public batchProducers;
    mapping(uint256 => string) public batchOrigins;
    mapping(uint256 => uint256) public batchTimestamps;

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

        
        batchNames[id] = _name;
        batchProducers[id] = _producer;
        batchOrigins[id] = _origin;
        batchTimestamps[id] = block.timestamp;

        nextBatchId++;
    }
}
