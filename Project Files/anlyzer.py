import os
import csv
import datetime
from Helpers.findcarlinks import *

def createCSVS():
    array = getBestCars()
    master_links = {}
    for car in array:
        url = urlManager('humboldt', 'owner') + addMakeModel(car)
        master_links[car] = findCarLinks(url)

    for car in master_links:
        createFile(car)
        for link in master_links[car]:
            dictToCSV(car, parsePages(link))

def getCSVS():
    current_dir = os.getcwd()
    car_file_dir = current_dir + '\\data\\cardata\\'
    files = os.listdir(car_file_dir)
    file_paths = []
    for file in files:
        file_paths.append(car_file_dir + file)
    return file_paths

def lowAnnualMilage(list_csv_locations, max_annual_miles):
    current_year = int(datetime.datetime.now().year)
    f = open('data\\filteredcars\\lowannualmiles.csv', 'w')
    for file in list_csv_locations:
        csv_file = open(file)
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            if count != 0:
                if row[9] != '' and row[3] != '':
                    years_drove = current_year - int(row[3])
                    if int(row[9]) < 400 and years_drove > 2:
                        annual_miles = round(((int(row[9]) * 1000) / years_drove), 2)
                        if annual_miles <= max_annual_miles:
                            f.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},\n'.format(row[0], row[1], row[2],
                                                                                                                    row[3], row[4], row[5],
                                                                                                                    row[6], row[7], row[8],
                                                                                                                    row[9], row[10], row[11],
                                                                                                                    row[12], row[13], row[14],
                                                                                                                    annual_miles, row[15]))
                    elif int(row[9]) < 4000 and years_drove > 3:
                        annual_miles = round(((int(row[9]) * 100) / years_drove), 2)
                        if annual_miles <= max_annual_miles:
                            f.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},\n'.format(row[0], row[1], row[2],
                                                                                                                    row[3], row[4], row[5],
                                                                                                                    row[6], row[7], row[8],
                                                                                                                    row[9], row[10], row[11],
                                                                                                                    row[12], row[13], row[14],
                                                                                                                    annual_miles, row[15]))
                    else:
                        annual_miles = round((int(row[9]) / years_drove), 2)
                        if annual_miles <= max_annual_miles:
                            f.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},\n'.format(row[0], row[1], row[2],
                                                                                                                    row[3], row[4], row[5],
                                                                                                                    row[6], row[7], row[8],
                                                                                                                    row[9], row[10], row[11],
                                                                                                                    row[12], row[13], row[14],
                                                                                                                    annual_miles, row[15]))
                    
            count += 1
    f.close()
            
if __name__ == '__main__':
    createCSVS()
    print(getCSVS())
    lowAnnualMilage(getCSVS(), 10000)