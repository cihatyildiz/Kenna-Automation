import requests

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
        print(self.api_key)

    def getCVEHistory(self):
        pass

    def getInfoForALlAssets(self): # get information from all assets
        pass

    def downloadVulnerabilities(self):
        pass

    def downloadAssets(self):
        pass

    def searchAssets(self, search_param):
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

