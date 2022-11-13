import smtplib
try:
    #Create your SMTP session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

   #Use TLS to add security
    smtp.starttls()

    #User Authentication
    smtp.login("faddhackathon@gmail.com","fadd1234")

    #Defining The Message
    message = "Hello"

    #Sending the Email
    smtp.sendmail("faddhackathon@gmail.com", "dmaiya@umass.edu", message)

    #Terminating the session
    smtp.quit()
    print ("Email sent successfully!")

except Exception as ex:
    print("Something went wrong....",ex)