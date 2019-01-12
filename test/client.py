# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:07:27 2019

@author: lx198
"""

from requests import get,put,post,delete

INFORMATION_DICT={"MESSAGE":
    {
            "SMS":{
                "tels":"15987738298",
                "content":"test3"
            },
            "EMAIL":{
                "receiver":"68545766@qq.com",
                "subject":"test subject 3",
                "html":"test main text 3",
                "file_name":""
            }
        }}
            
            
INFORMATION_DICT2={
            "SMS":{
                "telephone_numbers":"15987738298",
                "contents":"test4"
            },
            "EMAIL":{
                "email_address":"68545766@qq.com",
                "subject":"test subject 4",
                "contents":"test main text 4",
                
            }
        }
import json
data_json=json.dumps(INFORMATION_DICT2)

#t7=post('http://127.0.0.1:5000/message',data=data_json)
#print(t7)
#print(t7.text)

#t8=get('http://172.16.145.39:5000/message',data=data_json)

t8=get('http://127.0.0.1:5000/message',data=data_json)
print(t8)
print(t8.text)
print(t8.content)