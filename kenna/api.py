import requests
import encodings
import re

class Asset:

    def __init__(self, id, hostname, ip_addr, tags, ports, time_created, time_last_seen):
        self.id = id
        self.hostname = hostname
        self.ip_addr = ip_addr
        self.tags = tags
        self.ports = ports
        self.time_created = time_created
        self.time_last_seen = time_last_seen

class KennaAPI:

    def __init__(self, api_key):
        self.api_key = api_key
        #print(self.api_key)

    def getCVEHistory(self, cve_id):
        url = "https://api.kennasecurity.com/vulnerability_definitions/history?cve={}".format(cve_id)
        headers = {
            "X-Risk-Token": self.api_key,
            "Content-Type": "application/json"
        }
        print(headers)
        response = requests.get(url, headers=headers )
        print(response.json())
        return response

    def getInfoForALlAssets(self): 
        url = "https://api.kennasecurity.com/vulnerability_definitions/history"
        headers = {
            "X-Risk-Token": self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers )

        pass

    def downloadVulnerabilities(self):
        pass

    def downloadAssets(self):
        pass

    def searchAssets(self, search_param):
        url = "https://api.kennasecurity.com/assets/search?status[]=active&tags[]=foo&tags[]=bar"
        headers = {
            "X-Risk-Token": self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers )
        return response
        pass

    def validateAssetSearchQuery(self, search_param):
        pass

    def showAsset(self, asset_id):
        pass

    def createAsset(self, asset_attr):
        pass

    def updateAsset(self, asset_id, asset_attr):
        pass

    def getAssetVulnerabilities(self, asset_id):
        pass

    def getAssetTags(self, asset_id):
        pass

    def tagAnAsset(self, asset_id):
        pass

    def untagAnAsset(self, asset_id):
        pass

    def listAssetGroups(self):
        pass

    def showAssetGrooup(self, assetg_id):
        pass

    def getAssetGroupFixes(self, assetg_id):
        pass

    def getAssetGroupTopFixes(self, assetg_id):
        pass

    def createAssetGroup(self, ag_params):
        pass

    def updateAssetGroup(self, assetg_id, ag_params):
        pass

    def deleteAssetGroup(self, assetg_id):
        pass

    def getInfoForAllVulnerabilities(self): # get information from all vulnerabilities
        pass

    def searchVulnerabilities(self, search_param):
        pass

    def validateVulnerabilitySearchQuery(self, search_param):
        pass

    def showVulnerability(self, vulnerability_id):
        pass

    def createVulnerability(self, vulnerability_attr):
        pass

    def updateVulnerability(self, vulnerability_id, vulnerability_attr):
        pass

    def getInfoForAllFixes(self): # get information from all fixes
        pass

    def searchFixes(self, search_param):
        pass

    def showFix(self, vulnerability_id):
        pass


class AppTools:

    def isValidIPv4Address(self, ip_address):
        regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
        if type(ip_address) != str :
            print("data type is not valid")
            return False
        if re.search(regex, ip_address, re.IGNORECASE):
            return True
        else:
            return False

    def isInternalIPv4(self):
        return False

    def isValidCVENumber(self,cve_id):
        if type(cve_id) != str :
            print("data type is not valid")
            return False

        if re.search(r"^CVE\-[0-9][0-9][0-9][0-9]\-[0-9][0-9][0-9][0-9][0-9]?", cve_id, re.IGNORECASE):
            return True
        else:
            return False

    def urlEncodeSearchPattern(self, search_patern):
        url_pattern = None
        return url_pattern