#!/usr/bin/python

import requests, sys, os
import configparser
import fire 
from kenna.api import * 


def cvehistory(cve_number):
    '''
    Finds vulnerable assets related to teh CVE number 
    '''
    kt = AppTools()
    ka = KennaAPI(kenna_api_key)
    if kt.isValidCVENumber(cve_number): 
        print(cve_number.upper())
        cve=cve_number.upper()
        result=ka.getCVEHistory(cve)
        print(result)
    else:
        print("The CVE number is not valid...")

def summary():
    '''
    Show a summary about Kenna 
    '''
    pass

def assets(search_pattern):
    '''
    Show assets based on a search patten 
    '''
    if search_pattern == None:
        print("Please specify a search pattern")
        sys.exit(1)
    ka = KennaAPI(kenna_api_key)
    result = ka.searchAssets(search_pattern)
    print(result)
    print("assets")
    pass

def asset(key, value):
    '''
    Provide information about the assets based on key and value params.
    
    key : string
        hostname, asset_id, ip 
    value : string
        the value related to key
    '''
    if key == "ip":
        kt = AppTools()
        if kt.isValidIPv4Address(value):
            print(value)
        else:
            print("ss")
    elif key == "hostname":
        print("HOSTNAME")

def search(key, pattern):
    '''
    Searches the pattern in Kenna Platform.
    
    key : string
        asset, vulnerability 
    value : string
        the search pattern used in Kenna search
    '''
    if key == "ip":
        kt = AppTools()
        if kt.isValidIPv4Address(value):
            print(value)
        else:
            print("ss")
    elif key == "hostname":
        print("HOSTNAME")    


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('kenna.config')
    global kenna_api_key
    kenna_api_key = config['KENNA']['api_key']
    fire.Fire()