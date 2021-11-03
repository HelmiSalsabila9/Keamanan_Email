"""
by HelS

IG      : https://www.instagram.com/hels.ae/
YT      : https://www.youtube.com/channel/UCV3nFQJw1bf03Ds9Pf5JcxA
Github  : https://github.com/HelmiSalsabila9
"""

import smtplib
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#! Pengirim
mailAddress = input('Masukan email Anda... \n')
mailPassword = getpass.getpass('Masukan password email Anda... \n')

#! Penerima
mailTo = input('Masukan alamat email yang akan dikirimkan pesan... \n')

msg = MIMEMultipart()
msg['mailAddress'] = mailAddress
msg['mailPassword'] = mailPassword
msg['mailTo'] = mailTo
msg['Subject'] = 'Hi Bro..'

body = input('Masukan pesannya :D \n')
msg.attach(MIMEText(body, 'plain'))

gmailServer = smtplib.SMTP('smtp.gmail.com', 587)
gmailServer.starttls()
gmailServer.login(mailAddress, 'pssword email anda')
gmailtext = msg.as_string()
gmailServer.sendmail(mailAddress, mailTo, gmailtext)

print('\nSuccess!')

gmailServer.quit()
