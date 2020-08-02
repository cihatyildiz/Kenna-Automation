#!/usr/bin/python

import requests, sys, os
import configparser
import fire 

from kenna.assets import *
from kenna.vulns import *

class KennaCliApp:
    '''
    Provide information about the assets based on key and value params.
    
    key : string
        hostname, asset_id, ip 
    value : string
        the value related to key
    '''    

    def __init__(self):
        pass

    def cve(self, cve_number):
        '''
        Search a CVE number in your environment 
        '''
        print("CVE")
        pass

    def assets(self, param=None, value=None):
        '''
        Provide information about all assets
        '''
        print("assets")
        pass

    def asset(self, key, value):
        '''
        Provide information about the assets based on key and value params.
        
        key : string
            hostname, asset_id, ip 
        value : string
            the value related to key
        '''
        pass

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('kenna.config')
    global kenna_api_key
    kenna_api_key = config['KENNA']['api_key']
    fire.Fire(KennaCliApp)