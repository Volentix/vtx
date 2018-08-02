#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
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
import sys
home = os.environ['HOME'] 
os.environ['EOS_SOURCE'] = home + "/eos"

def createTokenObject(issuer, maximumsupply):
    tokenObject = {'issuer':issuer,'maximum_supply': maximumsupply}
    return tokenObject

def getCode(accountname):
    out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '--url', 'https://api.eosnewyork.io:443', 'get', 'code', accountname])
    
def getActions(accountname):
    out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '--url', 'https://api.eosnewyork.io:443','get', 'actions', accountname])   
    self.getInfoLabel.setText(out)
    
def setContractSteps(accountname): 
    out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '--url', 'https://api.eosnewyork.io:443', 'set', 'contract', accountname, os.environ['EOS_SOURCE'] + '/build/contracts/eosio.token'])
    
def createCurrency(accountname, tokenobject):
    tokenObject = json.dumps(tokenObject)
    out = subprocess.check_output(['/usr/local/eosio/bin/cleos', '--url', 'https://api.eosnewyork.io:443', 'push', 'action', 'create', tokenobject, '-p', accountname]) 

if __name__ == '__main__':
    accountname = input('Issuer name: ')
    currencyTotal = input('Amount and currency to create (ex.100000 EOS): ')
    tokenObject = createTokenObject(accountname, currencyTotal)
    setContractSteps(accountname)
    createCurrency(accountname, tokenObject)
