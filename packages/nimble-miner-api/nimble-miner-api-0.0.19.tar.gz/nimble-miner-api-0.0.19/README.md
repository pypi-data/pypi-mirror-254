# Nimble Miner API

It provides CLI, wallet and other APIs for the miners.

# Development
### Install

```bash
# installer option
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/nimble-technology/nimble-miner-api/master/scripts/install.sh)"

# pip install option
$ pip3 install nimble-miner-api

# from source
$ git clone https://github.com/nimble-technology/nimble-miner-api.git
$ cd nimble-miner-api
$ python3 -m pip install -e ./

# test install from command line
# usage: nbcli <command> <command args>
# commands:
#   subnets (s, subnet) - Commands for managing and viewing subnetworks.
#   root (r, roots) - Commands for managing and viewing the root network.
#   wallet (w, wallets) - Commands for managing and viewing wallets.
#   stake (st, stakes) - Commands for staking and removing stake from hotkey accounts.
#   sudo (su, sudos) - Commands for subnet management.
#   legacy (l) - Miscellaneous commands.
$ nbcli --help

# test install from python
import nimble-miner-api as nimble

# cuda dependency for cubit install - python 3.10 example
pip install https://github.com/nimble-technology/cubit/releases/download/v1.1.2/cubit-1.1.2-cp310-cp310-linux_x86_64.whl
```

# Wallet

Each wallet has a coldkey. Each coldkey may contain multiple hotkeys and each hotkey belong to a single coldkey. Coldkeys are for secure fund management like transfer, staking, and fund storage. Hotkeys are for all online operations like signing, mining and validating.


```bash
# wallet creation in python
import nimble-miner-api as nimble
wallet = nimble.wallet()
wallet.create_new_coldkey()
wallet.create_new_hotkey()
# Sign data with the keypair.
wallet.coldkey.sign( data )

# use nbcli with wallet subcommand or alias w.
$ nbcli wallet new_coldkey
$ nbcli wallet new_hotkey

$ nbcli wallet regen_coldkey --mnemonic **** *** **** **** ***** **** *** **** **** **** ***** *****

# keys are available here: ~/.nimble/wallets
$ nbcli wallet list

# more commands
$ nbcli wallet list
$ nbcli wallet transfer
```

### Release (Admin Only)

Run the following command to create dist folder
```bash
python setup.py sdist
```

Then use the following command to publish to pypi
```bash
twine upload dist/nimble-miner-api-{version}.tar.gz
```
