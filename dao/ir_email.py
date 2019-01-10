import base64
from io import BytesIO
import smtplib    
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage    
from email.header import Header

class Email():
    def __init__(self,smtpserver,username,password):
        self.username = username
        try:
            self.smtp = smtplib.SMTP()
            self.smtp.connect(smtpserver)    
            self.smtp.login(username, password)
            
        except Exception as ex:
            print(ex)




    def send(self,receiver,subject,html,sender=''):
        if not sender:
            sender = self.username
            
        msgRoot = MIMEMultipart('related') 
        msgRoot['From'] = sender
        if type(receiver)==type([]):
            msgRoot['To'] = ",".join(receiver)
        elif type(receiver)==type(""):
             msgRoot['To'] = receiver
            
       
        msgRoot['Subject'] = Header(subject,'GBK')    

        #构造正文

        mail_body = MIMEText(html, _subtype='html', _charset='utf-8')
        msgRoot.attach(mail_body)
        '''
        #构造附件
        if file_name:    
            att = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')    
            att["Content-Type"] = 'application/octet-stream'    
            att["Content-Disposition"] = 'attachment; filename="'+ file_name+'"'    
            msgRoot.attach(att)    
        '''

      

        try:
            print ('To:'+msgRoot['To'])
           
              
            self.smtp.sendmail(sender, receiver, msgRoot.as_string())    

        except Exception as ex:
            print("email fail!!!")
            print(ex)
            ret=0
        else:
            print("email success!!!!!!!!!")
            ret=1
        finally:
            self.smtp.quit()
          
        return ret
     
