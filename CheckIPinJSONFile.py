import json
import ipaddress

deviceJSON = '{"Version": "15.6", "locationN": "500 Northridge", "role": "Access", "upTime": "12:10:53.49", "hostname": "ATL-3650-1", "macAddress": "39:58:1f:9e:38:c1", "series": "Cisco Catalyst 3650 Series Switches", "lastUpdated": "2017-09-21 13:12:46", "bootDateTime": "2016-10-27 05:24:53", "interfaceCount": "24", "lineCardCount": "1", "managementIpAddress": "192.168.10.10", "interfaces": {"interface": [{"GigabitEthernet0": {"ipv4": "100.100.100.1"}}, {"GigabitEthernet1": {"ipv4": "10.10.10.2"}}]}}'
data = json.loads(deviceJSON)



for record in data['interfaces']['interface']:
    for interface in record:
        ipAddress = record[interface]['ipv4']
        try:
            if ipaddress.ip_address(ipAddress).is_private == True:
                print(f'{interface} has an ip address of {ipAddress} which is a Private Address')
            else:
                print(f'{interface} has an ip address of {ipAddress} which is not a Private Address')
        except ValueError:
            print(f"{interface} does not appear to have a valid ip address defined")





































#print(f'The Python data format for the "deviceJSON" variable is {type(deviceJSON)}')
#print()
#print(deviceJSON)
