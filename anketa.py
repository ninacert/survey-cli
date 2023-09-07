#!/usr/bin/env python3
import smtplib

SENDER = "sender@example.org"
RECEIVER = "receiver@example.org"
EMAILSERVER = "example.org"
EMAILPORT = 587
EMAILUSERNAME = "username"
EMAILPASSWORD = "password"

while True:
    print("Choose language[EN/sr]:")
    lang = input()
    if lang == "sr":
        filelang = open("srpski.txt","r")
    else:
        filelang = open("english.txt","r")
  
    questions = filelang.readlines()
    filelang.close()
    answers = []

    for question in questions:
        print(question)
        answers.append(input())

    fileuser = open("usernumber.txt","r")
    usernum = int(fileuser.readlines()[0])
    fileuser.close()

    usernum = usernum + 1

    if lang == 'sr':
      print("Hvala na odgovorima. Tvoj broj je: " + " " + str(usernum))
    else:
      print("Thank you for your responses. Your number is: " + " " + str(usernum))
    fileuserwrite = open("usernumber.txt","w")
    fileuserwrite.write(str(usernum))
    fileuserwrite.close()

    msg = "Subject: Survey results" + "\n"
    msg += "From: Survey-cli <" + SENDER + ">" + "\n"
    msg += "To: <" + RECEIVER + ">" + "\n" + "\n"
    if lang == 'sr':
      msg += "Broj korisnika:" + str(usernum) + "\n"
    else:
      msg += "User number:" + str(usernum) + "\n"

    i = 0
    for question in questions:
        msg += questions[i] + answers[i] + "\n"
        i = i + 1

    smtp = smtplib.SMTP(EMAILSERVER, EMAILPORT)
    smtp.starttls()
    smtp.login(EMAILUSERNAME, EMAILPASSWORD)
    smtp.sendmail(SENDER, RECEIVER, msg.encode("utf8"))
    smtp.quit()
