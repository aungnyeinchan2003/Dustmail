import smtplib, ssl
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
print("--------------+---------------")
print("[+]    !   Dust Mail   !     [+]")
print("--------------+---------------")
print("[+]command line mail sending tool[+]")
context = ssl.create_default_context()
a=0
sender_email = input("Enter your usenname and press enter: ")
password = getpass.getpass(prompt="Enter password and press enter: ")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    try:
        server.login(sender_email, password)
    except:
        a=1
    if a==0:
        print("[1]To a selected person")
        print("[2]To many selected peoples")
        select = int(input("Select an option: "))
        if select == 1:
            receiver_email = input("Enter username of gmail account you wnat to send: ")
            message = MIMEMultipart("alternative")
            message["Subject"] = input("Enter Your subject: ")
            message["From"] = sender_email
            message["To"] = receiver_email
            userchoice1 = input("Do you want to add Cc.[y/n]; ")
            if userchoice1 == "y":

                message["Cc"] = input("Enter Cc: ")
            userchoice2 = input("do you want to add Bcc[y/n]: ")
            if userchoice2 == "y":

                message["Bcc"] = input("Enter Bcc: ")
            write = input("Write message: ")
            text = write
            part1 = MIMEText(text, "plain")
            userchoice = input("Do you want to attach file.[y/n]:")
            if userchoice == "y":
                
                filename = input("Enter your file path: ") 
                with open(filename, "rb") as attachment:
                    part2 = MIMEBase("application", "octet-stream")
                    part2.set_payload(attachment.read())
                encoders.encode_base64(part2)
                message.attach(part2)
            message.attach(part1)
            server.sendmail(sender_email,receiver_email,message.as_string())
            print("Message sent to ",receiver_email)
        elif select == 2:
            maillist=[]
            i = 0
            
            mailname = "1"
            while mailname != "0":
                mailname = input("Enter Email address. type 0 to end: ")
                if mailname != "0":
                    maillist.append(mailname)
                    i += 1
                else:
                    print("[+]Mail list is ended.")
            message = MIMEMultipart("alternative")
            message["Subject"] = input("Enter Your subject: ")
            userchoice1 = input("Do you want to add Cc.[y/n]; ")
            if userchoice1 == "y":

                message["Cc"] = input("Enter Cc: ")
            userchoice2 = input("do you want to add Bcc[y/n]: ")
            if userchoice2 == "y":

                message["Bcc"] = input("Enter Bcc: ")
            write = input("Write message: ")
            text = write
            part1 = MIMEText(text, "plain")
            userchoice = input("Do yoy want to attach file.[y/n]: ")
            if userchoice == "y":

                filename = input("Enter your file path: ") 
                with open(filename, "rb") as attachment:
                    part2 = MIMEBase("application", "octet-stream")
                    part2.set_payload(attachment.read())
                encoders.encode_base64(part2)
                message.attach(part2)
            message.attach(part1)
            j=0
            while j < i:
                server.sendmail(sender_email,maillist[j],message.as_string())
                print("mail was sent to ",maillist[j])
                j += 1
        else:
            print("You have selected the wrong option.") 
    else:
        print("[+]Login failed.Username or Password is wrong.")