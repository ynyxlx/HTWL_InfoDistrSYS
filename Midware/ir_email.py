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




    def send(self,email_address,subject,contents,sender=''):
        if not sender:
            sender = self.username
            
        msgRoot = MIMEMultipart('related') 
        msgRoot['From'] = sender
        if type(email_address)==type([]):
            msgRoot['To'] = ",".join(email_address)
        elif type(email_address)==type(""):
             msgRoot['To'] = email_address
            
       
        msgRoot['Subject'] = Header(subject,'GBK')    

        #构造正文

        mail_body = MIMEText(contents, _subtype='html', _charset='utf-8')
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
           
              
            self.smtp.sendmail(sender, email_address, msgRoot.as_string())    

        except Exception as ex:
            print("email fail!!!")
            print(ex)
            ret=False
        else:
            print("email success!!!!!!!!!")
            ret=True
        finally:
            self.smtp.quit()
          
        return ret
     
