import json

import requests

ip = "https://management.azure.com/subscriptions/9213644b-3b72-4979-bc34-3e01d0eb1fcf/resourceGroups/NewResources/providers/Microsoft.Compute/virtualMachines/TestVMB?api-version=2022-08-01"
headers = {"Content-Type": "application/json",
           "Authorization": ""}
body = {
    "id": "/subscriptions/9213644b-3b72-4979-bc34-3e01d0eb1fcf/resourceGroups/NewResources/providers/Microsoft.Compute/virtualMachines/TestVMB",
    "type": "Microsoft.Compute/virtualMachines",
    "properties": {
    "osProfile": {
    "adminUsername": "jackosheadev",
    "secrets": [
    ],
    "computerName": "TestVMB",
    "linuxConfiguration": {
    "ssh": {
    "publicKeys": [
    {
    "path": "/home/jackosheadev/.ssh/authorized_keys",
    "keyData": ""
    }
    ]
    },
    "disablePasswordAuthentication": True
    }
    },
    "networkProfile": {
    "networkInterfaces": [
    {
    "id": "/subscriptions/9213644b-3b72-4979-bc34-3e01d0eb1fcf/resourceGroups/NewResources/providers/Microsoft.Network/networkInterfaces/TestNetInterfaceB",
    "properties": {
    "primary": True
    }
    }
    ]
    },
    "storageProfile": {
    "imageReference": {
    "sku": "16.04-LTS",
    "publisher": "Canonical",
    "version": "latest",
    "offer": "UbuntuServer"
    },
    "dataDisks": [
    ]
    },
    "hardwareProfile": {
    "vmSize": "Standard_D1_v2"
    },
    "provisioningState": "Creating"
    },
    "name": "TestVMB",
    "location": "uksouth"
}

query = requests.put(ip,data=json.dumps(body),headers=headers)

print(query.status_code)
print(query.text)