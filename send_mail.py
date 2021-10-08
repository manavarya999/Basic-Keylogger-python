import smtplib, ssl  


class send_mail:
        
    def sendEmail(message):
        smtp_server = "smtp.gmail.com"
        port = 587
        # use same email for sender and receiver while testing
        sender_email = "email-id-required"
        receiver_email = "enter-receiver-email-id"
        
        # password of the sender's email id
        password = "enter password"

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
            print("closing connection")
            server.quit()
