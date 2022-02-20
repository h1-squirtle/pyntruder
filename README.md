# pyntruder
A basic Intruder via python to test race condition issues without BurpSuite Intruder. This tool will send multiple concurrent requests with multiple threads mimicing the Burp Intruder "Null Payloads". 

**If you want to:**
- Change the default number of requests to send by changing value of *"NumberOfRequests"* parameter **[Default value=30]**
- Change the default number of concurrent requests by changing value of *"conRequests"* parameter **[Default value=60]**

Instructions:
---
1. Login into application and open network tab
2. Perform the action.
3. Copy the cURL request of that action with "Right Click>>Copy>>Copy as a cURL (bash)
4. Create a new txt file and paste the cURL request in that file. 
5. Change the parameter value which you want to test for race condition. (Values of parameters in copied cURL request has already been processed. 
7. Run the tool with following syntax
```
python pyndruder.py <file-containing-curl-request>
python pyndruder.py request.txt
```
8. Status code of successful requests will be printed on console but it is advised to check final results into application.


Usage:
-----
```
python pyndruder.py <file-containing-cURL-request>
python pyndruder.py request.txt
```
Output:
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

30 requests sent in  1.590660 seconds.
Please check into application for better results.
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
30 requests sent in  0.709497 seconds.
Please check into application for better results.
```


Note:
---------
Remember to change the value of parameter you want to check race condition on. The cURL request you copied contains value of which entry is already created. 

