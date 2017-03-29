#!/usr/bin/env python
import os
import suds
from suds.client import Client

def getDataTest(): 
    try: 
        client = Client('http://127.0.0.1:1242/ASF?wsdl') 
        #print client
        result = client.service.HandleCommand('status')
        return result
    except: 
        return 'error'

print getDataTest();
