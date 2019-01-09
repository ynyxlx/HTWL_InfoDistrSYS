
import time
import hashlib
import json
import logging
import requests



class SMS():

	

	def get_uuid(self,text):
		md5=hashlib.md5()
		md5.update(text.encode())
		return md5.hexdigest() [:9]+"-"+md5.hexdigest() [9:13]+"-"+md5.hexdigest() [13:17]+"-"+md5.hexdigest() [17:21]+"-"+md5.hexdigest() [21:]

	def __init__(self):
		logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='sms.log',
                filemode='w')	

		

	
		


	def send(self, content, tels):
		tels_list=[]
		if type(tels)!=type([]):
			tels_list.append(tels)
		else:
			tels_list=tels
            
		
		content=content.encode('utf-8').decode('latin-1')

		for tel in tels_list:
			user=str(tel)
			
			
			time.sleep(0.1)
			headers={'content-type': 'text/xml','charset':"utf-8"}
			data=self.create_SOAPXml(user,content)
			r = requests.post("http://10.96.45.32:28888/Service/WebService.asmx",headers=headers, data=data)
			logging.info(str(r)+":"+user)
		return True
			


	def create_SOAPXml(self,mobile, content,user_name,passwd):
		uuid =self.get_uuid(str(time.time()))
		print (uuid)
		return  '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:net="http://www.139130.net">
						<soapenv:Header/>
						<soapenv:Body>
							<net:Post>
								<!--Optional:-->
								<net:account>'''+user_name+'''</net:account>
								<!--Optional:-->
								<net:password>'''+passwd+'''</net:password>
								<!--Optional:-->
								<net:mtpack>
									<net:uuid>''' + uuid + '''</net:uuid>
									<net:batchID>''' + uuid + '''</net:batchID>
									<!--Optional:-->
									<net:batchName>111</net:batchName>
									<net:sendType>1</net:sendType>
									<net:msgType>1</net:msgType>
									<!--Optional:-->
									<net:medias>
									<!--Zero or more repetitions:-->
									<net:MediaItems>
										<!--Optional:-->
										<net:meta>111</net:meta>
										<!--Optional:-->
										<net:data>cid:978073000983</net:data>
									</net:MediaItems>
									</net:medias>
									<!--Optional:-->
									<net:msgs>
									<!--Zero or more repetitions:-->
									<net:MessageData>
										<!--Optional:-->
										<net:Phone>''' + mobile + '''</net:Phone>
										<!--Optional:-->
										<net:Content>''' + content + '''</net:Content>
										<net:vipFlag>1</net:vipFlag>
										<!--Optional:-->
										<net:customMsgID></net:customMsgID>
										<!--Optional:-->
										<net:medias>
											<!--Zero or more repetitions:-->
											<net:MediaItems>
												<!--Optional:-->
												<net:meta></net:meta>
												<!--Optional:-->
												<net:data>cid:1358137609904</net:data>
											</net:MediaItems>
										</net:medias>
									</net:MessageData>
									</net:msgs>
									<net:bizType>1</net:bizType>
									<net:distinctFlag>true</net:distinctFlag>
									<net:scheduleTime>0</net:scheduleTime>
									<!--Optional:-->
									<net:remark>111</net:remark>
									<!--Optional:-->
									<net:customNum>13801</net:customNum>
									<net:deadline>0</net:deadline>
								</net:mtpack>
							</net:Post>
						</soapenv:Body>
						</soapenv:Envelope> '''


if __name__=='__main__':
        sms=SMS()
        sms.send("测试：!!!一二三123abc",[123456789,987654321])
        
