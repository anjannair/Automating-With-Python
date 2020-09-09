#https://developers.google.com/gmail/api/v1/reference/ get the credentials.json file from here
import ezgmail, os
#os.chdir(r'credentials.json')      #use these first after downloading the credentials.json file 
#ezgmail.init()                     #after that comment it 
file1 = open('mail_to_send.txt', 'r')
Lines = file1.readlines()
for line in Lines:
    ezgmail.send(line.strip(), 'Waddup', 'Hello')   #title,body
#ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',         #These are for cc and bccing
#cc='friend@example.com', bcc='otherfriend@example.com,someoneelse@example.com')
print("DONE!")