# Gainz Emailer
# Python fitness tracker using webmail 


############################################
############################################
---------------Get Gainz Bro!---------------
############################################
############################################

______________$$$$$$$$$$____________________
_____________$$__$_____$$$$$________________
_____________$$_$$__$$____$$$$$$$$__________
____________$$_$$__$$$$$________$$$_________
___________$$_$$__$$__$$_$$$__$$__$$________
___________$$_$$__$__$$__$$$$$$$$__$$_______
____________$$$$$_$$_$$$_$$$$$$$$_$$$_______
_____________$$$$$$$$$$$$$_$$___$_$$$$______
________________$$_$$$______$$$$$_$$$$______
_________________$$$$_______$$$$$___$$$_____
___________________________$$_$$____$$$$____
___________________________$$_$$____$$$$$___
__________________________$$$$$_____$$$$$$__
_________________________$__$$_______$$$$$__
________________________$$$_$$________$$$$$_
________________________$$$___________$$$$$_
_________________$$$$___$$____________$$$$$$
__$$$$$$$$____$$$$$$$$$$_$____________$$$_$$
_$$$$$$$$$$$$$$$______$$$$$$$___$$____$$_$$$
$$________$$$$__________$_$$$___$$$_____$$$$
$$______$$$_____________$$$$$$$$$$$$$$$$$_$$
$$______$$_______________$$_$$$$$$$$$$$$$$$_
$$_____$_$$$$$__________$$$_$$$$$$$$$$$$$$$_
$$___$$$__$$$$$$$$$$$$$$$$$__$$$$$$$$$$$$$__
$$_$$$$_____$$$$$$$$$$$$________$$$$$$__$___
$$$$$$$$$$$$$$_________$$$$$______$$$$$$$___
$$$$_$$$$$______________$$$$$$$$$$$$$$$$____
$$__$$$$_____$$___________$$$$$$$$$$$$$_____
$$_$$$$$$$$$$$$____________$$$$$$$$$$_______
$$_$$$$$$$$$$$$____$$$$$$$$__$$$____________
$$$$__$$$$$$$$$$$$$$$$$$$$$$$$______________
$$_________$$$$$$$$$$$$$$$__________________

############################################
############################################

'''
To-Dos

-update mail function to retrieve message body-text
-write logic to parse structured body-text
	-write logic to check if data is new data
-write logic to organize, visualize and write data to file

-maybe write a function to create the auth file from user input at initial execution
'''

import smtplib
import time
import imaplib
import email

#Separate python file to hold Gmail account credentials
from GainzEmailer_authfile import address_cred
from GainzEmailer_authfile import pw_cred
 
##########################################################################
## Constants
##########################################################################

#Gmail Account Constants
#Email client setup in this script borrowed from here: https://codehandbook.org/how-to-read-email-from-gmail-using-python/
FROM_EMAIL  = address_cred
FROM_PWD    = pw_cred
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

#formatting label labels
lift_name = []
lift_variation = []

##########################################################################
## Constants
##########################################################################
 

#Webmail Client to receive data
#Email client setup in this script borrowed from here: https://codehandbook.org/how-to-read-email-from-gmail-using-python/

def read_email_from_gmail():
	try:
		mail = imaplib.IMAP4_SSL(SMTP_SERVER)
		mail.login(FROM_EMAIL,FROM_PWD)
		mail.select('inbox')

		type, data = mail.search(None, 'ALL')
		mail_ids = data[0]

		id_list = mail_ids.split()   
		
		for i in reversed(id_list):
			typ, data = mail.fetch(i, '(RFC822)' )

			for response_part in data:
				if isinstance(response_part, tuple):
					msg = email.message_from_string(response_part[1].decode('utf-8'))
					email_subject = msg['subject']
					email_from = msg['from']
					print 'From : ' + email_from + '\n'
					print 'Subject : ' + email_subject + '\n'

	except Exception, e:
		print str(e)
	
#Ux to provide instruction receive configuration 
#need Username and password 

#Data Parser 

#Data Visualization

#Data to File

##########################################################################
## Execute
##########################################################################
if __name__ == '__main__':
	read_email_from_gmail()