# GardenDAO Forks Wallet Server Side and API Intro

This is documentation of the server-side Forks Wallet system, including its API.

The server will be implemented initially in Python using the light API-friendly framework fastapi (https://github.com/tiangolo/fastapi).

Private keys and seed words are created in the local client, e.g. mobile app or browser extension, and must never be transmitted to or generated by the server.

Blockchain ID: We use the ticker symbol string of characters in lowercase as a blockchain ID, for easy readability. Ref: https://alltheblocks.net/

TODO: API versioning approach, using fastapi?

possible Forks Wallet Server API servicing domain name: api.forkswallet.gardendao.org


## Install

Requires redis, e.g. sudo apt-get install redis

```
git clone https://github.com/GardenDAO/forks-wallet-server-api
# change config.py

pip install -r requirements.txt
uvicorn openapi:app
```


## dev
c. Run python3 -m venv venv to create a virtual environment.

d. Run . ./venv/bin/activate to activate the virtual environment.

e. Run pip install .. This will take a few minutes.

uvicorn openapi:app --reload

point browser to

http://127.0.0.1:8000/

### Response Format

JSON, request & response format, similar approach to Kraken exchange Rest API replies, https://docs.kraken.com/rest/

Response data is in "result". If there were errors in processing request, details are in "errors"

Output listed below will be inside the "result" object.


### GetBalance

Get current balance of a wallet address

    Input
    address: wallet address
    blockchain: blockchain ID (ticker symbol, e.g. "xch", lowercase)
    [ possible future expansion: token list? (optional): default is primary token of the blockchain ]

    Output
      balance: balance of the address on the requested blockchain, amount in integer in unit of lowest denomination of the token, e.g. mojos for xch/chia


### SendTx (POST)

Receive Transaction from client, log as appropriate, submit to the appropriate blockchain network, and return a response code.

    Input
    tx - Transaction Bundle (POST body)
    blockchain - which blockchain to submit the transaction to, blockchain ID (ticker symbol, e.g. "xch", lowercase)

    Output
    status: response from full node client
    id: id if available/relevant
    TBD info: Some blockchain information, like transaction id; error code if error encountered, need to review standard api approach on this quickly again


### GetTx

Given a date range, get all transactions during that range.

    Input
    address: wallet address
    Start Date: Start date of the query
    End Date: End date of the query
    Output
    A list of transactions


[ GetBalances - possibly later]

Get current balance of a list of  wallet addresses

    Input
    addresses: list of wallet addresses
    blockchainID: which blockchain
    [ future expansion: token list (optional): default is primary token of the blockchain ]
    Output
    blockchainID
    balance: dictionary list of balances requested with amounts in integer of lowest denomination of the token, e.g. mojos for XCH { “XCH”: 1000 }
    Rate Limiting
    TBD: at some point look at if rate limiting needs to be looked at

## Adding Support For New Blockchains

TBD: These are the steps for adding support for an additional blockchain / chia fork

    create enum value for Blockchain ID
    integration of api calls to the blockchain’s software
    integration testing



### References/Resources

https://github.com/Chia-Network/chia-dev-tools

https://github.com/Chia-Network/chia-blockchain/wiki/RPC-Interfaces

https://chialisp.com/docs/tutorials/structure_of_a_chia_application


## GobyWallet Thanks

Thanks to the contributions of [Chia Mine](https://github.com/Chia-Mine/clvm-js), MetaMask and DeBank to crypto, we stand on your shoulders to complete this project. (🌱, 🌱)
