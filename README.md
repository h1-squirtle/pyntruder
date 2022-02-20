# pyntruder
A Low level Burp Intruder via python. This tool will let you send concurrent requests with multiple threads mimicing the Burp Intruder. 

If you want to:
- Change the default "Total requests to send" by changing value of *"NumberOfRequests"* parameter  **[Default value=30]**
- Change the default "concurrent requests" by changing value of *"conRequests"* parameter          **[Default value=60]**

Usage:
-----
```
python pyndruder.py <file-containing-python-code>
python pyndruder.py request.txt
```

Instructions:
---
1. Login into application and open network tab
2. Perform the action and  
3. Copy the cURL request of that action with "Right Click>>Copy>>Copy as a cURL (bash)
4. Goto https://curlconverter.com/ and paste the curl request
5. Copy the python code from there
6. Create a new txt file and paste the python code in that file
7. Run the tool with following syntax
```
python pyndruder.py <file-containing-python-code>
python pyndruder.py request.txt
```
8. Successful requests will be printed on console but it is advised to check results into application.



