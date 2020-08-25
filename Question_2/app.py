import os
import shutil
import csv
import sys
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired


# import utilities

import ibm_db
import ibm_db_dbi

import math
import sqlite3
import pandas as pd
import datetime
from datetime import datetime
from datetime import date
from datetime import timedelta

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Configurations
app.config['SECRET_KEY'] = 'blah blah blah blah'


# connect using ibm_db_dbi. Attempt to establish A connection with uncataloged database.
# using service credentials
conn = ibm_db_dbi.connect(
    # fetch data using ibm_db_dbi
myCursor = conn.cursor()


class NameForm(FlaskForm):
    name = StringField('Name', default="Bruce Springsteen")
    submit = SubmitField('Submit')

# ROUTES!


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        return render_template('index.html', form=form, name=name)
    return render_template('index.html', form=form, name=None)

# Reference : https://www.w3resource.com/python-exercises/math/python-math-exercise-27.php


@app.route('/one', methods=['GET', 'POST'])
def one():

    # Requesting form
    # requesting distance from form
    # request latituded and longitude from form
    latitude = math.radians(float(request.form['Latitude']))
    print("The latitude is : ", latitude)

    longitude = math.radians(float(request.form['Longitude']))
    print(" the longitude is : ", longitude)

    queryDist = float(request.form['dist'])
    print("The query distance is : ", queryDist)

    # Query to find distance

    myCursor.execute("SELECT COUNT(*)  FROM EARTHQUAKE WHERE (6371 * ACOS(SIN(?) * SIN(RADIANS(\"latitude\")) + COS(?) *COS(RADIANS(\"latitude\")) *COS(RADIANS(\"longitude\") - (?)))) <= ?",
                     (latitude, latitude, longitude, queryDist,))

    myResult = myCursor.fetchall()
    print("my result is ", myResult)

    myCursor.execute("SELECT *  FROM EARTHQUAKE WHERE (6371 * ACOS(SIN(?) * SIN(RADIANS(\"latitude\")) + COS(?) *COS(RADIANS(\"latitude\")) *COS(RADIANS(\"longitude\") - (?)))) <= ?",
                     (latitude, latitude, longitude, queryDist,))

    allOutput = myCursor.fetchall()

    return render_template('one.html', output=myResult, output1=allOutput)


@app.route('/two', methods=['GET', 'POST'])
def two():


    latitude = math.radians(float(request.form['Latitude']))
    print("The latitude is : ", latitude)

    longitude = math.radians(float(request.form['Longitude']))
    print(" the longitude is : ", longitude)

    queryDist = float(request.form['dist'])
    print("The query distance is : ", queryDist)


    # Dealing with time

    time_string = "T00:00:00.000Z"
    time_component = 'Z'

    # taking the current system time
    presentDate = datetime.now()
    print("The present date is : ",presentDate)

    # Requesting form
    # request how many days do you want to search for the number of earthquakes(Ex. For last 2-days enter 2) from form
    previousDay = int(request.form['userdate'])
    print("The previous day given by user is : ", previousDay)
    # The previous day given by user is :  7
    previousDate = timedelta(days=previousDay)
    print("previous Day with timedelta is : ", previousDate)
    # previous Day with timedelta is :  7 days, 0:00:00

    actualDate = presentDate - previousDate
    actualDate = str(actualDate)
    actualDate = actualDate.replace(" ", "T")
    actualDate = actualDate[:-3]
    actualDate += time_component

    presentDate = str(presentDate)
    print("The current date to string is  : ", presentDate)
    # The current date to string is  :  2020-07-21 15:27:28.289374

    presentDate = presentDate.replace(" ", "T")
    print(" the current date with T is  : ", presentDate)
    # the current date with T is  :  2020-07-21T15:27:28.289374

    presentDate = presentDate[:-3]
    print("sliced date is : ", presentDate)
    # sliced date is :  2020-07-21T15:27:28.289

    presentDate += time_component
    print("the current date is : ",presentDate)
    # 2020-07-21T15:27:28.289Z

    print("current date : ",presentDate)
    # 2020-07-21T15:27:28.289Z

    print("the previous Date is : ", previousDate)
    #  7 days, 0:00:00

    print("actual wanted date : ",actualDate)
    # 2020-07-14T15:32:17.386Z



    # time_string = "T00:00:00.000Z"
	# start_date = request.form['start_date']
	# end_date = request.form['end_date']
	# magnitude = request.form['magnitude']
	# start_date +=time_string
	# end_date +=time_string
	# print(start_date)
	# print(end_date)

    myCursor.execute("SELECT MAX(\"mag\")  FROM EARTHQUAKE WHERE ( \"time\" BETWEEN ? AND ? ) AND (6371 * ACOS(SIN(?) * SIN(RADIANS(\"latitude\")) + COS(?) *COS(RADIANS(\"latitude\")) *COS(RADIANS(\"longitude\") - (?)))) <= ?",
                     (actualDate,presentDate,latitude, latitude, longitude, queryDist,))

    myResult = myCursor.fetchone()
    print("my result is ", myResult[0])
    return render_template('two.html', output = myResult[0] )

    # myCursor.execute("SELECT *  FROM EARTHQUAKE WHERE (6371 * ACOS(SIN(?) * SIN(RADIANS(\"latitude\")) + COS(?) *COS(RADIANS(\"latitude\")) *COS(RADIANS(\"longitude\") - (?)))) <= ?",
    #                  (latitude, latitude, longitude, queryDist,))

    # allOutput = myCursor.fetchall()





@app.route('/three', methods=['GET', 'POST'])
def three():

    # Requesting form
    # request firstname from form
    latitude = math.radians(float(request.form['Latitude']))
    print("The latitude is : ", latitude)

    longitude = math.radians(float(request.form['Longitude']))
    print(" the longitude is : ", longitude)



    myCursor.execute(" SELECT MIN( 6371 * ACOS( SIN(?) * SIN(RADIANS(\"latitude\")) + COS(?) *COS(RADIANS(\"latitude\")) *COS(RADIANS(\"longitude\") - (?)) )) FROM (SELECT * FROM earthquake WHERE \"mag\" > 6 ) ",
                     (latitude, latitude, longitude,))


    myResult = myCursor.fetchone()
    print("my result is ", myResult[0])



    myCursor.execute("SELECT \"time\",\"place\" FROM EARTHQUAKE WHERE (6371 * ACOS(SIN(?) * SIN(RADIANS(\"latitude\")) + COS(?) *COS(RADIANS(\"latitude\")) *COS(RADIANS(\"longitude\") - (?)))) = ?",
                     (latitude, latitude, longitude,myResult[0],))


    finalResult = myCursor.fetchall()


    # myCursor.execute("SELECT *  FROM EARTHQUAKE WHERE (6371 * ACOS(SIN(?) * SIN(RADIANS(\"latitude\")) + COS(?) *COS(RADIANS(\"latitude\")) *COS(RADIANS(\"longitude\") - (?)))) <= ?",
    #                  (latitude, latitude, longitude, queryDist,))

    # allOutput = myCursor.fetchall()

    return render_template('three.html', output=finalResult)











   


@app.route('/help')
def help():
    text_list = []
    # Python Version
    text_list.append({
        'label': 'Python Version',
        'value': str(sys.version)})
    # os.path.abspath(os.path.dirname(__file__))
    text_list.append({
        'label': 'os.path.abspath(os.path.dirname(__file__))',
        'value': str(os.path.abspath(os.path.dirname(__file__)))
    })
    # OS Current Working Directory
    text_list.append({
        'label': 'OS CWD',
        'value': str(os.getcwd())})
    # OS CWD Contents
    label = 'OS CWD Contents'
    value = ''
    text_list.append({
        'label': label,
        'value': value})
    return render_template('help.html', text_list=text_list, title='help')


@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return render_template('404.html', title='404')


@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return render_template('500.html', title='500')


port = int(os.getenv('PORT', '3000'))
app.run(host='0.0.0.0', port=port)
