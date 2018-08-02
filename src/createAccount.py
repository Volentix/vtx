#############################################################################
# MIT License
#
# Copyright (c) 2018 Volentix Labs
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#############################################################################

# Author
# Sylvain Cormier sylvain@volentixlabs.com/sylvaincormier@protonmail.com
import subprocess
import os

class BlockChain():
    def __init__(self):
        self.producer = "https://api.eosnewyork.io:443"
        
class Account():
    def __init__(self):
        self.name = ""
        self.creator = ""
        self.receiver = ""
        self.creatorOwnerKey = ""
        self.creatorActiveKey = ""
#         self.eosioPublicKey = "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"
#         self.eosioPrivateKey = "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"
        self.cpu = ""
        self.bandwidth = ""
        self.ram = "" 

class Wallet():
    def __init__(self):
        self.name = ""
        self.key = ""
        self.ownerPrivateKey = ''
        self.ownerPublicKey = ''
        self.activePrivateKey = ''
        self.activePublicKey = ''
         
    def erasePrivateKeys(self):
        self.ownerPrivateKey = ""
        self.activePrivateKey = ""
        
def setOwnerKeys(wallet):    
    out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'create', 'key'])
    key = out[13:]
    key = key[:-67]
    key2 = out[77:]
    key2 = key2[:-1]
    wallet.ownerPrivateKey= key
    wallet.ownerPublicKey = key2
    print('Owner keys set')
       

def setActiveKeys(wallet):
    out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'create', 'key'])
    key = out[13:]
    key = key[:-67]
    key2 = out[77:]
    key2 = key2[:-1]
    wallet.activePrivateKey = key
    wallet.activePublicKey = key2
    print('Active keys set')
    
def importKeys(wallet):
    print(wallet.activePrivateKey)
    print('\n')
    print(wallet.ownerPrivateKey)
    out = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'wallet', 'import', '-n', wallet.name, '--private-key', wallet.ownerPrivateKey])
    print(out)
    out1 = subprocess.check_output(['/usr/local/eosio/bin/cleos', 'wallet', 'import', '-n', wallet.name, '--private-key', wallet.activePrivateKey])
    print(out)
    wallet.erasePrivateKeys()

def createWallet(name):
    walletDirectory = os.environ['HOME'] + '/eosio-wallet'
    if not os.path.exists(walletDirectory):
        os.makedirs(walletDirectory )
    out = subprocess.check_output(['/usr/local/eosio/bin/cleos','wallet', 'create', '-n', name])
    return out 

def createAccount(producer, creator, name, permission, bandwidth, cpu, ram, ownerPublicKey, activePublicKey):
    out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '-u', producer, 'system', 'newaccount', creator, name, ownerPublicKey, activePublicKey, '--stake-net', bandwidth, '--stake-cpu', cpu, '--buy-ram', ram, '--transfer', '-p', permission])
    return out

if __name__ == '__main__':
    account = Account()
    wallet = Wallet()
    blockchain = BlockChain()
    text = input("Name of the account to create ex.11volentix11:")
    wallet.name = text
    out = createWallet(wallet.name)
    print('****************************Private Key*************************')
    print(out)
    print('****************************************************************')
    condition = input('I have saved the key to this wallet in a proper place y/n')
    if condition == 'n':
         exit()
    setOwnerKeys(wallet)
    setActiveKeys(wallet)
    importKeys(wallet)
    account.name = wallet.name 
    account.creator = input("Name of the creating account ex.volentixtst2:")
    account.bandwidth = input("Amount of bandwidth ex. 0.0001 EOS:")
    account.cpu = input("Amount of cpu  ex. 0.0001 EOS:")    
    account.ram = input("Amount of ram  ex. 0.0001 EOS:")
    permission = account.creator + '@active'
#     print(blockchain.producer, account.name, account.bandwidth, account.cpu, account.ram, wallet.ownerPublicKey, wallet.activePublicKey)
    createAccount(blockchain.producer, account.creator, account.name, permission, account.bandwidth, account.cpu, account.ram, wallet.ownerPublicKey, wallet.activePublicKey)
