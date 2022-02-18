import requests
from sys import argv
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter

url=argv[1]
threadNo=int(argv[2])

def visit():
    r=requests.get(url)

before=perf_counter()
with ThreadPoolExecutor(max_workers=threadNo) as executor:
    x=0
    while x<=30:
        future=executor.submit(visit)
        x+=1
after=perf_counter()

print(f"Completed in {after-before: 3f} Seconds")
