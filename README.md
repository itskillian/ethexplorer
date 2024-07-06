# web3 portfolio project

Allows users to search for an Ethereum address to retrive its balance. Also provides real-time gas prices and the current ETH/USD price

## Features
- Eth address balance
- live Gas price
- live ETH price
- error page

### Technologies Used
- Django
    - use context processors to load Etherscan data into base.html (global) template
    - use Django forms for server side validation
    - use Django URLs for dynamic and clean urls, for example "/address/0x0000000000000000000000000000000000000000" will return the ETH balance of the address 0x0000000000000000000000000000000000000000
- Etherscan API: fetch web3 data
- requests library: handle API calls
- html
- CSS