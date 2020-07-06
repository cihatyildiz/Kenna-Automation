import requests

class KennaAsset:

    def __init__(self, id, hostname, ip_addr, tags, ports, time_created, time_last_seen):
        self.id = id
        self.hostname = hostname
        self.ip_addr = ip_addr
        self.tags = tags
        self.ports = ports
        self.time_created = time_created
        self.time_last_seen = time_last_seen


class KennaAssetsApp:

    def __init__(self, api_key):
        self.api_key = api_key
    
    def getByAssetId(self, asset_id):
        return

    def searchByCVE(self, cve):
        return

    def searchByHostname(self, hostname):
        return 




        
