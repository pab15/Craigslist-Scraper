import re
import ssl
import urllib
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from Helpers.urlmanager import *
# Uncomment to test in this file:
# from urlmanager import *

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

    response = urllib.request.urlopen(page_url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    result['url'] = page_url
    info = soup.find_all('b')
    pic_link = soup.find_all('img', attrs={'title':'1'})
    try:
        pic_link[0].get('src')
    except:
        result['pic'] = ""
    else:
        result['pic'] = pic_link[0].get('src')
    counter = 1
    for piece in info:
        new_piece = piece.parent.getText().encode('ascii', 'ignore').decode('utf-8')
        split_pieces = new_piece.split(':')
        if counter > 1:
            try:
                split_pieces[1] = split_pieces[1].replace(" ", "", 1)
                result[split_pieces[0]] = split_pieces[1]
            except:
                print('badcarvalue')
            else:
                split_pieces[1] = split_pieces[1].replace(" ", "", 1)
                result[split_pieces[0]] = split_pieces[1]
        else:
            result['car'] = split_pieces[0]
            try:
                int(split_pieces[0][0:4])
            except:
                result['model year'] = ""
            else:
                result['model year'] = split_pieces[0][0:4]
            price = soup.find_all('span', attrs={'class':'price'})
            try:
                price[0].string.strip('$')
            except:
                result['price'] = '0'
                result['model year'] = ""
            else:
                result['price'] = price[0].string.strip('$')

        counter += 1
    return result

def createFile(car):
    file_name = car + '.csv'
    f = open('data\\cardata\\' + file_name, 'w')
    potential_values = (['url', 'car', 'price', 'model year', 'VIN', 'condition', 
                        'cylinders', 'drive', 'fuel', 'odometer', 'paint color', 
                        'size', 'title status', 'transmission', 'type', 'pic'])
    for value in potential_values:
        f.write(value + ',')
    f.write('\n')
    f.close()

def dictToCSV(car, dictionary):
    file_name = car + '.csv'
    potential_values = (['url', 'car', 'price', 'model year', 'VIN', 'condition', 
                        'cylinders', 'drive', 'fuel', 'odometer', 'paint color', 
                        'size', 'title status', 'transmission', 'type', 'pic'])
    f = open('data\\cardata\\' + file_name, 'a')
    for value in potential_values:
        is_valid = dictionary.get(value)
        if is_valid:
            f.write(dictionary[value] + ',')
        else:
            f.write(',')
    f.write('\n')
    f.close()

def getBestCars():
    result = []
    scusa_url = 'https://santanderconsumerusa.com/blog/25-vehicles-that-hold-value-best-over-five-years-iseecars-com'

    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(scusa_url, context=context)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    cars = soup.find_all('strong')
    counter = 1
    for car in cars:
        if (car.parent.name != 'figcaption'):
            if (counter % 2 == 0):
                result.append(car.string)
                counter += 1
            else:
                counter += 1
    return result

if __name__ == '__main__':
    array = getBestCars()
    master_links = {}
    for car in array:
        url = urlManager('humboldt', 'owner') + addMakeModel(car)
        master_links[car] = findCarLinks(url)

    for car in master_links:
        createFile(car)
        for link in master_links[car]:
            dictToCSV(car, parsePages(link))

    