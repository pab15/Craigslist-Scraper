import re
import urllib
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
# for tests
import urlmanager as urlm

def findCarLinks(craigslist_url):
    result = []
    response = urllib.request.urlopen(craigslist_url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.find_all('a', attrs={'class':'result-title hdrlnk'})

    result = [link.get('href') for link in links]
    return result

def parsePages(page_url):
    result = {}
    result['url'] = page_url

    response = urllib.request.urlopen(page_url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    info = soup.find_all('b')
    counter = 1
    for piece in info:
        new_piece = piece.parent.getText().encode('ascii', 'ignore').decode('utf-8')
        split_pieces = new_piece.split(':')
        if counter > 1:
            split_pieces[1] = split_pieces[1].replace(" ", "", 1)
            result[split_pieces[0]] = split_pieces[1]
        else:
            result['car'] = split_pieces[0]
        counter += 1

    price = soup.find_all('span', attrs={'class':'price'})
    result['price'] = price[0].string.strip('$')

    return result

def createPriceDict(list_links):
    result = {}
    for link in list_links:
        result[parsePages(link)['car']] = int(parsePages(link)['price'])
    return result

def averageCarValues(value_dictionary):
    sum_prices = 0
    counter = 0
    for car in value_dictionary:
        sum_prices += value_dictionary[car]
        counter += 1
    avg = round((sum_prices / counter), 2)
    return avg

def compareToAvg(car_price, avg_price):
    return round((car_price - avg_price), 5)

def averagePriceToMilage(links):
    sum_price_per_mile = 0
    counter = 0
    for link in links:
        read_from = parsePages(link)
        price_per_mile = int(read_from['price']) / int(read_from['odometer'])
        sum_price_per_mile += price_per_mile
        counter += 1
    avg = round((sum_price_per_mile / counter), 5)
    return avg
def calcPricePerMile(link_parsed):
    ppm = round((int(link_parsed['price']) / int(link_parsed['odometer'])), 5)
    return ppm

def comparePricePerMilage(car_price_ratio, avg_price_ratio):
    return round((car_price_ratio - avg_price_ratio), 5)

if __name__ == '__main__':
    url = (urlm.urlManager('humboldt', 'all') + 
                        urlm.addDistance('100') + 
                        urlm.addPostal('95521') + 
                        urlm.addMinPrice('1000') + 
                        urlm.addMaxPrice('5000') + 
                        urlm.addMakeModel('Ford Explorer'))
    links = findCarLinks(url)
    print(url)
    print(links)
    print('\n')
    car_vals = createPriceDict(links)
    avg = averageCarValues(car_vals)
    avgpm = averagePriceToMilage(links)
    print(avg)
    print(avgpm)
    for link in links:
        print(parsePages(link))
        print(compareToAvg(int(parsePages(link)['price']), avg))
        ppm = calcPricePerMile(parsePages(link))
        print(comparePricePerMilage(ppm, avgpm))

    