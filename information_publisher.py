from dao.ir_email import Email
from dao.sms import SMS

class InformationPublisher():
    def __init__(self,smtpserver,username,password):
        self.username=username
        self.password=password

        self.email=Email(smtpserver,username,password)
        self.sms=SMS()

    def send(self,subject,content,tels,emails,file_name=""):      



        ret_sms = self.sms.send(content,tels)
        ret_email = self.email.send(self.username,emails,subject=subject,html=content,file_name=file_name)

        return ret_sms,ret_email

if __name__=='__main__':
    smtpserver = 'smtp.mxhichina.com' 
    username = ''
    password = ''

    ir=InformationPublisher(smtpserver,username,password)
    subject='测试主题123abcaaa'
    content='测试内容123abc'
    tels=[]
    emails=["test@qq.com",'test@test.test']

    ret=ir.send(subject=subject,content=content,tels=tels,emails=emails)

    print(ret)