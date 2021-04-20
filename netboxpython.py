import requests
import os

url = 'https://192.168.1.224:4430/api/dcim/devices'
headers = { 'Authorization': "Token f857d283c8a38333198893d4d99bce13cb45a1ce"}
r = requests.get(url, headers=headers, verify=False)
jsondata = r.json()
count = jsondata['count']
i=0
save_path = '/var/lib/awx/venv/'
file = os.path.join(save_path, "devices.yml")
f = open(file, "w")
type1 = 2
type2 = 2
while( i < count):
        device = jsondata['results'][i]
        deviceip = device['primary_ip']['address']
        devicename = device['name']
        devicegroup = device['tags'][0]
        ip = deviceip.split('/')
        deviceip = ip[0]
        i= i+1
        f.write("Switch"+str(i)+":"+'\n')
        f.write('  '+"ip:"+' '+deviceip+'\n')
        f.write('  '+"group:"+' '+devicegroup+'\n')
        f.write('  '+"name:"+' '+devicename+'\n')
        f.write('\n')
f.close()
