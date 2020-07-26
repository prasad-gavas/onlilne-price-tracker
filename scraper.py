# The requests module allows you to send HTTP requests using Python.
import requests
# Beautiful Soup is a Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup
import smtplib  # The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP

URL = 'https://www.amazon.in/Acer-SF314-57G-i5-1035G1-processor-Thunderbolt/dp/B07Z88C1ZR/ref=sr_1_1_sspa?crid=21MZ7CRIXA9GY&dchild=1&keywords=acer+swift+3+i5+8th+gen&qid=1595086375&sprefix=acer+swift+3+i5+%2Caps%2C330&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySThaS0VUNVc3TkpBJmVuY3J5cHRlZElkPUEwMTU0NDU4Qkg0QzA3U0NQWEFGJmVuY3J5cHRlZEFkSWQ9QTEwMDgwOTgzS0xUU1hYVVFUNzAxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'} 


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:8].replace(',', ''))

    if(converted_price < 60000.0):
        send_mail()

    print(converted_price)

    if(converted_price > 60000.0):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('prasadgavas1998@gmail.com', 'bikkqibjpqszdccy')

    subject = 'Price fell down'
    body = 'Check the amazon link https://www.amazon.in/Acer-SF314-57G-i5-1035G1-processor-Thunderbolt/dp/B07Z88C1ZR/ref=sr_1_1_sspa?crid=21MZ7CRIXA9GY&dchild=1&keywords=acer+swift+3+i5+8th+gen&qid=1595086375&sprefix=acer+swift+3+i5+%2Caps%2C330&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySThaS0VUNVc3TkpBJmVuY3J5cHRlZElkPUEwMTU0NDU4Qkg0QzA3U0NQWEFGJmVuY3J5cHRlZEFkSWQ9QTEwMDgwOTgzS0xUU1hYVVFUNzAxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'prasadgavas1998@gmail.com',
        'prasadgavas2854@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()


check_price()
