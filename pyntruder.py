from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from sys import argv
from uncurl import parse

print("Attack Started, please wait..\n")

with open(argv[1],"r") as f:
    data=f.read()
data=data.replace("$","")
data=data.replace("\\","")
data=parse(data)
data="response="+data

#To remove ssl warnings
if "urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)" in data:
    pass
else:
    warning="import urllib3,requests\nurllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)\n"
    data=warning+data

#To filter successful requests
ifLoopAdd="\nif response.status_code==200 or response.status_code==201: \n     print('A request passed:' ,response.status_code)\nelif response.status_code==401 or response.status.code==500:\n      print('Session Expired. Status code:',response.status_code)"

if "response.status_code" in data:
    pass
else:
    data=data+ifLoopAdd

def visit():
    exec(data)

print("Requests passed:\n-----------------------------")
before=perf_counter()

#Change number of request as per requirment
NumberOfRequests=30
conRequests=60
with ThreadPoolExecutor(max_workers=conRequests) as executor:
    x=0
    while x <=NumberOfRequests :
        executor.submit(visit)
        x += 1
after=perf_counter()

print(f"\n{NumberOfRequests} requests sent in {after-before: 3f} seconds.\nPlease check into application for better results.")
