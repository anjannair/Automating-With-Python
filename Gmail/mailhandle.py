#https://developers.google.com/gmail/api/v1/reference/ get the credentials.json file from here
import ezgmail, os, time
#os.chdir(r'credentials.json')      #use these first after downloading the credentials.json file 
#ezgmail.init()                     #after that comment it
if ezgmail.LOGGED_IN == True:
    print("Logged in using "+ ezgmail.EMAIL_ADDRESS)
    time.sleep(3)
    file1 = open('mail_to_send.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        ezgmail.send(line.strip(), 'Waddup', 'Hello')   #title,body
#ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',         #These are for cc and bccing
#cc='friend@example.com', bcc='otherfriend@example.com,someoneelse@example.com')
    print("DONE!")
else:
    print("Logging in failed. Check if correct credentials.json file is loaded and check if token.json is generated after line 2 and 3")