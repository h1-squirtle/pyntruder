import concurrent.futures as cp
from time import perf_counter
from sys import argv
import urllib3
import requests

print("\nAttack Started, please wait\n.......")
with open(argv[1],"r") as f:
    data=f.read()

#To remove ssl warnings
if "urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)" in data:
    pass
else:
    warning="import urllib3,requests\nurllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)\n"
    data=warning+data

#To filter successful requests
ifLoopAdd="\nif response.status_code==200 or response.status_code==201: \n     print('A request passed:' ,response.status_code)"

if "response.status_code" in data:
    pass
else:
    data=data+ifLoopAdd
def visit():
    exec(data)

before=perf_counter()

#Change number of request as per requirment
NumberOfRequests=30
with cp.ThreadPoolExecutor(max_workers=60) as executor:
    x=0
    while x <=NumberOfRequests :
        executor.submit(visit)
        x += 1
after=perf_counter()

print(f"\nAttack completed in {after-before: 3f} seconds.\nPlease check into application for better results.")
