
import requests
from math import floor
import time
import smtplib  as smtp
from email.message import EmailMessage


## Get data
book_url = 'hhttps://www.gutenberg.org/cache/epub/8300/pg8300.txt'
r = requests.get(book_url)

book_data = r.text.encode('ascii', 'ignore').decode('ascii')


word_list = book_data.split(" ")

msg_size = floor(len(word_list) / 1000)
final_msg_size = len(word_list) - (msg_size * 999)

#Set up SMTP
user = 'sorryaboutthat40@gmail.com'
password = ''
fr_address = 'sorryaboutthat40@gmail.com'
to_address = 'k'
smtp_host = 'smtp.gmail.com'
smtp_port = 587


subject = 'Communist Manifesto - Part'
msg_text = ''
start_pos = 0
msg_count = 0

#Create Loop
for b in range(20):

    server = smtp.SMTP(host=smtp_host, port=smtp_port)
    server.starttls()
    server.login(user=user, password=password)

    for i in range(50):
        if msg_count == 1000:
            start_pos = (len(word_list)-final_msg_size)
            msg_text = ' '.join(word_list[start_pos:])
        else:
            start_pos = msg_count * msg_size
            msg_text = ' '.join(word_list[start_pos:start_pos + msg_size])

        msg = EmailMessage()
        msg['From'] = fr_address
        msg['To'] = to_address
        msg['Subject'] = subject + str(msg_count+1)
        msg.set_payload(msg_text)

        msg_count += 1

        server.send_message(msg)


        time.sleep(0.5)
        print("Successful Troll")


    time.sleep(60)


server.close()
