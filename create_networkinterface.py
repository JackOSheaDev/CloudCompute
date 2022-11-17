import json

import requests

ip = "https://management.azure.com/subscriptions/9213644b-3b72-4979-bc34-3e01d0eb1fcf/resourceGroups/NewResources/providers/Microsoft.Network/networkInterfaces/TestNetInterfaceB?api-version=2022-05-01"
headers = {"Content-Type": "application/json",
           "Authorization": ""}
body = {
    "properties": {
        "ipConfigurations": [
        {
            "name": "TestNetInterfaceB",
            "properties": {
            "publicIPAddress": {
            "id": "/subscriptions/9213644b-3b72-4979-bc34-3e01d0eb1fcf/resourceGroups/NewResources/providers/Microsoft.Network/publicIPAddresses/TestIPAddressB"
            },
        "subnet": {
        "id": "/subscriptions/9213644b-3b72-4979-bc34-3e01d0eb1fcf/resourceGroups/NewResources/providers/Microsoft.Network/virtualNetworks/TestSubnet/subnets/default"
        }
        }
        }
    ]
    },
    "location": "uksouth"


}

query = requests.put(ip,data=json.dumps(body),headers=headers)


print(query.status_code)
print(query.text)