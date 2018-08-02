#!/usr/bin/env python3
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
import json
from collections import OrderedDict

class BlockChain():
    def __init__(self):
        self.producer = "https://api.eosnewyork.io:443"
        

def createMultiSigAccountObject(threshold, weight, actors, permission):
        multiSigObjects = []
        for i in actors:
            multiSigObjects.append(createMultiSigObject(weight, i, permission))
        multiSigAccountObject = {'threshold':threshold, 'keys':[],'accounts':multiSigObjects,"waits":[]}
        return multiSigAccountObject 
    
def createMultiSigObject(weight, actor, permission):
        lPermission = createPermissionObject(actor, permission)        
        multiSigObject = {'permission':lPermission, 'weight':weight}
        multiSigObject = OrderedDict(sorted(multiSigObject.items(), key=lambda t: t[0], reverse=False))
        return multiSigObject
    
def createPermissionObject(actor, permission):
        permissionobject = {'actor':actor,'permission':permission}
        return permissionobject
        
if __name__ == '__main__':
    blockchain = BlockChain()
    actors = []
    for i in range(3):
        actors.append(input("Name of actor number %d: " % (i + 1)))     
    multiSigAccountName = input("Name of the multisig account: ")
    threshold = input("Threshold: ")    
    weight = input("Weight: ")
    multiSigPermissionObject = json.dumps(createMultiSigAccountObject(threshold, weight, actors,'active'))        
    subprocess.check_output(['/usr/local/eosio/bin/cleos', '--url', blockchain.producer, 'set', 'account', 'permission', multiSigAccountName, 'active', multiSigPermissionObject, 'owner', '-p', multiSigAccountName +'@owner']) 
    multiSigPermissionObject = json.dumps(createMultiSigAccountObject(threshold, weight, actors,'owner'))
    out = subprocess.check_output(['/usr/local/eosio/bin/cleos','--url', blockchain.producer, 'set', 'account', 'permission',  multiSigAccountName, 'owner', multiSigPermissionObject, '-p',  multiSigAccountName  +'@owner'])
    print(out)             



        
    