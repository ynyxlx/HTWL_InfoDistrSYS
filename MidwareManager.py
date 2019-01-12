
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:07:27 2019

@author: lx
"""


class MessageHandle():
    @classmethod
    def __init__(self,config_dict):
        self.object_dict={}
        for mod_name in config_dict:
            self.object_dict[mod_name]=config_dict[mod_name]["CLASS"](**config_dict[mod_name]["CONFIG"])

    @classmethod
    def send(self, message_dict):
        try:
            for message_channel in message_dict:
                print('Message channel:{}\n'.format(message_channel))
                print('Message detail:{}\n'.format(message_dict[message_channel]))

                self.object_dict[message_channel].send(
                    **message_dict[message_channel]
                )
            return 'ok!',True
        except Exception as ex:
            return ex,False
    
    @classmethod
    def get_modules(self):
        return self.object_dict


if __name__ == '__main__':
    from  config import MODUL_DICT
    MessageHandle(MODUL_DICT)
    '''
    INFORMATION_DICT={
            "SMS":{
                "tels":"15987738298",
                "content":"test2"
            },
            "EMAIL":{
                "receiver":"68545766@qq.com",
                "subject":"test subject",
                "html":"test main text",
                "file_name":""
            }
        }

    MessageHandle.send(INFORMATION_DICT)
    '''
    import inspect
    import json

    message_template={}
    mods_dict=MessageHandle.get_modules()

    for cls_name in mods_dict:

        message_template[cls_name]={}

        for args in inspect.getfullargspec(mods_dict[cls_name].send)[0]:
            if args =='self':
                continue
            message_template[cls_name][args]=''
        
    print( json.dumps(message_template))