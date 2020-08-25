import ssl
from flask import Flask,render_template,request
import sys
import os
import pyodbc
import time
import redis
import pandas as pd
import random
import hashlib
import pickle

from redis.connection import NONBLOCKING_EXCEPTION_ERROR_NUMBERS, ssl_available

app = Flask(__name__)

# connections

hostname=
database = 
username = 
password = 
redis_password=
connection = pyodbc.connect()
cursor = connection.cursor()

red = redis.Redis(host=
        port=6380, db=0, password=,ssl=True)
print("am printing this value", red)





@app.route('/')
def index():
    return render_template('home.html')

@app.route('/try',methods=["POST"])
def displayDB():
    if request.method=='POST':
         sql=("SELECT TIME, LATITUDE, LONGITUDE from quake ;")
         cursor.execute(sql)
         myResult = cursor.fetchall()

         return render_template("displayDB.html",output = myResult)

@app.route('/one', methods=['GET','POST'])
def rand():
    if request.method == 'POST':
        num = int(request.form['num'])
        start_time = time.time()

        # num is a interger value
        for i in range(0, num):
            # random.uniform(a, b)
            #Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
            # #The end-point value b may or may not be included in the range depending on floating-point rounding in the equation a + (b-a) * random().
            # mag = random.uniform(0.5, 6.5)
            # print("the random number generated is : ",mag)
            # mag = str("{0:.2f}".format(mag))
            # print("taking only 2 digit after decimal : ",mag)
            # sql = ("SELECT * from quake where MAG =" + mag)
            sql = "SELECT mag FROM quake ;"
            cursor.execute(sql)
        end_time = time.time()
        time_diff = end_time - start_time

        return render_template("rand.html", time=time_diff, num=num)


@app.route('/two', methods=['POST'])
def restrand():
    num = int(request.form['num'])
    start_time = time.time()
    for i in range(0, num):
        mag = random.uniform(0.5, 6.5)
        mag = float("{0:.2f}".format(mag))
        sql = " select * from quake where \"mag\" = \'" + str(mag) + "\' and \"gap\" between 50 and 100 "
        cursor.execute(sql)
    end_time = time.time()
    time_diff = end_time - start_time
    return render_template("restrand.html", time=time_diff, num=num)




# Randrange function begins here.

def randrange(rangfro=None,rangto=None,num=None):
    # start time
    start = time.time()

    # loop through
    for i in range(0,num):
        mag= round(random.uniform(rangfro, rangto),1)
        print(" the mag value is : ", mag)
        # round(number, digits)
        # number	Required. The number to be rounded
        # digits	Optional. The number of decimals to use when rounding the number. Default is 0


        sql=" SELECT * from quake where \"mag\" > \'"+str(mag)+"\' "
        
        # Compute the hash key
        hash = hashlib.sha224(sql.encode('utf-8')).hexdigest()
        key = "redis_cache:" + hash


        if (red.get(key)):
           print("redis cached")
        else:
           # Do MySQL query
           cursor.execute(sql)
           myResult = cursor.fetchall()
           rows = []
           for i in myResult:
                rows.append(str(i))

           # Put data into cache for 1 hour
           red.set(key, pickle.dumps(list(rows)) )
           red.expire(key, 36)

        cursor.execute(sql)
    end = time.time()
    exectime = end - start
    return render_template('count.html', t=exectime)

@app.route('/multiplerun', methods=['POST'])
def randquery():
    # rangfro = float(request.args.get('rangefrom'))
    # rangto = float(request.args.get('rangeto'))
    # num = request.args.get('nom')

    rangfro = float(request.form['rangefrom'])
    rangto = float(request.form['rangeto'])
    num = int(request.form['nom'])
    # Take all the input and pass it to the function
    return randrange(rangfro,rangto,num)




# Multi run 2 begin

# Randrange function begins here.

def randrangetwo(num=None):
    # start time
    start = time.time()

    # loop through
    for i in range(0,num):
        # mag= round(random.uniform(rangfro, rangto),1)
        # print(" the mag value is : ", mag)
        # round(number, digits)
        # number	Required. The number to be rounded
        # digits	Optional. The number of decimals to use when rounding the number. Default is 0


        sql=" SELECT * from quake where \"mag\" > 2.4 "
        
        # Compute the hash key
        hash = hashlib.sha224(sql.encode('utf-8')).hexdigest()
        key = "redis_cache:" + hash


        if (red.get(key)):
           print("redis cached")
        else:
           # Do MySQL query
           cursor.execute(sql)
           myResult = cursor.fetchall()
           rows = []
           for i in myResult:
                rows.append(str(i))

           # Put data into cache for 1 hour
           red.set(key, pickle.dumps(list(rows)) )
           red.expire(key, 36)

        cursor.execute(sql)
    end = time.time()
    exectime = end - start
    return render_template('count1.html', t=exectime)

@app.route('/multipleruntwo', methods=['POST'])
def randquerytwo():
    num = int(request.form['nom'])
    # Take all the input and pass it to the function
    return randrangetwo(num)









port = os.getenv('PORT', '3000')
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=int(port))
