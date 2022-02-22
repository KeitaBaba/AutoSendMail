import mailbox
import datetime
import os
import os.path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


dt=datetime.datetime.now()
today=dt.strftime('%d%b%Y')
d = dt.strftime('%m/%d')

maildir=''
tempdir = ''

for message in mailbox.mbox(maildir):

    for part in message.walk():
        date=part.get("Date")
        fname=part.get_filename()
        print(date)

        if date != None:
            cdate=date.replace(" ","")
        if fname != None:
            cfname=fname


if today in cdate:
    csvname = tempdir+fname
    csvname = csvname.replace("\n","")

    if os.path.isfile(csvname) == False:
        fp = open(csvname, 'wb')
        fp.write(part.get_payload(decode=True))
        fp.close()

        stmp_server = ""
        stmp_port = ""
        stmp_user = ""
        stmp_password = ""

        to_address = ""
        cc_address= ""
        from_address=stmp_user
        subject = f""
        html = """\
            
            """

        filepath = csvname
        filename = os.path.basename(csvname)

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Cc'] = cc_address
        msg.attach(MIMEText(html, 'html'))

        sendToList=to_address.split(',')
        sendCcList=cc_address.split(',')

        with open(filepath, "rb") as f:
            mb = MIMEApplication(f.read())
            mb.add_header("Content-Disposition", "attachment", filename=filename)
            msg.attach(mb)

        s = smtplib.SMTP(stmp_server, stmp_port)
        s.login(stmp_user, stmp_password)
        s.sendmail(from_address, sendToList+sendCcList, msg.as_string())
        s.quit()



