
"""
by HelS

IG      : https://www.instagram.com/hels.ae/
YT      : https://www.youtube.com/channel/UCV3nFQJw1bf03Ds9Pf5JcxA
Github  : https://github.com/HelmiSalsabila9
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#! Pengirim
fromaddr = 'email anda'

#! Penerima
toaddr = 'email tujuan'

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Subject email'

body = 'Bebas isi apa aja'
msg.attach(MIMEText(body, 'plain'))

gmailServer = smtplib.SMTP('smtp.gmail.com', 587)
gmailServer.starttls()
gmailServer.login(fromaddr, 'pass email anda')
gmailtext = msg.as_string()
gmailServer.sendmail(fromaddr, toaddr, gmailtext)

print('\nSuccess!')

gmailServer.quit()
