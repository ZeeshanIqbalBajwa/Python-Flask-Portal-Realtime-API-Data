pseudoObj={
            "nodes": [
                {
                    "nodeId": "cec1b4b6-947d-40c0-8336-e74ee8a2014b",
                    "nodeType": "RAN",
                    "nodeName": "RGW1",
                    "domainId": "",
                    "datacenter": "",
                    "nodeExternalId": "",
                    "nodeSystemIpAddress": {
                        "ipv4Prefix": {
                            "string": "10.85.185.52"
                        },
                        "ipv6Prefix": ""
                    },
                    "endpoints": [
                        {
                            "epId": "17b133d9-12a6-48bb-9200-3483818247a6",
                            "epName": "ens224",
                            "epExternalId": ""
                        }
                    ]
                },
                {
                    "nodeId": "78ad7dfd-ba87-4355-8b56-7c7e2a7e14b2",
                    "nodeType": "RAN",
                    "nodeName": "RAN2",
                    "domainId": "",
                    "datacenter": "",
                    "nodeExternalId": "",
                    "nodeSystemIpAddress": {
                        "ipv4Prefix": {
                            "string": "10.85.185.53"
                        },
                        "ipv6Prefix": ""
                    },
                    "endpoints": [
                        {
                            "epId": "93d43b9e-1d7d-44cb-b99b-c809f4f8ffcb",
                            "epName": "ens224",
                            "epExternalId": ""
                        }
                    ]
                },
                {
                    "nodeId": "82ba0653-1bb2-436a-94f6-5dac9d0d40b9",
                    "nodeType": "PON",
                    "nodeName": "GPON_ONT3",
                    "domainId": "",
                    "datacenter": "",
                    "nodeExternalId": "",
                    "nodeSystemIpAddress": {
                        "ipv4Prefix": {
                            "string": "10.85.185.61"
                        },
                        "ipv6Prefix": ""
                    },
                    "endpoints": [
                        {
                            "epId": "3cf083bf-7bc4-47a3-be0a-4e3a5f098494",
                            "epName": "LAN1",
                            "epExternalId": ""
                        }
                    ]
                },
                {
                    "nodeId": "5154bace-f49a-47f4-b871-89b8fc9391ba",
                    "nodeType": "PON",
                    "nodeName": "XGS_ONT2",
                    "domainId": "",
                    "datacenter": "",
                    "nodeExternalId": "",
                    "nodeSystemIpAddress": {
                        "ipv4Prefix": {
                            "string": "10.85.185.62"
                        },
                        "ipv6Prefix": ""
                    },
                    "endpoints": [
                        {
                            "epId": "cbd2f250-e669-4fdb-9a18-d4b392ff10b9",
                            "epName": "10GE",
                            "epExternalId": ""
                        }
                    ]
                },
                {
                    "nodeId": "56e8d52d-4938-4b1a-b6bf-329ca7e6f2aa",
                    "nodeType": "PON",
                    "nodeName": "LS-MF2",
                    "domainId": "",
                    "datacenter": "",
                    "nodeExternalId": "",
                    "nodeSystemIpAddress": {
                        "ipv4Prefix": {
                            "string": "10.85.185.63"
                        },
                        "ipv6Prefix": ""
                    },
                    "endpoints": [
                        {
                            "epId": "de439409-33e6-469d-a86a-e95630707563",
                            "epName": "LAG-10",
                            "epExternalId": ""
                        }
                    ]
                },
                {
                    "nodeId": "46d40198-aa77-491e-a7e8-d62663bbcc37",
                    "nodeType": "BR",
                    "nodeName": "IXR-s-1",
                    "domainId": "",
                    "datacenter": "",
                    "nodeExternalId": "",
                    "nodeSystemIpAddress": {
                        "ipv4Prefix": {
                            "string": "10.85.185.26"
                        },
                        "ipv6Prefix": ""
                    },
                    "endpoints": [
                        {
                            "epId": "7277b73b-a8b0-43e8-91b6-1067267160db",
                            "epName": "Lag 1",
                            "epExternalId": "2095-b0f1d16a-d637-4b5d-958b-4e48c932ef90"
                        }
                    ]
                },
                {
                    "nodeId": "8f940557-1287-45c8-bdc8-03fb45338790",
                    "nodeType": "BR",
                    "nodeName": "SR-1-3",
                    "domainId": "",
                    "datacenter": "",
                    "nodeExternalId": "",
                    "nodeSystemIpAddress": {
                        "ipv4Prefix": {
                            "string": "10.85.185.60"
                        },
                        "ipv6Prefix": ""
                    },
                    "endpoints": [
                        {
                            "epId": "725d12f1-af47-4306-98d1-95861a0435cb",
                            "epName": "Lag 1",
                            "epExternalId": "1246-71143a7c-a1dd-47b3-b36c-c1af8b69e6a9"
                        }
                    ]
                },
                {
                    "nodeId": "30a4afe2-528c-4af0-b1d3-6976ad7067ac",
                    "nodeType": "CORE",
                    "nodeName": "UPF1",
                    "domainId": "",
                    "datacenter": "",
                    "nodeExternalId": "",
                    "nodeSystemIpAddress": {
                        "ipv4Prefix": {
                            "string": "10.85.185.30"
                        },
                        "ipv6Prefix": ""
                    },
                    "endpoints": [
                        {
                            "epId": "ad0b8079-a54c-4562-ab21-944060dd0d1b",
                            "epName": "eno1",
                            "epExternalId": ""
                        }
                    ]
                }
            ],
            "links": [
                {
                    "linkId": "200d6788-3216-47d8-8738-b8d1c8cd2ceb",
                    "linkName": "",
                    "sourceEndpoint": {
                        "nodeId": "56e8d52d-4938-4b1a-b6bf-329ca7e6f2aa",
                        "epId": "de439409-33e6-469d-a86a-e95630707563",
                        "nodeSystemIp": "10.85.185.63",
                        "epName": "LAG-10"
                    },
                    "destinationEndpoint": {
                        "nodeId": "46d40198-aa77-491e-a7e8-d62663bbcc37",
                        "epId": "7277b73b-a8b0-43e8-91b6-1067267160db",
                        "nodeSystemIp": "10.85.185.26",
                        "epName": "Lag 1"
                    }
                },
                {
                    "linkId": "10de0725-5ffa-4436-8d61-8b0770a91add",
                    "linkName": "",
                    "sourceEndpoint": {
                        "nodeId": "30a4afe2-528c-4af0-b1d3-6976ad7067ac",
                        "epId": "ad0b8079-a54c-4562-ab21-944060dd0d1b",
                        "nodeSystemIp": "10.85.185.30",
                        "epName": "eno1"
                    },
                    "destinationEndpoint": {
                        "nodeId": "8f940557-1287-45c8-bdc8-03fb45338790",
                        "epId": "725d12f1-af47-4306-98d1-95861a0435cb",
                        "nodeSystemIp": "10.85.185.60",
                        "epName": "Lag 1"
                    }
                },
                {
                    "linkId": "aee79cdf-3088-46ec-86bb-8f2ed05be0d6",
                    "linkName": "",
                    "sourceEndpoint": {
                        "nodeId": "cec1b4b6-947d-40c0-8336-e74ee8a2014b",
                        "epId": "17b133d9-12a6-48bb-9200-3483818247a6",
                        "nodeSystemIp": "10.85.185.52",
                        "epName": "ens224"
                    },
                    "destinationEndpoint": {
                        "nodeId": "82ba0653-1bb2-436a-94f6-5dac9d0d40b9",
                        "epId": "3cf083bf-7bc4-47a3-be0a-4e3a5f098494",
                        "nodeSystemIp": "10.85.185.61",
                        "epName": "LAN1"
                    }
                },
                {
                    "linkId": "3907d09c-b5c0-4041-9fd7-e69205ce2594",
                    "linkName": "",
                    "sourceEndpoint": {
                        "nodeId": "78ad7dfd-ba87-4355-8b56-7c7e2a7e14b2",
                        "epId": "93d43b9e-1d7d-44cb-b99b-c809f4f8ffcb",
                        "nodeSystemIp": "10.85.185.53",
                        "epName": "ens224"
                    },
                    "destinationEndpoint": {
                        "nodeId": "5154bace-f49a-47f4-b871-89b8fc9391ba",
                        "epId": "cbd2f250-e669-4fdb-9a18-d4b392ff10b9",
                        "nodeSystemIp": "10.85.185.62",
                        "epName": "10GE"
                    }
                }
            ]
        }


























