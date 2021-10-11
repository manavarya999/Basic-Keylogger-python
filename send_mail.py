import smtplib, ssl  
class send_mail:
        
    def sendEmail(message):
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "Email id required"           #Put sender and receiver email the same for testing
        password = "Enter password"               #Put password of the sender's email id
        receiver_email = "enter-receiver-email-id"
        
        context = ssl.create_default_context()

        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        
        except Exception as e:
            print("ERROR DETECTED",e)
        finally:
            print("failure")
            server.quit()
