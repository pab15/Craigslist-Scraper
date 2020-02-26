import os
import csv
from app import app
from anlyzer import *
from Helpers.findcarlinks import *
from Helpers.urlmanager import *
from app.forms import BestResaleForm, InDepthSearch
from flask import redirect, url_for, render_template, request, session, flash

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/Best-Cars', methods=['GET', 'POST'])
def best_cars():
    form = BestResaleForm(request.form)
    if request.method == 'POST':
        if request.form['target_annual_mileage'] == '':
            flash('No Entry! Entry must be entered')
            return render_template('bestcars.html', form=form)
        else:
            if form.checkbox.data == False:
                if request.form['target_price'] == '':
                    try:
                        int(request.form['target_annual_mileage'])
                    except:
                        flash('Bad Entry! Entry must be an integer')
                        return render_template('bestcars.html', form=form)
                    else:
                        requested_mileage = int(request.form['target_annual_mileage'])
                        lowAnnualMilage(getCSVS('\\data\\cardata\\'), requested_mileage, '\\data\\filteredcars\\lowannualmiles.csv')
                        current_dir = os.getcwd()
                        car_file_dir = current_dir + '\\data\\filteredcars\\'
                        csv_file = open(car_file_dir + 'lowannualmiles.csv')
                        csv_reader = csv.reader(csv_file, delimiter=',')
                        to_print = []
                        for row in csv_reader:
                            car_dict = {'Pic Link:' : row[16],
                                        'Url:' : row[0],
                                        'Listing:' : row[1],
                                        'Price:' : row[2],
                                        'Annual Miles:' : row[15],
                                        'Year:' : row[3],
                                        'VIN:' : row[4],
                                        'Condition:' : row[5],
                                        'Cylinders:' : row[6],
                                        'Drive:' : row[7],
                                        'Gas:' : row[8],
                                        'Mileage:' : row[9],
                                        'Paint Color:' : row[10],
                                        'Size:' : row[11],
                                        'Title Status:' : row[12],
                                        'Transmission:' : row[13],
                                        'Type:' : row[14]
                                        }
                            to_print.append(car_dict)
                        return render_template('filtered_best.html', list_cars=to_print)
                else:
                    requested_mileage = int(request.form['target_annual_mileage'])
                    lowAnnualMilage(getCSVS('\\data\\cardata\\'), requested_mileage, 'data\\filteredcars\\lowannualmiles.csv')
                    current_dir = os.getcwd()
                    car_file_dir = current_dir + '\\data\\filteredcars\\'
                    csv_file = open(car_file_dir + 'lowannualmiles.csv')
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    to_print = []
                    for row in csv_reader:
                        if int(row[2]) <= int(request.form['target_price']):
                            car_dict = {'Pic Link:' : row[16],
                                        'Url:' : row[0],
                                        'Listing:' : row[1],
                                        'Price:' : row[2],
                                        'Annual Miles:' : row[15],
                                        'Year:' : row[3],
                                        'VIN:' : row[4],
                                        'Condition:' : row[5],
                                        'Cylinders:' : row[6],
                                        'Drive:' : row[7],
                                        'Gas:' : row[8],
                                        'Mileage:' : row[9],
                                        'Paint Color:' : row[10],
                                        'Size:' : row[11],
                                        'Title Status:' : row[12],
                                        'Transmission:' : row[13],
                                        'Type:' : row[14]
                                        }
                            to_print.append(car_dict)
                    return render_template('filtered_best.html', list_cars=to_print)
            else:
                if request.form['target_price'] == '':
                    try:
                        int(request.form['target_annual_mileage'])
                    except:
                        flash('Bad Entry! Entry must be an integer')
                        return render_template('bestcars.html', form=form)
                    else:
                        requested_mileage = int(request.form['target_annual_mileage'])
                        lowAnnualMilage(getCSVS('\\data\\UserData\\'), requested_mileage, '\\data\\filteredcars\\userlowannualmiles.csv')
                        current_dir = os.getcwd()
                        car_file_dir = current_dir + '\\data\\filteredcars\\'
                        csv_file = open(car_file_dir + 'userlowannualmiles.csv')
                        csv_reader = csv.reader(csv_file, delimiter=',')
                        to_print = []
                        for row in csv_reader:
                            car_dict = {'Pic Link:' : row[16],
                                        'Url:' : row[0],
                                        'Listing:' : row[1],
                                        'Price:' : row[2],
                                        'Annual Miles:' : row[15],
                                        'Year:' : row[3],
                                        'VIN:' : row[4],
                                        'Condition:' : row[5],
                                        'Cylinders:' : row[6],
                                        'Drive:' : row[7],
                                        'Gas:' : row[8],
                                        'Mileage:' : row[9],
                                        'Paint Color:' : row[10],
                                        'Size:' : row[11],
                                        'Title Status:' : row[12],
                                        'Transmission:' : row[13],
                                        'Type:' : row[14]
                                        }
                            to_print.append(car_dict)
                        return render_template('filtered_best.html', list_cars=to_print)
                else:
                    requested_mileage = int(request.form['target_annual_mileage'])
                    lowAnnualMilage(getCSVS('\\data\\UserData\\'), requested_mileage, 'data\\filteredcars\\userlowannualmiles.csv')
                    current_dir = os.getcwd()
                    car_file_dir = current_dir + '\\data\\filteredcars\\'
                    csv_file = open(car_file_dir + 'userlowannualmiles.csv')
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    to_print = []
                    for row in csv_reader:
                        if float(row[2]) <= float(request.form['target_price']):
                            car_dict = {'Pic Link:' : row[16],
                                        'Url:' : row[0],
                                        'Listing:' : row[1],
                                        'Price:' : row[2],
                                        'Annual Miles:' : row[15],
                                        'Year:' : row[3],
                                        'VIN:' : row[4],
                                        'Condition:' : row[5],
                                        'Cylinders:' : row[6],
                                        'Drive:' : row[7],
                                        'Gas:' : row[8],
                                        'Mileage:' : row[9],
                                        'Paint Color:' : row[10],
                                        'Size:' : row[11],
                                        'Title Status:' : row[12],
                                        'Transmission:' : row[13],
                                        'Type:' : row[14]
                                        }
                            to_print.append(car_dict)
                    return render_template('filtered_best.html', list_cars=to_print)    
    else:
        return render_template('bestcars.html', form=form)

@app.route('/filter-search', methods=['GET', 'POST'])
def filter():
    form = InDepthSearch()
    if request.method == 'POST':
        array = [request.form['car_make_model']]
        master_links = {}
        for car in array:
            url = urlManager(request.form['new_area'], 'all') + addMakeModel(request.form['car_make_model'])
            master_links[car] = findCarLinks(url)

        for car in master_links:
            createFile(request.form['car_make_model'], 'data\\UserData\\')
            for link in master_links[car]:
                dictToCSV(request.form['car_make_model'], parsePages(link),'data\\UserData\\')
        flash('User CSVs Created')
        return render_template('filter.html', form=form)
    else:
        return render_template('filter.html', form=form)