import os
from gettext import install
from urllib.request import urlopen, localhost
from os import system
import smtplib

# system('python -m aiosmtpd -n -c aiosmtpd.handlers.Debugging --port 1025')
# system("pip3 install aiosmtpd")

with urlopen('https://docs.python.org/uk/3/tutorial/stdlib.html') as response:
    for line in response:
        line = line.decode()
        if line.startswith('datetime'):
            print(line.rstrip())

server = smtplib.SMTP('localhost', 1025)
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: 'jcaesar@example.org'
From: 'soothsayer@example.org'

Beware the Ides of March.
""")
server.quit()

# python -m aiosmtpd -n -c aiosmtpd.handlers.Debugging --port 1025 # local server, paste in terminal