from tools import *
import time

###
# arguments:

# 1) url of player (futwiz)
# 2) target price to send mail
# 3) google username (without @...)
# 4) password
# 5) mail to...

###


# url = 'https://www.futwiz.com/en/fifa20/player/emmanuel-petit/120'
url = sys.argv[1]
# target_price = 900000
target_price = int(sys.argv[2])
username = sys.argv[3]
password = sys.argv[4]
emailTo = sys.argv[5]

flag = True
timesScraped = 0
while(flag):
    timesScraped = timesScraped + 1
    result = scrap_function(url)
    flag = check_value(result, target_price, username, password, emailTo)
    print("web scrapping N", timesScraped)
    time.sleep(60*30)  # 30 min
