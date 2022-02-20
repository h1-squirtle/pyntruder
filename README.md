# pyntruder
A basic python tool to test _**RACE CONDITION ATTACKS**_ without BurpSuite Intruder. This tool will send multiple concurrent requests with multiple threads mimicking the Burp Intruder _"Null Payloads"._

**If you want to:**
- Change the number of requests to send by changing value of *"NumberOfRequests"* parameter **[Default value=30]**
- Change the number of concurrent requests (threads) by changing value of *"conRequests"* parameter **[Default value=100]**

Instructions:
---
1. Login into the application and open the network tab
2. Perform the action.
3. Copy the cURL request of that action with _"Right Click>>Copy>>Copy as a cURL (bash)"_
4. Create a new txt file and paste the cURL request in that file. 
5. Change the parameter value which you want to test for a race condition. (Values of parameters in copied cURL request have already been processed.) 
7. Run the tool with the following syntax
```
python pyndruder.py <file-containing-curl-request>
python pyndruder.py request.txt
```
8. Status code of successful requests will be printed on the console but it is advised to check final results into the application.


Usage:
-----
```
python pyndruder.py <file-containing-cURL-request>
python pyndruder.py request.txt
```
Expected Output:
--
### Successful requests:


```
root@root$ python pyndruder.py request.txt
>>
Attack Started, please wait..

Requests passed:
-----------------------------
A request passed: 201
A request passed: 201
A request passed: 201

30 requests sent in  1.590660 seconds.
Please check into an application for better results.
```

### Session Expired:

```
root@root$ python pyndruder.py request.txt
>>
Attack Started, please wait..

Requests passed:
-----------------------------------
Session Expired. Status code: 401
Session Expired. Status code: 401
Session Expired. Status code: 401
.......

30 requests sent in  0.709497 seconds.
Please check into an application for better results.
```
### Bad request:
```
root@root$ python pyndruder.py request.txt
>>
Attack Started, please wait..

Requests passed:
-----------------------------------
Bad Request: 400 | Please check the request.
Bad Request: 400 | Please check the request.
Bad Request: 400 | Please check the request.
Bad Request: 400 | Please check the request.
......

30 requests sent in  1.510456 seconds.
Please check into application for better results.
```
Note:
---------
Remember to change the value of the parameter you want to check race condition on. The cURL request you copied contains a value of which entry is already created. 
