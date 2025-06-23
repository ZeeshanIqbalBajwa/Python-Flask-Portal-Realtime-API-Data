import requests
import json
from apps.home.PseudoNodesAndLinks import pseudoObj

# req_token_ip='10.60.90.40'
#req_token_ip='10.198.118.150'
#req_ip_token='135.249.149.52'

#NSP_IP = '135.238.200.236'
# NSP_IP = '10.198.118.150'
NSP_IP = '147.75.102.178'
#TSC_IP = '135.238.200.236'
# TSC_IP = '10.198.118.150'
TSC_IP = '147.75.102.178'
TSC_PORT = '8549'

#SDN_IP = '135.238.200.224'
# SDN_IP = '10.198.118.146'
SDN_IP = '147.75.102.178'

SDN_PORT = '8543'
# req_ip='10.60.90.40:8549'
#req_ip='10.198.118.150:8549'
#req_ip='135.249.149.52:8549'

# req_ip_sdn='10.60.90.44:8543'
#req_ip_sdn='10.198.118.146:8543'
#req_ip_sdn='135.249.149.52:8543'


#proxies = {
        # "http": "138.203.26.244:8443",
        # "https": "138.203.26.244:8443"
#    }

def getToken():
    username='admin'
    password='C7Pmvqc3'
    data={ "grant_type": "client_credentials" }
    url = 'https://'+NSP_IP+'/rest-gateway/rest/api/v1/auth/token'

    payload = json.dumps({
        "grant_type": "client_credentials"
    })

    response=requests.post(url=url,auth=(username,password),json=data,verify=False)
    res=response.json()
    print("token received", res['access_token'], "++status code",response.status_code)

    return res['access_token']

def revokeToken(token):
    token1='Bearer '+token
    basic_token='U0FNcWE6NTYyMFNhbSE='
    url = 'https://' + NSP_IP + '/rest-gateway/rest/api/v1/auth/revocation'

    payload = "token=" + token1 + "&token_type_hint=token"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': 'Basic {}'.format(basic_token)
    }

    print(headers,payload)
    response = requests.post(url=url,headers=headers,data=payload,verify=False)
    print("revoke res",response)
    if response.status_code == 200:
        return True

def getTransportSlice():
    token=getToken()
    url='https://'+TSC_IP+":"+TSC_PORT+'/tsc/api/v4/connectivity/transport-slices/'

    response=requests.get(url=url,headers={'Content-Type': 'application/json',
                                           'Authorization': 'Bearer {}'.format(token)},verify=False)
    list=[]
    print(response.status_code)
    if response.status_code == 401:
        return 401
    print("response received", response)
    if response.status_code == 200:
        response = response.json()
        print("response received", response['response']['data'], "len",len(response['response']['data']))
        if len(response['response']['data']) >= 1:
            # print("response received", response, "++Data", response['response']['data'])
            list=transportSliceRealization(response['response']['data'],token)
    return list


def getRan():
    token = getToken()
    url = 'https://' + TSC_IP + ":" + TSC_PORT + '/tsc/api//v4/link/network'

    response = requests.get(url=url, headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(token)}, verify=False)
    list = []
    if response.status_code == 401:
        return 401
    if response.status_code == 200:
        response = response.json()
        print("response received", response['response']['data']["nodes"])
        for ranlist in response['response']['data']["nodes"]:
            if ranlist['nodeType'] == "RAN":
                list.append(ranlist['nodeName'])
    return list

def getCore():
    token = getToken()
    url = 'https://' + TSC_IP + ":" + TSC_PORT + '/tsc/api//v4/link/network'

    response = requests.get(url=url, headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(token)}, verify=False)
    list = []
    if response.status_code == 401:
        return 401
    if response.status_code == 200:
        response = response.json()
        print("response received", response['response']['data']["nodes"])
        for corelist in response['response']['data']["nodes"]:
            if corelist['nodeType'] == "CORE":
                list.append(corelist['nodeName'])
    return list

def transportSliceRealization(list,token):
    finalList=[]
    for x in list:
        val=getTSRealization(x['transportSlice']['tsId'],token)
        if val == 401:
            return val
        obj = {
            'tsId': x['transportSlice']['tsId'],
            'tsName': x['transportSlice']['tsName'],
            'customerId': val,
            'healthStatus': x['healthStatus'],
            'operStatus': x['operStatus'],
            'token':token,
        }
        finalList.append(obj)

    print("final list TS",finalList)
    return finalList

def getTSRealization(TransportSliceId,token):
    url = 'https://' + TSC_IP+":"+TSC_PORT + '/tsc/api/v4/connectivity/transport-slice-realization/'+TransportSliceId
    result = requests.get(url,
                          headers={'Content-Type': 'application/json',
                                   'Authorization': 'Bearer {}'.format(token)}, verify=False)
    if result.status_code == 401:
        return 401
    res = result.json()
    print("Transport slice response",res)
    res = res['response']['data']['connectionGroupsRealization']['realizationCommonInfo']['networkSlices'][0]['customerId']

    return res


def deleteTransplantSlice(TransportSliceId):
    token=getToken()
    url='https://'+TSC_IP+":"+TSC_PORT+'/tsc/api/v4/connectivity/transport-slices/'+TransportSliceId
    result = requests.delete(url,
                             headers={'Content-Type': 'application/json',
                                      'Authorization': 'Bearer {}'.format(token)},verify=False)
    print(result.status_code,"result",result)
    if result.status_code == 401:
        return 401
    if result.status_code == 202:
        return True

def updateLatecny(linkid,latency):
    token=getToken()
    data={
        "data":{
            "latency":latency
        }
    }
    print("data", json.dumps(data))
    url='https://'+SDN_IP +":"+SDN_PORT+'/sdn/api/v4/nsp/net/l3/link/'+linkid
    print("url",url)
    result = requests.patch(url,
                             headers={'Content-Type': 'application/json',
                                      'Authorization': 'Bearer {}'.format(token)},data=json.dumps(data),verify=False)
    print(result.status_code,"result",result)
    if result.status_code == 401:
        return 401
    if result.status_code == 200:
        return True

def getSelectionPolicy():
    token=getToken()
    url='https://'+TSC_IP+":"+TSC_PORT+'/tsc/api/v4/policy/transport-slice-selections'

    result = requests.get(url,
                          headers={'Content-Type': 'application/json',
                                   'Authorization': 'Bearer {}'.format(token)},verify=False)

    print(result.status_code,"result",result)
    if result.status_code == 401:
        return 401
    res = result.json()
    res=res['response']['data']
    # revokeToken(token)
    print("selection policy data", res)

    return res


def getSLAPolicy():
    token = getToken()
    url = 'https://'+TSC_IP+":"+TSC_PORT+'/tsc/api/v4/policy/transport-slice-slas'
    result = requests.get(url,
                          headers={'Content-Type': 'application/json',
                                   'Authorization': 'Bearer {}'.format(token)}, verify=False)
    print(result.status_code, "result", result)
    if result.status_code == 401:
        return 401
    res = result.json()
    res = res['response']['data']
    print("selection policy data", res)

    return res

def getMonitoringPolicy():
    token = getToken()
    url = 'https://'+TSC_IP+":"+TSC_PORT+'/tsc/api/v4/policy/transport-slice-monitors'
    result = requests.get(url,
                          headers={'Content-Type': 'application/json',
                                   'Authorization': 'Bearer {}'.format(token)}, verify=False)
    print(result.status_code, "result", result)
    if result.status_code == 401:
        return 401
    res = result.json()
    res = res['response']['data']
    print("selection policy data", res)
    return res

def createSlice(object):
    token=getToken()
    print("Form values",object)
    TPID=sourceANDdestinationTP(object['TP_ID'],object['tpid'])
    print("TP ID",TPID)
    if len(TPID) <= 1:
        return False
    elif len(TPID) > 1:
        policieslist = []
        # policieslist = getPolicies(token, object['selectionPolicy'], object['monitoringPolicy'], object['SLAPolicy'])
        policieslist = getPolicies(token, "", object['monitoringPolicy'], "")
        print("Policies Object", policieslist)
        head, sep, tail = object['NS_ID'].partition(':')
        sst=head
        sd=tail
        req = createObj(object, TPID, policieslist,sst,sd)
        print(type(req))
        req=json.dumps(req,indent=2).replace('\n', '\\n').replace('"', '\\"')
        print(type(req))
        print("calling api", req)
        # result = callingCreateSlice(token, req)
        result=True
        return result

def callingCreateSlice(token,request):
    url = 'https://' + TSC_IP+":"+TSC_PORT + '/tsc/api/v4/connectivity/transport-slices'
    result = requests.post(url,
                          headers={'Content-Type': 'application/json',
                                   'Authorization': 'Bearer {}'.format(token)}, data=request, verify=False)
    print(result.status_code, "result create slice", result)
    if result.status_code == 401:
        return 401
    if result.status_code == 201:
        return True


def getPolicies(token,selectionPolicy,monitoringPolicy,slaPolicy):

    r1=getSelectionPolicy()
    r2=getMonitoringPolicy()
    r3=getSLAPolicy()
    selectionPolicyid=''
    monitoringPolicyid=''
    slaPolicyid=''
    for x in r1:
        # if x['name'] == selectionPolicy:
        selectionPolicyid=x['id']
        selectionPolicy=x['name']
        break
    for y in r2:
        if y['name'] == monitoringPolicy:
            monitoringPolicyid=y['id']
            break
    for z in r3:
        # if z['name'] == slaPolicy:
        slaPolicyid=z['id']
        slaPolicy=z['name']
        break

    finalObject=[
        {
            'selectionPolicyName':selectionPolicy,
            'selectionPolicyId':selectionPolicyid
        },
        {
            'monitoringPolicyName':monitoringPolicy,
            'monitoringPolicyid':monitoringPolicyid
        },
        {
            'slaPolicyName':slaPolicy,
            'slaPolicyId':slaPolicyid
        }
    ]

    return finalObject


def sourceANDdestinationTP(tpSource,tpDestination):
    srcanddestpid=[]
    print(pseudoObj)
    for ranCore in pseudoObj['nodes']:
        if ranCore['nodeName'] == tpSource:
            ip=ranCore['nodeSystemIpAddress']['ipv4Prefix']['string']
            for epid in pseudoObj['links']:
                if ip == epid['sourceEndpoint']['nodeSystemIp']:
                    srcanddestpid.append(epid['sourceEndpoint']['epId'])
                    break
                elif ip == epid['destinationEndpoint']['nodeSystemIp']:
                    srcanddestpid.append(epid['sourceEndpoint']['epId'])
                    break

    for ranCore in pseudoObj['nodes']:
        if ranCore['nodeName'] == tpDestination:
            ip=ranCore['nodeSystemIpAddress']['ipv4Prefix']['string']
            for epid in pseudoObj['links']:
                if ip == epid['sourceEndpoint']['nodeSystemIp']:
                    srcanddestpid.append(epid['sourceEndpoint']['epId'])
                    break
                elif ip == epid['destinationEndpoint']['nodeSystemIp']:
                    srcanddestpid.append(epid['sourceEndpoint']['epId'])
                    break

    print("Source Destination TP ID's", srcanddestpid)
    return srcanddestpid

def createObj(object,TPID,policieslist,sst,sd):
    obj = {
        "data": {
            "tsHeader": {
                "transportSlice": {
                    "tsName": object['slice_name']
                }
            },
            "connectionGroups": {
                "commonInfo": {
                    "networkSlices": [
                        {
                            "customerServiceType": object['Service_type'],
                            "customerId": object['Customer_Id'],
                            "snssai": {
                                "sd": sd,
                                "sst": sst
                            },
                            "qciList": [
                                140
                            ],
                            "additionalInfo": [
                                {
                                    "valueName": "test1",
                                    "value": "test-value1"
                                }
                            ]
                        }
                    ]
                },
                "connectionGroup": [
                    {
                        "connectionGroupName": object['connectionGroupName'],
                        "link": [
                            {
                                "source": {
                                    "serviceIpAddress": object['Service_IP_address'],
                                    "sourceInnerTag": -1,
                                    "tpId": TPID[0],
                                    "sourceOuterTag": int(object['VLAN']),
                                    "tpIpAddress": {
                                        "ipv4Prefix": {
                                            "string": object['Service_IP_address']
                                        }
                                    },
                                    "sapIpAddress": {
                                        "ipv4Prefix": {
                                            "string": object['SAP_IP_address']
                                        }
                                    }
                                },
                                "destination": {
                                    "destinationInnerTag": -1,
                                    "serviceIpAddress": object['serviceipaddress'],
                                    "sapIpAddress": {
                                        "ipv4Prefix": {
                                            "string": object['sapipaddress']
                                        }
                                    },
                                    "destinationOuterTag": int(object['vlan1']),
                                    "tpId": TPID[1],
                                    "tpIpAddress": {
                                        "ipv4Prefix": {
                                            "string": object['serviceipaddress']
                                        }
                                    }
                                }
                            }
                        ],
                        "policies": [
                            {
                                "policyName": policieslist[0]['selectionPolicyName'],
                                "policyType": "TSS",
                                "policyId": policieslist[0]['selectionPolicyId']
                            },
                            {
                                "policyName": policieslist[1]['monitoringPolicyName'],
                                "policyType": "TSM",
                                "policyId": policieslist[1]['monitoringPolicyid']
                            },
                            {
                                "policyName": policieslist[2]['slaPolicyName'],
                                "policyType": "SLA",
                                "policyId": policieslist[2]['slaPolicyId']
                            }
                        ]
                    }
                ]
            }
        }
    }

    return obj

def getNeNameForLink():
    token=getToken()
    list=getNodeAndLink(token)
    proxies = {
        #"http": "138.203.26.244:8443",
        #"https": "138.203.26.244:8443"
    }
    print("Inside getNeNameForLink")
    # url = 'https://' + SDN_IP +":"+SDN_PORT+ '/sdn/api/v4/ports/servicetype/L3_VPN/'
    # result = requests.get(url,
    #                       headers={'Content-Type': 'application/json',
    #                                'Authorization': 'Bearer {}'.format(token)}, verify=False)
    # # print(result.status_code, "result", result)
    # res = result.json()
    # res = res['response']['data']
    # print(res)
    # for x in list:
    #     for y in res:
    #         if y['externalIds'] != None:
    #             if x['sourceip'] == find_between(y['externalIds'][0]['id'],":",":"):
    #                 key="neNameSource"
    #                 x[key]=y['neName']
    #                 break
    #
    # for x in list:
    #     for y in res:
    #         if y['externalIds'] != None:
    #             if x['destinationip'] == find_between(y['externalIds'][0]['id'],":",":"):
    #                 key="neNameDestination"
    #                 x[key]=y['neName']
    #                 break
    #
    # # print("list",list)
    # print("finalizelist",len(list))
    return list

def getNodeAndLink(token):
    proxies = {
        #"http": "138.203.26.244:8443",
        #"https": "138.203.26.244:8443"
    }


    print("Inside getNodeAndLink")
    url = 'https://'+SDN_IP +":"+SDN_PORT+'/sdn/api/v4/nsp/net/l3/networks'

    result = requests.get(url,
                          headers={'Content-Type': 'application/json',
                                   'Authorization': 'Bearer {}'.format(token)}, verify=False)

    print("After networks api call")
    print(result.status_code, "result", result)

    if result.status_code == 401:
        return 401
    res = result.json()
    res1=res['response']['data']
    # print(res['response']['data'])

    res = res['response']['data']['network']

    finalObj = []
    for x in res:
        link1=res1['network'][x]['link']
        print(len(link1))
        for l1 in link1:
            obi = {}
            s=link1[l1]['nspLink']['linkState']['linkParams']['name']
            for srcanddest in res['233-060bb2cb-5227-4402-8ff5-aea737bf24c5']['node']:
                if link1[l1]['source']['sourceNode'] == srcanddest:
                    for subnodes in res['233-060bb2cb-5227-4402-8ff5-aea737bf24c5']['node'][srcanddest]['terminationPoint']:
                        if link1[l1]['source']['sourceTp'] == subnodes:
                            obi['sourceip'] = res['233-060bb2cb-5227-4402-8ff5-aea737bf24c5']['node'][srcanddest]['terminationPoint'][subnodes]['nspTerminationPoint']['terminationPointState']['terminationPointParams']['routerIpAddress']
                if link1[l1]['destination']['destNode'] == srcanddest:
                    for subnodes in res['233-060bb2cb-5227-4402-8ff5-aea737bf24c5']['node'][srcanddest]['terminationPoint']:
                        if link1[l1]['destination']['destTp'] == subnodes:
                            obi['destinationip'] = res['233-060bb2cb-5227-4402-8ff5-aea737bf24c5']['node'][srcanddest]['terminationPoint'][subnodes]['nspTerminationPoint']['terminationPointState']['terminationPointParams']['routerIpAddress']

            sourceip=s.split(':')[0]
            destinationip=find_between(link1[l1]['nspLink']['linkState']['linkParams']['name'],"::","=>")
            linkipaddress=find_between(link1[l1]['nspLink']['linkState']['linkParams']['name'],"=>","-")
            obi['linkid']=l1
            obi['linkipaddress']=linkipaddress
            # obi['sourceip']=sourceip
            # obi['destinationip']=destinationip
            obi['latency']=link1[l1]['nspLink']['linkState']['linkParams']['latency']
            obi['token']=token
            finalObj.append(obi)
            # print("finl obj len",len(finalObj))

    return finalObj

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""