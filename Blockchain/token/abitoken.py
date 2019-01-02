# -*- coding: utf-8 -*-
def abi():
   abi = [
	{
		"constant": "false",
		"inputs": [
			{
				"name": "cadUn",
				"type": "bytes"
			}
		],
		"name": "revokeConf",
		"outputs": [],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "_spender",
				"type": "address"
			},
			{
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [
			{
				"name": "ok",
				"type": "bool"
			}
		],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "_limit",
				"type": "uint256"
			}
		],
		"name": "changeTransferLimit",
		"outputs": [],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [],
		"name": "retrieveEther",
		"outputs": [],
		"payable": "true",
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "_from",
				"type": "address"
			},
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [
			{
				"name": "ok",
				"type": "bool"
			}
		],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"name": "balances",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [],
		"name": "decimals",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [],
		"name": "initialSupply",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "controllerTransfer",
		"outputs": [],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [],
		"name": "Confreturn",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			},
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "_owner",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"name": "balance",
				"type": "uint256"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "transferToContract",
		"outputs": [],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [
			{
				"name": "ok",
				"type": "bool"
			}
		],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "generateTokens",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "_spender",
				"type": "address"
			},
			{
				"name": "_value",
				"type": "uint256"
			},
			{
				"name": "_extraData",
				"type": "bytes"
			}
		],
		"name": "approveAndCall",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "_objetive",
				"type": "address"
			},
			{
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "destroyTokens",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": "true",
		"inputs": [
			{
				"name": "_owner",
				"type": "address"
			},
			{
				"name": "_spender",
				"type": "address"
			}
		],
		"name": "allowance",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": "false",
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": "false",
		"inputs": [
			{
				"name": "cadEnv",
				"type": "bytes"
			}
		],
		"name": "confirm",
		"outputs": [],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": "false",
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"payable": "true",
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"anonymous": "false",
		"inputs": [
			{
				"indexed": "true",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": "false",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Burn",
		"type": "event"
	},
	{
		"anonymous": "false",
		"inputs": [
			{
				"indexed": "true",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": "true",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": "false",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"anonymous": "false",
		"inputs": [
			{
				"indexed": "true",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": "true",
				"name": "spender",
				"type": "address"
			},
			{
				"indexed": "false",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	}
]
   return(abi)