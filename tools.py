from bs4 import BeautifulSoup
import requests
import sys
import smtplib


# checks if the price is lower than the target price and raise a flag to finish if  condicion = true.
def check_value(result, target_price, username, password, emailTo):
    price = result['price']
    if(price < target_price):
        print("Target price reached! time to buy!")
        print("Savings:", "${:,}".format(
            target_price - price))
        send_mail(result, target_price, username, password, emailTo)
        return False
    else:
        return True


def send_mail(result, target_price, username, password, emailTo):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(username, password)
    subject = "Fifa player alert! time to buy"

    name = result['name']
    rating = result['rating']
    price = result['price']

    body = "Player: " + name + "\n" + "Rating: " + str(rating) + "\n" + "Lowest Price: " + "${:,}".format(
        price) + "\n" + "Target Price: " + "${:,}".format(target_price) + "\n" + "Target price reached! time to buy!" + "\n" + "Savings: " + "${:,}".format(
            target_price - price) + "\n" + "Messaged created automagically by Gonzalo Quintela using web scraping in Python."

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(username+"@gmail.com", emailTo, msg)
    print("email sent!")
    server.quit


def scrap_function(url):
    result = {}
    ### browser config ###
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    ### player name ###
    name = soup.find('h1').get_text()
    result['name'] = name

    ### player rating ###
    rating = soup.find("div", {'class': 'card-20-rating'}).get_text()
    result['rating'] = rating

    ### player price ###
    price = soup.findAll(
        "div", {"class": "playerprofile-price"})[1].get_text().strip()

    ###convert price to int ###
    price_int = int(price.replace(',', ''))
    result['price'] = price_int

    ### time of enquiry ###
    timeOfEnquiry = soup.find(
        "div", {'class': 'pull-right priceupdate'}).get_text()
    result['timeOfEnquiry'] = timeOfEnquiry

    return result


### aux for converting price to int ###


def my_filt(variable):
    comma = ','
    if variable in comma:
        return True
    else:
        return False

# def print_all(result, target_price):
#     price = result['price']
#     timeOfEnquiry = result['timeOfEnquiry']
#     name = result['name']
#     rating = result['rating']

#     print("Player name:", name)
#     print("rating:", rating)
#     print("Lowest Price:", "${:,}".format(price))
#     print("Target price:", "${:,}".format(target_price))
#     if(price < target_price):
#         print("Target price reached! time to buy!")
#         print("Savings:", "${:,}".format(
#             target_price - price))
#     else:
#         print("The price is still", "${:,}".format(
#             price - target_price), "above...")
#     print(timeOfEnquiry)
