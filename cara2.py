"""
by HelS

IG      : https://www.instagram.com/hels.ae/
YT      : https://www.youtube.com/channel/UCV3nFQJw1bf03Ds9Pf5JcxA
Github  : https://github.com/HelmiSalsabila9
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Alamat Email Pengirim
fromaddr = "email anda"

# Alamat Email Penerima
toaddr = "emai tujuan"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Subjectnya bebas"

body = "Isi body bebas"
msg.attach(MIMEText(body, 'plain'))

# Lampiram dan buat file
filename = 'namafile.txt'
attachment = open('namafile.txt', 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

gmailserver = smtplib.SMTP('smtp.gmail.com', 587)
gmailserver.starttls()
gmailserver.login(fromaddr, 'pass email anda')
text = msg.as_string()
gmailserver.sendmail(fromaddr, toaddr, text)

print('\nSuccess!')

gmailserver.quit()
