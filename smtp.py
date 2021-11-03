"""
by HelS

IG      : https://www.instagram.com/hels.ae/
YT      : https://www.youtube.com/channel/UCV3nFQJw1bf03Ds9Pf5JcxA
Github  : https://github.com/HelmiSalsabila9
"""

import smtplib

gmailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
gmailserver.login('Your Username', 'Your Password')
gmailserver.sendmail(
    'userhaluu@gmail.com',
    'helmisalsabila70@gmail.com',
    'This message is from python by Helmi Salsabila'
)
gmailserver.quit()
