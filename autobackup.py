from time import sleep
import os
from datetime import datetime

while True:
    my_date = datetime.now()
    print("Actual date is " + my_date.strftime('%Y-%m-%dT%H:%M'))
    os.system("git commit -m 'Auto backup - " + my_date.strftime('%Y-%m-%dT%H:%M') + "'")
    sleep(10)
    os.system("git push")
    sleep(60 * 60)
